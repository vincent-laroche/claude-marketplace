#!/usr/bin/env python3
"""Audit a social media asset or brief for platform fit and publish risk."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    from PIL import Image
except Exception:  # pragma: no cover
    Image = None  # type: ignore[assignment]


FORMATS = {
    "instagram-feed-square": {"size": (1080, 1080), "safe": (160, 160, 160, 160), "headline_max": 10, "caption_max": 2200, "hashtags_max": 5},
    "instagram-feed-portrait": {"size": (1080, 1350), "safe": (80, 160, 80, 160), "headline_max": 10, "caption_max": 2200, "hashtags_max": 5},
    "instagram-story-reel": {"size": (1080, 1920), "safe": (80, 250, 120, 250), "headline_max": 8, "caption_max": 2200, "hashtags_max": 5},
    "tiktok-video": {"size": (1080, 1920), "safe": (80, 180, 120, 260), "headline_max": 8, "caption_max": 150, "hashtags_max": 3},
    "facebook-feed": {"size": (1080, 1080), "safe": (120, 120, 120, 120), "headline_max": 10, "caption_max": 500, "hashtags_max": 3},
    "facebook-reel": {"size": (1080, 1920), "safe": (80, 220, 120, 260), "headline_max": 8, "caption_max": 500, "hashtags_max": 3},
    "youtube-thumbnail": {"size": (1280, 720), "safe": (128, 72, 128, 72), "headline_max": 5, "caption_max": 100, "hashtags_max": 0},
}

RISKY_CLAIMS = re.compile(
    r"\b(guaranteed|undetectable|invisible|permanent|cure|restore hair growth|zero maintenance|"
    r"works for everyone|no one will ever know|miracle|shocking|last chance|hurry)\b",
    re.I,
)


@dataclass
class Issue:
    severity: str
    category: str
    message: str
    fix: str


def issue(severity: str, category: str, message: str, fix: str) -> Issue:
    return Issue(severity, category, message, fix)


def read_image_size(path: Path) -> tuple[int, int] | None:
    if Image is None:
        return None
    with Image.open(path) as image:
        return image.size


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        parts = [int(part.strip()) for part in value.split(",")]
    except ValueError as exc:
        raise ValueError("Text boxes must be numeric x,y,width,height") from exc
    if len(parts) != 4:
        raise ValueError("Text boxes must be x,y,width,height")
    return tuple(parts)  # type: ignore[return-value]


def box_outside_safe(box: tuple[int, int, int, int], safe: tuple[int, int, int, int], size: tuple[int, int]) -> bool:
    x, y, width, height = box
    left, top, right, bottom = safe
    canvas_w, canvas_h = size
    return x < left or y < top or x + width > canvas_w - right or y + height > canvas_h - bottom


def word_count(value: str | None) -> int:
    if not value:
        return 0
    return len(re.findall(r"\b[\w'-]+\b", value))


def hashtag_count(value: str | None) -> int:
    if not value:
        return 0
    return len([item for item in re.split(r"[\s,]+", value) if item.strip().lstrip("#")])


def audit(args: argparse.Namespace) -> dict[str, object]:
    spec = FORMATS[args.format]
    expected_size = spec["size"]
    safe = spec["safe"]
    issues: list[Issue] = []
    image_size = None

    if args.image:
        image_path = Path(args.image).expanduser()
        if not image_path.exists():
            issues.append(issue("P1", "asset", f"Image file not found: {image_path}", "Provide the exported asset path."))
        else:
            image_size = read_image_size(image_path)
            if image_size and image_size != expected_size:
                issues.append(issue("P1", "dimensions", f"Image is {image_size[0]}x{image_size[1]}, expected {expected_size[0]}x{expected_size[1]}.", "Export the asset at the platform-specific canvas size."))

    boxes = []
    for raw in args.text_box or []:
        box = parse_box(raw)
        boxes.append(box)
        if box_outside_safe(box, safe, expected_size):
            issues.append(issue("P1", "safe-zone", f"Text box {box} intersects unsafe platform UI/crop area.", "Move critical text inside the safe zone."))

    headline_words = word_count(args.headline)
    if headline_words > spec["headline_max"]:
        issues.append(issue("P2", "hierarchy", f"Headline has {headline_words} words; recommended max is {spec['headline_max']}.", "Shorten to one dominant idea."))

    caption_len = len(args.caption or "")
    if caption_len > spec["caption_max"]:
        issues.append(issue("P2", "caption", f"Caption has {caption_len} characters; recommended max is {spec['caption_max']} for this format.", "Move secondary detail to comments, carousel slides, or landing page."))

    hashtags = hashtag_count(args.hashtags)
    if hashtags > spec["hashtags_max"]:
        issues.append(issue("P3", "caption", f"{hashtags} hashtags supplied; recommended max is {spec['hashtags_max']}.", "Use fewer, more relevant hashtags."))

    combined_text = " ".join(value for value in [args.headline, args.caption, args.cta] if value)
    if RISKY_CLAIMS.search(combined_text):
        issues.append(issue("P0", "claims", "Risky claim, urgency, or overpromise language detected.", "Rewrite with truthful, context-aware, non-shame framing."))

    if args.cta and word_count(args.cta) > 5:
        issues.append(issue("P2", "cta", "CTA is long for social placement.", "Use one short next-step action."))
    if not args.cta:
        issues.append(issue("P3", "cta", "No CTA supplied.", "Confirm whether this asset should educate only or include one soft next step."))

    if args.format in {"instagram-story-reel", "tiktok-video", "facebook-reel"} and not args.has_captions:
        issues.append(issue("P1", "accessibility", "Video format has no captions flag.", "Add native or burned-in captions for speech."))

    if not args.alt_text and args.format not in {"tiktok-video", "youtube-thumbnail"}:
        issues.append(issue("P2", "accessibility", "No alt text supplied.", "Add platform alt text or ensure the caption describes the visual."))

    if args.proof_type in {"testimonial", "before-after"} and not args.consent_verified:
        issues.append(issue("P0", "consent", f"{args.proof_type} content requires verified consent.", "Verify written consent for this exact asset and channel before use."))

    return {
        "format": args.format,
        "expected_size": expected_size,
        "safe_zone_ltrb": safe,
        "image_size": image_size,
        "text_boxes": boxes,
        "headline_words": headline_words,
        "caption_characters": caption_len,
        "hashtags": hashtags,
        "issues": [asdict(item) for item in issues],
        "issue_count": len(issues),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", required=True, choices=sorted(FORMATS), help="Target platform format")
    parser.add_argument("--image", help="Exported image path")
    parser.add_argument("--text-box", action="append", help="Critical text box x,y,width,height. Repeatable")
    parser.add_argument("--headline", help="Headline or overlay hook")
    parser.add_argument("--caption", help="Caption text")
    parser.add_argument("--hashtags", help="Comma or space separated hashtags")
    parser.add_argument("--cta", help="CTA text")
    parser.add_argument("--alt-text", help="Alt text or visual description")
    parser.add_argument("--has-captions", action="store_true", help="Video has captions for speech")
    parser.add_argument("--proof-type", choices=["none", "testimonial", "before-after"], default="none", help="Proof/consent type")
    parser.add_argument("--consent-verified", action="store_true", help="Consent is verified for this channel and asset")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    try:
        report = audit(args)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("Social asset audit")
        print("==================")
        print(f"format: {report['format']}")
        print(f"expected_size: {report['expected_size']}")
        print(f"image_size: {report['image_size']}")
        print(f"issue_count: {report['issue_count']}")
        for item in report["issues"]:  # type: ignore[index]
            print(f"- {item['severity']} {item['category']}: {item['message']} Fix: {item['fix']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Audit a hex color palette for contrast, distance, role fit, and brand discipline."""

from __future__ import annotations

import argparse
import colorsys
import json
import math
import re
import sys
from dataclasses import asdict, dataclass
from itertools import combinations


HEX_RE = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


@dataclass
class Color:
    hex: str
    rgb: tuple[int, int, int]
    luminance: float
    oklch: tuple[float, float, float]
    temperature: str
    suggested_roles: list[str]


def normalize_hex(value: str) -> str:
    match = HEX_RE.match(value.strip())
    if not match:
        raise ValueError(f"Invalid hex color: {value!r}")
    raw = match.group(1)
    if len(raw) == 3:
        raw = "".join(ch * 2 for ch in raw)
    return f"#{raw.upper()}"


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = normalize_hex(value).lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def srgb_to_linear(channel: int) -> float:
    value = channel / 255
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (srgb_to_linear(channel) for channel in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    l1 = relative_luminance(a)
    l2 = relative_luminance(b)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def rgb_to_oklab(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    r, g, b = (srgb_to_linear(channel) for channel in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def rgb_to_oklch(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    l, a, b = rgb_to_oklab(rgb)
    chroma = math.sqrt(a * a + b * b)
    hue = (math.degrees(math.atan2(b, a)) + 360) % 360
    return (l, chroma, hue)


def oklab_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    lab_a = rgb_to_oklab(a)
    lab_b = rgb_to_oklab(b)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(lab_a, lab_b)))


def temperature_from_hue(hue: float, chroma: float) -> str:
    if chroma < 0.035:
        return "neutral"
    if hue >= 330 or hue < 90:
        return "warm"
    if 90 <= hue < 170:
        return "green-warm"
    if 170 <= hue < 300:
        return "cool"
    return "violet-warm"


def suggested_roles(l: float, c: float, hue: float) -> list[str]:
    roles: list[str] = []
    if l < 0.28:
        roles.extend(["ink", "heading", "body text"])
    elif l < 0.45:
        roles.extend(["high-emphasis border", "secondary ink"])
    elif l < 0.72 and c < 0.05:
        roles.extend(["muted text candidate", "divider"])
    elif l > 0.90 and c < 0.05:
        roles.extend(["page background", "paper", "surface"])
    elif l > 0.78 and c < 0.10:
        roles.extend(["soft surface", "muted fill", "border"])
    if c >= 0.10:
        if hue >= 330 or hue < 90:
            roles.append("warm accent")
        elif 90 <= hue < 170:
            roles.append("success-like accent")
        elif 170 <= hue < 270:
            roles.append("info/link-like accent")
        else:
            roles.append("expressive accent")
    return roles or ["supporting token"]


def analyze_color(value: str) -> Color:
    normalized = normalize_hex(value)
    rgb = hex_to_rgb(normalized)
    l, c, h = rgb_to_oklch(rgb)
    return Color(
        hex=normalized,
        rgb=rgb,
        luminance=relative_luminance(rgb),
        oklch=(round(l, 4), round(c, 4), round(h, 1)),
        temperature=temperature_from_hue(h, c),
        suggested_roles=suggested_roles(l, c, h),
    )


def distance_label(distance: float) -> str:
    if distance < 0.035:
        return "near duplicate"
    if distance < 0.075:
        return "subtle separation"
    if distance < 0.16:
        return "clear separation"
    return "strong separation"


def contrast_label(ratio: float) -> str:
    if ratio >= 4.5:
        return "normal text"
    if ratio >= 3:
        return "large text / UI boundary"
    return "not text-safe"


def palette_summary(colors: list[Color]) -> dict[str, object]:
    temps = {color.temperature for color in colors}
    lightness = [color.oklch[0] for color in colors]
    chroma = [color.oklch[1] for color in colors]
    high_chroma_count = sum(1 for value in chroma if value >= 0.10)
    near_duplicate_pairs = []
    for a, b in combinations(colors, 2):
        distance = oklab_distance(a.rgb, b.rgb)
        if distance < 0.035:
            near_duplicate_pairs.append([a.hex, b.hex, round(distance, 4)])

    notes = []
    if max(lightness) - min(lightness) < 0.45:
        notes.append("Palette has limited lightness range; text/surface roles may be weak.")
    if high_chroma_count > 2:
        notes.append("Palette has several high-chroma colors; assign strict accent/status roles.")
    if len(temps - {"neutral"}) > 2:
        notes.append("Palette spans multiple temperature families; harmony needs role discipline.")
    if near_duplicate_pairs:
        notes.append("Palette contains near-duplicate colors that may not earn separate roles.")
    if not notes:
        notes.append("Palette has usable separation; final approval depends on role assignment and contrast pairs.")

    return {
        "temperature_families": sorted(temps),
        "lightness_range": round(max(lightness) - min(lightness), 4),
        "high_chroma_colors": high_chroma_count,
        "near_duplicate_pairs": near_duplicate_pairs,
        "brand_discipline_notes": notes,
    }


def build_report(values: list[str]) -> dict[str, object]:
    colors = [analyze_color(value) for value in values]
    pairs = []
    distances = []
    for a, b in combinations(colors, 2):
        ratio = contrast_ratio(a.rgb, b.rgb)
        distance = oklab_distance(a.rgb, b.rgb)
        pairs.append(
            {
                "colors": [a.hex, b.hex],
                "contrast_ratio": round(ratio, 2),
                "contrast_use": contrast_label(ratio),
            }
        )
        distances.append(
            {
                "colors": [a.hex, b.hex],
                "oklab_distance": round(distance, 4),
                "distance_use": distance_label(distance),
            }
        )
    pairs.sort(key=lambda item: item["contrast_ratio"], reverse=True)
    distances.sort(key=lambda item: item["oklab_distance"])
    return {
        "colors": [asdict(color) for color in colors],
        "contrast_pairs": pairs,
        "perceptual_distances": distances,
        "summary": palette_summary(colors),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("colors", nargs="+", help="Hex colors, for example #111111 #F8F4EE")
    parser.add_argument("--json", action="store_true", help="Emit full JSON report")
    args = parser.parse_args()

    try:
        report = build_report(args.colors)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    print("Palette audit")
    print("=============")
    for color in report["colors"]:  # type: ignore[index]
        print(
            f"{color['hex']}  OKLCH={tuple(color['oklch'])}  "
            f"{color['temperature']}  roles={', '.join(color['suggested_roles'])}"
        )
    print("\nStrongest contrast pairs")
    for pair in report["contrast_pairs"][:8]:  # type: ignore[index]
        print(f"{pair['colors'][0]} / {pair['colors'][1]}: {pair['contrast_ratio']}:1 ({pair['contrast_use']})")
    print("\nClosest perceptual pairs")
    for pair in report["perceptual_distances"][:8]:  # type: ignore[index]
        print(f"{pair['colors'][0]} / {pair['colors'][1]}: {pair['oklab_distance']} ({pair['distance_use']})")
    print("\nBrand discipline")
    for note in report["summary"]["brand_discipline_notes"]:  # type: ignore[index]
        print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

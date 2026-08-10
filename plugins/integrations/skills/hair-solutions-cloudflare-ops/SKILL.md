---
name: hair-solutions-cloudflare-ops
description: "Use when handling Hair Solutions Co. Cloudflare operations: selecting the right local /Users/vMac/.env token, safely inspecting token capabilities without exposing secrets, deploying private Worker or Pages studio sites, binding hairsolutions.co subdomains, and verifying Cloudflare Access protection. Do not use for generic Cloudflare tutorials, non-Hair Solutions domains, or customer/order/storefront work unless explicitly requested."
---

# Hair Solutions Cloudflare Ops

Use this skill when a Hair Solutions Co. internal tool, studio, or brand workspace needs Cloudflare DNS, Workers, Pages, custom-domain binding, or Cloudflare Access setup.

## Hard Rules

1. Never print, paste, commit, screenshot, or log secret values.
2. Read `/Users/vMac/.env` only for variable names or in-memory command use.
3. Do not dump the whole `.env`.
4. Treat `hairsolutions.co` DNS and Cloudflare Access as production-sensitive even for private tools.
5. Keep internal studio sites private behind Cloudflare Access unless Vincent explicitly asks for public access.
6. Prefer purpose-specific tokens over broad tokens.
7. Verify unauthenticated access after every Access change.

## Known Local Secret Location

Secrets live here:

```text
/Users/vMac/.env
```

Safe variable-name inspection:

```bash
awk -F= '/^[A-Za-z_][A-Za-z0-9_]*=/{print $1}' /Users/vMac/.env | sort
```

Safe presence/length check for one variable:

```bash
awk -F= '/^CLOUDFLARE_BRAND_WORKER_DEPLOY_TOKEN=/{print $1 ": present length=" length($2)}' /Users/vMac/.env
```

## Token Map

Use the narrowest token that can complete the job.

| Variable | Known Role | Use When |
| --- | --- | --- |
| `CLOUDFLARE_BRAND_WORKER_DEPLOY_TOKEN` | Narrow deploy token created for private Hair Solutions Worker deployments. Has Workers Scripts Write, Workers Routes Write, DNS Write, and Zone Read. | Deploying or rebinding private Worker studio sites such as `brand.hairsolutions.co`. Try this first for Worker custom domains. |
| `CLOUDFLARE_MASTER_ACCOUNT_API_TOKEN` | Broad account-level token. Can read/manage Workers/Pages/Access surfaces and was used to create the Brand Design System Cloudflare Access app. | Use only when the narrow deploy token cannot perform account-level Access or setup work. |
| `CLOUDFLARE_API_KEY` | Token-management and DNS-oriented token. Can inspect/create Cloudflare API tokens and manage DNS, but previously lacked Worker deploy permissions. | Creating purpose-specific tokens or doing DNS-only checks. |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare account identifier. | Required with Wrangler and account API calls. |

Do not assume other `CLOUDFLARE_*` variables are valid Cloudflare API tokens. `CLOUDFLARE_ACCESS_KEY_ID` and `CLOUDFLARE_SECRET_ACCESS_KEY` are S3/R2-style credentials, not normal Cloudflare API bearer tokens.

## Capability Check Pattern

When a token fails, test capabilities by endpoint and print only variable names/results, never values.

Useful endpoints:

- Token verify: `/user/tokens/verify`
- DNS read: `/zones/<zone_id>/dns_records`
- Workers services: `/accounts/<account_id>/workers/services`
- Worker custom domains: `/accounts/<account_id>/workers/scripts/<script>/domains/records`
- Access apps: `/accounts/<account_id>/access/apps`
- API token permission groups: `/user/tokens/permission_groups`

For `hairsolutions.co`, the known zone ID is:

```text
44c9e2d6eb71ce0de6bb40e563bbf351
```

## Private Studio Deployment Workflow

1. Inspect the repo and build scripts before deploying.
2. Run the repo's verification commands.
3. Build the deployable output.
4. Deploy with the narrow Worker deploy token when the project outputs a Worker.
5. Bind the requested `*.hairsolutions.co` custom domain.
6. Create or verify a Cloudflare Access self-hosted app.
7. Confirm unauthenticated requests redirect to Access login.

Typical Worker deploy shape, adjusted to the repo:

```bash
TOKEN=$(awk -F= '/^CLOUDFLARE_BRAND_WORKER_DEPLOY_TOKEN=/{print $2}' /Users/vMac/.env)
ACCOUNT_ID=$(awk -F= '/^CLOUDFLARE_ACCOUNT_ID=/{print $2}' /Users/vMac/.env)

CLOUDFLARE_API_TOKEN="$TOKEN" CLOUDFLARE_ACCOUNT_ID="$ACCOUNT_ID" ./node_modules/.bin/wrangler deploy --config wrangler.json --cwd dist/server --domain <subdomain>.hairsolutions.co
```

If Wrangler reports that the hostname already has externally managed DNS records, delete the existing DNS record for that hostname before retrying. A Worker custom domain manages the hostname binding.

## Cloudflare Access Standard

For private Hair Solutions studio sites, create a self-hosted Access app:

- App name: `Hair Solutions <Project Name>`
- Domain: `<subdomain>.hairsolutions.co`
- Policy name: `Vincent only`
- Decision: `allow`
- Include email: `vincent@hairsolutions.co`

Expected unauthenticated check:

```bash
curl -I https://<subdomain>.hairsolutions.co
```

Pass condition:

- HTTP `302`
- `location` points to `cloudflareaccess.com`
- `www-authenticate` mentions `Cloudflare-Access`

Fail condition:

- HTTP `200` with app HTML to an unauthenticated request.
- HTTP `522`, `1014`, or `403` from a broken DNS/origin setup.

## Brand Design System Reference State

Known working private deployment:

- URL: `https://brand.hairsolutions.co`
- Worker service: `hairsolutionsco-brand-design-system-site`
- Access app: `Hair Solutions Brand Design System`
- Access policy: `Vincent only`
- Allowed email: `vincent@hairsolutions.co`

Use this as the model for other private internal studios, such as email or social marketing studio sites.

## Creating Another Purpose-Specific Token

Use `CLOUDFLARE_API_KEY` only if a new token is needed.

Minimum useful permission groups for a Worker custom-domain deploy:

- Workers Scripts Write
- Workers Routes Write
- DNS Write
- Zone Read

Store the new token in `/Users/vMac/.env` with a specific name, for example:

```text
CLOUDFLARE_EMAIL_MARKETING_STUDIO_DEPLOY_TOKEN
CLOUDFLARE_SOCIAL_MARKETING_STUDIO_DEPLOY_TOKEN
```

Never output the created token value. Report only the variable name, token id, and permission labels.

## Error Handling

- `1014` on a proxied CNAME usually means Cloudflare blocks a cross-account CNAME target. Use a Worker custom domain instead.
- `522` on a placeholder/proxied record means the hostname is not correctly bound to a Worker or origin.
- Worker deploy succeeds but domain binding fails: check Workers Routes Write and existing DNS conflicts.
- Access app exists but site is public: verify the app domain exactly matches the hostname.

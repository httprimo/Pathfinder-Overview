# Free Domain Setup Guide for Vercel

## Option 1: Freenom (Free Domains)

Freenom offers free domains with extensions: `.tk`, `.ml`, `.ga`, `.cf`, `.gq`

### Steps:

1. **Get a Free Domain:**
   - Go to https://www.freenom.com
   - Sign up for a free account
   - Search for your desired domain name (e.g., `pathfinder-overview`)
   - Select a free extension (`.tk`, `.ml`, `.ga`, or `.cf`)
   - Complete the registration (it's free for 1 year, renewable)

2. **Configure DNS in Freenom:**
   - Log into your Freenom account
   - Go to "My Domains" → "Manage Domain"
   - Click on "Manage Freenom DNS"
   - Add these DNS records:
     - **Type:** A
     - **Name:** @ (or leave blank for root domain)
     - **Target:** `76.76.21.21` (Vercel's IP)
     - **TTL:** 3600

3. **Add Domain to Vercel:**
   - Go to your Vercel project
   - Settings → Domains
   - Add your domain (e.g., `pathfinder-overview.tk`)
   - Vercel will verify the DNS configuration
   - Wait for DNS propagation (can take a few hours)

### Important Notes:
- Free domains from Freenom are free for 1 year, then you need to renew (still free)
- Some free domain services have reliability issues
- `.tk` domains are the most popular free option

## Option 2: GitHub Student Pack (If You're a Student)

If you're a student, you can get free domain credits:
- Go to https://education.github.com/pack
- Apply with your student email
- Get free domain credits from Namecheap or other providers
- Use those credits to get a `.me` or other domain

## Option 3: Use Subdomain Services (Limited)

Some services offer free subdomains, but they usually don't work well with Vercel's custom domain setup.

---

**Recommendation:** Try Freenom first - it's the easiest way to get a completely free custom domain that works with Vercel.


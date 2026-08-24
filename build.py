#!/usr/bin/env python3
"""
Static site generator for Micro Service (mspointbd.com).
Run: python3 build.py
Regenerates every HTML page from the templates + content below.
Edit the CONTENT section (services list, home page copy, etc.) and re-run
this script any time you want to update the site.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "Micro Service"
DOMAIN = "mspointbd.com"
SUPPORT_URL = "contact.html"
PHONE_DISPLAY = "+880 1722-458581"
PHONE_TEL = "+8801722458581"
WHATSAPP_NUMBER = "8801722458581"
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}"
FIVERR_URL = "https://www.fiverr.com/"  # placeholder — replace with your exact Fiverr profile URL
LINKEDIN_URL = "https://www.linkedin.com/in/mdmhoque/"
FACEBOOK_URL = "https://www.facebook.com/mamungtg/"
EMAIL_DISPLAY = "support@mspointbd.com"  # placeholder — update with real inbox
# Real inbox the contact form delivers submissions to.
# Kept separate from EMAIL_DISPLAY since it doesn't need to be shown publicly.
FORM_TARGET_EMAIL = "mominul@mspointbd.com"
# The contact form now posts to your own mail-relay Worker (see the
# ms-mail-worker/ folder) instead of FormSubmit — that Worker logs into your
# Zoho mailbox over SMTP, so submissions arrive From: mominul@mspointbd.com
# instead of FormSubmit's own address. Deploy that Worker first (see its
# DEPLOY.md), then replace this URL with the *.workers.dev URL it prints
# (or your own custom domain/route once you've set one up) and re-run
# `python3 build.py`.
FORM_ENDPOINT = "https://mspointbd-mail-relay.YOUR-SUBDOMAIN.workers.dev/"

# Default trust badges shown under every service hero — override per page if needed.
DEFAULT_TRUST_BADGES = ["After-Sales Support", "Experienced Team", "Fair Pricing", "Fast Turnaround"]

# --------------------------------------------------------------------------
# INLINE SVG ICONS — self-contained, no external CDN dependency (a CDN like
# Font Awesome is blocked in some networks/sandboxes and adds a fragile
# external dependency for something this small).
# --------------------------------------------------------------------------
SOCIAL_ICONS = {
    "facebook": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06C2 17.06 5.66 21.2 10.44 22v-7.03H7.9v-2.91h2.54V9.85c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.91h-2.34V22C18.34 21.2 22 17.06 22 12.06z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 3.9 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM.4 8.4h4.1V23H.4V8.4zM8.3 8.4h3.9v2h.1c.55-1 1.9-2.1 3.9-2.1 4.2 0 5 2.8 5 6.3V23h-4.1v-6.6c0-1.6 0-3.6-2.2-3.6-2.2 0-2.5 1.7-2.5 3.5V23H8.3V8.4z"/></svg>',
    "x": '<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M18.24 3H21l-6.55 7.49L22.2 21h-6.1l-4.78-6.24L5.8 21H3l7-8L2.6 3h6.25l4.32 5.72L18.24 3zm-1.07 16.17h1.68L7.9 4.74H6.1l11.07 14.43z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor"><path d="M23 12s0-3.5-.45-5.17a2.78 2.78 0 0 0-1.96-1.97C18.88 4.4 12 4.4 12 4.4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.95 1.97C1 8.5 1 12 1 12s0 3.5.45 5.17a2.78 2.78 0 0 0 1.95 1.97c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.95-1.97C23 15.5 23 12 23 12zM9.75 15.3V8.7l5.75 3.3-5.75 3.3z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2.1a9.9 9.9 0 0 0-8.53 14.94L2 22l5.1-1.4A9.9 9.9 0 1 0 12 2.1zm0 18.05a8.1 8.1 0 0 1-4.15-1.14l-.3-.18-3.1.85.83-3-.19-.31A8.1 8.1 0 1 1 12 20.15zm4.4-6.06c-.24-.12-1.43-.7-1.65-.79-.22-.08-.38-.12-.55.13-.16.24-.63.78-.77.95-.14.16-.28.18-.52.06-.24-.12-1-.37-1.92-1.18-.71-.63-1.19-1.42-1.33-1.66-.14-.24-.02-.37.1-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32 .98 2.48c.12.16 1.7 2.6 4.13 3.64.58.25 1.03.4 1.38.51.58.18 1.11.16 1.53.1.47-.07 1.43-.58 1.63-1.15.2-.56.2-1.04.14-1.15-.06-.1-.22-.16-.46-.28z"/></svg>',
    "fiverr": '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M14.5 2C11 2 9 4.2 9 7.6V8H6v3h3v9h3v-9h3.5V8H12v-.4C12 6 12.8 5 14.6 5c.5 0 1 .1 1.4.2V2.2C15.6 2.1 15 2 14.5 2zM4 8v12h3V8H4zm14.5 0a1.75 1.75 0 1 0 0-3.5 1.75 1.75 0 0 0 0 3.5zM17 20h3V8h-3v12z"/></svg>',
}

# Flag icons for the currency menu — deliberately NOT emoji flags (🇺🇸 etc.).
# Windows browsers (Chrome/Edge) don't render colored flag-emoji glyphs; they
# fall back to showing the raw two-letter region code as plain text ("us",
# "GB"...), which is exactly the bug this replaces. Small inline SVGs render
# identically everywhere, same reasoning as SOCIAL_ICONS above.
FLAG_ICONS = {
    "US": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><g fill="#B22234"><rect width="20" height="1.08"/><rect width="20" height="1.08" y="2.15"/><rect width="20" height="1.08" y="4.3"/><rect width="20" height="1.08" y="6.46"/><rect width="20" height="1.08" y="8.6"/><rect width="20" height="1.08" y="10.75"/><rect width="20" height="1.08" y="12.9"/></g><rect width="8" height="7.5" fill="#3C3B6E"/></svg>',
    "EU": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#003399"/><g fill="#FFCC00"><circle cx="10" cy="3" r="0.7"/><circle cx="13" cy="4" r="0.7"/><circle cx="14.3" cy="7" r="0.7"/><circle cx="13" cy="10" r="0.7"/><circle cx="10" cy="11" r="0.7"/><circle cx="7" cy="10" r="0.7"/><circle cx="5.7" cy="7" r="0.7"/><circle cx="7" cy="4" r="0.7"/></g></svg>',
    "GB": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#00247D"/><g stroke="#fff" stroke-width="2.4"><line x1="0" y1="0" x2="20" y2="14"/><line x1="20" y1="0" x2="0" y2="14"/></g><g stroke="#CF142B" stroke-width="1.2"><line x1="0" y1="0" x2="20" y2="14"/><line x1="20" y1="0" x2="0" y2="14"/></g><rect x="8" width="4" height="14" fill="#fff"/><rect y="5" width="20" height="4" fill="#fff"/><rect x="8.8" width="2.4" height="14" fill="#CF142B"/><rect y="5.8" width="20" height="2.4" fill="#CF142B"/></svg>',
    "CA": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><rect width="5" height="14" fill="#D80621"/><rect x="15" width="5" height="14" fill="#D80621"/><path d="M10 3 L10.8 5 L12.5 4.3 L11.8 6 L13.5 6.5 L11.8 7.3 L12.3 9 L10.5 8.2 L10 10 L9.5 8.2 L7.7 9 L8.2 7.3 L6.5 6.5 L8.2 6 L7.5 4.3 L9.2 5 Z" fill="#D80621"/></svg>',
    "AU": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#00247D"/><g stroke="#fff" stroke-width="1"><line x1="0" y1="0" x2="10" y2="7"/><line x1="10" y1="0" x2="0" y2="7"/></g><rect x="4" width="2" height="7" fill="#fff"/><rect y="3" width="10" height="1" fill="#fff"/><rect x="4.4" width="1.2" height="7" fill="#CF142B"/><rect y="3.3" width="10" height="0.4" fill="#CF142B"/><g fill="#fff"><circle cx="15" cy="3" r="0.6"/><circle cx="17" cy="6" r="0.6"/><circle cx="14.5" cy="9" r="0.6"/><circle cx="17.5" cy="10.5" r="0.6"/><circle cx="12.5" cy="6.5" r="0.5"/></g></svg>',
}

PAYMENT_BADGES_HTML = """
<span class="pay-badge pay-badge--ssl" aria-label="SSL Secured">
  <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
  SSL SECURED
</span>
<span class="pay-badge pay-badge--stripe" aria-label="Powered by Stripe"><span class="pb-of">Powered by</span> <strong>stripe</strong></span>
<span class="pay-badge" style="background:#1a1f71;">VISA</span>
<span class="pay-badge pay-badge--mc" aria-label="Mastercard"><span class="mc-circle mc-red"></span><span class="mc-circle mc-yellow"></span></span>
<span class="pay-badge" style="background:#2557d6;">AMEX</span>
<span class="pay-badge pay-badge--pp" aria-label="PayPal"><span class="pp-pay">Pay</span><span class="pp-pal">Pal</span></span>
"""

# --------------------------------------------------------------------------
# NAV / SERVICE REGISTRY
# --------------------------------------------------------------------------
# Services that have full pages built (slug -> nav label). Order matters for nav.
SERVICES_LIVE = [
    ("services-website-repair-small-fixes.html", "Website Repair & Small Fixes"),
    ("services-malware-removal-security-hardening.html", "Malware Removal & Security Hardening"),
    ("services-speed-optimization.html", "Speed Optimization"),
    ("services-migration.html", "Migration"),
    ("services-redesign-development.html", "Redesign & Development"),
    ("services-infrastructure-devops.html", "Infrastructure & DevOps"),
    ("services-saas-systems-integration.html", "SaaS & Systems Integration"),
    ("services-ai-development-integration.html", "AI Development & Integration"),
]
# Old slugs that have been merged/renamed away — each gets a redirect stub
# (meta-refresh + canonical) pointing at its replacement, so old bookmarks,
# search-engine links, and shared URLs still land somewhere useful instead
# of 404ing.
REDIRECTS = [
    ("services-malware-removal.html", "services-malware-removal-security-hardening.html"),
    ("services-cybersecurity-compliance.html", "services-malware-removal-security-hardening.html"),
    ("services-small-tasks.html", "services-website-repair-small-fixes.html"),
    ("services-website-development.html", "services-redesign-development.html"),
    ("services-redesign.html", "services-redesign-development.html"),
    ("services-devops-automation-cicd.html", "services-infrastructure-devops.html"),
]
# Services mentioned on the reference site but not yet supplied — shown as "coming soon"
SERVICES_SOON = []

NAV_ITEMS = [
    ("index.html", "Home"),
    ("__SERVICES_DROPDOWN__", "Services"),
    ("care-plans.html", "Care Plans"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

# --------------------------------------------------------------------------
# HEADER / FOOTER
# --------------------------------------------------------------------------

# Site-wide fallback OG/social-share image, used by any page that doesn't
# pass its own og_image (see page()/service_page()). Per-service pages get
# a matching branded image generated for that specific service instead —
# see assets/og-*.png.
DEFAULT_OG_IMAGE = "assets/og-image.png"


def render_head(title, description, filename="index.html", og_image=None):
    page_title = f"{title} | {SITE_NAME}"
    # The homepage's canonical/OG URL is the bare domain, not "/index.html" —
    # avoids the two being treated as duplicate-content URLs by crawlers.
    url_path = "" if filename == "index.html" else filename
    canonical_url = f"https://{DOMAIN}/{url_path}"
    image_url = f"https://{DOMAIN}/{og_image or DEFAULT_OG_IMAGE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- Start cookieyes banner -->
<script id="cookieyes" type="text/javascript" src="https://cdn-cookieyes.com/client_data/292bc8bb93b9dc1c99121b49c73be720/script.js"></script>
<!-- End cookieyes banner -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical_url}">
<!-- Open Graph (Facebook, WhatsApp, LinkedIn) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{image_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<!-- Twitter/X Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{page_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{image_url}">
<link rel="stylesheet" href="{{ASSET}}css/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2248%22 fill=%22%230b2c4d%22/><text x=%2250%22 y=%2268%22 font-size=%2258%22 text-anchor=%22middle%22>\U0001F6E0️</text></svg>">
</head>
<body>
"""

def render_header(active_href):
    def is_active(href):
        return "active" if href == active_href else ""

    # Mega-menu: first 4 SERVICES_LIVE entries are the fixed-price /
    # fast-turnaround services, last 4 are the custom-quote / larger-scope
    # services — this split matches the order the taxonomy was designed in.
    fix_col, scale_col = SERVICES_LIVE[:4], SERVICES_LIVE[4:]
    services_dd = '<div class="dropdown mega-menu">'
    services_dd += '<div class="mega-col"><div class="mega-col-head">Fix &amp; Optimize</div>'
    for href, label in fix_col:
        services_dd += f'<a href="{{ROOT}}{href}" class="mega-item"><span class="mega-label">{label}</span></a>'
    services_dd += '</div>'
    services_dd += '<div class="mega-col"><div class="mega-col-head">Build &amp; Scale</div>'
    for href, label in scale_col:
        services_dd += f'<a href="{{ROOT}}{href}" class="mega-item"><span class="mega-label">{label}</span></a>'
    if SERVICES_SOON:
        services_dd += '<span class="soon">Coming soon</span>'
        for label in SERVICES_SOON:
            services_dd += f'<a href="#" class="mega-item" style="opacity:.55;pointer-events:none;"><span class="mega-label">{label}</span></a>'
    services_dd += '</div>'
    services_dd += '</div>'

    nav_html = ""
    for href, label in NAV_ITEMS:
        if href == "__SERVICES_DROPDOWN__":
            services_active = "active" if active_href.startswith("services-") or active_href == "services.html" else ""
            nav_html += f'<div class="has-dropdown"><a href="{{ROOT}}services.html" class="{services_active}">{label} ▾</a>{services_dd}</div>'
        else:
            nav_html += f'<a href="{{ROOT}}{href}" class="{is_active(href)}">{label}</a>'

    return f"""<header class="site-header">
  <div class="container nav-bar">
    <a href="{{ROOT}}index.html" class="logo">Micro<span class="accent">Service</span></a>
    <nav class="nav-links" id="nav-links">
      {nav_html}
    </nav>
    <div class="nav-cta">
      <a href="tel:{PHONE_TEL}" class="phone-link">\U0001F4DE {PHONE_DISPLAY}</a>
      <div class="has-dropdown currency-menu">
        <a href="{{ROOT}}contact.html" class="currency-toggle" aria-haspopup="true">{FLAG_ICONS['US']} USD <span class="chevron">▾</span></a>
        <div class="dropdown currency-dropdown">
          <a href="{{ROOT}}contact.html">{FLAG_ICONS['EU']} EUR</a>
          <a href="{{ROOT}}contact.html">{FLAG_ICONS['GB']} GBP</a>
          <a href="{{ROOT}}contact.html">{FLAG_ICONS['CA']} CAD</a>
          <a href="{{ROOT}}contact.html">{FLAG_ICONS['AU']} AUD</a>
        </div>
      </div>
      <a href="{{ROOT}}contact.html" class="btn btn-primary">Get Free Quote</a>
      <button type="button" class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""

def render_footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo">Micro<span class="accent">Service</span></div>
        <p>Website repair, security, infrastructure, integrations, and AI development for businesses worldwide. Fixes from $49. No long-term contracts required.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="{{ROOT}}services-website-repair-small-fixes.html">Website Repair &amp; Small Fixes</a></li>
          <li><a href="{{ROOT}}services-malware-removal-security-hardening.html">Malware Removal &amp; Security</a></li>
          <li><a href="{{ROOT}}services-speed-optimization.html">Speed Optimization</a></li>
          <li><a href="{{ROOT}}services-migration.html">Migration</a></li>
          <li><a href="{{ROOT}}services-redesign-development.html">Redesign &amp; Development</a></li>
          <li><a href="{{ROOT}}services-infrastructure-devops.html">Infrastructure &amp; DevOps</a></li>
          <li><a href="{{ROOT}}services-saas-systems-integration.html">SaaS &amp; Systems Integration</a></li>
          <li><a href="{{ROOT}}services-ai-development-integration.html">AI Development &amp; Integration</a></li>
        </ul>
      </div>
      <div>
        <h4>Plans &amp; Hosting</h4>
        <ul>
          <li><a href="{{ROOT}}care-plans.html">Care Plans</a></li>
          <li><a href="{{ROOT}}maintenance-plan.html">Maintenance Plan</a></li>
          <li><a href="{{ROOT}}care-plans.html">Security Plan</a></li>
          <li><a href="{{ROOT}}care-plans.html">Performance Plan</a></li>
          <li><a href="{{ROOT}}about.html">About Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Support Hours</h4>
        <ul>
          <li>Open 24/7 — every day of the week, no days off.</li>
          <li>Most repairs completed within 24 hours; urgent requests handled same day.</li>
          <li>✉️ {EMAIL_DISPLAY}</li>
          <li>\U0001F4DE <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        </ul>
      </div>
      <div>
        <h4>Pay With</h4>
        <div class="pay-icons">
          {PAYMENT_BADGES_HTML}
        </div>
        <h4 style="margin-top:22px;">Social Links</h4>
        <div class="social-links">
          <a href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Facebook">{SOCIAL_ICONS['facebook']}</a>
          <a href="#" aria-label="Instagram">{SOCIAL_ICONS['instagram']}</a>
          <a href="{LINKEDIN_URL}" target="_blank" rel="noopener" aria-label="LinkedIn">{SOCIAL_ICONS['linkedin']}</a>
          <a href="#" aria-label="X">{SOCIAL_ICONS['x']}</a>
          <a href="#" aria-label="YouTube">{SOCIAL_ICONS['youtube']}</a>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_ICONS['whatsapp']}</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {SITE_NAME} — {DOMAIN}. All rights reserved.</span>
      <div class="footer-legal">
        <a href="{{ROOT}}terms.html">Terms</a><a href="{{ROOT}}privacy.html">Privacy</a><a href="{{ROOT}}cookies.html">Cookies</a>
      </div>
    </div>
  </div>
</footer>
<div class="float-widgets">
  <a class="float-card" href="{FIVERR_URL}" target="_blank" rel="noopener">
    <span class="float-icon">{SOCIAL_ICONS['fiverr']}</span>
    <span class="float-label">Hire Me on Fiverr</span>
  </a>
  <a class="float-card" href="{WHATSAPP_LINK}" target="_blank" rel="noopener">
    <img class="qr" src="{{ROOT}}assets/whatsapp-qr.png" alt="Scan to chat on WhatsApp">
    <span class="float-label">Scan to chat on WhatsApp</span>
    <span class="float-icon whatsapp">{SOCIAL_ICONS['whatsapp']}</span>
  </a>
</div>
<!-- CookieYes "revisit consent" trigger — the cky-banner-element class is
     CookieYes's documented hook: their script binds a click handler to any
     element with this class to reopen the preferences panel. -->
<button type="button" class="cky-banner-element cookie-revisit-btn" id="cookie-revisit-btn" aria-label="Cookie Settings" title="Cookie Settings">\U0001F36A</button>
<script src="{{ROOT}}js/main.js" defer></script>
</body>
</html>
"""

def page(filename, title, description, body_html, active_href=None, asset_prefix="", og_image=None):
    active_href = active_href or filename
    html = render_head(title, description, filename, og_image) + render_header(active_href) + body_html + render_footer()
    html = html.replace("{ASSET}", asset_prefix).replace("{ROOT}", asset_prefix)
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


def redirect_page(old_filename, new_filename):
    """Minimal stub for a URL that has been merged/renamed away. Redirects
    real visitors instantly via meta-refresh, tells search engines the
    canonical location has moved (canonical link + noindex), and still
    shows a plain link/click-through in case the refresh is blocked."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={new_filename}">
<link rel="canonical" href="https://{DOMAIN}/{new_filename}">
<meta name="robots" content="noindex,follow">
<title>Moved — {SITE_NAME}</title>
</head>
<body>
<p>This page has moved. <a href="{new_filename}">Continue to the new page →</a></p>
</body>
</html>
"""
    with open(os.path.join(ROOT, old_filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote redirect", old_filename, "->", new_filename)


# --------------------------------------------------------------------------
# REUSABLE BLOCKS
# --------------------------------------------------------------------------

def faq_block(items):
    out = '<div class="faq-list">'
    for q, a in items:
        out += f'<details class="faq-item"><summary>{q}</summary><div class="faq-a">{a}</div></details>'
    out += "</div>"
    return out


def cta_banner(heading, sub, cta_label, cta_href="contact.html"):
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-banner">
      <h2>{heading}</h2>
      <p>{sub}</p>
      <a href="{{ROOT}}{cta_href}" class="btn btn-primary btn-lg">{cta_label}</a>
    </div>
  </div>
</section>"""


def service_hero(eyebrow, title, sub, stat_line, cta_label, cta_href="contact.html", badges=None, hero_stats=None, hero_checklist=None):
    badges = badges if badges is not None else DEFAULT_TRUST_BADGES
    badges_html = "".join(f"<span>{b}</span>" for b in badges)
    if hero_checklist:
        checklist_title, checklist_items = hero_checklist
        items_html = "".join(f'<div class="hero-checklist-item">{item}</div>' for item in checklist_items)
        art_html = f'<div class="hero-checklist"><div class="hero-checklist-title">{checklist_title}</div><div class="hero-checklist-grid">{items_html}</div></div>'
    elif hero_stats:
        items_html = "".join(
            f"""<div class="hero-trust-item"><div class="hero-trust-icon">{icon}</div><span class="hero-trust-value">{value}</span><span class="hero-trust-label">{label}</span></div>"""
            for icon, value, label in hero_stats
        )
        art_html = f'<div class="hero-trust-grid">{items_html}</div>'
    else:
        art_html = '<div class="emoji">\U0001F6E0️</div>'
    return f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow" style="background:rgba(255,255,255,0.14);color:#ffe1ad;">{eyebrow}</span>
        <h1>{title}</h1>
        <p class="lead">{sub}</p>
        <p class="lead" style="font-size:0.95rem;color:#b9cfe6;">{stat_line}</p>
        <div class="hero-cta">
          <a href="{{ROOT}}{cta_href}" class="btn btn-primary btn-lg">{cta_label}</a>
          <a href="{{ROOT}}care-plans.html" class="btn btn-outline btn-lg">View Care Plans</a>
        </div>
      </div>
      <div class="hero-art">
        {art_html}
      </div>
    </div>
  </div>
</section>
<div class="hero-badges"><div class="container">{badges_html}</div></div>"""


def three_steps(heading, sub, steps):
    cards = ""
    for i, (t, d) in enumerate(steps, start=1):
        cards += f"""<div class="step"><div class="step-num">{i}</div><h3>{t}</h3><p>{d}</p></div>"""
    return f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>{heading}</h2>
      <p>{sub}</p>
    </div>
    <div class="grid grid-3 steps">{cards}</div>
  </div>
</section>"""


def feature_cards(heading, sub, cards, bg="light"):
    items = ""
    for icon, t, d in cards:
        items += f"""<div class="card"><div class="icon">{icon}</div><h3>{t}</h3><p>{d}</p></div>"""
    bg_class = "section--light" if bg == "light" else "section--blue"
    return f"""
<section class="section {bg_class}">
  <div class="container">
    <div class="section-head">
      <h2>{heading}</h2>
      <p>{sub}</p>
    </div>
    <div class="grid grid-3">{items}</div>
  </div>
</section>"""


def service_page(slug, eyebrow, title, sub, stat_line, intro_heading, intro_paras,
                  steps, about_cards, faq_items, closing_heading, closing_sub, cta_label, badges=None, hero_stats=None, hero_checklist=None):
    body = service_hero(eyebrow, title, sub, stat_line, cta_label, badges=badges, hero_stats=hero_stats, hero_checklist=hero_checklist)
    body += f"""
<section class="section">
  <div class="container" style="max-width:820px;">
    <h2 class="text-center">{intro_heading}</h2>
    {''.join(f'<p>{p}</p>' for p in intro_paras)}
  </div>
</section>"""
    body += three_steps(f"How Our {title} Works" if "How" not in title else title,
                         "We keep the process simple so you always know what's happening.", steps)
    body += feature_cards(f"About Our {title}", "A closer look at exactly what's included.", about_cards)
    body += f"""
<section class="section">
  <div class="container" style="max-width:760px;">
    <div class="section-head"><h2>Frequently Asked Questions</h2></div>
    {faq_block(faq_items)}
  </div>
</section>"""
    body += cta_banner(closing_heading, closing_sub, cta_label)
    # Each service gets its own branded OG/social-share image if one has
    # been generated for it (assets/og-<slug-without-services->.png);
    # otherwise page() falls back to the site-wide default image.
    og_key = slug.removeprefix("services-").removesuffix(".html")
    og_candidate = f"assets/og-{og_key}.png"
    og_image = og_candidate if os.path.exists(os.path.join(ROOT, og_candidate)) else None
    page(slug, title, sub, body, og_image=og_image)


def coming_soon_service_page(slug, icon, eyebrow, title, sub, highlights):
    """Placeholder page for a service whose full copy hasn't been supplied yet.
    Keeps the page live and linkable now; swap in service_page() once real
    content (steps, about-cards, FAQ) is provided."""
    body = service_hero(eyebrow, title, sub, "Full service details coming soon · Contact us for immediate help", "Ask About This Service")
    items = "".join(f"<li>{h}</li>" for h in highlights)
    body += f"""
<section class="section">
  <div class="container" style="max-width:760px;">
    <div class="section-head">
      <span class="eyebrow">Page In Progress</span>
      <h2>{title} — Full Details Coming Soon</h2>
      <p>We're finalizing the full write-up for this service. In the meantime, here's what it covers — contact us directly and we'll scope your request right away.</p>
    </div>
    <ul class="checklist grid grid-2">{items}</ul>
  </div>
</section>"""
    body += cta_banner(f"Need {title} Now?", "Don't wait on the full page — send us your request and we'll get back to you with a quote or next steps.", "Contact Us")
    page(slug, title, sub, body)


# --------------------------------------------------------------------------
# CONTENT — SERVICE PAGES
# --------------------------------------------------------------------------

service_page(
    slug="services-malware-removal-security-hardening.html",
    eyebrow="Security",
    title="WordPress Malware Removal & Security Hardening",
    sub="Hacked or vulnerable WordPress site? We clean up active infections and harden your site against the next attack — one service, start to finish.",
    stat_line="3,000+ hacked sites cleaned · 200+ five-star reviews · Cleanup from $199 · Money-back guarantee",
    intro_heading="Hacked Right Now, or Trying to Stop It From Happening?",
    intro_paras=[
        "If your website is redirecting visitors, showing spam links, loading slowly, or displaying browser security warnings, it has likely been compromised — and malware does not fix itself.",
        "If your site handles logins, payments, or customer data, cleanup alone isn't enough. This service covers both sides: we remove what's already there, then harden your site so it's significantly harder to compromise again.",
    ],
    steps=[
        ("Scan & Audit", "We scan your WordPress site, plugins, themes, and database for malware and vulnerabilities, and run a full security audit across your site and hosting."),
        ("Clean & Harden", "We remove malware, hacked files, and backdoors, then configure firewalls, access controls, and hardening measures to block common attack methods."),
        ("Secure & Monitor", "We lock the site down and put ongoing monitoring in place so new risks are caught early instead of turning into the next incident."),
    ],
    about_cards=[
        ("\U0001F50D", "Scan Your Website", "We scan WordPress core files, themes, plugins, and the database to identify malware, injected code, and unauthorized file changes."),
        ("\U0001F9F9", "Remove Malicious Content", "We remove malware, hacked files, spam links, injected scripts, hidden backdoors, and infected database entries from your website."),
        ("\U0001F4C4", "Core File Check", "We review and clean critical files such as wp-config.php, .htaccess, and xmlrpc.php to ensure your site is no longer compromised."),
        ("\U0001F525", "Advanced Firewall &amp; Access Control", "Firewall rules and access-control configuration tailored to how your site is actually used, so the same attack doesn't work twice."),
        ("⚫", "Blacklist Removal", "If your site has been blacklisted or is showing browser warnings, we submit a review request to help restore access for visitors."),
        ("\U0001F6A8", "Incident Response Planning", "A clear, documented plan for what happens if your site is compromised again, so there's no scrambling next time."),
        ("\U0001F9EA", "Penetration-Style Security Testing", "Controlled testing that simulates real attack methods to confirm your defenses actually hold up, for business-critical sites."),
        ("\U0001F4CB", "Detailed Cleanup &amp; Hardening Report", "A clear report explaining what was found, what was removed, what was hardened, and the steps taken to secure your website."),
    ],
    faq_items=[
        ("How long does malware removal take?", "Most WordPress malware cleanups are completed within one business day after we receive access. Blacklist removals may take longer, depending on external review times."),
        ("How much does this cost?", "Cleanup starts at $199, with no contracts and a full money-back guarantee if we cannot fix your site. Sites needing a deeper security audit or compliance-aligned hardening are quoted after a quick review."),
        ("What if my site gets hacked again?", "If your site is compromised again within 30 days, we will clean it again at no extra cost."),
        ("Is hardening different from just cleaning it up?", "Yes. Cleanup removes an active infection. Hardening is proactive — firewall rules, access controls, and monitoring configured so the same attack doesn't work again. This service does both in one pass."),
        ("Do you guarantee compliance with specific regulations?", "We provide guidance aligned with common data-protection practices, but formal legal compliance certification should be confirmed with a qualified compliance professional."),
        ("Do you work with eCommerce and membership sites?", "Yes — hardening is built specifically for sites handling logins, payments, and sensitive customer data."),
        ("What information do you need to get started?", 'We’ll need your WordPress admin login and hosting account details. <a href="contact.html">Open a support ticket</a> and our team will guide you through it.'),
    ],
    closing_heading="Get Your Site Cleaned, Hardened, and Protected",
    closing_sub="Our service removes malware fast, cleans infected files, and hardens your site against the next attempt — restoring trust with visitors and search engines.<br>Order your cleanup now. 100% money-back guarantee if we cannot fix your site.",
    cta_label="Start My Security Cleanup",
    hero_stats=[
        ("\U0001F6E1️", "3,000+", "Hacked Sites Cleaned"),
        ("⭐", "200+", "Five-Star Reviews"),
        ("\U0001F4B0", "$199", "Starting Price"),
        ("✅", "100%", "Money-Back Guarantee"),
    ],
)

service_page(
    slug="services-speed-optimization.html",
    eyebrow="Speed Optimization",
    title="Website & Server Speed Optimization",
    sub="Slow website or sluggish server? We optimize WordPress sites and the Linux or Windows servers behind them for speed and performance.",
    stat_line="2,000+ sites optimized · 200+ five-star reviews · Speed optimization from $229 · Money-back guarantee",
    intro_heading="Need a One-Time Speed Optimization?",
    intro_paras=[
        "If your website feels slow, takes too long to load, or performs poorly on mobile, a one-time speed optimization can make an immediate difference.",
        "We work at both layers: WordPress-level tuning (caching, database, images, plugins) and, when the bottleneck is deeper, server-level tuning on the Linux or Windows machine actually hosting your site — without ongoing commitments.",
    ],
    steps=[
        ("Optimize", "We analyze your website and server setup and apply proven performance optimizations to reduce load times and improve responsiveness."),
        ("Fine-Tune", "We clean up performance bottlenecks at both the site and server level — images, database, plugins, and server resource usage."),
        ("Deliver", "Your website loads faster, responds more smoothly, and delivers a noticeably better experience for visitors across all devices."),
    ],
    about_cards=[
        ("\U0001F4BE", "Caching", "We configure advanced caching to reduce load times and improve how quickly pages are served to visitors."),
        ("\U0001F5C4️", "Database Optimization", "We clean unnecessary data such as old revisions and unused entries to keep your database fast and responsive."),
        ("\U0001F5BC️", "Image Compression", "We reduce image file sizes without sacrificing quality to help pages load faster on desktop and mobile."),
        ("\U0001F50C", "Plugin Audit", "We identify plugins that slow your site down and recommend changes where performance is being affected."),
        ("\U0001F5A5️", "Linux Server Tuning", "We tune Linux server resources — web server config, PHP/process limits, memory and CPU usage — when the bottleneck is the server, not the site."),
        ("\U0001FA9F", "Windows Server Tuning", "For sites or applications hosted on Windows Server (IIS), we tune server-level settings and resource allocation for faster response times."),
        ("⚠️", "Bad Requests", "We clean up broken or unnecessary requests that can delay page loading and hurt performance."),
        ("\U0001F512", "Brute Force Protection", "We reduce unnecessary login and bot activity that can slow your site and impact server performance."),
    ],
    faq_items=[
        ("Do you optimize the server, or just the website?", "Both, depending on where the bottleneck actually is. We diagnose first — sometimes it's WordPress-level tuning, sometimes it's the Linux or Windows server underneath, and sometimes it's both."),
        ("Should I use a CDN?", "A CDN can help in some cases, but many websites see major speed improvements through optimization alone. We focus on what will make the biggest impact for your setup."),
        ("How do you measure speed?", "We test performance before and after optimization using industry-standard tools. If speed does not improve, we offer a full refund."),
        ("Do you support WooCommerce websites?", "Yes. We optimize WooCommerce sites with care to ensure speed improvements without affecting functionality."),
        ("Can you help move my site to a faster server?", "If hosting performance is limiting your site, we can advise on next steps after optimization, including migration."),
        ("What access do you need?", 'We’ll need admin access and either FTP, hosting, or server (SSH/RDP) access depending on scope. <a href="contact.html">Open a support ticket</a> and our team will guide you through it.'),
    ],
    closing_heading="Get a Faster, Smoother Website",
    closing_sub="A slow website can frustrate visitors, reduce engagement, and hurt conversions. Order your speed optimization today. Satisfaction guaranteed.",
    cta_label="Start My Speed Optimization",
    hero_stats=[
        ("\U0001F680", "2,000+", "Sites Optimized"),
        ("⭐", "200+", "Five-Star Reviews"),
        ("\U0001F4B0", "$229", "Starting Price"),
        ("✅", "100%", "Money-Back Guarantee"),
    ],
)

service_page(
    slug="services-migration.html",
    eyebrow="Migration",
    title="Migration Services Without the Stress",
    sub="Move your website, database, software, or mail safely with zero downtime and no headaches.",
    stat_line="800+ migrations completed · 200+ five-star reviews · Migrations from $149 · Money-back guarantee",
    intro_heading="Need a One-Time Migration?",
    intro_paras=[
        "Whether you're switching hosting providers, changing domains, upgrading a database, moving software to a new server, or relocating a mail server, our migration service makes the process simple and stress free.",
        "We back up everything, move it securely, and reconfigure the destination so it works correctly in its new location — with no downtime and no data loss.",
    ],
    steps=[
        ("Backup", "We create a full backup of whatever is moving — website files and database, application data, or mailboxes."),
        ("Transfer", "We securely move it to the new host, server, or provider with minimal disruption."),
        ("Configure", "We reconfigure everything — DNS, connections, settings — so it works correctly in its new environment."),
    ],
    about_cards=[
        ("\U0001F4E6", "Full Backup", "We create a complete backup before touching anything — files, database, application data, or mailboxes — so nothing is at risk during the move."),
        ("\U0001F69A", "Website Migration", "Move your website to a new host or domain, ensuring everything works exactly as it did before."),
        ("\U0001F5C4️", "Database Migration", "Upgrade or relocate a database safely, with schema and data integrity checked before and after the move."),
        ("\U0001F4E5", "Software &amp; Application Migration", "Move installed software or applications to a new server, reconfigured to run correctly in the new environment."),
        ("✉️", "Mail Server Migration", "Move mailboxes and mail routing to a new provider or server without losing existing mail or breaking delivery."),
        ("\U0001F310", "Domain &amp; DNS Update", "If you are changing domains, we update DNS settings so everything points to the new location correctly."),
    ],
    faq_items=[
        ("How much downtime will I experience?", "We aim for zero downtime on every migration. DNS changes can take up to 24–48 hours to fully propagate, but the source stays accessible during that window."),
        ("Can you migrate my database separately from my website?", "Yes. Database migrations (upgrades, server moves) can be scoped and quoted independently of a full website migration."),
        ("What about my email addresses?", "If you're changing mail providers as part of the move, we migrate mailboxes directly. If email stays with your current provider, we'll explain what applies to your setup."),
        ("Can I change my domain name too?", "Yes. Domain changes are included, and we make sure everything is configured correctly afterward."),
        ("Can you migrate to any hosting provider or server?", "Yes. We can migrate to any hosting provider, cloud server, or on-premises server that supports your setup."),
        ("What do you need to get started?", "We'll need access to your current and new environments — hosting, database, server, or mailbox access depending on scope. Once the migration is complete, we'll guide you through any final steps."),
    ],
    closing_heading="Move It Without the Stress",
    closing_sub="Switching hosts, upgrading a database, or relocating mail and software doesn't have to be risky or time consuming. Quick, secure, and backed by a money-back guarantee.",
    cta_label="Start My Migration",
    hero_stats=[
        ("\U0001F69A", "800+", "Migrations Completed"),
        ("⭐", "200+", "Five-Star Reviews"),
        ("\U0001F4B0", "$149", "Starting Price"),
        ("✅", "100%", "Money-Back Guarantee"),
    ],
)

service_page(
    slug="services-website-repair-small-fixes.html",
    eyebrow="Website Repair",
    title="Website Repair & Small Fixes",
    sub="Broken pages, plugin errors, white screens, or just a quick edit — we handle website repairs and small fixes fast so you don’t have to.",
    stat_line="10,000+ issues resolved · 200+ five-star reviews · Fixes from $49 · Money-back guarantee",
    intro_heading="Something Broken, or Just Need a Quick Change?",
    intro_paras=[
        "Whether your site is throwing errors, showing a white screen, or crashing after an update, this service gets it diagnosed and fixed fast. If you just need a quick edit — text, images, layout — it's the same service, same flat-rate simplicity.",
        "Tell us what's wrong or what you'd like changed. We repair genuine issues (plugin conflicts, broken layouts, crashes) and handle small tasks (content edits, image swaps, small feature additions) with the same fast turnaround and one free revision.",
    ],
    steps=[
        ("Tell Us What's Wrong", "Send a repair request or task description — a broken feature, an error message, or just something you want changed."),
        ("We Review & Confirm", "We diagnose the issue or confirm task details and scope before starting."),
        ("Fixed & Confirmed", "We complete the fix or update and confirm everything's working before we close it out."),
    ],
    about_cards=[
        ("\U0001F50C", "Plugin Conflicts or Update Failures", "Errors or downtime after updates are common. We identify what caused the issue and repair it so updates stop breaking your site."),
        ("\U0001F5BC️", "Theme Display or Design Issues", "Broken layouts, missing sections, or visual glitches restored so every page looks as it should."),
        ("⚠️", "White Screens or 500 Errors", "If your site won't load or shows server errors, we find and fix what's blocking access."),
        ("\U0001F4DD", "Text &amp; Content Edits", "Need to update website text? We add, edit, or replace content quickly and accurately."),
        ("\U0001F3A8", "Layout Tweaks", "Want to adjust spacing, fonts, colors, or layout? We make small design changes to improve how your site looks."),
        ("✨", "Small Feature Additions", "Need something added? We install and configure simple features such as forms, feeds, or galleries."),
        ("✅", "One Free Revision", "Once your fix or task is complete, we confirm everything is finished and make one revision if needed."),
        ("\U0001F4CB", "Clear Scope Before We Start", "Once you submit your request, we review what you need and confirm scope and cost before getting started."),
    ],
    faq_items=[
        ("What counts as a repair vs. a small task?", "A repair is something broken — an error, a crash, a layout issue. A small task is something you want changed — content, images, layout. Both are handled through this same service, at the same starting price."),
        ("How long does it take?", "Most repairs and small tasks are completed within one to two business days after approval. Let us know if something is urgent."),
        ("How much does it cost?", "Pricing starts at $49. We always confirm the exact cost before starting any work."),
        ("How many revisions are included?", "Each request includes one free revision to make sure everything looks and works right."),
        ("Is this a subscription?", "No. This is a one-time, pay-as-you-go service. There are no ongoing fees."),
        ("Do you fix WooCommerce checkout or form issues?", "Yes. We inspect, test, and repair WooCommerce checkout problems and form errors so visitors can complete actions without issues."),
        ("What do you need to get started?", '<a href="contact.html">Submit a support request</a> describing the issue or what you\'d like changed. We\'ll review, confirm scope, and get started.'),
    ],
    closing_heading="Get It Fixed or Updated Today",
    closing_sub="From broken pages and plugin errors to quick content edits, one fast, flat-rate service handles it all. Fixes start at $49 with a full money-back guarantee.",
    cta_label="Start My Fix",
    hero_stats=[
        ("\U0001F527", "10,000+", "Issues Resolved"),
        ("⭐", "200+", "Five-Star Reviews"),
        ("\U0001F4B0", "$49", "Starting Price"),
        ("✅", "100%", "Money-Back Guarantee"),
    ],
)

service_page(
    slug="services-infrastructure-devops.html",
    eyebrow="Infrastructure & DevOps",
    title="Infrastructure & DevOps",
    sub="Servers, networks, and deployment pipelines built and managed properly — staging environments, CI/CD, system administration, firewalls, and virtualization, all under one team.",
    stat_line="Custom-scoped engagements · Free scoping call · Money-back guarantee on setup work",
    intro_heading="Need Infrastructure You Can Actually Trust?",
    intro_paras=[
        "If every deployment feels risky, your servers are managed ad hoc, or nobody's quite sure how your network and Active Directory are actually configured, your infrastructure needs a safer foundation.",
        "This service covers the full stack: CI/CD and deployment automation, day-to-day system administration, network and firewall security, and virtualization/Active Directory setup — scoped and quoted based on what you actually need, not a one-size-fits-all package.",
    ],
    steps=[
        ("Assess", "We review your current infrastructure, hosting, workflow, and tooling to see what's missing or risky."),
        ("Build", "We set up staging environments, CI/CD pipelines, server administration, firewalls, and virtualization as scoped."),
        ("Handover", "We test everything with you and document it so your team can run it independently — or we manage it ongoing."),
    ],
    about_cards=[
        ("\U0001F5A5️", "Staging &amp; Production Setup", "A proper staging environment so changes are tested before they ever touch production."),
        ("\U0001F501", "Automated Deployment Pipelines (CI/CD)", "Pipelines that push tested changes to production automatically and consistently."),
        ("\U0001F5C2️", "Version Control Workflows", "Git-based workflows so every change is tracked and reversible."),
        ("\U0001F4BE", "Automated Backups &amp; Rollback", "Scheduled backups with a fast, tested rollback process if a deployment goes wrong."),
        ("\U0001F6E0️", "System Administration", "Ongoing or one-time server administration — patching, resource monitoring, routine maintenance across Linux and Windows Server."),
        ("\U0001F525", "Network &amp; Firewall Security", "Firewall rules, network segmentation, and VPN configuration tailored to how your infrastructure is actually used."),
        ("\U0001F5C3️", "Virtualization &amp; Active Directory", "VM setup and management, plus Active Directory domain, user, and group configuration for Windows-based environments."),
        ("\U0001F514", "Monitoring &amp; Alerts", "Automated checks and alerts so you know immediately if a deployment or system issue needs attention."),
    ],
    faq_items=[
        ("Do I need an in-house developer or IT team?", "No. We set up the workflow and document it clearly enough for a non-technical owner to follow, though it's most useful if you or your team make regular changes."),
        ("Will this work with my current hosting or servers?", "In most cases, yes — we work with your existing infrastructure. If something doesn't support the tooling required, we'll flag that upfront before starting."),
        ("There's no fixed price here — how does pricing work?", "Infrastructure work varies too much for a flat rate to be honest. We scope your specific needs on a free call, then send a clear, itemized quote before any work begins."),
        ("What if something breaks after setup?", "That's the point of the rollback and monitoring we build — you can revert to a known-good state quickly instead of troubleshooting live."),
        ("Do you manage this ongoing, or just set it up once?", "Both are available. Some clients want a one-time setup handed off to their team; others prefer we manage it on an ongoing basis."),
        ("What access do you need?", 'We\'ll need hosting/server access and access to any existing repository, network, or directory service depending on scope. <a href="contact.html">Open a support ticket</a> and we\'ll guide you through it.'),
    ],
    closing_heading="Ready for Infrastructure You Can Trust?",
    closing_sub="From CI/CD pipelines to firewalls and Active Directory, we scope exactly what your infrastructure needs on a free call, then send a clear quote.",
    cta_label="Get a Custom Quote",
    hero_stats=[
        ("\U0001F5A5️", "Custom", "Scoped Engagements"),
        ("\U0001F4DE", "Free", "Scoping Call"),
        ("\U0001F4B0", "Money-Back", "Guarantee on Setup"),
        ("✅", "No", "Long-Term Contract"),
    ],
)

# --------------------------------------------------------------------------
# REDESIGN & DEVELOPMENT — tiered pricing page (Rebuild / Redesign / New
# Website) plus one-time development sessions, merged into one service.
# --------------------------------------------------------------------------

redesign_body = service_hero(
    "Redesign & Development",
    "Redesign, Rebuild & Custom Development",
    "Modernize your website with a redesign or rebuild, or book a one-time development session for new features and integrations.",
    "10,000+ issues resolved · 200+ five-star reviews · Projects from $1,995 · Trusted by 1,000+ site owners",
    "Start My Website Project",
    hero_stats=[
        ("\U0001F527", "10,000+", "Issues Resolved"),
        ("⭐", "200+", "Five-Star Reviews"),
        ("\U0001F4B0", "$1,995", "Starting Price"),
        ("\U0001F91D", "1,000+", "Site Owners Trust Us"),
    ],
)

redesign_body += """
<section class="section">
  <div class="container" style="max-width:820px;">
    <h2 class="text-center">Is Your Website Holding You Back?</h2>
    <p class="text-center">If your website is built on an outdated or unsupported WordPress theme, it may be quickly limiting your growth.</p>
    <ul class="checklist problem-list grid grid-2" style="max-width:640px;margin:24px auto;">
      <li>Slow loading speeds</li>
      <li>Bugs or recurring technical issues</li>
      <li>Security vulnerabilities</li>
      <li>Poor mobile experience</li>
      <li>Difficult or risky updates</li>
      <li>Dated or unprofessional design</li>
      <li>Declining traffic or search visibility</li>
      <li>A website that no longer reflects your business</li>
    </ul>
    <p>Visitors expect a modern, seamless experience. When a site feels clunky or outdated, trust drops and visitors leave. Our WordPress redesign services fix the underlying foundation, improve performance and security, and give you a website that's easier to manage and built to support long-term growth.</p>
  </div>
</section>
"""

redesign_body += """
<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <h2>What We Offer</h2>
      <p>We provide three options depending on how much change your website needs. Each service is designed to remove risk, modernize your site, and deliver a reliable WordPress foundation.</p>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <div class="icon">\U0001F5A5️</div>
        <h3>WordPress Rebuild</h3>
        <p>Rebuild your existing WordPress website using the same layout and content, but on a modern, secure, and fully supported foundation. Ideal if your site looks fine but is held back by an outdated or abandoned theme — we fix the technical foundation without changing the design, resulting in a faster, safer, easier-to-manage website.</p>
      </div>
      <div class="card">
        <div class="icon">\U0001F527</div>
        <h3>WordPress Redesign</h3>
        <p>We redesign your WordPress website with a fresh, modern look while keeping the content and structure that still works. The right choice if your site feels outdated or no longer reflects your brand — we deliver improved usability, mobile responsiveness, and layouts that guide visitors toward action.</p>
      </div>
      <div class="card">
        <div class="icon">\U0001F680</div>
        <h3>New Website</h3>
        <p>Designed for businesses starting fresh or making a complete change. We design, build, and launch a new WordPress website from the ground up — a custom layout, brand-aligned styling, mobile-first design, and a scalable WordPress foundation built for growth.</p>
      </div>
    </div>
  </div>
</section>
"""

redesign_body += """
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Compare Packages</h2>
    </div>
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead>
          <tr>
            <th></th>
            <th>WordPress Rebuild<span class="tier-price">From $1,995</span></th>
            <th class="popular"><span class="tier-badge">Most Popular</span><br>WordPress Redesign<span class="tier-price">From $5,995</span></th>
            <th>New Website<span class="tier-price">From $7,995</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Built with WordPress</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Reliable, supported theme</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Mobile-responsive design</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Easy content management</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Google Analytics integration</td><td class="yes">✓</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>New design and layout</td><td class="no">—</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Visual branding and styling</td><td class="no">—</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Conversion-focused page layouts</td><td class="no">—</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Basic on-site SEO setup</td><td class="no">—</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Content guidance</td><td class="no">—</td><td class="yes">✓</td><td class="yes">✓</td></tr>
          <tr><td>Revisions included</td><td class="no">—</td><td>1-2 rounds</td><td>Up to 3 rounds</td></tr>
          <tr><td>Estimated turnaround</td><td>4 weeks</td><td>8 weeks</td><td>12 weeks</td></tr>
        </tbody>
      </table>
    </div>
    <p class="hint text-center" style="margin-top:16px;">Pricing shown is a starting point — confirm exact scope-based pricing before launch.</p>
  </div>
</section>
"""

redesign_body += """
<section class="section">
  <div class="container" style="max-width:820px;">
    <h2 class="text-center">Just Need Development Work, Not a Full Redesign?</h2>
    <p class="text-center">If you want new features, layout updates, or integrations without a full rebuild, book a one-time development session instead — no ongoing contract required.</p>
  </div>
</section>
"""

redesign_body += feature_cards(
    "One-Time Development Sessions",
    "Hire an experienced developer for a half-day or full day to complete focused work — starting at $399 for a half-day or $798 for a full day.",
    [
        ("⚙️", "Custom Features", "We build tailored functionality such as booking tools, user dashboards, or e-commerce enhancements to support your website's needs."),
        ("\U0001F3A8", "Design Updates", "We improve layouts, styling, and page structure to create a cleaner, more effective user experience."),
        ("\U0001F50C", "Third-Party Integrations", "We connect your website with payment systems, CRMs, marketing tools, and other third-party services."),
        ("\U0001F4C4", "Content Enhancements", "We improve how content is displayed to make it clearer, more engaging, and easier for visitors to use."),
        ("\U0001F4BB", "Advanced Development", "We handle complex development tasks, custom code, and advanced functionality with care and precision."),
        ("\U0001F4A1", "Strategic Planning", "We provide clear guidance during your development session to ensure the work completed delivers real value."),
    ],
)

redesign_body += three_steps(
    "Our WordPress Redesign Process",
    "We follow a clear, structured process so you always know what's happening and what comes next.",
    [
        ("Project Review", "We review your current site, goals, and requirements to understand exactly what you need."),
        ("Quote & Timeline", "You receive a clear quote and estimated timeline before any work begins."),
        ("Development", "Our team designs, builds, and tests your new WordPress site, keeping you updated throughout."),
    ],
)

redesign_body += cta_banner(
    "Ready to Modernize Your Website?",
    "Whether you need a light rebuild or a complete redesign, we'll help you choose the right option and get started with a clear quote.",
    "Start My Website Project",
)

page("services-redesign-development.html", "Redesign & Development Services", "Redesign, rebuild, or launch a new website with a modern, conversion-focused foundation — or book a one-time development session.", redesign_body, og_image="assets/og-redesign-development.png")

# --------------------------------------------------------------------------
# STANDALONE MAINTENANCE PLAN LANDING PAGE
# --------------------------------------------------------------------------

maint_body = service_hero(
    "Maintenance Plan",
    "WordPress Maintenance Plan",
    "Keep your WordPress website updated, secure, and running smoothly — without lifting a finger.",
    "10,000+ issues resolved · 200+ five-star reviews · Maintenance from $89/month · 30-day money-back guarantee",
    "Discuss My Site",
    hero_checklist=("SLA & Service Commitment", [
        "Fast Response Times",
        "Priority-Based Support",
        "Scheduled Maintenance",
        "Security &amp; Backup Monitoring",
        "Transparent Communication",
        "Monthly Service Reports",
        "Emergency Support Available",
        "Clear Escalation Process",
    ]),
)

maint_body += """
<section class="section">
  <div class="container" style="max-width:820px;">
    <h2 class="text-center">Is WordPress Maintenance Right for You?</h2>
    <p>If you're tired of handling updates, fixes, and website issues yourself, our WordPress Maintenance Plan takes care of it for you.</p>
    <p>We handle routine updates, monitoring, and small fixes behind the scenes so your site stays secure, stable, and running smoothly without constant attention.</p>
    <p>If it's not the right fit, you're covered by our 30-day money-back guarantee. No hassle, no risk.</p>
  </div>
</section>
"""

maint_body += three_steps(
    "How Our WordPress Maintenance Plan Works",
    "A simple, repeatable process that keeps your site running smoothly month after month.",
    [
        ("Contact", "Tell us about your WordPress website and any ongoing support needs."),
        ("Setup", "We review your site, configure backups and monitoring, and begin routine updates."),
        ("Maintain", "We provide ongoing WordPress maintenance, checks, and fixes as part of your monthly plan."),
    ],
)

maint_body += feature_cards(
    "About the WordPress Maintenance Plan",
    "A reliable WordPress maintenance service designed to cover everyday upkeep and small fixes.",
    [
        ("\U0001F527", "Quick Fixes", "Unlimited small fixes (up to 30 minutes each) to handle common WordPress issues, tweaks, and adjustments."),
        ("\U0001F504", "Regular Updates", "WordPress core, theme, and plugin updates applied routinely to reduce risk and avoid problems."),
        ("\U0001F4BE", "Daily Backups", "Automatic daily backups so your site can be restored quickly if anything goes wrong."),
        ("\U0001F512", "Security Monitoring", "Daily security checks to spot issues early and keep your website protected."),
        ("⏱️", "24/7 Uptime Monitoring", "We monitor your website every minute, every day of the week, and respond quickly if it goes offline."),
        ("\U0001F4CA", "Detailed Reports", "Clear reports showing updates, checks, and recommendations, so you always know what's been done."),
    ],
)

_maint_faq_html = faq_block([
    ("How long does it take to set up the WordPress maintenance plan?", "We usually begin setup within one business day. Most sites are fully onboarded within 1-2 business days."),
    ("What's included in the $89/month maintenance plan?", "The plan includes updates, daily backups, uptime monitoring, security checks, and unlimited small fixes up to 30 minutes each."),
    ("What if my site needs a bigger repair?", "Larger issues aren't included, but we'll explain the options clearly and provide a quote before doing any additional work."),
    ("How do you monitor my website's uptime?", "We check your site every minute, every day of the week. If it goes offline, our team is alerted and investigates promptly."),
    ("What access do you need to get started?", "We need WordPress admin access and hosting access, or FTP credentials if hosting access isn't available."),
    ("How do I sign up for the monthly maintenance plan?", "<a href='care-plans.html'>Choose your plan from the comparison page</a>, or <a href='contact.html'>discuss your site with us</a> first if you'd like guidance."),
])
maint_body += f"""
<section class="section">
  <div class="container" style="max-width:760px;">
    <div class="section-head"><h2>Frequently Asked Questions</h2></div>
    {_maint_faq_html}
  </div>
</section>
"""

maint_body += cta_banner(
    "Keep Your Website Running Smoothly",
    "Avoid missed updates, plugin issues, and unexpected downtime. The WordPress Maintenance Plan provides steady, reliable care so your website stays healthy without constant attention from you. If you'd like to confirm this is the right plan for your site, we're happy to review it and make a recommendation.",
    "Discuss My Site",
)

page("maintenance-plan.html", "WordPress Maintenance Plan", "Ongoing WordPress maintenance — updates, backups, monitoring, and small fixes from $89/month.", maint_body)

# --------------------------------------------------------------------------
# SAAS & SYSTEMS INTEGRATION — new service line. Copy below is a first
# draft to get the page live; replace with real platform names, specific
# case studies, and any certifications/compliance credentials before
# launch, especially for the Core Banking & Payment Systems section, which
# is a very different (and more trust-sensitive) buyer than the SaaS/CRM
# side and should eventually get its own proof points.
# --------------------------------------------------------------------------

service_page(
    slug="services-saas-systems-integration.html",
    eyebrow="SaaS & Integration",
    title="SaaS & Systems Integration",
    sub="A full business solution built on the Zoho Suite — CRM, Creator, Forms, Invoice, Meeting, and workflow automation — plus payment gateway integration and, where needed, core banking systems.",
    stat_line="Custom-scoped engagements · Free scoping call · Confidential handling of sensitive integrations",
    intro_heading="Your Tools Should Talk to Each Other",
    intro_paras=[
        "If your team is copying data between systems by hand, chasing invoices manually, or running sales, support, and billing out of separate spreadsheets, that's time and accuracy lost every single day.",
        "We set up and connect the tools that actually run your business day to day — Zoho CRM, Creator, Forms, Invoice, Meeting, and Flow for workflow automation — plus payment gateway integrations and, for clients who need it, core banking systems. These are different kinds of work with different stakes, and we scope and quote them separately.",
    ],
    steps=[
        ("Map", "We map your current tools, data flows, and the gaps or manual steps costing you time."),
        ("Connect", "We configure and connect the platforms — Zoho apps, other SaaS tools, or banking/payment systems as scoped — with proper authentication and data handling."),
        ("Verify", "We test data flows end-to-end and hand over clear documentation of what's connected and how."),
    ],
    about_cards=[
        ("\U0001F4C7", "Zoho CRM Setup &amp; Customization", "Pipelines, lead tracking, and sales automation configured and customized to match how your team actually sells."),
        ("\U0001F9F1", "Zoho Creator (Custom Apps)", "Purpose-built internal apps and databases for workflows that off-the-shelf software doesn't cover."),
        ("\U0001F4DD", "Zoho Forms &amp; Workflow Automation", "Forms that feed straight into your CRM or apps, with Zoho Flow automating the steps in between."),
        ("\U0001F9FE", "Zoho Invoice &amp; Billing", "Invoicing, recurring billing, and payment tracking set up and connected to the rest of your tools."),
        ("\U0001F4F9", "Zoho Meeting Setup", "Video meetings and webinars configured and integrated into your existing scheduling and CRM workflow."),
        ("\U0001F4B3", "Payment Gateway Integration", "Connecting payment gateways and processors to your website or systems, with careful attention to security and reconciliation."),
        ("\U0001F517", "SaaS-to-SaaS Integration &amp; Data Sync", "Connecting the platforms you already use so data moves automatically instead of being re-entered by hand."),
        ("\U0001F3E6", "Core Banking Systems Integration", "Integration work with core banking platforms for financial institutions — scoped individually given the sensitivity and compliance requirements involved."),
        ("\U0001F510", "Secure, Confidential Handling", "NDAs and confidentiality as standard for any engagement touching financial or customer-sensitive systems."),
    ],
    faq_items=[
        ("Do you only work with Zoho?", "Zoho is our primary SaaS suite — CRM, Creator, Forms, Invoice, Meeting, and Flow — but we work with other CRM and business SaaS tools too. Tell us what you're using or considering."),
        ("Can you set up a complete business system, not just one app?", "Yes — that's the point of this service. We connect CRM, forms, billing, meetings, and workflow automation into one working system instead of separate disconnected tools."),
        ("What's the difference between the SaaS side and the banking side of this service?", "SaaS/CRM integration is general business tooling — most companies need it. Core banking and payment systems integration is specialized, higher-stakes work for financial institutions or businesses processing payments at scale. We scope and price these very differently."),
        ("Do you sign NDAs?", "Yes, standard practice for any integration touching financial data, customer PII, or proprietary systems."),
        ("How is this priced?", "Scoped per engagement — a Zoho/CRM setup and a core banking integration have very different levels of effort and risk, so we quote after understanding what you actually need."),
        ("What do you need to get started?", 'Tell us which systems need to talk to each other and what\'s not working today. <a href="contact.html">Open a support ticket</a> and we\'ll schedule a scoping call.'),
    ],
    closing_heading="Stop Moving Data by Hand",
    closing_sub="Whether it's a CRM setup or a core banking integration, we'll scope exactly what's needed on a free call, then send a clear quote.",
    cta_label="Get a Custom Quote",
    hero_stats=[
        ("\U0001F50C", "Custom", "Scoped Engagements"),
        ("\U0001F4DE", "Free", "Scoping Call"),
        ("\U0001F510", "Confidential", "Integration Handling"),
        ("✅", "No", "Long-Term Contract"),
    ],
)

# --------------------------------------------------------------------------
# AI DEVELOPMENT & INTEGRATION — new service line. First-draft copy;
# replace with specific tools/models used and real project examples
# before launch.
# --------------------------------------------------------------------------

service_page(
    slug="services-ai-development-integration.html",
    eyebrow="AI Development",
    title="AI Development & Integration",
    sub="Custom chatbots, automation, and AI features built into your website or business systems — practical AI, not hype.",
    stat_line="Custom-scoped engagements · Free scoping call · Money-back guarantee on setup work",
    intro_heading="Where Does AI Actually Save You Time?",
    intro_paras=[
        "Most businesses don't need \"AI\" in the abstract — they need one or two specific, repetitive tasks handled automatically: answering common customer questions, summarizing documents, drafting responses, sorting requests.",
        "We build and integrate AI features scoped to a real workflow — a chatbot on your website, an internal automation, or a custom integration with an AI API — rather than bolting on a generic tool that doesn't fit how you work.",
    ],
    steps=[
        ("Identify", "We find the specific task or workflow where AI will actually save time, not just sound impressive."),
        ("Build", "We build and integrate the chatbot, automation, or AI feature into your website or existing systems."),
        ("Refine", "We test with real inputs, tune it based on results, and document how it works and how to maintain it."),
    ],
    about_cards=[
        ("\U0001F916", "Website Chatbots", "Custom chatbots trained on your business content to answer visitor and customer questions automatically."),
        ("\U0001F504", "Workflow Automation", "AI-assisted automation for repetitive tasks — sorting requests, drafting responses, summarizing documents."),
        ("\U0001F50C", "AI API Integration", "Integrating AI models and APIs into your existing website, CRM, or internal tools."),
        ("\U0001F4DD", "Content &amp; Document AI", "Tools for summarizing, drafting, or processing documents and content at scale."),
        ("\U0001F4CA", "Custom AI Features", "Purpose-built AI functionality for your specific product or business, not a generic off-the-shelf plugin."),
        ("\U0001F6E1️", "Responsible Integration", "Clear handling of data privacy and model limitations, so you know what the system can and can't be trusted to do."),
    ],
    faq_items=[
        ("Do I need my own AI model?", "No. We typically integrate existing AI APIs and models rather than training one from scratch, which keeps cost and complexity down for most business use cases."),
        ("Will this actually save us time, or is it a gimmick?", "We scope against a specific workflow first — if AI isn't the right tool for what you're trying to solve, we'll tell you before building anything."),
        ("Can you add a chatbot to my existing website?", "Yes, including WordPress sites we've already built or repaired for you."),
        ("How is this priced?", "Scoped per project depending on complexity — a simple chatbot and a custom workflow integration are very different amounts of work."),
        ("What do you need to get started?", 'Tell us what task or workflow you want automated. <a href="contact.html">Open a support ticket</a> and we\'ll schedule a scoping call.'),
    ],
    closing_heading="Let's Find the AI That Actually Helps",
    closing_sub="Practical AI features scoped to a real workflow, not a generic bolt-on. We'll scope it on a free call, then send a clear quote.",
    cta_label="Get a Custom Quote",
    hero_stats=[
        ("\U0001F916", "Custom", "Scoped Engagements"),
        ("\U0001F4DE", "Free", "Scoping Call"),
        ("\U0001F4B0", "Money-Back", "Guarantee on Setup"),
        ("✅", "No", "Long-Term Contract"),
    ],
)

# --------------------------------------------------------------------------
# HOME PAGE
# --------------------------------------------------------------------------

home_body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow" style="background:rgba(255,255,255,0.14);color:#ffe1ad;">IT &amp; Digital Solutions</span>
        <h1>Website Repair, Infrastructure &amp; Custom Development — Handled by Experts</h1>
        <p class="lead">From fixing a broken website to running your infrastructure, integrating your systems, or building AI into your workflow — one team, start to finish.</p>
        <p class="lead" style="font-size:0.95rem;color:#b9cfe6;">Fixes from $49. No contracts. Expert, reliable support.</p>
        <div class="hero-cta">
          <a href="{{ROOT}}services.html" class="btn btn-primary btn-lg">Explore Services</a>
          <a href="{{ROOT}}contact.html" class="btn btn-outline btn-lg">Get a Free Quote</a>
        </div>
      </div>
      <div class="hero-art">
        <div class="orbit">
          <svg class="orbit-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
            <line x1="50" y1="50" x2="50" y2="10"></line>
            <line x1="50" y1="50" x2="78" y2="22"></line>
            <line x1="50" y1="50" x2="90" y2="50"></line>
            <line x1="50" y1="50" x2="78" y2="78"></line>
            <line x1="50" y1="50" x2="50" y2="90"></line>
            <line x1="50" y1="50" x2="22" y2="78"></line>
            <line x1="50" y1="50" x2="10" y2="50"></line>
            <line x1="50" y1="50" x2="22" y2="22"></line>
          </svg>
          <div class="orbit-hub"><span>\U0001F6E0️</span></div>
          <div class="orbit-node" style="top:10%;left:50%;">
            <span class="orbit-icon">\U0001F527</span>
            <span class="orbit-label">Repair &amp; Fixes</span>
          </div>
          <div class="orbit-node" style="top:22%;left:78%;">
            <span class="orbit-icon">\U0001F6E1️</span>
            <span class="orbit-label">Security</span>
          </div>
          <div class="orbit-node" style="top:50%;left:90%;">
            <span class="orbit-icon">\U0001F680</span>
            <span class="orbit-label">Speed</span>
          </div>
          <div class="orbit-node" style="top:78%;left:78%;">
            <span class="orbit-icon">\U0001F69A</span>
            <span class="orbit-label">Migration</span>
          </div>
          <div class="orbit-node" style="top:90%;left:50%;">
            <span class="orbit-icon">\U0001F3A8</span>
            <span class="orbit-label">Redesign &amp; Dev</span>
          </div>
          <div class="orbit-node" style="top:78%;left:22%;">
            <span class="orbit-icon">\U0001F5A5️</span>
            <span class="orbit-label">Infrastructure</span>
          </div>
          <div class="orbit-node" style="top:50%;left:10%;">
            <span class="orbit-icon">\U0001F50C</span>
            <span class="orbit-label">SaaS &amp; Integration</span>
          </div>
          <div class="orbit-node" style="top:22%;left:22%;">
            <span class="orbit-icon">\U0001F916</span>
            <span class="orbit-label">AI Development</span>
          </div>
        </div>
        <p style="color:#dbe8f5;margin-top:14px;font-size:0.9rem;">Web, infrastructure &amp; AI — handled for you, end to end.</p>
      </div>
    </div>
  </div>
</section>
<div class="trust-bar">
  <div class="container">
    <span>\U0001F527 10,000+ Issues Resolved</span>
    <span>\U0001F6E1️ Money-Back Guarantee</span>
    <span>⭐ 200+ Five-Star Reviews</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Is Your Website Broken, Hacked, or Slow?</span>
      <h2>We Repair Websites Every Day — Then Handle Whatever Comes Next</h2>
      <p>If you've searched "fix my website" or "website repair," you're in the right place. Whether your site is down or just not working as it should, we'll find the cause and fix it fast so everything runs smoothly again — and if you need more (security, infrastructure, integrations, AI), we handle that too.</p>
    </div>
    <ul class="checklist grid grid-3" style="max-width:820px;margin:0 auto;">
      <li>Broken pages, plugin errors, and theme display issues</li>
      <li>Hacked websites, malware alerts, and security problems</li>
      <li>Slow loading times on desktop and mobile</li>
    </ul>
  </div>
</section>
"""

home_body += feature_cards(
    "Fast Repairs for Common Website Problems",
    "Most customers come to us because their WordPress site has stopped working and they need help fast.",
    [
        ("\U0001F50C", "Plugin Conflicts or Update Failures", "Errors or downtime after updates are common. We identify what caused the issue, repair it, and make sure your plugins work together properly so updates stop breaking your site."),
        ("\U0001F5BC️", "Theme Display or Design Issues", "Broken layouts, missing sections, or visual glitches can make a site look unprofessional. We restore your theme and correct display problems so every page looks as it should."),
        ("\U0001F6D2", "Checkout or Form Bugs", "When checkout pages or forms stop working, you lose sales and enquiries. We inspect, test, and repair WooCommerce checkout issues and form errors so visitors can complete actions without problems."),
        ("⚠️", "White Screens or 500 Errors", "If your website won't load or shows server error messages, we investigate the cause and repair the issue blocking access so your site is back online quickly."),
        ("\U0001F41B", "Malware or Hacked Websites", "A hacked website can lock you out and scare visitors away. We remove malware, clean infected files, secure your site, and restore access fast."),
        ("\U0001F680", "Slow Website Performance", "A slow website frustrates visitors and hurts rankings. We identify what's slowing your site down and fix performance issues so pages load faster across all devices."),
    ],
    bg="light",
)

home_body += three_steps(
    "Simple, No-Fuss Website Repair",
    "Getting started is quick and straightforward.",
    [
        ("Tell Us What's Wrong", "Send a repair request with a short description of the problem."),
        ("We Get to Work", "We review your site, find the cause, and start fixing the issue."),
        ("You Relax", "Your website is repaired and running smoothly again."),
    ],
)

home_body += f"""
<section class="section section--blue">
  <div class="container">
    <div class="section-head">
      <h2>Our Services</h2>
      <p>One-time fixes and project work for the most common needs, or ongoing care plans if you'd rather not think about it at all.</p>
    </div>
    <div class="grid grid-4">
      <div class="card">
        <div class="icon">\U0001F527</div>
        <h3>Website Repair &amp; Small Fixes</h3>
        <p>Broken pages, plugin errors, white screens, or a quick edit — diagnosed and fixed fast.</p>
        <span class="price">From $49</span>
        <a href="{{ROOT}}services-website-repair-small-fixes.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F6E1️</div>
        <h3>Malware Removal &amp; Security</h3>
        <p>Full malware scan, cleanup, core file check, and security hardening in one service.</p>
        <span class="price">From $199</span>
        <a href="{{ROOT}}services-malware-removal-security-hardening.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F680</div>
        <h3>Speed Optimization</h3>
        <p>Caching, database cleanup, image compression, and Linux/Windows server tuning.</p>
        <span class="price">From $229</span>
        <a href="{{ROOT}}services-speed-optimization.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F69A</div>
        <h3>Migration</h3>
        <p>Website, database, software, or mail migrations with a full backup and reconfiguration.</p>
        <span class="price">From $149</span>
        <a href="{{ROOT}}services-migration.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F3A8</div>
        <h3>Redesign &amp; Development</h3>
        <p>Rebuild, redesign, or launch a new site — or book a one-time development session.</p>
        <span class="price">From $1,995</span>
        <a href="{{ROOT}}services-redesign-development.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F5A5️</div>
        <h3>Infrastructure &amp; DevOps</h3>
        <p>CI/CD, system administration, network &amp; firewall security, and virtualization/AD.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-infrastructure-devops.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F50C</div>
        <h3>SaaS &amp; Systems Integration</h3>
        <p>Zoho/SaaS setup and integration, plus core banking &amp; payment systems work.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-saas-systems-integration.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F916</div>
        <h3>AI Development &amp; Integration</h3>
        <p>Custom chatbots, workflow automation, and AI features built into your systems.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-ai-development-integration.html" class="card-link">Learn more →</a>
      </div>
    </div>
  </div>
</section>
"""

home_body += f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Choose {SITE_NAME}</span>
      <h2>Fast, Reliable WordPress Repairs With No Long-Term Commitments</h2>
    </div>
    <ul class="checklist grid grid-2" style="max-width:760px;margin:0 auto;">
      <li>Thousands of WordPress issues fixed for site owners worldwide</li>
      <li>200+ five-star reviews from real customers</li>
      <li>One-time website repairs with clear, upfront pricing</li>
      <li>Full money-back guarantee if we cannot complete the repair</li>
    </ul>
  </div>
</section>
"""

home_body += f"""
<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <h2>Trusted by WordPress Site Owners</h2>
      <p>Sample feedback — replace with your real customer reviews before launch.</p>
    </div>
    <div class="grid grid-3">
      <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p>"Our site was hacked and showing warnings in Chrome. {SITE_NAME} cleaned it up and had us back online the same day."</p>
        <div class="who">— Sample review, replace with a real one</div>
      </div>
      <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p>"Clear pricing, fast turnaround, and they explained exactly what was wrong. Would use again."</p>
        <div class="who">— Sample review, replace with a real one</div>
      </div>
      <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p>"Our checkout page had been broken for days before we found them. Fixed within hours."</p>
        <div class="who">— Sample review, replace with a real one</div>
      </div>
    </div>
  </div>
</section>
"""

home_body += f"""
<section class="section section--blue">
  <div class="container" style="max-width:760px;">
    <div class="section-head"><h2>Frequently Asked Questions</h2></div>
    {faq_block([
        ("What counts as a website repair?", "Plugin errors, broken layouts, white screens, site crashes, or features that stop working. If something is broken or behaving unpredictably, it usually counts as a repair."),
        ("How fast will my issue be fixed?", "Most website repairs are completed within 24 hours, often the same day. If a request is more complex, we'll let you know upfront."),
        ("Is there a contract?", "No. All website repairs are one-time fixes with no ongoing commitment."),
        ("Do you repair WooCommerce sites?", "Yes. We fix WooCommerce checkout problems, broken product pages, and payment issues."),
    ])}
    <p class="text-center" style="margin-top:24px;"><a href="{{ROOT}}about.html">See more FAQs →</a></p>
  </div>
</section>
"""

home_body += cta_banner(
    "Whatever It Is, Let's Fix It or Build It",
    "One-time website repairs and security hardening, ongoing infrastructure, systems integration, and AI development — all under one team. Fast turnaround. No long-term contracts required. Fixes start at $49 with a full money-back guarantee.",
    "Get a Free Quote",
)

page("index.html", "IT, Web & Infrastructure Solutions", "We fix broken, hacked, and slow websites, run infrastructure and DevOps, integrate SaaS and banking systems, and build AI features — one team, start to finish.", home_body)

# --------------------------------------------------------------------------
# SERVICES OVERVIEW PAGE
# --------------------------------------------------------------------------

services_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{{ROOT}}index.html">Home</a> / Services</div>
    <h1>IT, Web &amp; Infrastructure Services</h1>
    <p style="max-width:640px;">From one-time website repairs to infrastructure, integrations, and AI development. Pick what you need, or send us a request and we'll diagnose it or scope it for you.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card">
        <div class="icon">\U0001F527</div>
        <h3>Website Repair &amp; Small Fixes</h3>
        <p>Broken pages, plugin errors, white screens, and site crashes — diagnosed and fixed fast, plus quick edits and small feature additions.</p>
        <span class="price">From $49</span>
        <a href="{{ROOT}}services-website-repair-small-fixes.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F6E1️</div>
        <h3>Malware Removal &amp; Security Hardening</h3>
        <p>Full scan, malware cleanup, core file check, blacklist removal, and proactive security hardening.</p>
        <span class="price">From $199</span>
        <a href="{{ROOT}}services-malware-removal-security-hardening.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F680</div>
        <h3>Speed Optimization</h3>
        <p>Caching, database cleanup, image compression, plugin audits, and Linux/Windows server tuning.</p>
        <span class="price">From $229</span>
        <a href="{{ROOT}}services-speed-optimization.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F69A</div>
        <h3>Migration</h3>
        <p>Zero-downtime website, database, software, or mail-server migration, backup included.</p>
        <span class="price">From $149</span>
        <a href="{{ROOT}}services-migration.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F3A8</div>
        <h3>Redesign &amp; Development</h3>
        <p>Rebuild, redesign, or fully relaunch your site — or book a one-time development session for new features.</p>
        <span class="price">From $1,995</span>
        <a href="{{ROOT}}services-redesign-development.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F5A5️</div>
        <h3>Infrastructure &amp; DevOps</h3>
        <p>CI/CD pipelines, system administration, network &amp; firewall security, and virtualization/Active Directory.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-infrastructure-devops.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F50C</div>
        <h3>SaaS &amp; Systems Integration</h3>
        <p>Zoho and business SaaS setup and integration, plus core banking &amp; payment systems work.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-saas-systems-integration.html" class="card-link">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">\U0001F916</div>
        <h3>AI Development &amp; Integration</h3>
        <p>Custom chatbots, workflow automation, and AI features built into your website or business systems.</p>
        <span class="price price-quote">Custom Quote</span>
        <a href="{{ROOT}}services-ai-development-integration.html" class="card-link">Learn more →</a>
      </div>
    </div>
  </div>
</section>
"""
services_body += cta_banner("Not Sure Which Service You Need?", "Send us a request and we'll review it and recommend the right fix or scope — no pressure, no hard sell.", "Get a Free Assessment")

page("services.html", "IT, Web &amp; Infrastructure Services", "Website repair, security hardening, speed optimization, migration, redesign, infrastructure, SaaS integration, and AI development.", services_body)

# --------------------------------------------------------------------------
# CARE PLANS PAGE  (placeholder pricing — confirm real numbers before launch)
# --------------------------------------------------------------------------

care_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{{ROOT}}index.html">Home</a> / Care Plans</div>
    <h1>WordPress Care Plans</h1>
    <p style="max-width:640px;">Keep your site secure, fast, and running smoothly with expert monthly support and proactive maintenance. No contracts. Cancel anytime.</p>
  </div>
</section>
"""

care_body += feature_cards(
    "WordPress Care Plans For Different Types Of Sites",
    "Understand the differences between Maintenance, Security, and Performance plans so you can quickly see which level of care your website needs.",
    [
        ("\U0001F3D7️", "Maintenance — Reliable upkeep for everyday websites", "Best for personal sites, blogs, and small business websites with low to moderate traffic that need steady maintenance, dependable support, and peace of mind when small issues crop up."),
        ("\U0001F46E", "Security — Stronger protection for sensitive sites", "Best for eCommerce, membership, and lead generation websites handling logins, payments, and customer data where security, stability, and uptime are critical to day-to-day operations."),
        ("\U0001F680", "Performance — Speed and priority support for busy sites", "Best for content-driven blogs, marketing sites, and revenue-critical websites with high traffic and image-heavy pages, where traffic spikes and slowdowns have a real business impact."),
    ],
)

care_body += f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Compare WordPress Care Plans and Pricing</h2>
      <p>Free WordPress health check included when you sign up (normally $99).</p>
    </div>
    <div class="grid grid-3">
      <div class="plan-card">
        <h3>Maintenance Plan</h3>
        <div class="plan-price">$99 <span>/ month</span></div>
        <p style="font-size:0.82rem;color:var(--color-body);margin-top:-8px;">Month-to-month</p>
        <p style="font-size:0.9rem;">Reliable upkeep for personal sites, blogs, and small business websites.</p>
        <ul>
          <li>Weekly WordPress Updates</li>
          <li>Daily Offsite Backups</li>
          <li>Security &amp; Uptime Monitoring</li>
          <li>Monthly Reports</li>
          <li>Website Repair</li>
          <li>Email Support</li>
        </ul>
        <a href="{{ROOT}}maintenance-plan.html" class="btn btn-secondary btn-block">Get Started</a>
      </div>
      <div class="plan-card popular">
        <span class="plan-badge">Most Popular</span>
        <h3>Security Plan</h3>
        <div class="plan-price">$159 <span>/ month</span></div>
        <p style="font-size:0.82rem;color:var(--color-body);margin-top:-8px;">Month-to-month</p>
        <p style="font-size:0.9rem;">Stronger protection for eCommerce and membership sites handling sensitive data.</p>
        <ul>
          <li><strong>All Maintenance Features</strong></li>
          <li>Security Hardening</li>
          <li>Advanced Security Monitoring</li>
          <li>Small Tasks</li>
          <li>Malware Removal</li>
          <li>eCommerce &amp; Membership Support</li>
        </ul>
        <a href="{{ROOT}}contact.html" class="btn btn-primary btn-block">Get Started</a>
      </div>
      <div class="plan-card">
        <h3>Performance Plan</h3>
        <div class="plan-price">$239 <span>/ month</span></div>
        <p style="font-size:0.82rem;color:var(--color-body);margin-top:-8px;">Month-to-month</p>
        <p style="font-size:0.9rem;">Speed and priority support for high-traffic or growing websites.</p>
        <ul>
          <li><strong>All Maintenance + Security Features</strong></li>
          <li>Speed Optimization</li>
          <li>Image Optimization</li>
          <li>Premium Plugin Bundle</li>
          <li>Performance Monitoring</li>
          <li>Priority Support</li>
        </ul>
        <a href="{{ROOT}}contact.html" class="btn btn-secondary btn-block">Get Started</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--blue">
  <div class="container">
    <div style="max-width:640px;margin:0 auto;text-align:center;display:flex;gap:20px;align-items:center;background:#fff;padding:24px 28px;border-radius:var(--radius-md);box-shadow:var(--shadow-sm);">
      <span style="font-size:2.2rem;">\U0001F4AF</span>
      <div style="text-align:left;">
        <h3 style="margin-bottom:4px;">Your Satisfaction, Guaranteed</h3>
        <p style="margin:0;font-size:0.92rem;">We stand behind every WordPress care plan we offer. If you're not completely satisfied within the first 30 days, we'll give you a full refund. No hassle, no hard feelings.</p>
      </div>
    </div>
  </div>
</section>
"""

care_body += feature_cards(
    "Included In Every Plan",
    "Core WordPress maintenance and support, handled for you.",
    [
        ("\U0001F504", "Weekly WordPress Updates", "Core, theme, and plugin updates handled weekly to reduce risk and avoid breakages."),
        ("\U0001F4BE", "Daily Offsite Backups", "Automatic daily backups so your site can be restored quickly if anything goes wrong."),
        ("⏱️", "Every-Minute Uptime Monitoring", "We check your site every minute to ensure it stays online and responsive."),
        ("\U0001F6E1️", "Security Checks", "Ongoing security checks to catch issues early and keep your site protected."),
        ("\U0001F527", "Website Repairs", "Small 30-minute repairs with clear notes explaining what we changed and why."),
        ("\U0001F4CA", "Monthly Reports", "A simple monthly summary with updates, checks, and recommendations for what to improve next."),
    ],
)

care_body += three_steps(
    "How It Works",
    "Getting started is simple. Choose a plan, share access, and we begin ongoing care.",
    [
        ("Choose Your Plan", "Pick the plan that fits your website and traffic level, then complete checkout."),
        ("Share Access Securely", "We guide you through secure access so we can manage your website safely."),
        ("Ongoing Care Begins", "We handle updates, monitoring, and fixes to keep your website running smoothly."),
    ],
)

_care_rows = [
    ("Weekly WordPress Updates", True, True, True),
    ("Daily Offsite Backups", True, True, True),
    ("Daily Security Checks", True, True, True),
    ("Every Minute Uptime Monitoring", True, True, True),
    ("Repairs (30 min)", True, True, True),
    ("Detailed Repair Notes", True, True, True),
    ("Monthly Report", True, True, True),
    ("Email Support", True, True, True),
    ("Weekly Performance Check", True, True, True),
    ("Broken Link Monitoring", True, True, True),
    ("Weekly Spam Cleanup", True, True, True),
    ("Google Analytics Connected", True, True, True),
    ("Security Hardening", False, True, True),
    ("Web Application Firewall (WAF)*", False, True, True),
    ("Malware Removal", False, True, True),
    ("Server-Side Malware Scanner", False, True, True),
    ("Audit Logs", False, True, True),
    ("Security Checks (Every 6 hours)", False, True, True),
    ("Extra Backup Location*", False, True, True),
    ("Small Tasks (15 min)", False, True, True),
    ("eCommerce Site Support", False, True, True),
    ("Membership Site Support", False, True, True),
    ("Advanced Site Support", False, True, True),
    ("Speed Optimization", False, False, True),
    ("Mobile &amp; Tablet Optimization", False, False, True),
    ("Image Optimization", False, False, True),
    ("Content Delivery Network (CDN)*", False, False, True),
    ("Quality Assurance Checks", False, False, True),
    ("Free Hosting for Extra Sites", False, True, True),
]
_care_rows_html = ""
for label, m, s, p in _care_rows:
    cell = lambda v: '<td class="yes">✓</td>' if v else '<td class="no">—</td>'
    _care_rows_html += f"<tr><td>{label}</td>{cell(m)}{cell(s)}{cell(p)}</tr>"
_care_rows_html += '<tr><td>Average Response Time</td><td>8 hours</td><td>8 hours</td><td>4 hours</td></tr>'
_care_rows_html += '<tr><td>Repair Requests at a Time</td><td>1</td><td>1</td><td>Up to 3</td></tr>'
_care_rows_html += '<tr><td>Managed Hosting (Optional)</td><td>Essential</td><td>Enhanced</td><td>VIP</td></tr>'

care_body += f"""
<section class="section section--light">
  <div class="container">
    <div class="section-head">
      <h2>Compare Our WordPress Care Plans</h2>
      <p>See what's included at each level and how Maintenance, Security, and Performance compare.</p>
    </div>
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead>
          <tr><th></th><th>Maintenance</th><th class="popular">Security</th><th>Performance</th></tr>
        </thead>
        <tbody>
          {_care_rows_html}
        </tbody>
      </table>
    </div>
    <p class="hint" style="margin-top:14px;">* Hosting-level features (such as WAF, extra backup location, and CDN) apply when using {SITE_NAME} managed hosting.</p>
  </div>
</section>
"""

care_body += f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <h2>Managed Cloud Hosting Resources</h2>
      <p>When hosting is added, resources scale with your plan, from Essential to VIP.</p>
    </div>
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead><tr><th></th><th>Essential</th><th class="popular">Enhanced</th><th>VIP</th></tr></thead>
        <tbody>
          <tr><td>Memory (RAM)</td><td>2GB</td><td>4-8GB</td><td>16-32GB</td></tr>
          <tr><td>CPU</td><td>1 Premium AMD CPU</td><td>2-4 Premium AMD CPUs</td><td>8 Premium AMD CPUs</td></tr>
          <tr><td>Storage</td><td>50GB NVMe SSD</td><td>80-160GB NVMe SSD</td><td>320-400GB NVMe SSD</td></tr>
          <tr><td>Data Transfer</td><td>2TB per month</td><td>4-5TB per month</td><td>6-10TB per month</td></tr>
          <tr><td>Estimated Monthly Visits</td><td>~50,000</td><td>~100,000-200,000</td><td>~300,000-600,000</td></tr>
        </tbody>
      </table>
    </div>
    <p class="hint" style="margin-top:14px;">Visit estimates are guidelines. Actual usage depends on page weight, caching, traffic patterns, and bot activity.</p>
  </div>
</section>
"""

care_body += feature_cards(
    "Included When You Add Hosting",
    f"When you choose {SITE_NAME} hosting, everything is fully managed by our team.",
    [
        ("\U0001F5A5️", "WordPress Cloud Hosting", "High-performance cloud servers optimized for WordPress, designed to load fast and remain stable during traffic spikes."),
        ("\U0001F310", "Domain and DNS Management", "We manage your domain and DNS settings to keep your website accessible without downtime or technical headaches."),
        ("\U0001F512", "Free SSL Certificate", "A free SSL certificate protects visitor data, improves trust, and renews automatically to keep your site secure."),
        ("\U0001F4C4", "Staging Site", "Test changes safely in a staging environment before pushing them live, reducing the risk of broken updates or errors."),
        ("✉️", "Transactional Emails", "Reliable delivery for contact forms, order confirmations, password resets, and other essential website emails."),
        ("\U0001F5C4️", "Server Backups", "Regular server-level backups provide additional restore points if anything needs to be rolled back quickly."),
    ],
    bg="light",
)

care_body += f"""
<section class="section">
  <div class="container" style="max-width:760px;">
    <div class="section-head"><h2>Care Plan FAQ</h2></div>
    {faq_block([
        ("Can I cancel anytime?", "Yes. All care plans are month-to-month with no long-term contract — cancel anytime."),
        ("What happens if I need more than my plan includes?", "We'll always confirm scope and any extra cost with you before doing additional work beyond your plan."),
        ("Do you offer a free health check?", "Yes — a free WordPress health check is included when you sign up for any care plan (normally $99)."),
    ])}
  </div>
</section>
"""
care_body += cta_banner("Not Sure Which Plan Is Right for You?", "We'll review your site and recommend the best care plan with no pressure, no hard sell, and honest advice from a team that has resolved over 10,000 WordPress issues.", "Discuss My Site")

page("care-plans.html", "WordPress Care Plans", "Monthly WordPress maintenance, security, and performance care plans with no contracts.", care_body)

# --------------------------------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------------------------------

about_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{{ROOT}}index.html">Home</a> / About</div>
    <h1>About {SITE_NAME}</h1>
    <p style="max-width:640px;">We're an IT and digital services team — website repair and security, infrastructure and DevOps, systems integration, and AI development — for owners, marketers, and agencies worldwide.</p>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px;">
    <div class="section-head"><h2>General Questions</h2></div>
    {faq_block([
        (f"What does {SITE_NAME} do?", "We started as WordPress specialists and still handle website repair, security, and performance every day — one-time fixes and monthly care plans. We've since expanded into infrastructure and DevOps, SaaS and systems integration, and AI development for clients who need more than just a website fixed."),
        ("Do you only work with WordPress?", "No, though it's still a large part of what we do and where we started. We also handle server infrastructure, network and system administration, SaaS/CRM and banking-systems integration, and AI development — see the full list on our <a href='services.html'>Services page</a>."),
        ("Where are you based?", f"We're a fully remote team serving the global market, in every time zone. Reach us any time at {EMAIL_DISPLAY}."),
        ("Who do you work with?", "We help business owners, marketers, and agencies who need anything from a website fix to infrastructure work, systems integration, or custom AI development. Our services take the technical burden off your plate so you can focus on your business."),
    ])}
  </div>
</section>
"""
about_body += cta_banner("Not Sure Which Service Is Right for You?", "We'll review what you need and recommend the right service or plan — no pressure, no hard sell, and honest advice.", "Discuss My Project")

page("about.html", f"About {SITE_NAME}", f"Learn about {SITE_NAME} — website repair, security, infrastructure, systems integration, and AI development.", about_body)

# --------------------------------------------------------------------------
# CONTACT / SUPPORT REQUEST PAGE
# --------------------------------------------------------------------------

contact_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{{ROOT}}index.html">Home</a> / Contact</div>
    <h1>Get a Free Quote</h1>
    <p style="max-width:640px;">Tell us what you need — a website fix, security work, infrastructure, an integration, or an AI feature. We'll get back to you fast with a quote or next steps.</p>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px;">
    <form class="support-form" id="repair-form" action="{FORM_ENDPOINT}" method="post" enctype="multipart/form-data">
      <!-- Honeypot: real visitors never see or fill this in (hidden via CSS).
           The mail-relay Worker treats any submission with this field
           non-empty as a bot and silently drops it. -->
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div class="form-row">
        <div class="form-group">
          <label>Your First Name <span class="req">*</span></label>
          <input type="text" name="first_name" required>
        </div>
        <div class="form-group">
          <label>Your Last Name <span class="req">*</span></label>
          <input type="text" name="last_name" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label>Your Email <span class="req">*</span></label>
          <input type="email" name="email" required>
        </div>
        <div class="form-group">
          <label>Confirm Email <span class="req">*</span></label>
          <input type="email" name="email_confirm" required>
        </div>
      </div>
      <div class="form-group">
        <label>Website / Company URL <span class="req">*</span></label>
        <input type="url" name="website_url" placeholder="https://yourwebsite.com (or your company site, if this isn't about an existing website)" required>
      </div>
      <div class="form-group">
        <label>What do you need help with? <span class="req">*</span></label>
        <textarea name="issue" maxlength="1000" placeholder="e.g. Homepage shows an error, site hacked, need a firewall set up, want to integrate Zoho, want a chatbot on our site" required></textarea>
        <div class="hint">Max 1000 characters.</div>
      </div>
      <div class="form-group">
        <label>Upload Screenshots (optional)</label>
        <input type="file" name="screenshots" multiple>
        <div class="hint">Add any files or screenshots that help explain the issue. 10MB combined limit.</div>
      </div>
      <div class="form-group radio-group">
        <label>How soon do you need it? <span class="req">*</span></label>
        <label><input type="radio" name="urgency" value="urgent" required> \U0001F525 Urgent — ASAP (within hours)</label>
        <label><input type="radio" name="urgency" value="soon"> \U0001F680 Soon — Next 24 hours</label>
        <label><input type="radio" name="urgency" value="no_rush"> \U0001F550 No rush — Within a few days</label>
      </div>
      <div class="form-group">
        <label>Who's your hosting provider? (optional)</label>
        <input type="text" name="hosting_provider" placeholder="e.g. SiteGround, Bluehost, GoDaddy">
      </div>
      <div class="form-group checkbox-group">
        <label><input type="checkbox" required> I confirm that I've read and agree to the <a href="{{ROOT}}terms.html">terms and conditions</a>.</label>
        <label><input type="checkbox" required> I consent to {SITE_NAME} storing my information in accordance with the <a href="{{ROOT}}privacy.html">privacy policy</a>, so they can respond to my request.</label>
      </div>
      <button type="submit" class="btn btn-primary btn-lg btn-block">Send</button>
      <p class="hint text-center" id="form-note" style="margin-top:14px;">Your request goes straight to our inbox — we typically reply the same day.</p>
    </form>
  </div>
</section>
"""
contact_body += f"""
<section class="section section--navy">
  <div class="container text-center">
    <h2>How Can We Help?</h2>
    <p>For a free assessment of your website, simply send your request above or reach us directly.</p>
    <p style="color:#eaf2fb;">✉️ {EMAIL_DISPLAY} &nbsp;·&nbsp; \U0001F4DE {PHONE_DISPLAY}</p>
  </div>
</section>
"""

page("contact.html", "Get a Free Quote — Contact", f"Send a request to {SITE_NAME} and get a quote fast — website repair, security, infrastructure, integrations, or AI development.", contact_body)

# --------------------------------------------------------------------------
# CONTACT THANK-YOU PAGE — FormSubmit redirects here after a successful send
# --------------------------------------------------------------------------
thanks_body = f"""
<section class="page-hero">
  <div class="container text-center">
    <h1>Thanks — We've Got Your Request</h1>
    <p style="max-width:560px;margin-left:auto;margin-right:auto;">Your message is in our inbox. We typically reply the same day with a
    quote or next steps — for anything urgent, you can also reach us directly.</p>
  </div>
</section>
<section class="section">
  <div class="container text-center">
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a class="btn btn-primary btn-lg" href="{{ROOT}}index.html">Back to Home</a>
      <a class="btn btn-secondary btn-lg" href="{WHATSAPP_LINK}" target="_blank" rel="noopener">Message Us on WhatsApp</a>
    </div>
    <p class="hint" style="margin-top:22px;">✉️ {EMAIL_DISPLAY} &nbsp;·&nbsp; \U0001F4DE {PHONE_DISPLAY}</p>
  </div>
</section>
"""
page("contact-thanks.html", f"Request Received — {SITE_NAME}", "Your website repair request has been received.", thanks_body)

# --------------------------------------------------------------------------
# LEGAL PAGES — Terms, Privacy, Cookies
# --------------------------------------------------------------------------
# Standard, general-purpose boilerplate written for a remote WordPress
# service business (contact-form lead capture, no on-site checkout, no
# tracking/analytics currently installed). This is a starting draft, not
# legal advice — have it reviewed by a lawyer familiar with your target
# markets before relying on it, especially for GDPR/CCPA-style obligations.
LEGAL_UPDATED = "August 21, 2026"


def legal_page(filename, title, heading, body_html):
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="{{ROOT}}index.html">Home</a> / {heading}</div>
    <h1>{heading}</h1>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="legal-content">
      <p class="legal-updated">Last updated: {LEGAL_UPDATED}</p>
      {body_html}
    </div>
  </div>
</section>
"""
    page(filename, f"{title} — {SITE_NAME}", f"{heading} for {SITE_NAME} ({DOMAIN}).", body)


# ---- Terms of Service -----------------------------------------------------
terms_body = f"""
<p>These Terms of Service ("Terms") govern your use of the {DOMAIN} website and the
WordPress support, repair, security, optimization, development, and care-plan
services (the "Services") provided by {SITE_NAME}. By requesting a quote, submitting
the contact form, or purchasing any Service, you agree to these Terms.</p>

<h2>1. Who We Are</h2>
<p>{SITE_NAME} is a remote WordPress support team serving clients globally. We do not
operate a physical storefront; all services are delivered online.</p>

<h2>2. Our Services</h2>
<p>We provide one-time services (such as malware removal, speed optimization,
migration, small tasks, redesign, DevOps/CI-CD setup, cybersecurity hardening,
and custom development) and ongoing monthly Care Plans and Maintenance Plans.
Specific inclusions, turnaround times, and pricing for each Service are described
on the relevant service page and may be confirmed with you directly before work begins.</p>

<h2>3. Client Responsibilities</h2>
<ul>
  <li>You must provide accurate, working access credentials (e.g. WordPress admin,
  hosting, FTP/SFTP) needed to perform the Service, or make these available promptly
  when requested.</li>
  <li>You are responsible for maintaining your own regular backups. While we take
  reasonable precautions and, where practical, take a backup before making changes,
  we recommend you also keep an independent, up-to-date backup of your site at all times.</li>
  <li>You confirm that you own or are authorized to request work on the website(s)
  you submit to us.</li>
</ul>

<h2>4. Payment &amp; Pricing</h2>
<p>Prices shown on the site are starting prices and may vary based on the condition,
size, and complexity of your website; we'll confirm final pricing with you before
starting paid work. Payment is due as agreed at the time of order unless otherwise
arranged in writing.</p>

<h2>5. Money-Back Guarantee</h2>
<p>Where a Service page states a money-back guarantee, that guarantee applies under
the conditions described on that page (for example, if we're unable to resolve the
specific issue you engaged us for). It does not cover unrelated pre-existing issues,
new issues introduced by third-party changes to your site after our work is complete,
or dissatisfaction with design/subjective preferences once the agreed scope has been
delivered. Contact us to request a refund review.</p>

<h2>6. Service Limitations</h2>
<p>WordPress sites depend on many third-party plugins, themes, hosting environments,
and services outside our control. While we work carefully and test our changes, we
cannot guarantee that every issue is fixable, that third-party software will remain
compatible after our work, or that your host, domain registrar, or other vendors
will not independently cause disruptions. We are not liable for issues caused by
actions taken on your site by you or third parties after our work is delivered.</p>

<h2>7. Limitation of Liability</h2>
<p>To the maximum extent permitted by law, {SITE_NAME} is not liable for any indirect,
incidental, or consequential damages (including lost revenue or lost data) arising
from use of our Services. Our total liability for any claim is limited to the amount
you paid us for the specific Service giving rise to the claim.</p>

<h2>8. Intellectual Property</h2>
<p>You retain ownership of your website, content, and any custom code we build for
you as part of a paid engagement, once paid in full. We retain ownership of our own
internal tools, scripts, and processes used to deliver the Service.</p>

<h2>9. Third-Party Services</h2>
<p>Some Services may involve installing or configuring third-party plugins, themes,
or platforms. Your use of those third-party products is subject to their own terms,
and we are not responsible for their pricing, availability, or policy changes.</p>

<h2>10. Termination</h2>
<p>Monthly Care Plans and Maintenance Plans can be cancelled at any time; cancellation
takes effect at the end of the current billing period unless otherwise agreed. We may
decline or discontinue service for any site involved in illegal activity or that
violates these Terms.</p>

<h2>11. Changes to These Terms</h2>
<p>We may update these Terms from time to time. Continued use of our Services after
changes are posted constitutes acceptance of the revised Terms.</p>

<h2>12. Contact Us</h2>
<p>Questions about these Terms? Reach us at {EMAIL_DISPLAY} or via
<a href="{{ROOT}}contact.html">our contact page</a>.</p>
"""
legal_page("terms.html", "Terms of Service", "Terms of Service", terms_body)

# ---- Privacy Policy ---------------------------------------------------------
privacy_body = f"""
<p>This Privacy Policy explains how {SITE_NAME} ("we", "us") collects, uses, and
protects information when you visit {DOMAIN} or use our Services. We serve clients
globally and aim to handle personal data responsibly regardless of where you're
located.</p>

<h2>1. Information We Collect</h2>
<ul>
  <li><strong>Contact &amp; request details</strong> — name, email address, phone/WhatsApp
  number, website URL, and message details you submit through our contact or request
  forms.</li>
  <li><strong>Service access details</strong> — where needed to perform paid work, we may
  temporarily receive WordPress admin, hosting, or FTP/SFTP credentials. We use these
  only to deliver the Service you requested.</li>
  <li><strong>Communications</strong> — records of emails, WhatsApp messages, or other
  correspondence you have with us about a Service.</li>
</ul>
<p>We do not currently use analytics or advertising tracking scripts on this site. See
our <a href="{{ROOT}}cookies.html">Cookie Policy</a> for details.</p>

<h2>2. How We Use Your Information</h2>
<ul>
  <li>To respond to quote requests and deliver the Services you order.</li>
  <li>To communicate with you about your order, appointment, or ongoing Care Plan.</li>
  <li>To improve our services and internal processes.</li>
  <li>To meet legal or accounting obligations.</li>
</ul>
<p>We do not sell your personal information to third parties.</p>

<h2>3. How We Share Information</h2>
<p>We only share information with third parties where necessary to deliver a
Service you've requested (for example, a hosting provider or plugin vendor you've
asked us to work with), to comply with the law, or to protect our legal rights. We
do not share your data with third parties for their own marketing purposes.</p>

<h2>4. Data Retention</h2>
<p>We retain contact and service records for as long as reasonably necessary to
provide support, meet legal/accounting requirements, and resolve any disputes.
Access credentials shared with us for a specific job are used only for that job
and deleted or revoked once the work is complete, unless you've asked us to retain
them for an ongoing Care Plan.</p>

<h2>5. Your Rights</h2>
<p>Depending on where you live, you may have rights to access, correct, delete, or
export the personal data we hold about you, or to object to or restrict certain
processing (for example, under GDPR if you're in the EU/UK, or under similar laws
elsewhere). To exercise any of these rights, contact us at {EMAIL_DISPLAY} and we'll
respond within a reasonable time.</p>

<h2>6. Security</h2>
<p>We use reasonable administrative and technical safeguards to protect the
information you share with us, including access credentials. No method of
transmission or storage is 100% secure, and we encourage you to use strong, unique
passwords and to revoke temporary access once work is complete.</p>

<h2>7. Children's Privacy</h2>
<p>Our Services are intended for business use and are not directed at children. We
do not knowingly collect personal information from children.</p>

<h2>8. International Data</h2>
<p>As a remote, globally-serving team, information you share with us may be
accessed or processed from different locations. We take reasonable steps to protect
your data wherever it is handled.</p>

<h2>9. Changes to This Policy</h2>
<p>We may update this Privacy Policy occasionally. The "Last updated" date above
reflects the most recent revision.</p>

<h2>10. Contact Us</h2>
<p>Questions about this policy or your data? Reach us at {EMAIL_DISPLAY} or via
<a href="{{ROOT}}contact.html">our contact page</a>.</p>
"""
legal_page("privacy.html", "Privacy Policy", "Privacy Policy", privacy_body)

# ---- Cookie Policy -----------------------------------------------------------
cookies_body = f"""
<p>This Cookie Policy explains how {SITE_NAME} uses cookies and similar technologies
on {DOMAIN}.</p>

<h2>1. What Are Cookies?</h2>
<p>Cookies are small text files placed on your device by a website to store
information, such as your preferences or login state.</p>

<h2>2. Cookies We Use</h2>
<p>{DOMAIN} uses CookieYes to manage cookie consent. When you visit the site, CookieYes
sets a cookie to remember your consent choices so we don't ask again on every visit.
Beyond this consent-management cookie, {SITE_NAME} does not currently run analytics,
advertising, or other third-party tracking cookies.</p>

<h2>3. If This Changes</h2>
<p>If we add analytics (such as visit statistics) or other tools that use cookies in
the future, we will update this policy to describe what's used and why, and rely on
CookieYes to request your consent where required by law.</p>

<h2>4. Managing Cookies</h2>
<p>You can control or delete cookies through your browser settings at any time.
Since this site does not currently rely on cookies for core functionality, disabling
them should not affect your ability to browse the site or submit the contact form.</p>

<h2>5. Contact Us</h2>
<p>Questions about this Cookie Policy? Reach us at {EMAIL_DISPLAY} or via
<a href="{{ROOT}}contact.html">our contact page</a>.</p>
"""
legal_page("cookies.html", "Cookie Policy", "Cookie Policy", cookies_body)

# --------------------------------------------------------------------------
# REDIRECT STUBS — old service URLs that were merged/renamed in the service
# taxonomy update. See REDIRECTS above.
# --------------------------------------------------------------------------
for old_slug, new_slug in REDIRECTS:
    redirect_page(old_slug, new_slug)

print("All pages generated.")

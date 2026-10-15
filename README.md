# Halcyon Stereo

A fictional vintage hi-fi and records shop in Portland, Oregon. Design and development
portfolio piece by Stephen Fehon. Every business, person, product, price, event, and
contact detail on the site is invented.

## What it is
- 18-page static site, no frameworks, no build step
- Warm retro-futurist 1970s identity: bone cream, burnt orange, mustard, walnut, avocado
- Self-hosted variable fonts: Anybody (display, width axis) and Figtree (body)
- Film-grain overlay, sunburst and wood-grain motifs, ticket-stub cards
- Canvas vinyl turntable hero (clickable needle) and animated VU meters
- Lamp-switch theme toggle (persists via localStorage)
- Filterable inventory with search and sort
- CSS scroll-driven animations with IntersectionObserver fallback
- prefers-reduced-motion honored throughout; WCAG 2.2 AA target
- _headers and _redirects for Cloudflare Pages; versioned asset URLs

## Structure
- assets/css/main.css - design system
- assets/js/main.js - interactions
- assets/fonts - variable WOFF2, self-hosted
- build/ - Python generators that assemble the pages
- sitemap.xml, robots.txt, llms.txt, site.webmanifest

# [theshoemaker.de](https://theshoemaker.de)

This is the repository used for my website.
I generate the HTML with [raydor](https://github.com/pfirsich/raydor) and serve it with [htcpp](https://github.com/pfirsich/htcpp).

# To Do
## Tech
* Add metrics (collect Prometheus metrics somewhere and add some dashboards or something)
* SEO:
  - Optimize Images (optipng, pngcrush, jpegoptim, tinypng/tinyjpeg API)
  - meta tags (description)
  - alt attributes for all images
  - https://pagespeed.web.dev/
* Analytics: goatcounter is blocked by many adblockers. Add a /stats endpoint or something that the page's path and referrer via query argument. Then use those and User-Agent to collect stats on Browser, Location, OS, Referrer and Path Visited (count separately and don't store IP).
* DIY CDN
  Latency from US is shit. I want to keep using my own webserver, so I need to build something myself
  Use Route 58, Cloudflare DNS or whatever to point theshoemaker.de to multiple PoPs
  Figure out a way to share certificate and add reverse-proxy mode to htcpp
* Lazy Image Loading? (`loading="lazy"`)
* Reprocess Markdown to add `target="_blank"` into links
* Atom Feed

## Content
* Videos
  - exquisite
  - myl
  - muwa

# Notes for Later
* `sort_effort` in projects is roughly the number of 8h work days spent on it
* Sort project links roughly by likelihood of visiting: dedicated page (itch, LD), video, GitHub, other
* I wanted to show the project tags, but it's too much noise and there is not enough space
* Similarly there is not enough space for #commits, LOC or #stars

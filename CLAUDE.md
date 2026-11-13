# AYVA CO demos

Each shop demo is one static page at `public/<slug>/index.html`, served at `https://ayvaco.net/<slug>`.
Cloudflare Workers (Git integration) deploys `public/` automatically on every push to `main` (see `wrangler.jsonc`).

## Add or update a shop
1. Put the shop's logo and banner in `shops/<slug>/` (logo.png, cover.jpg).
2. Write `shops/<slug>/build.sh` calling `tools/make_shop.py` (copy an existing one). Bases: `grocery` or `vape` (vape includes the 21+ gate, vapes, shisha, accessories, cigars).
3. Run `bash shops/<slug>/build.sh` from the repo root.
4. Test in Playwright (21+ gate, add to basket, WhatsApp link uses the shop number), commit, push to `main`.
5. Check `https://ayvaco.net/<slug>` loads, then send the user the link.

Rules: no Edit button on shop pages (default). Name "AYVA CO" everywhere. Opening hours from Google Maps if readable, otherwise 2GIS; say which.

## Templates
- `templates/grocery-base.html`: grocery demo source.
- `templates/vape-base.html`: built by `tools/build_vape.py` from the grocery base (products and icons live there).
- `public/vape/`: the editable vape demo for the user (Edit button on).

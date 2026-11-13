#!/usr/bin/env python3
"""Build one shop demo: public/<slug>/index.html

Example:
  python3 tools/make_shop.py --base vape --slug qaser --name "Qaser Al Barsha" \
    --area "Al Barsha" --kind "Vape & shisha shop" --open "3 AM" --time "30 min" \
    --min 40 --fee 0 --color "#22375B" --phone 971553684719 \
    --logo logo.png --cover banner.jpg
"""
import argparse, base64, io, json, os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASES = {"grocery": "templates/grocery-base.html", "vape": "templates/vape-base.html"}

def data_url(path, w, h, q=85):
    im = Image.open(path).convert("RGB")
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - w) // 2, (im.height - h) // 2
    im = im.crop((l, t, l + w, t + h))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--base", choices=BASES, required=True)
    a.add_argument("--slug", required=True)
    a.add_argument("--name", required=True)
    a.add_argument("--area", required=True)
    a.add_argument("--kind", default=None, help='Label before the area, e.g. "Grocery"')
    a.add_argument("--open", default="2 AM", help='"24/7" or a closing time like "3 AM"')
    a.add_argument("--time", default="30 min")
    a.add_argument("--min", type=float, default=25)
    a.add_argument("--fee", type=float, default=0)
    a.add_argument("--color", default="#0F7B3A")
    a.add_argument("--phone", required=True)
    a.add_argument("--logo"); a.add_argument("--cover")
    a.add_argument("--editable", action="store_true", help="keep the Edit button")
    o = a.parse_args()

    s = open(os.path.join(ROOT, BASES[o.base])).read()
    cfg = {"name": o.name, "area": o.area, "openUntil": o.open, "time": o.time,
           "min": int(o.min) if o.min == int(o.min) else o.min,
           "fee": int(o.fee) if o.fee == int(o.fee) else o.fee,
           "color": o.color, "phone": re.sub(r"\D", "", o.phone),
           "logo": data_url(o.logo, 300, 300, 90) if o.logo else None,
           "cover": data_url(o.cover, 1200, 525) if o.cover else None}
    key = re.sub(r"\W", "", o.slug)
    pat = re.compile(r'const cfg=Object\.assign\(\{.*?\},ls\.get\("\w+"\)\|\|\{\}\);', re.S)
    assert pat.search(s), "cfg line not found"
    s = pat.sub(lambda m: f'const cfg=Object.assign({json.dumps(cfg, ensure_ascii=False)},ls.get("{key}_cfg")||{{}});', s, 1)
    s = re.sub(r'ls\.(get|set)\("(mm2|vp|sm|qa)_cart\d*"', lambda m: f'ls.{m.group(1)}("{key}_cart"', s)
    s = re.sub(r'ls\.set\("(mm2|vp|sm|qa)_cfg"', f'ls.set("{key}_cfg"', s)
    s = re.sub(r"<title>.*?</title>", lambda m: f"<title>{o.name}</title>", s, count=1)
    if o.kind:
        s = re.sub(r'"(Grocery|Vape shop) · "\+', lambda m: json.dumps(o.kind + " · ", ensure_ascii=False) + "+", s)
    if not o.editable:
        s = s.replace("</style>", "#editBtn,[data-edit]{display:none!important}\n</style>", 1)
    head = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>[hidden]{display:none!important}</style></head><body style="margin:0">\n')
    out = os.path.join(ROOT, "public", o.slug, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(head + s + "\n</body></html>\n")
    print("wrote", out, f"({os.path.getsize(out)//1024} KB)")

if __name__ == "__main__":
    main()

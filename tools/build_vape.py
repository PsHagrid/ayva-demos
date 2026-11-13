import re,sys
src=open(sys.argv[1]).read()
def rep(a,b,count=1):
    global src
    assert src.count(a)>=1, a[:80]
    src=src.replace(a,b) if count==0 else src.replace(a,b,count)

# data
start=src.index('const CATS=');end=src.index('const byId=')
DATA=r'''const CATS=[["alfakher","Al Fakher vapes"],["mega","40K+ puffs"],["value","Under 40K"],["shisha","Shisha & tobacco"],["acc","Shisha accessories"],["cigar","Cigars & lighters"]];
const FL={apple:["#FF5A4E","#9B1B1B"],straw:["#FF6B8B","#A4133C"],gummint:["#6FE3D5","#0E7F76"],razz:["#4F8BFF","#1B2C8F"],grape:["#A66BFF","#3D1478"],mint:["#7DF0C4","#0F7B5C"],blue:["#6C7BFF","#262E91"],melon:["#FF6F91","#1FA463"],mango:["#FFC247","#E8590C"],peach:["#FFC09F","#EE5D3B"],coffee:["#C08B66","#4A2C1D"],ice:["#9EE7FF","#2A7FB8"],kiwi:["#C3F25A","#2E8B57"],cherry:["#FF4F6E","#7A0E2A"],cola:["#8A5A44","#2A1510"],silver:["#EEF1F5","#8A93A0"],gold:["#F6D77A","#A97A1F"],black:["#5A5D66","#121317"],clay:["#E09A64","#7A3D1C"],leather:["#A8703F","#3E2213"],coal:["#6A6A6A","#1A1A1A"],glass:["#BFE7FF","#4B8FC7"]};
const P=[
 ["a1","alfakher","Crown Bar E-Hose X","Double Apple · 60K puffs","bottle","apple",55,65],
 ["a2","alfakher","Crown Bar E-Hose X","Strawberry Punch · 60K puffs","bottle","straw",55],
 ["a9","alfakher","Crown Bar Cloud Box","Two Apple · 50K puffs","box","apple",44],
 ["a10","alfakher","Crown Bar Cloud Box","Blueberry Mint · 50K puffs","box","blue",44],
 ["a3","alfakher","Crown Bar Mega Max","Gum Mint · 40K puffs","box","gummint",48],
 ["a4","alfakher","Crown Bar Mega Max","Blue Razz Lemonade · 40K puffs","box","razz",45,48],
 ["a5","alfakher","Crown Bar Mega Max","Grape Mint · 40K puffs","box","grape",48],
 ["a11","alfakher","Crown Bar Mega Max","Watermelon Kiwi · 40K puffs","box","kiwi",48],
 ["a12","alfakher","Crown Bar Mega Max","Peach Ice · 40K puffs","box","peach",48],
 ["a13","alfakher","Crown Bar Mega Max","Cool Mango · 40K puffs","box","mango",48],
 ["a14","alfakher","Crown Bar Ultra","Lush Ice · 25K puffs","bar","melon",46],
 ["a6","alfakher","Crown Bar Hypermax","Two Apple · 15K puffs","bar","apple",42],
 ["a7","alfakher","Crown Bar 12000","Berry Ice · 12K puffs","slim","blue",38,50],
 ["a15","alfakher","Crown Bar Crystal","Gum Mint · 8K puffs · Dual Mode","slim","gummint",37],
 ["a8","alfakher","Crown Bar Pro","Mint · 8K puffs","pen","mint",38,null,true],
 ["m8","mega","JNR Shisha Classic","Baghdadi · 80K puffs","bottle","cherry",50],
 ["m9","mega","JNR Shisha Classic","Lemon Mint · 80K puffs","bottle","mint",50],
 ["m1","mega","Hayati Pro Ultra+ S","Blueberry Ice · 50K puffs","bar","blue",55],
 ["m2","mega","Oxbar TRI Fusion","Watermelon Ice · 45K puffs","bar","melon",50],
 ["m3","mega","Elf Bar Moon Night","Blue Razz Lemonade · 40K puffs","bar","razz",49],
 ["m4","mega","Vozol Rave","Mango Ice · 40K puffs","box","mango",50],
 ["m5","mega","Vozol Star","Blueberry Storm · 40K puffs","slim","blue",50],
 ["v4","value","Lost Mary MT35000 Turbo","Watermelon Ice · 35K puffs","slim","melon",45,49],
 ["v5","value","Pod Salt 35000","Grape · 35K puffs","bar","grape",50],
 ["v6","value","Elf Bar E-Shisha Luxe","Double Apple · 30K puffs","bottle","apple",43],
 ["v7","value","BECO POP 30K","Strawberry Kiwi · 30K puffs","slim","straw",45,60],
 ["v8","value","DOVPO 30K","Cola Ice · 30K puffs","bar","cola",45],
 ["v1","value","Tugboat Pulse","Peach Ice · 20K puffs","slim","peach",45],
 ["v2","value","Waka soPro PA10000","Smooth Cappuccino · 10K puffs","pen","coffee",45],
 ["v3","value","Yuoto XXL","Mango · 2,500 puffs","pen","mango",20],
 ["s1","shisha","Al Fakher Shisha 250g","Two Apples","tin","apple",60],
 ["s2","shisha","Al Fakher Shisha 250g","Gum Mint","tin","gummint",60],
 ["s3","shisha","Al Fakher Shisha 250g","Grape Mint","tin","grape",55,60],
 ["s4","shisha","Al Fakher Shisha 250g","Lemon Mint","tin","kiwi",60],
 ["s5","shisha","Al Fakher Shisha 1 kg","Mint","tin","mint",190],
 ["s6","shisha","Al Fakher Shisha 50g","Blueberry","tin","blue",15],
 ["s7","shisha","Afzal Pan Raas","Shisha molasses · 50g","tin","straw",15],
 ["s8","shisha","Richman Hookah","Complete set","hookah","black",210],
 ["s9","shisha","Medium Hookah","Glass base · 1 hose","hookah","glass",120],
 ["x1","acc","Coconut Charcoal","Cubes · 1 kg","coal","coal",25],
 ["x2","acc","Quick-Light Charcoal","10 rolls","coal","black",15],
 ["x3","acc","Washable Hose","Silicone · 1.8 m","hose","black",25],
 ["x4","acc","Clay Bowl","Egyptian style","bowl","clay",15],
 ["x5","acc","Silicone Bowl","Heat resistant","bowl","razz",25],
 ["x6","acc","Shisha Foil","Pre-cut · 50 sheets","papers","silver",10],
 ["x7","acc","Mouth Tips","Disposable · 100 pcs","papers","glass",15],
 ["c1","cigar","Cigar Cutter","Guillotine · double blade","cutter","silver",35],
 ["c2","cigar","V-Cut Cigar Cutter","Stainless steel","cutter","black",45],
 ["c3","cigar","Double Torch Lighter","Windproof · refillable","lighter","black",45,55],
 ["c4","cigar","Jet Lighter","Single flame","lighter","gold",25],
 ["c5","cigar","Butane Gas Refill","300 ml","can","razz",20],
 ["c6","cigar","Cigar Case","Leather · holds 3","tin","leather",85],
 ["c7","cigar","RAW Classic Papers","1¼ size","papers","clay",10],
 ["c8","cigar","Hornet Rolling Papers","King size","papers","gold",10]
].map(a=>({id:a[0],cat:a[1],name:a[2],size:a[3],shape:a[4],fl:a[5],price:a[6],was:a[7]||null,sold:!!a[8]}));
let GID=0;
function ico(s,f){const[c1,c2]=FL[f]||FL.ice,g="g"+(GID++),d=`<defs><linearGradient id="${g}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${c1}"/><stop offset="1" stop-color="${c2}"/></linearGradient></defs>`;
  const hl='<rect x="16" y="20" width="4" height="60" rx="2" fill="#fff" opacity=".28"/>';
  const scr=(x,y,w,h)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="3" fill="#0d0f14"/><rect x="${x+3}" y="${y+3}" width="${w*.45}" height="${h-6}" rx="1.5" fill="#43f59a"/><rect x="${x+w*.55}" y="${y+3}" width="${w*.3}" height="2.5" rx="1" fill="#fff" opacity=".7"/><rect x="${x+w*.55}" y="${y+8}" width="${w*.22}" height="2.5" rx="1" fill="#fff" opacity=".45"/>`;
  let b="";
  if(s==="bottle")b=`<rect x="27" y="3" width="6" height="22" rx="3" fill="#1b1d22"/><rect x="21" y="22" width="18" height="10" rx="4" fill="#2a2d34"/><rect x="13" y="30" width="34" height="66" rx="13" fill="url(#${g})"/><rect x="17" y="40" width="4" height="46" rx="2" fill="#fff" opacity=".3"/><rect x="20" y="58" width="20" height="14" rx="4" fill="#fff" opacity=".22"/>`;
  else if(s==="box")b=`<rect x="22" y="4" width="16" height="20" rx="6" fill="#1b1d22"/><rect x="8" y="20" width="44" height="76" rx="12" fill="url(#${g})"/>${hl.replace('x="16"','x="13"')}${scr(18,32,24,15)}<circle cx="30" cy="84" r="3" fill="#000" opacity=".25"/>`;
  else if(s==="slim")b=`<rect x="22" y="3" width="16" height="12" rx="5" fill="#1b1d22"/><rect x="15" y="12" width="30" height="30" rx="11" fill="${c1}" opacity=".55"/><rect x="13" y="34" width="34" height="62" rx="14" fill="url(#${g})"/><rect x="18" y="44" width="4" height="40" rx="2" fill="#fff" opacity=".3"/>${scr(20,50,20,12)}`;
  else if(s==="pen")b=`<rect x="24" y="2" width="12" height="14" rx="5" fill="#1b1d22"/><rect x="21" y="12" width="18" height="84" rx="9" fill="url(#${g})"/><rect x="24" y="20" width="3" height="60" rx="1.5" fill="#fff" opacity=".3"/><circle cx="30" cy="88" r="2.5" fill="#43f59a"/>`;
  else if(s==="tin")b=`<rect x="8" y="30" width="44" height="60" rx="7" fill="url(#${g})"/><rect x="8" y="26" width="44" height="12" rx="5" fill="#000" opacity=".25"/><rect x="14" y="48" width="32" height="24" rx="4" fill="#fff" opacity=".85"/><rect x="18" y="54" width="24" height="3" rx="1.5" fill="${c2}"/><rect x="21" y="61" width="18" height="3" rx="1.5" fill="${c2}" opacity=".6"/><rect x="12" y="34" width="3" height="50" rx="1.5" fill="#fff" opacity=".3"/>`;
  else if(s==="hookah")b=`<rect x="27" y="2" width="6" height="8" rx="2" fill="#7a3d1c"/><path d="M22 10h16l-3 7H25z" fill="#c97d4a"/><rect x="18" y="17" width="24" height="3" rx="1.5" fill="#9aa3ad"/><rect x="28" y="20" width="4" height="40" fill="#b8c0c8"/><rect x="26" y="34" width="8" height="4" rx="2" fill="#8a93a0"/><path d="M32 46c10 2 16 10 18 24" stroke="#222" stroke-width="2.5" fill="none" stroke-linecap="round"/><path d="M20 60h20c6 8 10 14 10 22a12 12 0 0 1-12 12H22a12 12 0 0 1-12-12c0-8 4-14 10-22z" fill="url(#${g})"/><path d="M15 76c3-6 6-9 8-11" stroke="#fff" stroke-width="2.5" opacity=".35" fill="none" stroke-linecap="round"/>`;
  else if(s==="coal")b=`<rect x="8" y="44" width="44" height="48" rx="6" fill="#e9e3d8"/><rect x="8" y="44" width="44" height="12" rx="6" fill="${c1}"/><rect x="14" y="64" width="32" height="16" rx="3" fill="${c2}" opacity=".85"/>${[[12,28],[24,26],[36,28],[18,38],[30,36],[42,38]].map(([x,y])=>`<rect x="${x}" y="${y}" width="10" height="10" rx="2" fill="url(#${g})"/>`).join("")}`;
  else if(s==="hose")b=`<rect x="6" y="6" width="10" height="16" rx="3" fill="#9aa3ad"/><path d="M11 22c0 14 38 6 38 22s-38 6-38 22 38 6 38 18" stroke="url(#${g})" stroke-width="7" fill="none" stroke-linecap="round"/><rect x="44" y="82" width="10" height="16" rx="3" fill="#9aa3ad"/>`;
  else if(s==="bowl")b=`<ellipse cx="30" cy="40" rx="22" ry="7" fill="${c2}"/><path d="M8 40h44l-10 26H18z" fill="url(#${g})"/><rect x="24" y="66" width="12" height="26" rx="3" fill="url(#${g})"/><ellipse cx="30" cy="40" rx="16" ry="4" fill="#000" opacity=".25"/><circle cx="24" cy="40" r="1.5" fill="#000" opacity=".4"/><circle cx="30" cy="41" r="1.5" fill="#000" opacity=".4"/><circle cx="36" cy="40" r="1.5" fill="#000" opacity=".4"/>`;
  else if(s==="papers")b=`<rect x="10" y="30" width="40" height="56" rx="4" fill="url(#${g})"/><rect x="10" y="30" width="40" height="10" rx="4" fill="#fff" opacity=".5"/><rect x="16" y="52" width="28" height="4" rx="2" fill="#000" opacity=".2"/><rect x="16" y="60" width="20" height="4" rx="2" fill="#000" opacity=".14"/><rect x="13" y="42" width="3" height="40" rx="1.5" fill="#fff" opacity=".35"/>`;
  else if(s==="cutter")b=`<rect x="6" y="38" width="48" height="26" rx="13" fill="url(#${g})"/><circle cx="30" cy="51" r="8" fill="#f2f2f2" stroke="#000" stroke-opacity=".25" stroke-width="2"/><rect x="2" y="44" width="8" height="14" rx="4" fill="${c2}"/><rect x="50" y="44" width="8" height="14" rx="4" fill="${c2}"/><rect x="12" y="42" width="12" height="3" rx="1.5" fill="#fff" opacity=".4"/>`;
  else if(s==="lighter")b=`<path d="M30 6c6 8 8 13 4 19-2 3-6 3-8 0-4-6-2-11 4-19z" fill="#3fa9ff"/><path d="M30 13c3 5 4 8 2 11-1 1-3 1-4 0-2-3-1-6 2-11z" fill="#bfe6ff"/><rect x="22" y="26" width="16" height="10" rx="2" fill="#9aa3ad"/><rect x="16" y="34" width="28" height="60" rx="7" fill="url(#${g})"/><rect x="20" y="40" width="3" height="48" rx="1.5" fill="#fff" opacity=".3"/>`;
  else if(s==="can")b=`<rect x="26" y="6" width="8" height="10" rx="2" fill="#9aa3ad"/><rect x="18" y="14" width="24" height="10" rx="5" fill="#cfd5db"/><rect x="16" y="22" width="28" height="72" rx="8" fill="url(#${g})"/><rect x="20" y="44" width="20" height="22" rx="3" fill="#fff" opacity=".85"/><rect x="20" y="28" width="3" height="60" rx="1.5" fill="#fff" opacity=".3"/>`;
  else b=`<rect x="21" y="3" width="18" height="16" rx="6" fill="#1b1d22"/><rect x="12" y="14" width="36" height="82" rx="11" fill="url(#${g})"/>${hl}${scr(19,30,22,15)}<circle cx="30" cy="86" r="2.5" fill="#000" opacity=".25"/>`;
  return `<svg viewBox="0 0 60 100" aria-hidden="true">${d}${b}</svg>`}
P.forEach(p=>Object.defineProperty(p,"e",{get(){return ico(p.shape,p.fl)}}));
'''
src=src[:start]+DATA+src[end:]

rep('const cfg=Object.assign({name:"Al Noor Mini Mart",area:"Al Barsha 1",openUntil:"2 AM",time:"20 min",min:25,fee:0,color:"#0F7B3A",phone:"",logo:null,cover:null},ls.get("mm2_cfg")||{});',
    'const cfg=Object.assign({name:"Cloud Vape",area:"JVC",openUntil:"3 AM",time:"30 min",min:40,fee:0,color:"#5B21B6",phone:"971563383733",logo:null,cover:null},ls.get("vp_cfg")||{});')
src=src.replace('"mm2_cfg"','"vp_cfg"').replace('"mm2_cart"','"vp_cart"')
rep('"Grocery · "+','"Vape shop · "+')
rep('<span id="area">Grocery · Al Barsha 1</span>','<span id="area">Vape shop · JVC</span>')
rep('<h1 id="name">Al Noor Mini Mart</h1>','<h1 id="name">Cloud Vape</h1>')
rep('<span id="openTxt">Open until 2 AM</span>','<span id="openTxt">Open until 3 AM</span>')
rep('<title>Mart Menu Demo</title>','<title>Vape Shop Demo</title>')
rep('(al|the|mini|mart|supermarket|grocery|baqala)','(al|the|mini|mart|supermarket|grocery|baqala|vape|shop|store)')
rep('Example products and prices · Orders are sent to the shop on WhatsApp','For adults 21+ only · Example products and prices · Orders are sent to the shop on WhatsApp')
rep('placeholder="Ring the bell, don\'t knock"','placeholder="Call when outside"')
rep('const L=[`*New order · ${cfg.name}*`,""];','const L=[`*New order · ${cfg.name}*`,"Customer confirmed 21+",""];')
# css: hide edit, svg sizing, age gate
css='.thumb .em{position:absolute;inset:8% 0 10%;display:flex;align-items:center;justify-content:center;font-size:0;filter:drop-shadow(0 8px 10px rgba(0,0,0,.18))}.thumb .em svg{height:100%;width:auto;display:block}\n.cover .fallback{background:radial-gradient(60% 90% at 85% 10%,color-mix(in srgb,var(--brand) 85%,#fff 15%) 0,transparent 60%),radial-gradient(70% 100% at 0% 100%,color-mix(in srgb,var(--brand) 70%,#000) 0,transparent 70%),linear-gradient(135deg,#120a24,color-mix(in srgb,var(--brand) 60%,#0b0b10))!important}\n.line .e svg{height:40px;width:auto}\n.gate{position:fixed;inset:0;z-index:60;background:#0b0b10;color:#fff;display:grid;place-items:center;padding:24px;text-align:center}.gate[hidden]{display:none}.gate h2{font-size:24px;margin:14px 0 8px}.gate p{color:#b9b9c6;margin:0 0 22px;font-size:15px}.gate .b{display:grid;gap:10px;width:min(320px,100%);margin:0 auto}.gate button{border:0;border-radius:14px;padding:15px;font:inherit;font-weight:700;font-size:16px}.gate .y{background:var(--brand);color:var(--on-brand)}.gate .n{background:#1d1d26;color:#ddd}.gate .badge{display:inline-grid;place-items:center;width:64px;height:64px;border-radius:50%;border:3px solid #fff;font-weight:800;font-size:20px}\n'
rep('</style>',css+'</style>')
gate='<div class="gate" id="gate" hidden><div><span class="badge">21+</span><h2>Are you 21 or older?</h2><p>This store sells vaping and tobacco products. You must be 21 or older to enter.</p><div class="b"><button class="y press" type="button" id="gYes">Yes, I\'m 21 or older</button><button class="n press" type="button" id="gNo">No</button></div></div></div>\n'
rep('<div class="layout" id="layout">',gate+'<div class="layout" id="layout">')
js='''
(function(){const g=$("#gate");let ok=false;try{ok=sessionStorage.getItem("vp_21")==="1"}catch(e){}
 if(!ok)g.hidden=false;$("#gYes").onclick=()=>{try{sessionStorage.setItem("vp_21","1")}catch(e){}g.hidden=true};
 $("#gNo").onclick=()=>{g.querySelector("h2").textContent="Sorry, this store is for adults only.";g.querySelector("p").textContent="";g.querySelector(".b").remove()}})();
'''
rep('renderDeals();renderCats();renderList();applyBrand();','renderDeals();renderCats();renderList();applyBrand();'+js)
open(sys.argv[2],'w').write(src)
print("ok")

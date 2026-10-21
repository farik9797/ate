import re,sys,cairosvg
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
S=sys.argv[1] if len(sys.argv)>1 else "/tmp"
svg=open("assets/logo/source/ate-logo-cdr.svg").read()
paths=[re.sub(r"\s+"," ",m.group(1)).strip() for m in re.finditer(r'<path d="(.*?)"\s*style="([^"]*)"',svg,re.S)]
assert len(paths)==9
NAVY="#1D3C8D"; BLUE="#008AC7"; WHITE="#FFFFFF"
TE,A,DROP,WAVE,AQUA,WRENCH=paths[1],paths[2],paths[3],paths[4],paths[5],paths[7]

def to_geom(d,seg=48):
    toks=re.findall(r"[MLCZ]|-?\d+(?:\.\d+)?",d); i=0; subs=[]; cur=[]; pos=None
    while i<len(toks):
        t=toks[i]
        if t=="M":
            if len(cur)>2: subs.append(cur)
            pos=(float(toks[i+1]),float(toks[i+2])); cur=[pos]; i+=3
        elif t=="L":
            pos=(float(toks[i+1]),float(toks[i+2])); cur.append(pos); i+=3
        elif t=="C":
            p1=(float(toks[i+1]),float(toks[i+2])); p2=(float(toks[i+3]),float(toks[i+4])); p3=(float(toks[i+5]),float(toks[i+6])); p0=pos
            for k in range(1,seg+1):
                u=k/seg; a=(1-u)**3; b=3*(1-u)**2*u; c=3*(1-u)*u**2; e=u**3
                cur.append((a*p0[0]+b*p1[0]+c*p2[0]+e*p3[0], a*p0[1]+b*p1[1]+c*p2[1]+e*p3[1]))
            pos=p3; i+=7
        elif t=="Z":
            if len(cur)>2: subs.append(cur)
            cur=[]; i+=1
        else: raise ValueError(t)
    if len(cur)>2: subs.append(cur)
    g=None
    for s in subs:
        p=Polygon(s).buffer(0)
        g=p if g is None else g.symmetric_difference(p)   # even-odd
    return g

def geom_to_d(g):
    polys=[g] if isinstance(g,Polygon) else list(getattr(g,"geoms",[]))
    out=[]
    for p in polys:
        if p.is_empty: continue
        for ring in [p.exterior]+list(p.interiors):
            c=list(ring.coords)[:-1]
            out.append("M"+" L".join("%.2f %.2f"%xy for xy in c)+" Z")
    return " ".join(out)

wr=to_geom(WRENCH)
cut=lambda d: geom_to_d(to_geom(d).difference(wr).simplify(0.01))
A_c,DROP_c,WAVE_c=cut(A),cut(DROP),cut(WAVE)

def bbox(ds):
    xs=[];ys=[]
    for d in ds:
        n=[float(v) for v in re.findall(r"-?\d+(?:\.\d+)?",d)]; xs+=n[0::2]; ys+=n[1::2]
    return min(xs),min(ys),max(xs),max(ys)
def build(parts,pad=1.5,bg=None,square=False,radius=0,scale=4):
    x0,y0,x1,y1=bbox([d for d,_ in parts]); x0-=pad;y0-=pad;x1+=pad;y1+=pad
    w,h=x1-x0,y1-y0
    if square:
        side=max(w,h); cx=(x0+x1)/2; cy=(y0+y1)/2; x0=cx-side/2; y0=cy-side/2; w=h=side
    body="".join('<path d="%s" fill="%s" fill-rule="evenodd"/>'%(d,c) for d,c in parts)
    bgrect='<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%.2f" fill="%s"/>'%(x0,y0,w,h,radius*w,bg) if bg else ""
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.2f %.2f %.2f %.2f" width="%.0f" height="%.0f">%s%s</svg>'%(x0,y0,w,h,w*scale,h*scale,bgrect,body)

light=lambda desc:[(TE,NAVY),(A_c,BLUE),(DROP_c,NAVY),(WAVE_c,BLUE)]+([(AQUA,NAVY)] if desc else [])
dark =lambda desc:[(TE,WHITE),(A_c,BLUE),(DROP_c,WHITE),(WAVE_c,BLUE)]+([(AQUA,WHITE)] if desc else [])
files={"ate.svg":build(light(True)),"ate-mark.svg":build(light(False)),
       "ate-white.svg":build(dark(True)),"ate-mark-white.svg":build(dark(False))}
for n,c in files.items(): open("assets/logo/"+n,"w").write(c)
fav=build([(A_c,BLUE),(DROP_c,NAVY)],pad=10,bg=WHITE,square=True,radius=0.18)
open("favicon.svg","w").write(fav)
cairosvg.svg2png(bytestring=fav.encode(),write_to="favicon.png",output_width=64,output_height=64)
cairosvg.svg2png(bytestring=fav.encode(),write_to="favicon-32.png",output_width=32,output_height=32)
ati=build([(A_c,BLUE),(DROP_c,NAVY)],pad=26,bg=WHITE,square=True)
cairosvg.svg2png(bytestring=ati.encode(),write_to="apple-touch-icon.png",output_width=180,output_height=180)
cairosvg.svg2png(url="assets/logo/ate.svg",write_to="assets/logo/ate.png",output_height=400)
cairosvg.svg2png(url="assets/logo/ate-white.svg",write_to="assets/logo/ate-white.png",output_height=400)
for n in files: cairosvg.svg2png(url="assets/logo/"+n,write_to=S+"/prev-"+n.replace(".svg",".png"),output_height=240)
cairosvg.svg2png(bytestring=fav.encode(),write_to=S+"/prev-favicon.png",output_width=180,output_height=180)
import os
for n in files: print(n, os.path.getsize("assets/logo/"+n),"bytes")

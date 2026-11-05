import math, sys

W, H = 1200, 320
depot = (930, 165)
routes = [
    [(1010, 70), (1090, 95), (1120, 150), (1060, 135)],
    [(1100, 220), (1130, 270), (1040, 285), (980, 245)],
    [(860, 250), (790, 270), (740, 210), (800, 175)],
    [(820, 95), (760, 60), (870, 45), (930, 75)],
]
themes = {
    "light": dict(bg="#ffffff", border="#d0d7de", title="#1f2328", sub="#59636e", grid="#eef1f4",
                  routes=["#2563eb", "#0d9488", "#d97706", "#db2777"], depot="#1f2328"),
    "dark": dict(bg="#0d1117", border="#30363d", title="#f0f6fc", sub="#9198a1", grid="#161b22",
                 routes=["#60a5fa", "#2dd4bf", "#fbbf24", "#f472b6"], depot="#f0f6fc"),
}
font = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

def svg(t):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Guilherme Almeida Zeni, Senior Software Engineer">']
    out.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}"/>')
    for x in range(40, W, 40):
        out.append(f'<line x1="{x}" y1="1" x2="{x}" y2="{H-1}" stroke="{t["grid"]}"/>')
    for y in range(40, H, 40):
        out.append(f'<line x1="1" y1="{y}" x2="{W-1}" y2="{y}" stroke="{t["grid"]}"/>')
    for color, r in zip(t["routes"], routes):
        pts = [depot] + r + [depot]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="1000" stroke-dashoffset="1000"><animate attributeName="stroke-dashoffset" from="1000" to="0" dur="2.4s" fill="freeze"/></path>')
        for x, y in r:
            out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{t["bg"]}" stroke="{color}" stroke-width="2.5"/>')
    dx, dy = depot
    out.append(f'<rect x="{dx-9}" y="{dy-9}" width="18" height="18" rx="3" fill="{t["depot"]}"/>')
    out.append(f'<text x="64" y="138" font-family="{font}" font-size="46" font-weight="700" fill="{t["title"]}">Guilherme Almeida Zeni</text>')
    out.append(f'<text x="64" y="186" font-family="{font}" font-size="24" fill="{t["sub"]}">Senior Software Engineer</text>')
    out.append(f'<text x="64" y="224" font-family="{font}" font-size="20" fill="{t["sub"]}">B.Tech and M.Sc., Unicamp  ·  Vehicle routing and optimization</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"

dest = sys.argv[1]
for name, t in themes.items():
    open(f"{dest}/banner-{name}.svg", "w").write(svg(t))

"""
Run this script to rebuild the final self-contained HTML file.
It reads index_template.html + the /images folder and outputs
Sarwar_Alam_Portfolio.html with all images embedded as base64.
"""
import base64, os

def b64(path, mime="image/jpeg"):
    with open(path, "rb") as f:
        data = f.read()
    return f"data:{mime};base64," + base64.b64encode(data).decode()

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(BASE, "images")

subs = {
    "images/profile.jpg": b64(os.path.join(IMAGES, "profile.jpg")),
    "images/cv.jpg": b64(os.path.join(IMAGES, "cv.jpg")),
    "images/cert_infosys_cyber.jpg": b64(os.path.join(IMAGES, "cert_infosys_cyber.jpg")),
    "images/cert_infosys_python.jpg": b64(os.path.join(IMAGES, "cert_infosys_python.jpg")),
    "images/cert_tech_veda.jpg": b64(os.path.join(IMAGES, "cert_tech_veda.jpg")),
    "images/cert_roti_bank.jpg": b64(os.path.join(IMAGES, "cert_roti_bank.jpg")),
}

with open(os.path.join(BASE, "index_template.html"), "r", encoding="utf-8") as f:
    html = f.read()

for k, v in subs.items():
    html = html.replace(k, v)

out_path = os.path.join(BASE, "Sarwar_Alam_Portfolio.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Built:", out_path)

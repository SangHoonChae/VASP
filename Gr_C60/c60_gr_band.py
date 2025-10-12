import pandas as pd
import re
import matplotlib.pyplot as plt

Efer=[-3.0744,-3.0754,-3.0740,-3.0742,-3.0723,-3.0760,-3.0763,-3.0750,-5.0187,-3.3521]

# ===== 파일 경로와 EF값만 수정 =====
file_path = "/home/ufo/VASP/band_ownership/C60_bandown.txt"   # band_ownership.txt 파일 경로
E_fermi = Efer[8]                  # OUTCAR에서 grep "E-fermi"로 얻은 값


# ===== 파일 읽고 파싱 =====
data = []
pattern = re.compile(r"k=(\S+) band=(\S+) E=(\S+) occ=(\S+) +G=([\d.]+)% +C60=([\d.]+)% +-> (\S+)")
with open(file_path, "r") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            k, band, E, occ, g, c, label = m.groups()
            data.append({
                "kpoint": float(k),
                "band": int(band),
                # Fermi energy를 0으로 맞춤
                "Energy(eV)": float(E) - E_fermi,
                "Occupation": float(occ),
                "Graphene(%)": float(g),
                "C60(%)": float(c),
                "Label": label
            })

df = pd.DataFrame(data)

# ===== 색상 정의 =====
colors = {"GRAPHENE": "blue", "C60": "green", "HYBRID": "red"}

# ===== 플롯 (band index vs E) =====
plt.figure(figsize=(12,8))
for label, group in df.groupby("Label"):
    plt.scatter(group["band"], group["Energy(eV)"], 
                c=colors[label], label=label, s=10, alpha=0.7)

# Fermi level (0 eV) 기준선
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

plt.xlabel("Band index")
plt.ylabel("Energy - E$_F$ (eV)")
plt.axis([395.0,495.0,-3.0,3.0])
#plt.title("C60 on Graphene (TRP) Band Ownership")
plt.title("C60 Band Ownership")
plt.legend()
plt.tight_layout()
plt.grid(linestyle='--')
plt.show()

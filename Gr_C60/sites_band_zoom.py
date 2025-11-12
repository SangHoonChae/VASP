import pandas as pd
import re
import matplotlib.pyplot as plt

Efer=[-3.0744,-3.0754,-3.0740,-3.0742,-3.0763,-3.0723,-3.0760,-3.0750,]
atp=Efer[0]
bri=Efer[1]
ptg=Efer[2]
ptgr=Efer[3]
ring=Efer[4]
ring2=Efer[5]
ring3=Efer[6]
trp=Efer[7]
# ===== 파일 경로와 EF값만 수정 =====
file_path = "/home/csh/Desktop/VESTA/reverse_sandwich/ring_ring/band_ownership.txt"   # band_ownership.txt 파일 경로
E_fermi = -2.77738001                  # OUTCAR에서 grep "E-fermi"로 얻은 값


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
plt.figure(figsize=(6,4))
for label, group in df.groupby("Label"):
    plt.scatter(group["band"], group["Energy(eV)"], 
                c=colors[label], label=label, s=10, alpha=0.7)

# Fermi level (0 eV) 기준선
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

plt.xlabel("Band index")
plt.ylabel("Energy - E$_F$ (eV)")
plt.axis([560.0,570.0,-0.25,0.25])

points = [563, 564, 565, 566]

for p in points:
    row = df.loc[df["band"] == p, ["band", "Energy(eV)"]]
    if not row.empty:
        x = int(row["band"].values[0])
        y = row["Energy(eV)"].values[0]

        # 그래프에 좌표 찍기
        plt.scatter(x, y,color='blue', zorder=5)
        plt.text(x, y + 0.01 , f"{y:.3f}", ha='center', fontsize=9)

plt.title("RING-Graphene-RING Band Ownership")
plt.legend()
plt.tight_layout()
plt.grid(linestyle='--')
#plt.savefig('ATP_zoom')
plt.show()

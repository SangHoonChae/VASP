import pandas as pd
import re
import matplotlib.pyplot as plt

# ===== 파일 경로 & Fermi 에너지 설정 =====
file_path = "/home/ufo/VASP/band_ownership/C60_bandown.txt"   # 네 파일 이름
E_fermi = -4.679019                 # OUTCAR에서 grep "E-fermi"로 얻은 값

# ===== 파일 읽기 =====
data = []
pattern = re.compile(r"k=(\S+)\s+band=(\S+)\s+E=(\S+)\s+occ=(\S+)\s+C60=([\d.]+)%")

with open(file_path, "r") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            k, band, E, occ, c = m.groups()
            data.append({
                "kpoint": float(k),
                "band": int(band),
                "Energy(eV)": float(E) - E_fermi,  # EF=0 기준 정렬
                "Occupation": float(occ),
                "C60(%)": float(c)
            })

df = pd.DataFrame(data)

# ===== 플롯 =====
plt.figure(figsize=(12,8))
plt.scatter(df["band"], df["Energy(eV)"], c="green", s=8, alpha=0.7, label="C60")

plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.xlabel("Band index")
plt.ylabel("Energy - E$_F$ (eV)")
plt.axis([100.0,140.0,-4.0,4.0])
plt.title("C60 (isolated molecule) Band Eigenvalues")
plt.grid(linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

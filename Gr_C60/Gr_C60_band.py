import pandas as pd
import re
import matplotlib.pyplot as plt

def load_bandownership(file_path, E_fermi, system_label):
    """band_ownership.txt 파일을 읽어서 DataFrame으로 변환"""
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
                    "Energy(eV)": float(E) - E_fermi,  # EF=0 정렬
                    "Occupation": float(occ),
                    "Graphene(%)": float(g),
                    "C60(%)": float(c),
                    "Label": label,
                    "System": system_label
                })
    return pd.DataFrame(data)

# ===== 파일 경로와 EF 값 입력 =====
Efermi_graphene = -4.20   # OUTCAR에서 grep "E-fermi"로 확인
Efermi_c60      = -3.10
Efermi_mixed    = -3.45

df_graphene = load_bandownership("graphene_bandownership.txt", Efermi_graphene, "Graphene")
df_c60      = load_bandownership("c60_bandownership.txt", Efermi_c60, "C60")
df_mixed    = load_bandownership("mixed_bandownership.txt", Efermi_mixed, "Mixed")

# 합치기
df_all = pd.concat([df_graphene, df_c60, df_mixed])

# ===== 시각화 =====
plt.figure(figsize=(10,6))

# 시스템별로 색 구분
colors = {"Graphene": "blue", "C60": "green", "Mixed": "red"}

for sys, group in df_all.groupby("System"):
    plt.scatter(group["band"], group["Energy(eV)"], 
                c=colors[sys], label=sys, s=10, alpha=0.6)

plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.xlabel("Band index")
plt.ylabel("Energy - E$_F$ (eV)")
plt.title("Graphene vs C60 vs Mixed system")
plt.legend()
plt.tight_layout()
plt.show()

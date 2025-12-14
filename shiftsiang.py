
# app.py
import streamlit as st
from datetime import date
import pandas as pd

# ==== Utilitas ====
def hitung_persentase(total_aktual, target):
    if target and target != 0:
        return (total_aktual / target) * 100
    return None

def format_ribuan(nilai):
    try:
        return f"{int(nilai):,}".replace(",", ".")
    except (TypeError, ValueError):
        return str(nilai)

# ==== Kategori ====
KATEGORI = [
    "psm",
    "pwp",
    "serba",
    "seger",
    "ceban",
    "new member",
    "murah sejagat"
]

# ==== Tampilan ====
st.title("📊 Laporan Sales & Fokus (Sederhana) - 3 Shift per Promo")

# Informasi Umum
tanggal = st.date_input("Tanggal", value=date.today())
toko = st.text_input("Nama Toko", value="KE53")

st.write("---")
st.subheader("Input Target & Aktual (Shift 1–2–3) per Kategori")

# Input data
target_data = {}
aktual_s1 = {}
aktual_s2 = {}
aktual_s3 = {}

for kat in KATEGORI:
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    with col1:
        st.write(kat.upper())
    with col2:
        target_data[kat] = st.number_input(
            f"Target {kat}",
            min_value=0,
            step=1,
            key=f"tgt_{kat}"
        )
    with col3:
        aktual_s1[kat] = st.number_input(
            f"Aktual S1 {kat}",
            min_value=0,
            step=1,
            key=f"act_{kat}_s1"
        )
    with col4:
        aktual_s2[kat] = st.number_input(
            f"Aktual S2 {kat}",
            min_value=0,
            step=1,
            key=f"act_{kat}_s2"
        )
    with col5:
        aktual_s3[kat] = st.number_input(
            f"Aktual S3 {kat}",
            min_value=0,
            step=1,
            key=f"act_{kat}_s3"
        )

# Proses data -> total aktual & ACH%
rows = []
for i, kat in enumerate(KATEGORI, start=1):  # Nomor urut mulai dari 1
    tgt = target_data[kat]
    s1 = aktual_s1[kat]
    s2 = aktual_s2[kat]
    s3 = aktual_s3[kat]
    total_act = s1 + s2 + s3
    ach = hitung_persentase(total_act, tgt)

    rows.append({
        "No": i,
        "Kategori": kat.upper(),
        "Target": tgt,
        "S1": s1,
        "S2": s2,
        "S3": s3,
        "Total Aktual": total_act,
        "ACH%": round(ach, 2) if ach is not None else None
    })

df = pd.DataFrame(rows)

# ==== Baris Total Keseluruhan ====
sum_target = df["Target"].sum()
sum_s1 = df["S1"].sum()
sum_s2 = df["S2"].sum()
sum_s3 = df["S3"].sum()
sum_total_aktual = df["Total Aktual"].sum()
ach_total = hitung_persentase(sum_total_aktual, sum_target)
row_total = {
    "No": "",
    "Kategori": "TOTAL",
    "Target": sum_target,
    "S1": sum_s1,
    "S2": sum_s2,
    "S3": sum_s3,
    "Total Aktual": sum_total_aktual,
    "ACH%": round(ach_total, 2) if ach_total is not None else None
}

df_total = pd.concat([df, pd.DataFrame([row_total])], ignore_index=True)

# ==== Format tampilan (ribuan & persen) ====
df_tampil = df_total.copy()
for col in ["Target", "S1", "S2", "S3", "Total Aktual"]:
    df_tampil[col] = df_tampil[col].apply(format_ribuan)

df_tampil["ACH%"] = df_tampil["ACH%"].apply(lambda x: f"{x:.2f}%" if isinstance(x, (int, float)) else "-")

# ==== Tabel tanpa index ====
st.write("---")
st.subheader("📋 Tabel Pencapaian (Total = S1 + S2 + S3)")
st.dataframe(
    df_tampil.style.hide(axis="index"),
    use_container_width=True
)


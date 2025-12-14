
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
        "Target": format_ribuan(tgt),
        "S1": format_ribuan(s1),
        "S2": format_ribuan(s2),
        "S3": format_ribuan(s3),
        "Total Aktual": format_ribuan(total_act),
        "ACH%": f"{ach:.2f}%" if ach is not None else "-"
    })

df = pd.DataFrame(rows)

st.write("---")
st.subheader("📋 Tabel Pencapaian (Total = S1 + S2 + S3)")
st.dataframe(df, use_container_width=True)


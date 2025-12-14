
# app.py
import streamlit as st
from datetime import date
import pandas as pd

# ==== Utilitas ====
def hitung_persentase(aktual, target):
    if target and target != 0:
        return (aktual / target) * 100
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
st.title("📊 Laporan Sales & Fokus (Sederhana)")

# Informasi Umum
shift = st.selectbox("Shift", [1, 2, 3], index=0)
tanggal = st.date_input("Tanggal", value=date.today())
toko = st.text_input("Nama Toko", value="KE53")

st.write("---")
st.subheader("Input Target & Aktual per Kategori")

# Input data
target_data = {}
aktual_data = {}

for kat in KATEGORI:
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write(kat.upper())
    with col2:
        target_data[kat] = st.number_input(f"Target {kat}", min_value=0, step=1, key=f"tgt_{kat}")
    with col3:
        aktual_data[kat] = st.number_input(f"Aktual {kat}", min_value=0, step=1, key=f"act_{kat}")

# Proses data
rows = []
for i, kat in enumerate(KATEGORI, start=1):  # Nomor urut mulai dari 1
    tgt = target_data[kat]
    act = aktual_data[kat]
    ach = hitung_persentase(act, tgt)
    rows.append({
        "No": i,
        "Kategori": kat.upper(),
        "Target": format_ribuan(tgt),
        "Aktual": format_ribuan(act),
        "ACH%": f"{ach:.2f}%" if ach is not None else "-"
    })

df = pd.DataFrame(rows)

st.write("---")
st.subheader("📋 Tabel Pencapaian")
st.dataframe(df, use_container_width=True)


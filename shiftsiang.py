
# app.py
import streamlit as st
from datetime import date
import pandas as pd

# ==== Utilitas ====
def format_ribuan(nilai):
    try:
        return f"{int(nilai):,}".replace(",", ".")
    except (TypeError, ValueError):
        return str(nilai)

def hitung_persentase(aktual, target):
    if target and target != 0:
        return (aktual / target) * 100
    return None

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

# ==== Konfigurasi Halaman ====
st.set_page_config(
    page_title="Laporan Sales & Fokus",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Laporan Sales & Fokus Toko")
st.caption("Aplikasi input target & aktual per kategori dengan perhitungan pencapaian otomatis (ACH%).")

# ==== Sidebar: Input Informasi Umum ====
st.sidebar.header("Informasi Umum")
shift = st.sidebar.selectbox("Shift", options=[1, 2, 3], index=0)
tanggal = st.sidebar.date_input("Tanggal", value=date.today(), format="YYYY-MM-DD")
toko = st.sidebar.text_input("Nama Toko", value="KE53")

st.sidebar.divider()
st.sidebar.write("**Tip:** Tekan Enter untuk konfirmasi input angka, atau gunakan panah ↑/↓.")

# ==== Input Target & Aktual per Kategori ====
st.subheader("Input Target & Aktual per Kategori")

# Inisialisasi state untuk data
if "target_data" not in st.session_state:
    st.session_state.target_data = {kat: 0 for kat in KATEGORI}
if "aktual_data" not in st.session_state:
    st.session_state.aktual_data = {kat: 0 for kat in KATEGORI}

cols = st.columns([1, 1, 1])  # judul kolom
with cols[0]:
    st.markdown("**Kategori**")
with cols[1]:
    st.markdown("**Target**")
with cols[2]:
    st.markdown("**Aktual**")

for kat in KATEGORI:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.write(kat.upper())
    with c2:
        st.session_state.target_data[kat] = st.number_input(
            f"Target {kat.upper()}",
            min_value=0,
            step=1,
            value=st.session_state.target_data[kat],
            key=f"tgt_{kat}"
        )
    with c3:
        st.session_state.aktual_data[kat] = st.number_input(
            f"Aktual {kat.upper()}",
            min_value=0,
            step=1,
            value=st.session_state.aktual_data[kat],
            key=f"act_{kat}"
        )

st.divider()

# ==== Ringkasan Header ====
st.markdown("### Ringkasan")
h1, h2, h3 = st.columns(3)
h1.metric("Shift", shift)
h2.metric("Tanggal", tanggal.strftime("%Y-%m-%d"))
h3.metric("Toko", toko)

# ==== Olah Data & Tampilkan Tabel ====
rows = []
for kat in KATEGORI:
    tgt = st.session_state.target_data[kat]
    act = st.session_state.aktual_data[kat]
    ach = hitung_persentase(act, tgt)
    rows.append({
        "Kategori": kat.upper(),
        "Target": tgt,
        "Aktual": act,
        "ACH%": round(ach, 2) if ach is not None else None
    })

df = pd.DataFrame(rows)

# Format tampilan angka
df_tampil = df.copy()
df_tampil["Target"] = df_tampil["Target"].apply(format_ribuan)
df_tampil["Aktual"] = df_tampil["Aktual"].apply(format_ribuan)
df_tampil["ACH%"] = df_tampil["ACH%"].apply(lambda x: f"{x:.2f}%" if x is not None else "-")

st.markdown("### Tabel Pencapaian")
st.dataframe(df_tampil, use_container_width=True)

# ==== Kartu Metrik per Kategori ====
st.markdown("### Metrik per Kategori")
for kat in KATEGORI:
    tgt = st.session_state.target_data[kat]
    act = st.session_state.aktual_data[kat]
    ach = hitung_persentase(act, tgt)
    delta = f"ACH {ach:.2f}%" if ach is not None else "ACH -"
    st.metric(
        label=kat.upper(),
        value=f"{format_ribuan(act)}",
        delta=delta
    )

# ==== Total & ACH Keseluruhan ====
total_target = sum(st.session_state.target_data.values())
total_aktual = sum(st.session_state.aktual_data.values())
ach_total = hitung_persentase(total_aktual, total_target)

st.divider()
st.markdown("### Total Keseluruhan")
t1, t2, t3 = st.columns(3)
t1.metric("Total Target", format_ribuan(total_target))
t2.metric("Total Aktual", format_ribuan(total_aktual))
t3.metric("Total ACH%", f"{ach_total:.2f}%" if ach_total is not None else "-")

# ==== Unduh CSV ====
st.markdown("### Unduh Laporan")
# Siapkan data mentah (tanpa format ribuan) agar berguna untuk olah data lanjut
df_export = df.copy()
df_export.insert(0, "Shift", shift)
df_export.insert(1, "Tanggal", tanggal.strftime("%Y-%m-%d"))
df_export.insert(2, "Toko", toko)

csv = df_export.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Unduh CSV",
    data=csv,
    file_name=f"laporan_{toko}_{tanggal.strftime('%Y%m%d')}_shift{shift}.csv",
    mime="text/csv"
)

# ==== Reset ====
st.divider()
if st.button("Reset Input ke 0"):
    for kat in KATEGORI:
        st.session_state.target_data[kat] = 0
        st.session_state.aktual_data[kat] = 0
    st.experimental_rerun()

st.success("Terimakasih 🙌")

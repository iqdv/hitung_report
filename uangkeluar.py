
# app.py
import streamlit as st
import pandas as pd
from datetime import date

# -------------------- Konfigurasi Halaman --------------------
st.set_page_config(page_title="Laporan Pengeluaran Bulanan", page_icon="💸", layout="centered")
st.title("💸 Laporan Pengeluaran Bulanan dengan Keterangan Rinci")

# -------------------- Inisialisasi Session State --------------------
DEFAULT_COLS = ["Tanggal", "Kategori", "Keperluan", "Deskripsi", "Nominal", "Metode", "Tempat", "Tags"]

if "pengeluaran" not in st.session_state:
    st.session_state.pengeluaran = pd.DataFrame(columns=DEFAULT_COLS)

# -------------------- Sidebar: Filter & Budget --------------------
st.sidebar.header("Filter & Budget")

bulan_names = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
               "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
today = date.today()

bulan_pilih = st.sidebar.selectbox("Bulan", options=list(range(1, 13)),
                                   format_func=lambda x: bulan_names[x-1], index=today.month-1)
tahun_pilih = st.sidebar.number_input("Tahun", min_value=2000, max_value=2100, value=today.year, step=1)
budget_bulan = st.sidebar.number_input("Budget Bulanan (opsional)", min_value=0, step=100000, value=0)

st.sidebar.divider()
st.sidebar.caption("Batas per kategori (opsional):")

# Daftar kategori standar
DAFTAR_KATEGORI = ["Makan/Minum", "Transport", "Belanja", "Tagihan", "Hiburan", "Kesehatan", "Pendidikan", "Lainnya"]

# Inisialisasi batas per kategori di session
if "batas_kategori" not in st.session_state:
    st.session_state.batas_kategori = {k: 0 for k in DAFTAR_KATEGORI}

# Input batas per kategori
for k in DAFTAR_KATEGORI:
    st.session_state.batas_kategori[k] = st.sidebar.number_input(
        f"Batas {k} (Rp)", min_value=0, step=50000, value=st.session_state.batas_kategori[k]
    )

# -------------------- Form Input Transaksi --------------------
st.subheader("Tambah Pengeluaran")
with st.form("form_pengeluaran", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        tanggal = st.date_input("Tanggal", value=today, format="YYYY-MM-DD")
        kategori = st.selectbox("Kategori", options=DAFTAR_KATEGORI, index=0)
        metode = st.selectbox("Metode Bayar", options=["Tunai", "Transfer", "Kartu", "E-Wallet"], index=0)
    with c2:
        nominal = st.number_input("Nominal (Rp)", min_value=0, step=1000)
        tempat = st.text_input("Tempat / Penjual (opsional)", value="")
        tags = st.text_input("Tags (pisahkan dengan koma, opsional)", value="")  # contoh: 'makan siang, kantor'

    keperluan = st.text_input("Keperluan (apa & untuk apa)", placeholder="Contoh: Makan siang, bayar parkir, token listrik")
    deskripsi = st.text_area("Catatan (detail tambahan, opsional)", placeholder="Contoh: Promo 20%, berbagi dengan teman, dsb.")

    submit = st.form_submit_button("Tambah")

if submit:
    new_row = {
        "Tanggal": tanggal,
        "Kategori": kategori,
        "Keperluan": keperluan.strip(),
        "Deskripsi": deskripsi.strip(),
        "Nominal": int(nominal),
        "Metode": metode,
        "Tempat": tempat.strip(),
        "Tags": tags.strip()
    }
    st.session_state.pengeluaran = pd.concat([st.session_state.pengeluaran, pd.DataFrame([new_row])], ignore_index=True)
    st.success("Pengeluaran ditambahkan.")

st.divider()

# -------------------- Filter Data Bulan / Tahun --------------------
df = st.session_state.pengeluaran.copy()
if not df.empty:
    df["Tanggal"] = pd.to_datetime(df["Tanggal"]).dt.date

if df.empty:
    df_bulan = df
else:
    df_bulan = df[[d.month == bulan_pilih and d.year == tahun_pilih for d in df["Tanggal"]]]

# -------------------- Hitung Ringkasan --------------------
total_bulan = int(df_bulan["Nominal"].sum()) if not df_bulan.empty else 0
hari_unik = len(set([d.day for d in df_bulan["Tanggal"]])) if not df_bulan.empty else 0
rata_harian = int(total_bulan / hari_unik) if hari_unik > 0 else 0
sisa_budget = (budget_bulan - total_bulan) if budget_bulan > 0 else None

st.markdown(f"### Ringkasan {bulan_names[bulan_pilih-1]} {tahun_pilih}")
st.write(f"- **Total Pengeluaran**: Rp {total_bulan:,}".replace(",", "."))
st.write(f"- **Rata-rata Harian**: Rp {rata_harian:,}".replace(",", "."))
if sisa_budget is not None:
    st.write(f"- **Budget Bulanan**: Rp {budget_bulan:,} → **Sisa**: Rp {sisa_budget:,}".replace(",", "."))

# -------------------- Rekap per Kategori & Peringatan Batas --------------------
st.subheader("📊 Rekap per Kategori")
if df_bulan.empty:
    st.info("Belum ada transaksi di bulan ini.")
    rekap = pd.DataFrame(columns=["Kategori", "Jumlah Transaksi", "Total (Rp)"])
else:
    rekap = df_bulan.groupby("Kategori").agg(
        **{
            "Jumlah Transaksi": ("Kategori", "count"),
            "Total (Rp)": ("Nominal", "sum")
        }
    ).reset_index().sort_values(by="Total (Rp)", ascending=False)

    # Tampilkan rekap tanpa index + format rupiah
    rekap_tampil = rekap.copy()
    rekap_tampil["Total (Rp)"] = rekap_tampil["Total (Rp)"].apply(lambda x: f"{int(x):,}".replace(",", "."))
    st.dataframe(rekap_tampil.style.hide(axis="index"), use_container_width=True)

    # Peringatan jika melewati batas kategori
    for _, row in rekap.iterrows():
        kat = row["Kategori"]
        total_kat = int(row["Total (Rp)"])
        batas = int(st.session_state.batas_kategori.get(kat, 0))
        if batas > 0 and total_kat > batas:
            st.warning(f"⚠️ **{kat}** melewati batas: Rp {total_kat:,} / Rp {batas:,}".replace(",", "."))

st.divider()

# -------------------- Tabel Transaksi (Tanpa Index) --------------------
st.subheader("📋 Daftar Transaksi (detail keperluan)")
if df_bulan.empty:
    st.info("Belum ada transaksi di bulan ini.")
else:
    df_tampil = df_bulan.copy()
    # Urutkan terbaru dulu
    df_tampil = df_tampil.sort_values(by="Tanggal", ascending=False)
    df_tampil["Nominal"] = df_tampil["Nominal"].apply(lambda x: f"{int(x):,}".replace(",", "."))
    # Pilih kolom yang informatif
    df_tampil = df_tampil[["Tanggal", "Kategori", "Keperluan", "Deskripsi", "Nominal", "Metode", "Tempat", "Tags"]]
    st.dataframe(df_tampil.style.hide(axis="index"), use_container_width=True)

st.divider()

# -------------------- Reset & Export --------------------
col_a, col_b = st.columns(2)
with col_a:
    if st.button("Reset Semua Data"):
        st.session_state.pengeluaran = pd.DataFrame(columns=DEFAULT_COLS)
        st.experimental_rerun()
with col_b:
    if not st.session_state.pengeluaran.empty:
        csv = st.session_state.pengeluaran.to_csv(index=False).encode("utf-8")
        st.download_button("Unduh Semua Data (CSV)", data=csv, file_name="pengeluaran.csv", mime="text/csv")

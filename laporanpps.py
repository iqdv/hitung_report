
import streamlit as st
from datetime import date
import pandas as pd

# ===== Fungsi bantu =====
def hitung_persentase(aktual, target):
    if target == 0:
        return 0.0
    return (aktual / target) * 100

def format_ribuan(nilai):
    try:
        return f"{int(nilai):,}".replace(",", ".")
    except:
        return str(nilai)

st.set_page_config(page_title="Laporan Sales & Fokus Mkt", layout="wide")

# ===== Judul Aplikasi =====
st.title("📊 Laporan Sales & Fokus Mkt")

# ===== Input Umum =====
col_info1, col_info2, col_info3 = st.columns([1,1,2])
with col_info1:
    shift = st.number_input("Shift (1/2/3):", min_value=1, max_value=3, step=1, value=1)
with col_info2:
    tanggal = st.date_input("Tanggal:", value=date.today())
with col_info3:
    toko = st.text_input("Nama Toko:", value="KE53")

st.markdown("---")

# ===== Daftar kategori dasar =====
kategori_list = ["sales", "voucher", "psm", "pwp", "serba", "seger", "newmem"]

# ===== Input Target & Aktual (berdampingan) =====
st.subheader("Masukkan Target & Aktual per Kategori")
col_target, col_aktual = st.columns(2)

# Default target (boleh diedit user)
default_target = {
    "sales": 8_378_500,
    "voucher": 378_500,
    "psm": 82,
    "pwp": 10,
    "serba": 11,
    "seger": 33,
    "newmem": 2
}

target_data = {}
aktual_data = {}

with col_target:
    st.caption("🎯 Target")
    for k in kategori_list:
        target_data[k] = st.number_input(
            f"Target {k.upper()}:", min_value=0.0, step=1.0, value=float(default_target.get(k, 0))
        )

with col_aktual:
    st.caption("✅ Aktual (Tercapai)")
    for k in kategori_list:
        aktual_data[k] = st.number_input(
            f"Aktual {k.upper()}:", min_value=0.0, step=1.0, value=0.0
        )

# ===== Input CEBAN & Kontribusi =====
st.subheader("Masukkan CEBAN & Kontribusi")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    ceban_actual = st.number_input("CEBAN:", min_value=0.0, step=1.0, value=0.0)

with col_c2:
    kontribusi_member = st.number_input("Kontribusi member report 47 (%):", min_value=0.0, step=0.1, value=0.0)
    vcr_jsm = st.number_input("Vcr JSM:", min_value=0.0, step=1.0, value=0.0)
    vcr_susu_hebat = st.number_input("Vcr susu hebat:", min_value=0.0, step=1.0, value=0.0)

with col_c3:
    murah_sejagat = st.number_input("Murah sejagat:", min_value=0.0, step=1.0, value=0.0)
    indonesia_juara = st.number_input("Indonesia juara:", min_value=0.0, step=1.0, value=0.0)
    item_jsm = st.number_input("Item JSM:", min_value=0.0, step=1.0, value=0.0)

st.markdown("---")

# ===== Tampilkan Laporan (tabel sisi-sisi) =====
if st.button("Tampilkan Laporan"):
    # Susun dataframe ringkas Target vs Aktual vs Ach%
    rows = []
    for k in kategori_list:
        target_val = target_data[k]
        aktual_val = aktual_data[k]
        ach = hitung_persentase(aktual_val, target_val)
        rows.append({
            "Kategori": k.upper(),
            "Target": target_val,
            "Aktual": aktual_val,
            "Ach (%)": round(ach, 2)
        })
    df = pd.DataFrame(rows)

    # Header info
    st.markdown(f"""
    **LAPORAN Sales & Fokus Mkt**  
    **SHIFT**: {shift} &nbsp;&nbsp; | &nbsp;&nbsp; **TGL**: {tanggal} &nbsp;&nbsp; | &nbsp;&nbsp; **Toko**: {toko}
    """)

    # Tabel utama (Target & Aktual berdampingan)
    st.subheader("Ringkasan Target vs Aktual")
    st.dataframe(
        df.style.format({
            "Target": lambda x: format_ribuan(x),
            "Aktual": lambda x: format_ribuan(x),
            "Ach (%)": "{:.2f}"
        }),
        use_container_width=True
    )

    # Seksi detail tambahan
    st.subheader("Detail Tambahan")
    col_d1, col_d2 = st.columns([1,1])
    with col_d1:
        st.markdown(f"**CEBAN:** {format_ribuan(ceban_actual)}")
    with col_d2:
        st.markdown(f"""
        **Kontribusi:**
        - Kontribusi member report 47: **{kontribusi_member:.2f}%**
        - Vcr JSM: **{format_ribuan(vcr_jsm)}**
        - Vcr susu hebat: **{format_ribuan(vcr_susu_hebat)}**
        - Murah sejagat: **{format_ribuan(murah_sejagat)}**
        - Indonesia juara: **{format_ribuan(indonesia_juara)}**
        - Item JSM: **{format_ribuan(item_jsm)}**
        """)

    # Opsi ekspor teks rapi (opsional)
    st.markdown("---")
    st.caption("📋 Salin teks laporan (opsional)")
    laporan_txt = f"""
LAPORAN Sales & Fokus Mkt

SHIFT  : {shift}
TGL    : {tanggal}
Toko   : {toko}

TARGET / AKTUAL / ACH%

"""[1:]  # Hapus newline pertama

    for k in kategori_list:
        laporan_txt += (
            f"{k.upper()}: "
            f"{format_ribuan(target_data[k])} / "
            f"{format_ribuan(aktual_data[k])} / "
            f"{hitung_persentase(aktual_data[k], target_data[k]):.2f}%\n"
        )

    laporan_txt += f"""
CEBAN: {format_ribuan(ceban_actual)}

Kontribusi member report 47: {kontribusi_member:.2f}%
Vcr JSM : {format_ribuan(vcr_jsm)}
Vcr susu hebat: {format_ribuan(vcr_susu_hebat)}
Murah sejagat : {format_ribuan(murah_sejagat)}
Indonesia juara: {format_ribuan(indonesia_juara)}
Item JSM : {format_ribuan(item_jsm)}

Terima kasih
"""[1:]

    st.text_area("Teks Laporan:", value=laporan_txt, height=260)


import streamlit as st
from datetime import date

# =========================
# FUNGSI BANTU
# =========================
def hitung_persentase(aktual, target):
    return (aktual / target * 100) if target else 0

def format_ribuan(nilai):
    return f"{int(nilai):,}".replace(",", ".")

def ach_color(ach):
    if ach >= 100:
        return "🟢"
    elif ach >= 80:
        return "🟡"
    else:
        return "🔴"

def input_angka_titik(label, key):
    teks = st.text_input(label, key=key, placeholder="contoh: 8.378.500")
    if teks:
        return int(teks.replace(".", "").replace(",", ""))
    return 0

# =========================
# JUDUL
# =========================
st.title("📊 Laporan Sales & Fokus MKT")
st.caption("by fresadaper | TikTok: @fresadaper03")

# =========================
# INPUT UMUM
# =========================
c1, c2, c3 = st.columns(3)
with c1:
    shift = st.number_input("Shift", 1, 3, 1)
with c2:
    tanggal = date.today()
    st.text_input("Tanggal", tanggal.strftime("%d-%m-%Y"), disabled=True)
with c3:
    toko = st.text_input("Nama Toko", "KE53")

# =========================
# INPUT TARGET & ACTUAL
# =========================
st.subheader("Input Target & Actual (ACV)")

kategori = [
    ("sales", "Sales"),
    ("voucher", "Voucher"),
    ("psm", "PSM"),
    ("pwp", "PWP"),
    ("serba", "SERBA"),
    ("seger", "SEGER"),
    ("newmem", "New Member"),
]

target_data, aktual_data = {}, {}

h1, h2, h3 = st.columns([2, 4, 4])
h1.markdown("**Kategori**")
h2.markdown("**Target**")
h3.markdown("**Actual (ACV)**")

for key, label in kategori:
    a, b, c = st.columns([2, 4, 4])
    a.write(label)

    if key in ["sales", "voucher"]:
        with b:
            target_data[key] = input_angka_titik("Target", f"t_{key}")
        with c:
            aktual_data[key] = input_angka_titik("Actual", f"a_{key}")
    else:
        target_data[key] = b.number_input("Target", min_value=0, step=1, key=f"t_{key}")
        aktual_data[key] = c.number_input("Actual", min_value=0, step=1, key=f"a_{key}")

# =========================
# INPUT TAMBAHAN
# =========================
st.subheader("Input Tambahan")
ceban = st.number_input("CEBAN", 0, step=1)

# =========================
# TAMPILKAN LAPORAN
# =========================
if st.button("📄 Tampilkan Laporan"):
    ach = {}
    for k in target_data:
        ach[k] = hitung_persentase(aktual_data[k], target_data[k])

    laporan = f"""
LAPORAN SALES & FOKUS MKT
SHIFT : {shift}
TGL   : {tanggal}
TOKO  : {toko}

TARGET / ACTUAL / ACH%

Sales    : {format_ribuan(target_data['sales'])} / {format_ribuan(aktual_data['sales'])} / {ach['sales']:.2f}% {ach_color(ach['sales'])}
Voucher  : {format_ribuan(target_data['voucher'])} / {format_ribuan(aktual_data['voucher'])} / {ach['voucher']:.2f}% {ach_color(ach['voucher'])}

PSM      : {target_data['psm']} / {aktual_data['psm']} / {ach['psm']:.2f}% {ach_color(ach['psm'])}
PWP      : {target_data['pwp']} / {aktual_data['pwp']} / {ach['pwp']:.2f}% {ach_color(ach['pwp'])}
SERBA    : {target_data['serba']} / {aktual_data['serba']} / {ach['serba']:.2f}% {ach_color(ach['serba'])}
SEGER    : {target_data['seger']} / {aktual_data['seger']} / {ach['seger']:.2f}% {ach_color(ach['seger'])}

CEBAN    : {ceban}

New Mem  : {target_data['newmem']} / {aktual_data['newmem']} / {ach['newmem']:.2f}% {ach_color(ach['newmem'])}

By : fresadaper
TikTok : @fresadaper03
"""

    st.text(laporan)

    st.text_area(
        "📋 Salin laporan ini → paste ke WhatsApp",
        laporan,
        height=350
    )

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>📱 TikTok : <b>@fresadaper03</b> | Made with ❤️ by <b>fresadaper</b></center>",
    unsafe_allow_html=True
)

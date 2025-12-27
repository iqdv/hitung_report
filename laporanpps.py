import streamlit as st
from datetime import date

# =========================
# FUNGSI BANTU
# =========================
def hitung_persentase(aktual, target):
    return (aktual / target * 100) if target else 0

def format_ribuan(nilai):
    return f"{int(nilai):,}".replace(",", ".")

# =========================
# JUDUL APLIKASI
# =========================
st.title("📊 Laporan Sales & Fokus MKT")
st.caption("by fresadaper | TikTok: @fresadaper03")

# =========================
# INPUT UMUM
# =========================
col_a, col_b, col_c = st.columns(3)
with col_a:
    shift = st.number_input("Shift", min_value=1, max_value=3, step=1)
with col_b:
    tanggal = date.today()
    st.text_input("Tanggal", value=tanggal.strftime("%d-%m-%Y"), disabled=True)
with col_c:
    toko = st.text_input("Nama Toko", value="KE53")

# =========================
# INPUT TARGET & ACTUAL
# =========================
st.subheader("Input Target & Actual (ACV)")

kategori = [
    ("sales", "Sales", 1000),
    ("voucher", "Voucher", 1000),
    ("psm", "PSM", 1),
    ("pwp", "PWP", 1),
    ("serba", "SERBA", 1),
    ("seger", "SEGER", 1),
    ("newmem", "New Member", 1),
]

target_data = {}
aktual_data = {}

# Header kolom
h1, h2, h3 = st.columns([2, 2, 1])
h1.markdown("**Kategori**")
h2.markdown("**Target**")
h3.markdown("**Actual**")

for key, label, step in kategori:
    c1, c2, c3 = st.columns([2, 2, 1])
    c1.write(label)
    target_data[key] = c2.number_input(
        "", min_value=0, step=step, key=f"t_{key}"
    )
    aktual_data[key] = c3.number_input(
        "", min_value=0, step=step, key=f"a_{key}"
    )

# =========================
# INPUT TAMBAHAN
# =========================
st.subheader("Input Tambahan")

ceban_actual = st.number_input("CEBAN", min_value=0, step=1)

st.subheader("Kontribusi")
kontribusi = {
    "konstribusi member": st.number_input("Kontribusi Member Report 47 (%)", min_value=0, step=1),
    "vcr jsm": st.number_input("VCR JSM", min_value=0, step=1),
    "vcr susu hebat": st.number_input("VCR Susu Hebat", min_value=0, step=1),
    "murah sejagat": st.number_input("Murah Sejagat", min_value=0, step=1),
    "indonesia juara": st.number_input("Indonesia Juara", min_value=0, step=1),
    "item jsm": st.number_input("Item JSM", min_value=0, step=1),
}

# =========================
# TAMPILKAN LAPORAN
# =========================
if st.button("📄 Tampilkan Laporan"):

    laporan = f"""
LAPORAN SALES & FOKUS MKT

SHIFT : {shift}
TGL   : {tanggal}
TOKO  : {toko}

           TARGET / ACTUAL / ACH%

Sales    : {format_ribuan(target_data['sales'])} / {format_ribuan(aktual_data['sales'])} / {hitung_persentase(aktual_data['sales'], target_data['sales']):.2f}%
Voucher  : {format_ribuan(target_data['voucher'])} / {format_ribuan(aktual_data['voucher'])} / {hitung_persentase(aktual_data['voucher'], target_data['voucher']):.2f}%

PSM      : {target_data['psm']} / {aktual_data['psm']} / {hitung_persentase(aktual_data['psm'], target_data['psm']):.2f}%
PWP      : {target_data['pwp']} / {aktual_data['pwp']} / {hitung_persentase(aktual_data['pwp'], target_data['pwp']):.2f}%
SERBA    : {target_data['serba']} / {aktual_data['serba']} / {hitung_persentase(aktual_data['serba'], target_data['serba']):.2f}%
SEGER    : {target_data['seger']} / {aktual_data['seger']} / {hitung_persentase(aktual_data['seger'], target_data['seger']):.2f}%

CEBAN    : {ceban_actual}

New Mem  : {target_data['newmem']} / {aktual_data['newmem']} / {hitung_persentase(aktual_data['newmem'], target_data['newmem']):.2f}%

Kontribusi Member : {kontribusi['konstribusi member']}%
VCR JSM           : {kontribusi['vcr jsm']}
VCR Susu Hebat    : {kontribusi['vcr susu hebat']}
Murah Sejagat     : {kontribusi['murah sejagat']}
Indonesia Juara   : {kontribusi['indonesia juara']}
Item JSM          : {kontribusi['item jsm']}

Terima kasih

By : fresadaper
TikTok : @fresadaper03
"""

    st.text(laporan)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>📱 TikTok : <b>@fresadaper03</b> | Made with ❤️ by <b>fresadaper</b></center>",
    unsafe_allow_html=True
)

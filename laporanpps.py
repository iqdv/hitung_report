import streamlit as st
from datetime import date

# =========================
# FUNGSI BANTU
# =========================
def hitung_persentase(aktual, target):
    return (aktual / target * 100) if target else 0

def format_ribuan(nilai):
    return f"{int(nilai):,}".replace(",", ".")

def parse_angka(teks):
    if teks is None or teks == "":
        return 0
    return int(teks.replace(".", ""))

def input_angka_titik(label, key):
    teks = st.text_input(label, key=key)
    angka = parse_angka(teks)
    st.session_state[key] = format_ribuan(angka) if angka > 0 else ""
    return angka

# =========================
# JUDUL APLIKASI
# =========================
st.title("📊 Laporan Sales & Fokus MKT")
st.caption("by fresadaper | TikTok: @fresadaper03")

# =========================
# INPUT UMUM
# =========================
col1, col2, col3 = st.columns(3)
with col1:
    shift = st.number_input("Shift", min_value=1, max_value=3, step=1)
with col2:
    tanggal = date.today()
    st.text_input("Tanggal", value=tanggal.strftime("%d-%m-%Y"), disabled=True)
with col3:
    toko = st.text_input("Nama Toko", value="KE53")

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

target_data = {}
aktual_data = {}

# Header
h1, h2, h3 = st.columns([2, 4, 4])
h1.markdown("**Kategori**")
h2.markdown("**Target**")
h3.markdown("**Actual (ACV)**")

for key, label in kategori:
    c1, c2, c3 = st.columns([2, 4, 4])
    c1.write(label)

    if key in ["sales", "voucher"]:
        with c2:
            target_data[key] = input_angka_titik("Target", f"t_{key}")
        with c3:
            aktual_data[key] = input_angka_titik("Actual", f"a_{key}")
    else:
        target_data[key] = c2.number_input("Target", min_value=0, step=1, key=f"t_{key}")
        aktual_data[key] = c3.number_input("Actual", min_value=0, step=1, key=f"a_{key}")

# =========================
# INPUT TAMBAHAN
# =========================
st.subheader("Input Tambahan")
ceban_actual = st.number_input("CEBAN", min_value=0, step=1)

st.subheader("Kontribusi")
kontribusi = {
    "member": st.number_input("Kontribusi Member Report 47 (%)", min_value=0, step=1),
    "vcr_jsm": st.number_input("VCR JSM", min_value=0, step=1),
    "vcr_susu": st.number_input("VCR Susu Hebat", min_value=0, step=1),
    "murah": st.number_input("Murah Sejagat", min_value=0, step=1),
    "juara": st.number_input("Indonesia Juara", min_value=0, step=1),
    "item_jsm": st.number_input("Item JSM", min_value=0, step=1),
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

Kontribusi Member : {kontribusi['member']}%
VCR JSM           : {kontribusi['vcr_jsm']}
VCR Susu Hebat    : {kontribusi['vcr_susu']}
Murah Sejagat     : {kontribusi['murah']}
Indonesia Juara   : {kontribusi['juara']}
Item JSM          : {kontribusi['item_jsm']}

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


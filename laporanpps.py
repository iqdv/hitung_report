import streamlit as st
from datetime import date

# =========================
# FUNGSI
# =========================
def ach(act, tgt):
    return (act / tgt * 100) if tgt > 0 else 0

def ribuan(x):
    return f"{int(x):,}".replace(",", ".")

# =========================
# HEADER
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
    tanggal = st.date_input("Tanggal", date.today())
with c3:
    toko = st.text_input("Toko", "KE53")

# =========================
# INPUT TARGET & ACTUAL
# =========================
st.subheader("Target & Actual")

data = {
    "Sales": {},
    "Voucher": {},
    "PSM": {},
    "PWP": {},
    "SERBA": {},
    "SEGER": {},
    "New Member": {}
}

for k in data:
    col1, col2 = st.columns(2)
    with col1:
        data[k]["t"] = st.number_input(f"Target {k}", 0, step=1)
    with col2:
        data[k]["a"] = st.number_input(f"Actual {k}", 0, step=1)

ceban = st.number_input("CEBAN", 0, step=1)

st.subheader("Kontribusi")
kontribusi = {
    "member": st.number_input("Kontribusi member report 47 (%)", 0, step=1),
    "jsm": st.number_input("Vcr JsM", 0, step=1),
    "susu": st.number_input("Vcr susu hebat", 0, step=1),
    "murah": st.number_input("Murah sejagat", 0, step=1),
    "indo": st.number_input("Indonesia juara", 0, step=1),
    "item": st.number_input("Item JSM", 0, step=1),
}

# =========================
# OUTPUT
# =========================
if st.button("📄 Tampilkan Laporan"):

    laporan = f"""LAPORAN  sales & FOKUS 	Mkt

SHIFT  : {shift}
TGL    : {tanggal}
Toko   : {toko}

          TARGET /ACT/ACH%

Sales: {ribuan(data['Sales']['t'])} / {ribuan(data['Sales']['a'])} / {ach(data['Sales']['a'], data['Sales']['t']):.2f}%
Voucher: {ribuan(data['Voucher']['t'])} / {ribuan(data['Voucher']['a'])} / {ach(data['Voucher']['a'], data['Voucher']['t']):.2f}%

PSM: {data['PSM']['t']} / {data['PSM']['a']} / {ach(data['PSM']['a'], data['PSM']['t']):.2f}%
PWP: {data['PWP']['t']} / {data['PWP']['a']} / {ach(data['PWP']['a'], data['PWP']['t']):.2f}%
SERBA: {data['SERBA']['t']} / {data['SERBA']['a']} / {ach(data['SERBA']['a'], data['SERBA']['t']):.2f}%

SEGER: {data['SEGER']['t']} / {data['SEGER']['a']} / {ach(data['SEGER']['a'], data['SEGER']['t']):.2f}%
CEBAN: {ceban}

New Member: {data['New Member']['t']} / {data['New Member']['a']} / {ach(data['New Member']['a'], data['New Member']['t']):.2f}%
Kontribusi member report 47: {kontribusi['member']}%
Vcr JsM : {kontribusi['jsm']}
Vcr susu hebat: {kontribusi['susu']}
Murah sejagat : {kontribusi['murah']}
Indonesia juara: {kontribusi['indo']}
Item JSM : {kontribusi['item']}

Terimakasih
"""

    st.code(laporan, language="text")  # ada tombol COPY



import streamlit as st
from datetime import date

def hitung_persentase(aktual, target):
    if target == 0:
        return 0
    return (aktual / target) * 100

target_data = {
    "sales": 8378500,
    "voucher": 378500,
    "psm": 82,
    "pwp": 10,
    "serba": 11,
    "seger": 33,
    "newmem": 2
}

st.title("Cek Pencapaian Toko")

# Input shift, tanggal, toko
shift = st.selectbox("Shift", [1, 2, 3])
tanggal = st.date_input("Tanggal", value=date.today())
toko = st.text_input("Toko", value="KE53")

# Input aktual
st.subheader("Masukkan Data Aktual")
aktual_data = {}
for kategori in target_data:
    aktual_data[kategori] = st.number_input(f"{kategori.upper()}", min_value=0.0)

# Input kontribusi member
st.subheader("Kontribusi Member")
kontribusi = {
    "pwp personal care unilever": st.number_input("PWP Personal Care Unilever", min_value=0.0),
    "voucher cashback 10k": st.number_input("Voucher Cashback 10k", min_value=0.0),
    "murah sejagat": st.number_input("Murah Sejagat", min_value=0.0)
}

# Output
st.markdown("### Hasil Pencapaian")
st.markdown(f"""
**Shift** : {shift}  
**Tanggal** : {tanggal}  
**Toko** : {toko}  

&nbsp;  
**Target / Acv / Ach%**  
""")

for kategori in target_data:
    persen = hitung_persentase(aktual_data[kategori], target_data[kategori])
    st.markdown(f"{kategori.upper():<10} : {target_data[kategori]} / {aktual_data[kategori]} / {persen:.2f}%")

st.markdown("&nbsp;  \n**Kontribusi Member:**")
for item, nilai in kontribusi.items():
    st.markdown(f"{item} : {nilai}")

st.markdown("&nbsp;  \n**Terimakasih**")

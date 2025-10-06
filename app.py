import streamlit as st

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
    "sejagat": 10,
    "newmem": 2
}

st.title("Cek Pencapaian Toko")

aktual_data = {}
for kategori in target_data:
    aktual_data[kategori] = st.number_input(f"Masukkan nilai {kategori.upper()}", min_value=0.0)

st.write("### Hasil Pencapaian:")
for kategori in target_data:
    persen = hitung_persentase(aktual_data[kategori], target_data[kategori])
    st.write(f"{kategori.upper()}: {persen:.2f}%")

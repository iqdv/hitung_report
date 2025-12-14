
import streamlit as st

# ---------- Utilitas ----------
def format_rupiah(x: float) -> str:
    """Format angka ke Rupiah dengan titik sebagai pemisah ribuan."""
    return "Rp " + f"{x:,.0f}".replace(",", ".")

# ---------- Pengaturan Halaman ----------
st.set_page_config(page_title="Kalkulator Diskon", page_icon="🧮", layout="centered")

st.title("🧮 Kalkulator Diskon")
st.caption("Masukkan harga dan diskon untuk menghitung total bayar.")

# ---------- Input ----------
with st.form("form_diskon"):
    col1, col2 = st.columns(2)

    with col1:
        harga = st.number_input(
            "HARGA",
            min_value=0,
            step=1000,
            help="Masukkan harga sebelum diskon.",
            format="%d",
        )
    with col2:
        diskon = st.number_input(
            "DISKON (%)",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            help="Persentase diskon (0–100).",
        )

    submit = st.form_submit_button("Hitung")

# ---------- Perhitungan & Output ----------
if submit:
    # Validasi sederhana
    if harga <= 0:
        st.error("Harga harus lebih dari 0.")
    elif not (0 <= diskon <= 100):
        st.error("Diskon harus di antara 0–100%.")
    else:
        nilai_diskon = harga * diskon / 100
        total = harga - nilai_diskon

        st.success("Perhitungan berhasil!")

        # Ringkasan cepat
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Harga Awal", format_rupiah(harga))
        with c2:
            st.metric("Diskon", f"{diskon:.0f}%")
        with c3:
            st.metric("Potongan", format_rupiah(nilai_diskon))

        st.subheader("Total Bayar")
        st.markdown(
            f"""
            ### {format_rupiah(total)}
            """
        )

        # Detail breakdown
        with st.expander("Detail Perhitungan"):
            st.write(f"Harga awal  : {format_rupiah(harga)}")
            st.write(f"Diskon      : {diskon:.0f}%")
            st.write(f"Potongan    : {format_rupiah(nilai_diskon)}")
            st.write(f"Total bayar : **{format_rupiah(total)}**")

# Footer tip
st.caption("Tip: Ubah step input harga ke 1 jika ingin granularity per 1 rupiah.")

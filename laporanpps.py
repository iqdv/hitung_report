
import streamlit as st
from datetime import date
from math import floor

# ===== Fungsi bantu =====
def format_ribuan(nilai):
    """Format angka ke ribuan dengan titik (8.378.500)"""
    try:
        return f"{int(round(nilai)):,}".replace(",", ".")
    except Exception:
        return str(nilai)

def hitung_act_dari_acv(target, acv_persen):
    """Hitung ACT = target * (acv/100)"""
    if target is None or acv_persen is None:
        return 0
    return round(target * (acv_persen / 100.0), 0)

# ===== Judul & info umum =====
st.title("📊 Laporan Sales & Fokus Mkt by FRESADAPER")
st.caption("Input berurutan: Target (atas) → ACV (%)(bawah). ACT dihitung otomatis dari ACV.")

with st.form("form_laporan"):
    # Header umum
    cols_info = st.columns(3)
    with cols_info[0]:
        shift = st.number_input("Shift (1/2/3)", min_value=1, max_value=3, step=1, value=1)
    with cols_info[1]:
        tanggal = date.today()
        st.text_input("Tanggal", value=str(tanggal), disabled=True)
    with cols_info[2]:
        toko = st.text_input("Nama Toko", value="KE53")

    st.divider()
    st.subheader("🎯 Target & ACV (%) — diisi berurutan (Target di atas, ACV di bawah)")

    # Helper untuk render pasangan input target/acv
    def pair_target_acv(label, default_target=0, default_acv=0.0):
        st.markdown(f"**{label}**")
        target = st.number_input(f"Target {label}", min_value=0, step=1, value=int(default_target), key=f"t_{label}")
        acv = st.number_input(f"ACV {label} (%)", min_value=0.0, max_value=500.0, step=0.1, value=float(default_acv), key=f"a_{label}")
        st.write("")  # spacer kecil
        return target, acv

    # Urutan input: setiap KPI target lalu ACV
    sales_t, sales_acv = pair_target_acv("Sales", 8_378_500, 0.0)
    voucher_t, voucher_acv = pair_target_acv("Voucher", 378_500, 0.0)
    psm_t, psm_acv       = pair_target_acv("PSM", 82, 0.0)
    pwp_t, pwp_acv       = pair_target_acv("PWP", 10, 0.0)
    serba_t, serba_acv   = pair_target_acv("SERBA", 11, 0.0)
    seger_t, seger_acv   = pair_target_acv("SEGER", 33, 0.0)
    newmem_t, newmem_acv = pair_target_acv("New Member", 2, 0.0)

    st.divider()

    # Input CEBAN & Kontribusi
    ceban_actual = st.number_input("CEBAN (Aktual)", min_value=0, step=1, value=0)

    st.subheader("Kontribusi")
    kontribusi_member = st.number_input("Konstribusi member report 47 (%)", min_value=0.0, step=0.1, value=0.0)
    vcr_jsm           = st.number_input("Vcr JsM", min_value=0, step=1, value=0)
    vcr_susu_hebat    = st.number_input("Vcr susu hebat", min_value=0, step=1, value=0)
    murah_sejagat     = st.number_input("Murah sejagat", min_value=0, step=1, value=0)
    indonesia_juara   = st.number_input("Indonesia juara", min_value=0, step=1, value=0)
    item_jsm          = st.number_input("Item JSM", min_value=0, step=1, value=0)

    submit = st.form_submit_button("Tampilkan Laporan")

# ===== Setelah submit: buat laporan =====
if submit:
    # Hitung ACT dari ACV
    sales_act   = hitung_act_dari_acv(sales_t, sales_acv)
    voucher_act = hitung_act_dari_acv(voucher_t, voucher_acv)
    psm_act     = hitung_act_dari_acv(psm_t, psm_acv)
    pwp_act     = hitung_act_dari_acv(pwp_t, pwp_acv)
    serba_act   = hitung_act_dari_acv(serba_t, serba_acv)
    seger_act   = hitung_act_dari_acv(seger_t, seger_acv)
    newmem_act  = hitung_act_dari_acv(newmem_t, newmem_acv)

    # Bentuk laporan teks
    laporan = f"""
LAPORAN  sales & FOKUS \tMkt

SHIFT  : {shift}
TGL    : {tanggal}
Toko   : {toko}

          TARGET / ACT / ACH%

Sales   : {format_ribuan(sales_t)} / {format_ribuan(sales_act)} / {sales_acv:.2f}%
Voucher : {format_ribuan(voucher_t)} / {format_ribuan(voucher_act)} / {voucher_acv:.2f}%

PSM     : {format_ribuan(psm_t)} / {format_ribuan(psm_act)} / {psm_acv:.2f}%
PWP     : {format_ribuan(pwp_t)} / {format_ribuan(pwp_act)} / {pwp_acv:.2f}%
SERBA   : {format_ribuan(serba_t)} / {format_ribuan(serba_act)} / {serba_acv:.2f}%

SEGER   : {format_ribuan(seger_t)} / {format_ribuan(seger_act)} / {seger_acv:.2f}%
CEBAN   : {format_ribuan(ceban_actual)}

New Member: {format_ribuan(newmem_t)} / {format_ribuan(newmem_act)} / {newmem_acv:.2f}%

Kontribusi member report 47: {kontribusi_member:.2f}%
Vcr JsM             : {vcr_jsm}
Vcr susu hebat      : {vcr_susu_hebat}
Murah sejagat       : {murah_sejagat}
Indonesia juara     : {indonesia_juara}
Item JSM            : {item_jsm}

Terimakasih
""".strip()

    # Tampilkan teks laporan standar
    st.text(laporan)

    # ===== Menu Copy Text Laporan (HTML + JS) =====
    st.markdown(
        f"""
<div style="margin-top: 12px; margin-bottom: 6px;">
  <label style="font-weight:600;">📋 Salin / Edit Laporan:</label>
  <textarea id="laporan_textarea" rows="18" style="width:100%; font-family: monospace; font-size: 13px;">{laporan}</textarea>
  <button id="copy_btn" style="margin-top:8px; padding:6px 10px; cursor:pointer;">📋 Copy</button>
  <span id="copy_status" style="margin-left:8px; color:green;"></span>
</div>
<script>
const btn = document.getElementById('copy_btn');
const ta  = document.getElementById('laporan_textarea');
const statusEl = document.getElementById('copy_status');

btn.addEventListener('click', async () => {{
  try {{
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      await navigator.clipboard.writeText(ta.value);
    }} else {{
      ta.select();
      ta.setSelectionRange(0, ta.value.length);
      document.execCommand('copy');
    }}
    statusEl.textContent = 'Tersalin!';
    statusEl.style.color = 'green';
    setTimeout(() => {{ statusEl.textContent = ''; }}, 1500);
  }} catch (err) {{
    statusEl.textContent = 'Gagal menyalin';
    statusEl.style.color = 'red';
    console.error(err);
  }}
}});
</script>
        """,
        unsafe_allow_html=True,
    )

    # Tombol download .txt
    st.download_button(
        label="⬇️ Download Laporan (.txt)",
        data=laporan,
        file_name=f"laporan_sales_{toko}_{tanggal}.txt",
        mime="text/plain",
    )

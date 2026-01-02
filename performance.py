
import streamlit as st
import datetime

# =========================
# Utilitas umum
# =========================
def hitung_persen(target, actual):
    return (actual / target * 100.0) if target else 0.0

def format_persen(n):
    s = f"{n:.2f}".rstrip('0').rstrip('.')
    return s + '%'

def format_rupiah(n):
    try:
        return "Rp " + f"{int(n):,}".replace(",", ".")
    except Exception:
        return "Rp 0"

def format_ribuan(nilai):
    # cocok untuk angka tanpa "Rp"
    return f"{int(nilai):,}".replace(",", ".")

def format_tanggal_id(d: datetime.date):
    bulan_id = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    return f"{d.day:02d} {bulan_id[d.month-1]} {d.year}"

st.set_page_config(page_title="Performance & Fokus Cabang", layout="centered")

# =========================
# Sidebar untuk memilih menu
# =========================
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["1. Laporan FOKUS ALL SHIFT PER HARI", "2. Laporan Sales & Fokus Mkt", "3. Menghitung Persentase"]
)

st.title("FORM PERFORMANCE & FOCUS CABANG CIKOKOL")

# =========================
# MENU 1
# =========================
if menu.startswith("1"):
    st.subheader("Laporan FOKUS ALL SHIFT PER HARI (Template Lengkap)")

    # Header
    tgl = st.date_input("TGL", value=datetime.date.today())
    kode = st.text_input("KODE", "")
    toko = st.text_input("TOKO", "")

    # REVENUE
    st.markdown("### REVENUE")
    target_sales = st.number_input("TARGET NET SALES (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    actual_sales = st.number_input("ACTUAL NET SALES (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    sales_achive = hitung_persen(target_sales, actual_sales)
    sales_gap = target_sales - actual_sales

    # PSM + Week
    week_psm = st.text_input("PSM WEEK (contoh: WEEK 1)", value="WEEK 1")
    t_psm = st.number_input("TARGET PSM", min_value=0.0, step=1.0)
    a_psm = st.number_input("ACTUAL PSM", min_value=0.0, step=1.0)
    ach_psm = hitung_persen(t_psm, a_psm)

    # PWP + Periode
    periode_pwp = st.text_input("PWP PERIODE (contoh: PERIODE 1)", value="PERIODE 1")
    t_pwp = st.number_input("TARGET PWP", min_value=0.0, step=1.0)
    a_pwp = st.number_input("ACTUAL PWP", min_value=0.0, step=1.0)
    ach_pwp = hitung_persen(t_pwp, a_pwp)

    # SERTIS + Periode
    periode_sertis = st.text_input("SERTIS PERIODE (contoh: PERIODE 1)", value="PERIODE 1")
    t_sertis = st.number_input("TARGET SERTIS", min_value=0.0, step=1.0)
    a_sertis = st.number_input("ACTUAL SERTIS", min_value=0.0, step=1.0)
    ach_sertis = hitung_persen(t_sertis, a_sertis)

    # INVENTORY
    st.markdown("---")
    st.markdown("### INVENTORY")
    b_pl = st.number_input("BUDGET PL (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    a_pl = st.number_input("ACTUAL PL (Rp)", min_value=0.0, step=1000.0, format="%.0f")

    b_br = st.number_input("BUDGET BR,BKE (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    a_br = st.number_input("ACTUAL BR,BKE (Rp)", min_value=0.0, step=1000.0, format="%.0f")

    # FOCUS CABANG
    st.markdown("---")
    st.markdown("### FOCUS CABANG")
    t_telur = st.number_input("TARGET TELUR", min_value=0.0, step=1.0)
    a_telur = st.number_input("ACTUAL TELUR", min_value=0.0, step=1.0)
    ach_telur = hitung_persen(t_telur, a_telur)

    t_toys = st.number_input("TARGET TOYS", min_value=0.0, step=1.0)
    a_toys = st.number_input("ACTUAL TOYS", min_value=0.0, step=1.0)
    ach_toys = hitung_persen(t_toys, a_toys)

    t_hw = st.number_input("TARGET HOTWHEELS BASIC", min_value=0.0, step=1.0)
    a_hw = st.number_input("ACTUAL HOTWHEELS BASIC", min_value=0.0, step=1.0)
    ach_hw = hitung_persen(t_hw, a_hw)

    t_djoy = st.number_input("TARGET DJOY", min_value=0.0, step=1.0)
    a_djoy = st.number_input("ACTUAL DJOY", min_value=0.0, step=1.0)
    ach_djoy = hitung_persen(t_djoy, a_djoy)

    t_unipin = st.number_input("TARGET UNIPIN", min_value=0.0, step=1.0)
    a_unipin = st.number_input("ACTUAL UNIPIN", min_value=0.0, step=1.0)
    ach_unipin = hitung_persen(t_unipin, a_unipin)

    t_sueegerr = st.number_input("TARGET SUEEGERR", min_value=0.0, step=1.0)
    a_sueegerr = st.number_input("ACTUAL SUEEGERR", min_value=0.0, step=1.0)
    ach_sueegerr = hitung_persen(t_sueegerr, a_sueegerr)

    t_fjsm = st.number_input("TARGET FOKUS JSM", min_value=0.0, step=1.0)
    a_fjsm = st.number_input("ACTUAL FOKUS JSM", min_value=0.0, step=1.0)
    ach_fjsm = hitung_persen(t_fjsm, a_fjsm)

    st.markdown("#### Beanspot")
    t_rtd = st.number_input("TARGET BEANSPOT RTD", min_value=0.0, step=1.0)
    a_rtd = st.number_input("ACTUAL BEANSPOT RTD", min_value=0.0, step=1.0)
    ach_rtd = hitung_persen(t_rtd, a_rtd)

    t_oni = st.number_input("TARGET BEANSPOT ONIGIRI", min_value=0.0, step=1.0)
    a_oni = st.number_input("ACTUAL BEANSPOT ONIGIRI", min_value=0.0, step=1.0)
    ach_oni = hitung_persen(t_oni, a_oni)
    avg_toko = (ach_rtd + ach_oni) / 2.0 if (t_rtd or t_oni) else 0.0

    # ECOMMERCE
    st.markdown("---")
    st.markdown("### ECOMMERCE")
    t_ev = st.number_input("TARGET EVOUCHER (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    a_ev = st.number_input("ACTUAL EVOUCHER (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    ach_ev = hitung_persen(t_ev, a_ev)

    t_fb = st.number_input("TARGET FEE BASED (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    a_fb = st.number_input("ACTUAL FEE BASED (Rp)", min_value=0.0, step=1000.0, format="%.0f")
    ach_fb = hitung_persen(t_fb, a_fb)

    # Build output teks persis template
    output_text = f"""*PERFORMANCE & FOCUS CABANG CIKOKOL*\t
TGL : \t{format_tanggal_id(tgl)}

KODE : {kode}
TOKO : {toko}

*REVENUE*\t
*1.NET SALES*\t
TARGET :\t{format_rupiah(target_sales)}
ACTUAL :\t{format_rupiah(actual_sales)}
ACHIVE :\t{format_persen(sales_achive)}
GAP TO TARGET :\t{format_rupiah(sales_gap)}

*2.PSM*\t
*{week_psm}*\t
TARGET :\t{t_psm:g}
ACTUAL :\t{a_psm:g}
ACHIVE :\t{format_persen(ach_psm)}

*3.PWP*\t
*{periode_pwp}*\t
TARGET :\t{t_pwp:g}
ACTUAL :\t{a_pwp:g}
ACHIVE :\t{format_persen(ach_pwp)}

*4.SERTIS*\t
*{periode_sertis}*\t
TARGET :\t{t_sertis:g}
ACTUAL :\t{a_sertis:g}
ACHIVE :\t{format_persen(ach_sertis)}
--------------------------------\t
*INVENTORY*\t
*5.PL*\t
BUDGET ( 0,14% ) Rp :\t{format_rupiah(b_pl)}
ACTUAL Rp :\t{format_rupiah(a_pl)}
*6.BR,BKE*\t
BUDGET (0,30) Rp :\t{format_rupiah(b_br)}
ACTUAL Rp :\t{format_rupiah(a_br)}
--------------------------------\t
*FOCUS CABANG*\t
*7.TELUR*\t
TARGET :\t{t_telur:g}
ACTUAL :\t{a_telur:g}
ACHIVE :\t{format_persen(ach_telur)}
*8.TOYS* :\t
TARGET :\t{t_toys:g}
ACTUAL :\t{a_toys:g}
ACHIVE :\t{format_persen(ach_toys)}
*HOTWHEELS BASIC*\t
TARGET :\t{t_hw:g}
ACTUAL :\t{a_hw:g}
ACHIVE :\t{format_persen(ach_hw)}
*9.DJOY* :\t
TARGET :\t{t_djoy:g}
ACTUAL :\t{a_djoy:g}
ACHIVE :\t{format_persen(ach_djoy)}
*10.UNIPIN*\t
TARGET :\t{t_unipin:g}
ACTUAL :\t{a_unipin:g}
ACHIVE :\t{format_persen(ach_unipin)}
*11.SUEEGERR*\t
TARGET :\t{t_sueegerr:g}
ACTUAL :\t{a_sueegerr:g}
ACHIVE :\t{format_persen(ach_sueegerr)}
*12.FOKUS JSM*\t
TARGET :\t{t_fjsm:g}
ACTUAL :\t{a_fjsm:g}
ACHIVE :\t{format_persen(ach_fjsm)}
*13.BEANSPOT*\t
*RTD*\t
TARGET :\t{t_rtd:g}
ACTUAL :\t{a_rtd:g}
ACHIVE :\t{format_persen(ach_rtd)}
*ONIGIRI*\t
TARGET :\t{t_oni:g}
ACTUAL :\t{a_oni:g}
ACHIVE :\t{format_persen(ach_oni)}
AVG/TOKO :\t{format_persen(avg_toko)}
--------------------------------\t
*ECOMMERCE*\t
*14.EVOUCHER*\t
TARGET :\t{format_rupiah(t_ev)}
ACTUAL :\t{format_rupiah(a_ev)}
ACHIVE :\t{format_persen(ach_ev)}
*15.FEE BASED*\t
TARGET :\t{format_rupiah(t_fb)}
ACTUAL :\t{format_rupiah(a_fb)}
ACHIVE :\t{format_persen(ach_fb)}

*TERIMA KASIH*"""

    col1, col2 = st.columns(2)
    with col1:
        show_btn = st.button("Tampilkan Laporan (Menu 1)")
    with col2:
        download_btn = st.button("Siapkan File TXT")

    if show_btn:
        # ✅ Tampilkan sebagai blok kode agar ada tombol Copy
        st.code(output_text, language="text")

        # (opsional) Tambah text_area juga, biar bisa edit/copy manual
        st.text_area("Salin/Copy (Menu 1)", value=output_text, height=400)

    if download_btn:
        st.download_button(
            label="Download sebagai TXT",
            data=output_text,
            file_name=f"performance_cabang_{tgl.strftime('%Y%m%d')}.txt",
            mime="text/plain",
        )


# =========================
# MENU 2 (kode kamu — tampilkan dengan st.code)
# =========================
elif menu.startswith("2"):
    st.subheader("Laporan Sales & Fokus Mkt (Menu 2)")

    shift = st.number_input("Shift (1/2/3):", min_value=1, max_value=3, step=1)
    tanggal = datetime.date.today()
    toko = st.text_input("Nama Toko:", value="KE53")

    target_data = {
        "sales": 8378500,
        "voucher": 378500,
        "psm": 82,
        "pwp": 10,
        "serba": 11,
        "seger": 33,
        "newmem": 2
    }

    st.subheader("Masukkan Data Aktual")
    aktual_data = {}
    for kategori in target_data:
        aktual_data[kategori] = st.number_input(f"{kategori.upper()}:", min_value=0, step=1)

    ceban_actual = st.number_input("CEBAN:", min_value=0, step=1)

    st.subheader("Masukkan Kontribusi")
    kontribusi = {
        "konstribusi member": st.number_input("Konstribusi member report 47:", min_value=0, step=1),
        "vcr jsm": st.number_input("Vcr JsM:", min_value=0, step=1),
        "vcr susu hebat": st.number_input("Vcr susu hebat:", min_value=0, step=1),
        "murah sejagat": st.number_input("Murah sejagat:", min_value=0, step=1),
        "indonesia juara": st.number_input("Indonesia juara:", min_value=0, step=1),
        "item jsm": st.number_input("Item JSM:", min_value=0, step=1)
    }

    if st.button("Tampilkan Laporan (Menu 2)"):
        laporan = f"""
LAPORAN  sales & FOKUS \tMkt

SHIFT  : {shift}
TGL    : {tanggal}
Toko   : {toko}
                                
          TARGET /ACT/ACH%

Sales: {format_ribuan(target_data['sales'])} / {format_ribuan(aktual_data['sales'])} / {hitung_persen(target_data['sales'], aktual_data['sales']):.2f}%
Voucher: {format_ribuan(target_data['voucher'])} / {format_ribuan(aktual_data['voucher'])} / {hitung_persen(target_data['voucher'], aktual_data['voucher']):.2f}%

PSM: {format_ribuan(target_data['psm'])} / {format_ribuan(aktual_data['psm'])} / {hitung_persen(target_data['psm'], aktual_data['psm']):.2f}%
PWP: {format_ribuan(target_data['pwp'])} / {format_ribuan(aktual_data['pwp'])} / {hitung_persen(target_data['pwp'], aktual_data['pwp']):.2f}%
SERBA: {format_ribuan(target_data['serba'])} / {format_ribuan(aktual_data['serba'])} / {hitung_persen(target_data['serba'], aktual_data['serba']):.2f}%

SEGER: {format_ribuan(target_data['seger'])} / {format_ribuan(aktual_data['seger'])} / {hitung_persen(target_data['seger'], aktual_data['seger']):.2f}%
CEBAN: {format_ribuan(ceban_actual)}

New Member: {format_ribuan(target_data['newmem'])} / {format_ribuan(aktual_data['newmem'])} / {hitung_persen(target_data['newmem'], aktual_data['newmem']):.2f}%
Kontribusi member report 47: {kontribusi['konstribusi member']}%
Vcr JsM : {kontribusi['vcr jsm']}
Vcr susu hebat: {kontribusi['vcr susu hebat']}
Murah sejagat : {kontribusi['murah sejagat']}
Indonesia juara: {kontribusi['indonesia juara']}
Item JSM : {kontribusi['item jsm']}

Terimakasih
"""
        # ✅ Tampilkan sebagai blok kode agar ada tombol Copy
        st.code(laporan, language="text")

        # (opsional) Tambah text_area juga
        st.text_area("Salin/Copy (Menu 2)", value=laporan, height=350)

# =========================
# MENU 3 (hitung persentase cepat)
# =========================
else:
    st.subheader("Menghitung Persentase Cepat")
    targettoko = st.number_input("NILAI TARGET", min_value=0.0, step=0.01)
    actualtoko = st.number_input("NILAI ACTUAL", min_value=0.0, step=0.01)
    persen = hitung_persen(targettoko, actualtoko)

    st.write(f"ACHIVE = {format_persen(persen)}")

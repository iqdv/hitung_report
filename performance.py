
import streamlit as st
import datetime

# ========== UTILITAS ==========
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
    return f"{int(nilai):,}".replace(",", ".")

def format_tanggal_id(d: datetime.date):
    bulan_id = [
        "Januari","Februari","Maret","April","Mei","Juni",
        "Juli","Agustus","September","Oktober","November","Desember"
    ]
    return f"{d.day:02d} {bulan_id[d.month-1]} {d.year}"

st.set_page_config(page_title="Performance & Fokus Cabang", layout="centered")
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu:", [
    "1. Laporan FOKUS ALL SHIFT PER HARI",
    "2. Laporan Sales & Fokus Mkt",
    "3. Menghitung Persentase"
])
st.title("FORM PERFORMANCE & FOCUS CABANG CIKOKOL")

# ========== MENU 1 ==========
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

    # Bangun teks output
    output_text = (
        "*PERFORMANCE & FOCUS CABANG CIKOKOL*\t\n"
        f"TGL : \t{format_tanggal_id(tgl)}\n\n"
        f"KODE : {kode}\n"
        f"TOKO : {toko}\n\n"
        "*REVENUE*\t\n"
        "*1.NET SALES*\t\n"
        f"TARGET :\t{format_rupiah(target_sales)}\n"
        f"ACTUAL :\t{format_rupiah(actual_sales)}\n"
        f"ACHIVE :\t{format_persen(sales_achive)}\n"
        f"GAP TO TARGET :\t{format_rupiah(sales_gap)}\n\n"
        "*2.PSM*\t\n"
        f"*{week_psm}*\t\n"
        f"TARGET :\t{t_psm:g}\n"
        f"ACTUAL :\t{a_psm:g}\n"
        f"ACHIVE :\t{format_persen(ach_psm)}\n\n"
        "*3.PWP*\t\n"
        f"*{periode_pwp}*\t\n"
        f"TARGET :\t{t_pwp:g}\n"
        f"ACTUAL :\t{a_pwp:g}\n"
        f"ACHIVE :\t{format_persen(ach_pwp)}\n\n"
        "*4.SERTIS*\t\n"
        f"*{periode_sertis}*\t\n"
        f"TARGET :\t{t_sertis:g}\n"
        f"ACTUAL :\t{a_sertis:g}\n"
        f"ACHIVE :\t{format_persen(ach_sertis)}\n"
        "--------------------------------\t\n"
        "*INVENTORY*\t\n"
        "*5.PL*\t\n"
        f"BUDGET ( 0,14% ) Rp :\t{format_rupiah(b_pl)}\n"
        f"ACTUAL Rp :\t{format_rupiah(a_pl)}\n"
        "*6.BR,BKE*\t\n"
        f"BUDGET (0,30) Rp :\t{format_rupiah(b_br)}\n"
        f"ACTUAL Rp :\t{format_rupiah(a_br)}\n"
        "--------------------------------\t\n"
        "*FOCUS CABANG*\t\n"
        "*7.TELUR*\t\n"
        f"TARGET :\t{t_telur:g}\n"
        f"ACTUAL :\t{a_telur:g}\n"
        f"ACHIVE :\t{format_persen(ach_telur)}\n"
        "*8.TOYS* :\t\n"
        f"TARGET :\t{t_toys:g}\n"
        f"ACTUAL :\t{a_toys:g}\n"
        f"ACHIVE :\t{format_persen(ach_toys)}\n"
        "*HOTWHEELS BASIC*\t\n"
        f"TARGET :\t{t_hw:g}\n"
        f"ACTUAL :\t{a_hw:g}\n"
        f"ACHIVE :\t{format_persen(ach_hw)}\n"
        "*9.DJOY* :\t\n"
        f"TARGET :\t{t_djoy:g}\n"
        f"ACTUAL :\t{a_djoy:g}\n"
        f"ACHIVE :\t{format_persen(ach_djoy)}\n"
        "*10.UNIPIN*\t\n"
        f"TARGET :\t{t_unipin:g}\n"
        f"ACTUAL :\t{a_unipin:g}\n"
        f"ACHIVE :\t{format_persen(ach_unipin)}\n"
        "*11.SUEEGERR*\t\n"
        f"TARGET :\t{t_sueegerr:g}\n"
        f"ACTUAL :\t{a_sueegerr:g}\n"
        f"ACHIVE :\t{format_persen(ach_sueegerr)}\n"
        "*12.FOKUS JSM*\t\n"
        f"TARGET :\t{t_fjsm:g}\n"
        f"ACTUAL :\t{a_fjsm:g}\n"
        f"ACHIVE :\t{format_persen(ach_fjsm)}\n"
        "*13.BEANSPOT*\t\n"
        "*RTD*\t\n"
        f"TARGET :\t{t_rtd:g}\n"
        f"ACTUAL :\t{a_rtd:g}\n"
        f"ACHIVE :\t{format_persen(ach_rtd)}\n"
        "*ONIGIRI*\t\n"
        f"TARGET :\t{t_oni:g}\n"
        f"ACTUAL :\t{a_oni:g}\n"
        f"ACHIVE :\t{format_persen(ach_oni)}\n"
        f"AVG/TOKO :\t{format_persen(avg_toko)}\n"
        "--------------------------------\t\n"
        "*ECOMMERCE*\t\n"
        "*14.EVOUCHER*\t\n"
        f"TARGET :\t{format_rupiah(t_ev)}\n"
        f"ACTUAL :\t{format_rupiah(a_ev)}\n"
        f"ACHIVE :\t{format_persen(ach_ev)}\n"
        "*15.FEE BASED*\t\n"
        f"TARGET :\t{format_rupiah(t_fb)}\n"
        f"ACTUAL :\t{format_rupiah(a_fb)}\n"
        f"ACHIVE :\t{format_persen(ach_fb)}\n\n"
        "*TERIMA KASIH*"
    )

    col1, col2 = st.columns(2)
    with col1:
        show_btn = st.button("Tampilkan Laporan (Menu 1)")
    with col2:
        download_btn = st.button("Siapkan File TXT")

    if show_btn:
        # Tampilkan biasa tanpa menu salin
        st.text(output_text)

    if download_btn:
        st.download_button(
            label="Download sebagai TXT",
            data=output_text,
            file_name=f"performance_cabang_{tgl.strftime('%Y%m%d')}.txt",
            mime="text/plain",
        )

# ========== MENU 2 ==========
elif menu.startswith("2"):
    st.subheader("Laporan Sales & Fokus Mkt (Menu 2)")

    shift = st.number_input("Shift (1/2/3):", min_value=1, max_value=3, step=1)
    tanggal = datetime.date.today()
    toko = st.text_input("Nama Toko:", value="KE53")

    target_data = {
        "sales": 8378500, "voucher": 378500, "psm": 82,
        "pwp": 10, "serba": 11, "seger": 33, "newmem": 2
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
        laporan = (
            "LAPORAN  sales & FOKUS \tMkt\n\n"
            f"SHIFT  : {shift}\n"
            f"TGL    : {tanggal}\n"
            f"Toko   : {toko}\n\n"
            "          TARGET /ACT/ACH%\n\n"
            f"Sales: {format_ribuan(target_data['sales'])} / {format_ribuan(aktual_data['sales'])} / {hitung_persen(target_data['sales'], aktual_data['sales']):.2f}%\n"
            f"Voucher: {format_ribuan(target_data['voucher'])} / {format_ribuan(aktual_data['voucher'])} / {hitung_persen(target_data['voucher'], aktual_data['voucher']):.2f}%\n\n"
            f"PSM: {format_ribuan(target_data['psm'])} / {format_ribuan(aktual_data['psm'])} / {hitung_persen(target_data['psm'], aktual_data['psm']):.2f}%\n"
            f"PWP: {format_ribuan(target_data['pwp'])} / {format_ribuan(aktual_data['pwp'])} / {hitung_persen(target_data['pwp'], aktual_data['pwp']):.2f}%\n"
            f"SERBA: {format_ribuan(target_data['serba'])} / {format_ribuan(aktual_data['serba'])} / {hitung_persen(target_data['serba'], aktual_data['serba']):.2f}%\n\n"
            f"SEGER: {format_ribuan(target_data['seger'])} / {format_ribuan(aktual_data['seger'])} / {hitung_persen(target_data['seger'], aktual_data['seger']):.2f}%\n"
            f"CEBAN: {format_ribuan(ceban_actual)}\n\n"
            f"New Member: {format_ribuan(target_data['newmem'])} / {format_ribuan(aktual_data['newmem'])} / {hitung_persen(target_data['newmem'], aktual_data['newmem']):.2f}%\n"
            f"Kontribusi member report 47: {kontribusi['konstribusi member']}%\n"
            f"Vcr JsM : {kontribusi['vcr jsm']}\n"
            f"Vcr susu hebat: {kontribusi['vcr susu hebat']}\n"
            f"Murah sejagat : {kontribusi['murah sejagat']}\n"
            f"Indonesia juara: {kontribusi['indonesia juara']}\n"
            f"Item JSM : {kontribusi['item jsm']}\n\n"
            "Terimakasih\n"
        )
        st.text(laporan)

# ========== MENU 3 ==========
else:
    st.subheader("Menghitung Persentase Cepat")
    targettoko = st.number_input("NILAI TARGET", min_value=0.0, step=0.01)
    actualtoko = st.number_input("NILAI ACTUAL", min_value=0.0, step=0.01)
    persen = hitung_persen(targettoko, actualtoko)
    st.write(f"ACHIVE = {format_persen(persen)}")

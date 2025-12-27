
# ... (semua import, fungsi, dan input sebelumnya tetap)

if st.button("Tampilkan Laporan"):
    # Susun dataframe Target vs Aktual vs Ach%
    rows = []
    for k in kategori_list:
        target_val = float(target_data[k])
        aktual_val = float(aktual_data[k])
        ach = hitung_persentase(aktual_val, target_val)
        rows.append({
            "Kategori": k.upper(),
            "Target": target_val,
            "Aktual": aktual_val,
            "Ach (%)": round(ach, 2)
        })
    df = pd.DataFrame(rows)

    st.markdown(f"""
    **LAPORAN Sales & Fokus Mkt**  
    **SHIFT**: {shift} &nbsp;&nbsp; | &nbsp;&nbsp; **TGL**: {tanggal} &nbsp;&nbsp; | &nbsp;&nbsp; **Toko**: {toko}
    """)

    # ===== Styling: warna hijau untuk Ach% >= 100 =====
    def style_ach(val):
        """Kembalikan style CSS berbeda untuk nilai Ach%."""
        try:
            v = float(val)
        except:
            return ""
        if v >= 100:
            # Hijau
            return "background-color:#d9fdd3; color:#0f5132; font-weight:600;"
        elif v >= 80:
            # Kuning/amber
            return "background-color:#fff3cd; color:#664d03; font-weight:600;"
        else:
            # Merah
            return "background-color:#f8d7da; color:#842029; font-weight:600;"

    styled = (
        df.style
        .format({
            "Target": lambda x: format_ribuan(x),
            "Aktual": lambda x: format_ribuan(x),
            "Ach (%)": "{:.2f}"
        })
        .applymap(style_ach, subset=["Ach (%)"])
    )

    st.subheader("Ringkasan Target vs Aktual (warna Ach%)")
    st.dataframe(styled, use_container_width=True)

    # ===== Detail tambahan tetap =====
    st.subheader("Detail Tambahan")
    col_d1, col_d2 = st.columns([1,1])
    with col_d1:
        st.markdown(f"**CEBAN:** {format_ribuan(ceban_actual)}")
    with col_d2:
        st.markdown(f"""
        **Kontribusi:**
        - Kontribusi member report 47: **{kontribusi_member:.2f}%**
        - Vcr JSM: **{format_ribuan(vcr_jsm)}**
        - Vcr susu hebat: **{format_ribuan(vcr_susu_hebat)}**
        - Murah sejagat : **{format_ribuan(murah_sejagat)}**
        - Indonesia juara: **{format_ribuan(indonesia_juara)}**
        - Item JSM : **{format_ribuan(item_jsm)}**
        """)

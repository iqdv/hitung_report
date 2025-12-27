
# Di bagian input Aktual (kanan), setelah setiap number_input:
for k in kategori_list:
    aktual_data[k] = st.number_input(
        f"Aktual {k.upper()}:", min_value=0.0, step=1.0, value=0.0, key=f"akt_{k}"
    )
    # Hitung ach saat ini
    ach_now = hitung_persentase(aktual_data[k], target_data[k])
    if ach_now >= 100:
        st.markdown(f"<span style='background:#d9fdd3;color:#0f5132;padding:4px 8px;border-radius:6px;font-size:0.9rem;'>Ach {ach_now:.2f}% ✅</span>", unsafe_allow_html=True)
    elif ach_now >= 80:
        st.markdown(f"<span style='background:#fff3cd;color:#664d03;padding:4px 8px;border-radius:6px;font-size:0.9rem;'>Ach {ach_now:.2f}% ⚠️</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='background:#f8d7da;color:#842029;padding:4px 8px;border-radius:6px;font-size:0.9rem;'>Ach {ach_now:.2f}% ❌</span>", unsafe_allow_html=True)

import streamlit as st
import math

# --- DATA MASTER DARI CSV ---
data_material = {
    "Stiker printing (100x100)": 11.98, 
    "Oracal 651 Glossy (100x126)": 6.75,
    "Oracal 651 Doff (100x126)": 11.90,
    "Oracal 651 Gold/Silver": 13.49,
    "3M Reflective (60x50)": 28.33
}

# Biaya Operasional Tetap (per cm) sesuai CSV
BIAYA_OPERASIONAL = 5 + 11.90 + 20 + 5 # Cutting + Listrik + Ads + Packaging

st.set_page_config(page_title="Kalkulator Stiker Pro V4", layout="centered")

st.title("✂️ Kalkulator Stiker V4")
st.write("Profit: Easy(2x), Medium(3x), Hard(4x) | +80% per tambahan warna")

# --- INPUT USER ---
material = st.selectbox("Pilih Material", list(data_material.keys()))

col1, col2 = st.columns(2)
with col1:
    p = st.number_input("Panjang (cm)", min_value=0.1, value=7.0, step=0.1)
with col2:
    l = st.number_input("Lebar (cm)", min_value=0.1, value=7.0, step=0.1)

kesulitan = st.select_slider("Pilih Tingkat Kesulitan", options=["Easy", "Medium", "Hard"])
warna = st.number_input("Jumlah Warna", min_value=1, value=1)

# --- LOGIKA OTOMATIS PROFIT ---
if kesulitan == "Easy":
    profit_setting = 2.0
elif kesulitan == "Medium":
    profit_setting = 3.0
else:  # Hard
    profit_setting = 4.0

# --- HITUNGAN ---
hpp_material_awal = data_material[material]
total_hpp_per_cm = hpp_material_awal + BIAYA_OPERASIONAL
luas = p * l

# Modal dasar untuk 1 warna
modal_dasar = total_hpp_per_cm * luas

# LOGIKA TAMBAHAN WARNA (+80% setiap nambah warna)
# Jika warna = 1, pengali = 1
# Jika warna = 2, pengali = 1 + 0.8 = 1.8
# Jika warna = 3, pengali = 1 + 0.8 + 0.8 = 2.6
pengali_warna = 1 + ((warna - 1) * 0.8)
total_modal = modal_dasar * pengali_warna

# Harga Jual
harga_jual = total_modal * profit_setting

# Pembulatan ke 1000 terdekat ke atas
harga_final = math.ceil(harga_jual / 1000) * 1000

# --- TAMPILAN HASIL ---
st.divider()
st.subheader("Hasil Perhitungan Akhir:")
c1, c2 = st.columns(2)
c1.metric("Profit applied", f"{profit_setting}x")
c2.metric("Harga Jual", f"Rp {harga_final:,}")

with st.expander("Detail Analisis Harga"):
    st.write(f"**Luas Stiker:** {luas} cm²")
    st.write(f"**Modal 1 Warna:** Rp {modal_dasar:,.2f}")
    st.write(

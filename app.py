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

# Biaya Operasional Tetap (per cm)
BIAYA_OPERASIONAL = 5 + 11.90 + 20 + 5  # Cutting + Listrik + Ads + Packaging

st.set_page_config(page_title="Kalkulator Stiker Pro", layout="centered")

st.title("✂️ Kalkulator Stiker V3")
st.write("Profit: Easy(2x), Medium(3x), Hard(4x)")

# --- INPUT USER ---
material = st.selectbox("Pilih Material", list(data_material.keys()))

col1, col2 = st.columns(2)
with col1:
    p = st.number_input("Panjang (cm)", min_value=0.1, value=7.0, step=0.1)
with col2:
    l = st.number_input("Lebar (cm)", min_value=0.1, value=7.0, step=0.1)

kesulitan = st.select_slider("Pilih Tingkat Kesulitan", options=["Easy", "Medium", "Hard"])
warna = st.number_input("Jumlah Warna", min_value=1, value=1)

# --- LOGIKA OTOMATIS (UPDATE PROFIT BARU) ---
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

# Modal per stiker
total_modal = (total_hpp_per_cm * luas) + ((warna - 1) * 500)

# Harga Jual
harga_jual = total_modal * profit_setting

# Pembulatan ke 1000 terdekat ke atas (Cth: 14.200 jadi 15.000)
harga_final = math.ceil(harga_jual / 1000) * 1000

# --- TAMPILAN HASIL ---
st.divider()
st.subheader("Hasil Perhitungan:")
c1, c2 = st.columns(2)
c1.metric("Profit applied", f"{profit_setting}x")
c2.metric("Harga Jual", f"Rp {harga_final:,}")

with st.expander("Detail Modal & Margin"):
    st.write(f"**Luas Stiker:** {luas} cm²")
    st.write(f"**Total Modal (HPP):** Rp {total_modal:,.2f}")
    st.write(f"**Laba Bersih:** Rp {harga_final - total_modal:,.2f}")
    st.caption("Note: Harga sudah termasuk pembulatan ke ribuan terdekat.")

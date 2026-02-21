import streamlit as st
import math

# Data dari spreadsheet lo
data_material = {
    "Stiker printing (100x100)": 53.89,
    "Oracal 651 Glossy (100x126)": 25.95,
    "Oracal 651 Doff (100x126)": 50.65,
    "Oracal 651 Gold/Silver": 57.40,
    "3M Reflective (60x50)": 72.24
}

st.set_page_config(page_title="Kalkulator Stiker", layout="centered")

st.title("✂️ Kalkulator Stiker")
st.write("Hitung cepat harga jual dari HP")

# Input User
material = st.selectbox("Pilih Material", list(data_material.keys()))
col1, col2 = st.columns(2)
with col1:
    p = st.number_input("Panjang (cm)", min_value=0.1, value=7.0)
with col2:
    l = st.number_input("Lebar (cm)", min_value=0.1, value=7.0)

kesulitan = st.select_slider("Kesulitan", options=["Easy", "Medium", "Hard"])
warna = st.number_input("Jumlah Warna", min_value=1, value=1)
profit = st.slider("Profit Margin", 1.0, 3.0, 1.5)

# Logika Hitung
hpp_material = data_material[material]
multi_susah = {"Easy": 1.0, "Medium": 1.25, "Hard": 1.5}[kesulitan]

total_hpp = (p * l * hpp_material * multi_susah) + (warna * 500)
harga_jual = total_hpp * profit
harga_bulat = math.ceil(harga_jual / 1000) * 1000

# Hasil
st.divider()
st.subheader("Estimasi Harga Jual:")
st.header(f"Rp {harga_bulat:,}")
st.caption(f"HPP Asli: Rp {total_hpp:,.0f} | Tanpa Bulat: Rp {harga_jual:,.0f}")
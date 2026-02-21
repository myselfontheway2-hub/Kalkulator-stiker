import streamlit as st
import math

# --- DATA MASTER DARI CSV ---
data_material = {
    "Stiker printing (100x100)": 11.98, # Harga per CM dasar
    "Oracal 651 Glossy (100x126)": 6.75,
    "Oracal 651 Doff (100x126)": 11.90,
    "Oracal 651 Gold/Silver": 13.49,
    "3M Reflective (60x50)": 28.33
}

# Biaya Operasional Flat (per cm) sesuai spreadsheet lo
BIAYA_OPERASIONAL = 5 + 11.90 + 20 + 5  # Cutting + Listrik + Ads + Packaging

st.set_page_config(page_title="Kalkulator Stiker Otomatis", layout="centered")

st.title("✂️ Kalkulator Stiker V2")
st.write("Profit otomatis berdasarkan tingkat kesulitan.")

# --- INPUT USER ---
material = st.selectbox("Pilih Material", list(data_material.keys()))

col1, col2 = st.columns(2)
with col1:
    p = st.number_input("Panjang (cm)", min_value=0.1, value=7.0, step=0.1)
with col2:
    l = st.number_input("Lebar (cm)", min_value=0.1, value=7.0, step=0.1)

kesulitan = st.select_slider("Pilih Tingkat Kesulitan", options=["Easy", "Medium", "Hard"])
warna = st.number_input("Jumlah Warna", min_value=1, value=1)

# --- LOGIKA OTOMATIS (REQUEST LO) ---
# Menentukan profit berdasarkan kesulitan
if kesulitan == "Easy":
    profit_setting = 1.00
elif kesulitan == "Medium":
    profit_setting = 1.50
else:  # Hard
    profit_setting = 2.00

# --- HITUNGAN ---
hpp_material_awal = data_material[material]
total_hpp_per_cm = hpp_material_awal + BIAYA_OPERASIONAL
luas = p * l

# Total Modal Dasar
modal_dasar = total_hpp_per_cm * luas

# Tambahan biaya jika lebih dari 1 warna (Contoh: tambah Rp 500 per warna tambahan)
biaya_warna = (warna - 1) * 500 

total_modal = modal_dasar + biaya_warna
harga_jual = total_modal * profit_setting

# Pembulatan ke 1000 terdekat ke atas
harga_final = math.ceil(harga_jual / 1000) * 1000

# --- TAMPILAN HASIL ---
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    st.metric("Profit Otomatis", f"{profit_setting}x")
with col_b:
    st.metric("Estimasi Harga", f"Rp {harga_final:,}")

with st.expander("Lihat Rincian Biaya"):
    st.write(f"HPP Material per cm: Rp {hpp_material_awal}")
    st.write(f"Total HPP + Operasional: Rp {total_hpp_per_cm:.2f}")
    st.write(f"Total Modal (HPP x Luas): Rp {total_modal:,.2f}")
    st.info(f"Karena kesulitan **{kesulitan}**, profit diset ke **{profit_setting}x**")

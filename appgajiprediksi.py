import streamlit as st
import joblib
import numpy as np

#memuat model regresi linear yang sudah disimpan
lin_reg_loaded = joblib.load('lin_reg_model.joblib')

#Judul Aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

#Input tahun pengalaman bekerja
years_experience = st.number_input("Masukkan jumlah tahun bekerja", min_value=0.0, step=0.1)

#Prediksi gaji
if st.button("Prediksi Gaji"):
	gaji = lin_reg_loaded.predict([[years_experience]])
	st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah Rp{gaji[0]:,.2f}")

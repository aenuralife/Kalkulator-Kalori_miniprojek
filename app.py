import streamlit as st
from main import hitung_bmi, kategori_bmi, hitung_kalori_harian

st.set_page_config(page_title="Kalkulator BMI & Kalori", page_icon="⚖️")

st.title("⚖️ Kalkulator BMI & Kebutuhan Kalori")
st.write("Aplikasi sederhana untuk menghitung Indeks Massa Tubuh (BMI) dan Kebutuhan Kalori Harian.")

st.sidebar.header("Input Data Diri")
gender = st.sidebar.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
usia = st.sidebar.number_input("Usia (Tahun)", min_value=1, max_value=120, value=25)
berat = st.sidebar.number_input("Berat Badan (kg)", min_value=1.0, max_value=300.0, value=70.0)
tinggi = st.sidebar.number_input("Tinggi Badan (cm)", min_value=1.0, max_value=250.0, value=170.0)

if st.sidebar.button("Hitung Hasil"):
    try:
        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)
        kalori = hitung_kalori_harian(gender, berat, tinggi, usia)

        col1, col2, col3 = st.columns(3)
        col1.metric("Skor BMI", f"{bmi}")
        col2.metric("Kategori Status Gizi", kategori)
        col3.metric("Kebutuhan Kalori", f"{kalori} kcal")

        st.success("Perhitungan berhasil dijalankan menggunakan fungsi logika utama!")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
import pandas as pd
import streamlit as st

st.title("Aplikasi Sederhana Data Mahasiswa")

data_mahasiswa = {
    'Nama': ['Budi', 'Siti', 'Joko', 'Ani', 'Rina'],
    'NIM' : ['202542001','202542002','202543001','202544001','202544001'],
    'Usia': [21, 22, 20, 23, 21],
    'Jurusan': ['Informatika', 'Informatika', 'Sistem Informasi', 'Desain', 'Matematika'],
    'Nilai': [85, 92, 78, 88, 95]
}
df_mahasiswa = pd.DataFrame(data_mahasiswa)

st.subheader("Tabel Data Mahasiswa:")
st.dataframe(df_mahasiswa)

rata_rata_usia = df_mahasiswa['Usia'].mean()
st.write(f"Rata-rata usia mahasiswa adalah: **{rata_rata_usia:.2f} tahun**")

df_informatika = df_mahasiswa[df_mahasiswa['Jurusan'] == 'Informatika']
st.subheader("\nMahasiswa Jurusan Informatika:")
st.dataframe(df_informatika)

st.markdown("---")
st.subheader("Statistik Berdampingan")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Mahasiswa", len(df_mahasiswa))

with col2:
    st.metric("Total Jurusan Unik", len(df_mahasiswa['Jurusan'].unique()))

st.markdown("---")

st.subheader("Filter Data Berdasarkan Jurusan")

jurusan_pilihan = st.selectbox(
    "Pilih Jurusan yang Ingin Ditampilkan:",
    df_mahasiswa['Jurusan'].unique()
)
df_terfilter = df_mahasiswa[df_mahasiswa['Jurusan'] == jurusan_pilihan]
st.write(f"Menampilkan mahasiswa jurusan: **{jurusan_pilihan}**")
st.dataframe(df_terfilter)

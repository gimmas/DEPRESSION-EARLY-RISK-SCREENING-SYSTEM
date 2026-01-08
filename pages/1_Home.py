import streamlit as st

st.markdown("""
<style>
.card {
    background-color: #1c1f26;
    padding: 30px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>✨ Depression Detector</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<p style="font-size:16px;">
Aplikasi ini mendeteksi indikasi awal depresi berdasarkan teks berbahasa Inggris
menggunakan model Machine Learning.
</p>

<p>
⚠️ <b>Bukan alat diagnosis medis.</b><br>
Digunakan untuk edukasi dan mitigasi awal.
</p>
</div>
""", unsafe_allow_html=True)

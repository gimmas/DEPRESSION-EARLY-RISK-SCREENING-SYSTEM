import streamlit as st

st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️",
    layout="centered"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>ℹ️ Tentang Aplikasi</h2>

<p>
Aplikasi ini merupakan sistem <b>deteksi dini gejala depresi</b> berbasis
<b>Natural Language Processing (NLP)</b> dan <b>Machine Learning</b>.
</p>

<p>
Model dilatih menggunakan data teks berbahasa Inggris yang didapat dari kaggle
dan dirancang untuk mendeteksi pola bahasa yang sering muncul pada individu
dengan gejala depresi.
</p>

<h4>⚙️ Cara Kerja</h4>
<ul>
  <li>Pengguna memasukkan teks dalam bahasa Inggris</li>
  <li>Teks diproses dan dianalisis oleh model machine learning</li>
  <li>Sistem memberikan hasil skrining awal</li>
</ul>

<h4>⚠️ Catatan Penting</h4>
<p>
Aplikasi ini <b>bukan alat diagnosis medis</b>.
Hasil yang ditampilkan hanya bersifat skrining awal dan tidak menggantikan
konsultasi dengan tenaga kesehatan profesional.
</p>

<h4>🎓 Tujuan Pengembangan</h4>
<p>
Aplikasi ini dikembangkan untuk keperluan pembelajaran dan responsi
di bidang <b>Machine Learning dan NLP</b>, dengan fokus pada isu kesehatan mental.
</p>
</div>
""", unsafe_allow_html=True)

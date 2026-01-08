import streamlit as st

from src.inference import load_model, predict, predict_confidence
from src.preprocessing import light_clean, validate_text
from src.postprocess import mitigate_false_positive

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Deteksi Depresi",
    page_icon="🧠",
    layout="centered"
)

# ===============================
# LOAD CSS
# ===============================
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ===============================
# LOAD MODEL (CACHE)
# ===============================
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# ===============================
# HEADER
# ===============================
st.markdown("""
<div class="card">
  <h1>✨ Deteksi Dini Gejala Depresi</h1>
  <p class="subtitle">
    Skrining awal berbasis machine learning.<br>
    <b>Bukan diagnosis medis.</b>
  </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# INPUT
# ===============================
st.markdown("""
<div class="card">
  <h4>Tuliskan perasaan atau pikiran Anda</h4>
</div>
""", unsafe_allow_html=True)

text = st.text_area(
    label="",
    placeholder="Saya merasa lelah dan kosong akhir-akhir ini...",
    height=150
)

analyze = st.button("Analisis Teks")

# ===============================
# INFERENCE + POST-PROCESSING
# ===============================
if analyze:
    cleaned = light_clean(text)
    valid, msg = validate_text(cleaned)

    if not valid:
        st.warning(msg)
        st.stop()

    with st.spinner("Menganalisis pola emosional..."):
        raw_label = predict(model, cleaned)
        confidence = predict_confidence(model, cleaned)

    # POST-PROCESSING
    label, reason = mitigate_false_positive(
        cleaned,
        raw_label,
        confidence
    )

    # ===============================
    # OUTPUT
    # ===============================
    if label == 1:
        st.error("⚠️ Terdeteksi kemungkinan gejala depresi")

        if confidence is not None:
            st.progress(float(confidence))
            st.caption(f"Tingkat keyakinan: **{confidence * 100:.1f}%**")

        st.info(
            "Jika perasaan ini berlangsung lama atau mengganggu aktivitas sehari-hari, "
            "pertimbangkan untuk berbicara dengan tenaga profesional atau orang terpercaya."
        )

    elif reason == "mixed":
        st.warning("⚖️ Sinyal emosional campuran terdeteksi")
        st.caption(
            "Teks menunjukkan adanya tekanan emosional, namun juga terdapat "
            "tanda-tanda penerimaan diri atau usaha untuk pulih."
        )

    else:
        st.success("✅ Tidak terdeteksi gejala depresi")

        if confidence is not None:
            st.progress(float(1 - confidence))
            st.caption(f"Tingkat keyakinan: **{(1 - confidence) * 100:.1f}%**")

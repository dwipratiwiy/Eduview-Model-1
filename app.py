import streamlit as st
from PIL import Image
import torch
import os
import tempfile
from ultralytics import YOLO

# Fungsi untuk memuat model YOLO (gunakan cache agar tidak loading terus)
@st.cache_resource
def load_model():
    model_path = "/Users/tokyo/Downloads/runs/detect/yolov11/weights/best.pt"
    if not os.path.exists(model_path):
        st.error("Model tidak ditemukan di path yang ditentukan.")
        st.stop()
    return YOLO(model_path)

model = load_model()

# Judul aplikasi
st.title("🔍 Real-Time Object Detection for Student Cheating in a Classroom Using YOLO")

# Upload gambar
uploaded_file = st.file_uploader("📤 Upload Gambar", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Baca gambar dari upload dan tampilkan
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🖼️ Gambar yang Diupload", use_column_width=True)

    # Tombol untuk memulai deteksi
    if st.button("🔎 Mulai Deteksi"):
        with st.spinner("🔄 Sedang memproses deteksi..."):
            try:
                # Simpan gambar sementara untuk diproses oleh YOLO
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    image.save(temp_file.name)
                    results = model(temp_file.name)

                # Ambil dan tampilkan gambar hasil deteksi
                result_img = results[0].plot()
                st.image(result_img, caption="✅ Hasil Deteksi", use_column_width=True)

                # Tampilkan detail deteksi (label dan confidence)
                st.subheader("📋 Detail Deteksi")
                for box in results[0].boxes:
                    cls_id = int(box.cls[0])
                    cls_name = model.names.get(cls_id, "Unknown")
                    conf = float(box.conf[0])
                    st.markdown(f"- **Label:** {cls_name} | **Confidence:** {conf:.2f}")
            except Exception as e:
                st.error(f"Terjadi kesalahan saat mendeteksi objek: {e}")

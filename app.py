import streamlit as st
from PIL import Image

st.set_page_config(page_title="Multi-Crop Disease Detection", layout="centered")
st.title("🌱 Multi-Crop Disease Detection")
st.write("Upload a leaf image and select the crop to see predictions.")

# -------------------
# Predefined outputs for all crops
# -------------------
demo_data = {
    "Tomato": {
        "status": "Diseased",
        "color": "red",
        "top_predictions": [
            ("Tomato leaf late blight", 60.0),
            ("Tomato Septoria leaf spot", 30.0),
            ("Tomato healthy leaf", 10.0)
        ],
        "solutions": {
            "organic": "Destroy infected leaves, neem spray.",
            "inorganic": "Mancozeb/Metalaxyl."
        }
    },
    "Potato": {
        "status": "Diseased",
        "color": "red",
        "top_predictions": [
            ("Potato leaf late blight", 60.0),
            ("Potato leaf early blight", 30.0),
            ("Potato healthy leaf", 10.0)
        ],
        "solutions": {
            "organic": "Destroy infected leaves, copper sprays.",
            "inorganic": "Metalaxyl fungicide."
        }
    },
    "Bell Pepper": {
        "status": "Diseased",
        "color": "red",
        "top_predictions": [
            ("Bell_pepper leaf spot", 70.0),
            ("Bell_pepper leaf", 20.0),
            ("Bell_pepper healthy leaf", 10.0)
        ],
        "solutions": {
            "organic": "Remove infected leaves, neem oil.",
            "inorganic": "Copper-based bactericides."
        }
    },
    "Cherry": {
        "status": "Healthy",
        "color": "green",
        "top_predictions": [
            ("Cherry leaf", 90.0),
            ("Cherry healthy leaf", 10.0)
        ],
        "solutions": {
            "organic": "No action needed.",
            "inorganic": "No action needed."
        }
    },
    "Corn": {
        "status": "Diseased",
        "color": "red",
        "top_predictions": [
            ("Corn Gray leaf spot", 50.0),
            ("Corn leaf blight", 30.0),
            ("Corn rust leaf", 20.0)
        ],
        "solutions": {
            "organic": "Rotate crops, neem spray.",
            "inorganic": "Azoxystrobin/Mancozeb fungicide."
        }
    }
}

# -------------------
# Crop selection
# -------------------
selected_crop = st.selectbox("Select Crop", list(demo_data.keys()))

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg","jpeg","png","jfif","bmp"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Leaf Image', use_column_width=True)

    # Get data for selected crop
    data = demo_data[selected_crop]

    # -------------------
    # Display results in columns
    # -------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Crop:")
        st.write(selected_crop)

        st.subheader("Status:")
        status_emoji = "✅" if data["status"] == "Healthy" else "⚠️"
        st.markdown(f"<span style='color:{data['color']}; font-weight:bold'>{status_emoji} {data['status']}</span>", unsafe_allow_html=True)

    with col2:
        st.subheader("Solutions:")
        st.write("**Organic:**", data["solutions"]["organic"])
        st.write("**Inorganic:**", data["solutions"]["inorganic"])

    st.markdown("---")

    st.subheader("Top Predictions:")
    for cls, prob in data["top_predictions"]:
        st.write(f"{cls}: {prob:.2f}%")
        st.progress(int(prob))
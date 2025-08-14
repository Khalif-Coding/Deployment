import streamlit as st
import os
from PIL import Image

def show():
    st.write("## Exploratory Data Analysis (EDA)")

    img1 = os.path.join("EDA", "eda1.png")
    st.image(img1, caption="Distribusi Tiap Kelas")
    st.markdown("""
    **Insights:**
    
    """)

    img2 = os.path.join("EDA", "eda2.png")
    st.image(img2, caption="Distribusi Size Images")
    st.markdown("""
    **Insights:**
   
    """)

    img3 = os.path.join("EDA", "eda3.png")
    st.image(img3, caption="Distribusi Color Modes Pada Images")
    st.markdown("""
    **Insights:**
    
    """)

    # img4 = os.path.join("Deployment", "EDA", "eda4_1.png")
    # st.image(img4)
    # img5 = os.path.join("Deployment", "EDA", "eda4_2.png")
    # st.image(img5)
    # img6 = os.path.join("Deployment", "EDA", "eda4_3.png")
    # st.image(img6)
    # img7 = os.path.join("Deployment", "EDA", "eda4_4.png")
    # st.image(img7, caption="Sample Tiap Kelas")
    st.markdown("""
    **Insights:**
    
    """)

if __name__ == "__main__":
    show()
import streamlit as st

st.title("Optometry Pathology Guide")

st.write("Search and learn about common eye conditions.")

pathology = st.selectbox(
    "Choose a pathology:",
    [
        "Keratoconus",
        "Cataract",
        "Anterior Uveitis",
        "AMD",
        "Diabetic Retinopathy"
    ]
)

if pathology == "Keratoconus":

    st.header("Keratoconus")

    st.subheader("Symptoms")
    st.write("- Blurred vision")
    st.write("- Distorted vision")
    st.write("- Frequent prescription changes")
    st.write("- Glare and halos")

    st.subheader("Clinical Signs")
    st.write("- Irregular astigmatism")
    st.write("- Corneal thinning")
    st.write("- Fleischer ring")
    st.write("- Vogt striae")
    st.write("- Munson sign")

elif pathology == "Cataract":

    st.header("Cataract")
    st.image(
        "images/Cataracts.jpg",
        caption=" Cataracts",
        width =500

    st.subheader("Symptoms")
    st.write("- Gradual reduction in vision")
    st.write("- Glare")
    st.write("- Reduced contrast")
    st.write("- Difficulty driving at night")

    st.subheader("Clinical Signs")
    st.write("- Lens opacity")
    st.write("- Reduced red reflex")
    st.write("- Reduced visual acuity")

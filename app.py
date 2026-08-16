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
   

    st.subheader("Symptoms")
    st.write("- Gradual reduction in vision")
    st.write("- Glare")
    st.write("- Reduced contrast")
    st.write("- Difficulty driving at night")
    st.subheader("Different types of cataracts")
    st.write(- "Nuclear cataracts; Forms in the centre of the lens; The nucleaus. Usually turn yellow or brown depending of the severity")

    st.subheader("Clinical Signs")
    st.write("- Lens opacity")
    st.write("- Reduced red reflex")
    st.write("- Reduced visual acuity")

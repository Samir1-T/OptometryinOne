import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F7FA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Optometry Pathology Guide")
st.write("Search and learn about common eye conditions.")

st.title("Optometry in One")

area = st.selectbox(
    "Select area",
    [
        "Anterior Eye",
        "Posterior Eye",
        "Neuro-Ophthalmology",
        "Visual field defects"
    ]
)

if area == "Anterior Eye":
    pathology = st.selectbox(
        "Select pathology",
        [
            "Dry eyes",
            "Cataracts",
            "Keratoconus",
            "Conjunctivtis",
            "Uveitis"
        ]
    )

elif area == "Posterior Eye":
    pathology = st.selectbox(
        "Select pathology",
        [
            "AMD",
            "Diabetic Retinopathy",
            "Retinal Detachment",
            "PVD"
        ]
    )

elif area == "Neuro-Ophthalmology":
    pathology = st.selectbox(
        "Select pathology",
        [
            "Optic Neuritis",
            "Papilloedema",
            "NAION"
        ]
    )
elif area == "Visual field defects":
    pathology = st.selectbox(
    "Select pathology",
    [
        "Homonymous heminopia"
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

elif pathology == "Cataracts":

    st.header("Cataracts")
    tab1, tab2, tab3,tab4 = st.tabs(
        ["Overview","Symptoms", "Signs", "Management"]
    )
    with tab1:
        st.subheader("Cataracts")
        st.write (" A common eye condition in which the lens turns cloudy")
        st.write ("#### Different types of cataracts")
        st.write (" - Nuclear")
        st.write (" - Cortical")
        st.write (" - Posterior subcapsular")
    
    with tab2:
        st.subheader("Symptoms")
        st.write("- Gradual reduction in vision")
        st.write("- Glare")
        st.write("- Reduced contrast")
        st.write("- Difficulty driving at night")
    with tab3:
        st.subheader ("Clinical signs")
        st.write("- Lens opacity")
        st.write("- Reduced red reflex")
        st.write("- Reduced visual acuity")
    with tab4:
        st.subheader("Management")
        st.write(" ##### Referral is only required; ")
        st.write (" 1. If vision is worse than 6/12 in the affected eye")
        st.write (" 2. Visual symptoms e.g Glare, loss of colour/contrast ,anisometropia")
        st.write (" 3. Affecting daily tasks/living independantly")

import pandas as pd
import streamlit as st

from iris_shared import FEATURES, get_iris_data, get_model


flowers, species_names = get_iris_data()

st.markdown("## Identify an Iris")
st.write("Adjust the measurements, then ask the trained model for a species.")

with st.form("iris_prediction"):
    first, second = st.columns(2)
    values = {}
    for index, feature in enumerate(FEATURES):
        column = first if index % 2 == 0 else second
        with column:
            values[feature] = st.slider(
                feature.replace(" (cm)", "").title() + " (cm)",
                min_value=float(flowers[feature].min()),
                max_value=float(flowers[feature].max()),
                value=float(flowers[feature].median()),
                step=0.1,
            )
    submitted = st.form_submit_button("Predict species", type="primary")

if submitted:
    model = get_model()
    sample = pd.DataFrame(
        [[values[feature] for feature in FEATURES]], columns=FEATURES
    )
    prediction = int(model.predict(sample)[0])
    st.success(f"Predicted species: **{species_names[prediction].title()}**")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(sample)[0]
        confidence = float(probabilities[prediction])
        st.caption(f"Model confidence: {confidence:.1%}")
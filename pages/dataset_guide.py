import pandas as pd
import streamlit as st

from iris_shared import FEATURES, get_iris_data


flowers, species_names = get_iris_data()

st.markdown("## A classic in flower classification")
st.write(
    "The Iris dataset records four measurements for 150 flowers across "
    "three species. It is a compact way to explore how measurements can "
    "separate closely related groups."
)

first, second, third = st.columns(3)
first.metric("Flowers", len(flowers))
second.metric("Measurements", len(FEATURES))
third.metric("Species", len(species_names))

st.markdown("### What is measured")
descriptions = {
    "sepal length (cm)": "Length of the outer flower part",
    "sepal width (cm)": "Width of the outer flower part",
    "petal length (cm)": "Length of the inner flower part",
    "petal width (cm)": "Width of the inner flower part",
}
st.dataframe(
    pd.DataFrame({"Measurement": FEATURES, "Description": descriptions.values()}),
    hide_index=True,
    width="stretch",
)

left, right = st.columns([1, 1.35])
with left:
    st.markdown("### Species in the sample")
    counts = (
        flowers["species"]
        .value_counts()
        .rename_axis("Species")
        .reset_index(name="Flowers")
    )
    st.dataframe(counts, hide_index=True, width="stretch")
with right:
    st.markdown("### First observations")
    st.dataframe(flowers.head(6), hide_index=True, width="stretch")
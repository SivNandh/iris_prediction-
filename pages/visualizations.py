import streamlit as st

from iris_shared import FEATURES, get_iris_data


flowers, _ = get_iris_data()

st.markdown("## Explore the measurements")
st.write("Choose two measurements to compare flowers by species.")

x_axis, y_axis = st.columns(2)
with x_axis:
    x_feature = st.selectbox("Horizontal axis", FEATURES, index=2)
with y_axis:
    y_feature = st.selectbox("Vertical axis", FEATURES, index=3)

st.scatter_chart(
    flowers,
    x=x_feature,
    y=y_feature,
    color="species",
    height=420,
    width="stretch",
)

left, right = st.columns(2)
with left:
    selected_feature = st.selectbox(
        "Compare average by species", FEATURES, index=2
    )
    averages = (
        flowers.groupby("species", sort=False)[selected_feature]
        .mean()
        .rename("Average (cm)")
        .reset_index()
    )
    st.bar_chart(
        averages,
        x="species",
        y="Average (cm)",
        color="species",
        width="stretch",
    )
with right:
    st.markdown("### Measurement correlations")
    st.dataframe(flowers[FEATURES].corr().round(2), width="stretch")
import streamlit as st


def main():
    st.set_page_config(page_title="Iris Field Guide", page_icon="🌸", layout="wide")
    st.markdown(
        """
        <style>
        .block-container {max-width: 1120px; padding-top: 2rem;}
        [data-testid="stAppViewContainer"] {background: #f7f8f2;}
        h1, h2, h3 {font-family: Georgia, serif; color: #243b32;}
        [data-testid="stMetric"] {background: #eaf0e6; padding: 1rem; border-radius: 6px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Iris Field Guide")
    st.caption("A small dataset, three ways to understand it")

    navigation = st.navigation(
        [
            st.Page("pages/dataset_guide.py", title="Dataset guide", default=True),
            st.Page("pages/visualizations.py", title="Visualizations"),
            st.Page("pages/prediction.py", title="Prediction"),
        ],
        position="top",
    )
    navigation.run()


if __name__ == "__main__":
    main()

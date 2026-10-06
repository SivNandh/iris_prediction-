from pathlib import Path
import pickle

import streamlit as st
from sklearn.datasets import load_iris


FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]


@st.cache_data
def get_iris_data():
    dataset = load_iris(as_frame=True)
    flowers = dataset.frame[FEATURES].copy()
    flowers["species"] = dataset.frame["target"].map(
        dict(enumerate(dataset.target_names))
    )
    return flowers, dataset.target_names


@st.cache_resource
def get_model():
    model_path = Path(__file__).with_name("iris_model.pkl")
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)
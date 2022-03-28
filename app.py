import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("yelp.csv")

st.title("Yelp DataFrame")

cntsdf = pd.DataFrame({'stars' : df['stars'].value_counts().index.values, 'counts' : df['stars'].value_counts().values})

st.markdown(
    """
    This is a plot showing the count of reviews for each star rating in the dataset.
    """
)

st.bar_chart(cntsdf)
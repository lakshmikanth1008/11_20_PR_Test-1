import streamlit as st
import pandas as pd

trafficking_df = pd.read_csv('Trafficking_Data.csv')

st.dataframe(trafficking_df)

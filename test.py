import streamlit as st
import pandas as pd
import altair as alt



trafficking_df = pd.read_csv('Trafficking_Data.csv')

st.dataframe(trafficking_df)

chart1=alt.Chart(trafficking_df).mark_bar().encode(
    x='gender',
    y='count()'
)

st.altair_chart(chart1, use_container_width=True)

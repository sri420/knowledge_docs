import streamlit as st
import pandas as pd

st.title("CSV Table with Selection")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    selected_rows = st.multiselect("Select Rows", df.index.tolist())
    selected_df = df.loc[selected_rows]
    st.write(selected_df)

    if st.button("Select All"):
        selected_rows = df.index.tolist()
    elif st.button("Deselect All"):
        selected_rows = []

    if st.button("Export Selected Rows"):
        csv = selected_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="selected_rows.csv",
            mime="text/csv",
        )

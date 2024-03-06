import streamlit as st
import pandas as pd

st.title("CSV Table with Selection")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    select_all = st.checkbox("Select All")

    if select_all:
        selected_rows = df.index.tolist()
    else:
        selected_rows = st.multiselect("Select Rows", df.index.tolist(), default=[])

    selected_df = df.loc[selected_rows]

    # Display the entire CSV file as a table
    st.write("CSV Table:")
    st.write(df)

    # Display the selected rows
    st.write("Selected Rows:")
    st.write(selected_df)

    if st.button("Export Selected Rows"):
        csv = selected_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="selected_rows.csv",
            mime="text/csv",
        )

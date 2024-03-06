import streamlit as st
import pandas as pd

st.title("CSV Table with Selection")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    select_all = st.checkbox("Select All")

    # Display the entire CSV file as a table with selection option
    edited_df = st.data_editor(df, use_container_width=True)

    if select_all:
        selected_rows = edited_df.index.tolist()
    else:
        selected_rows = edited_df.index[edited_df.iloc[:, 0]].tolist()

    selected_df = edited_df.loc[selected_rows]

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

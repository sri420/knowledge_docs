import streamlit as st
import pandas as pd

st.title("CSV Table with Selection")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    select_all = st.checkbox("Select All")

    # Add a new column for checkboxes
    df['Select'] = False

    # Display the entire CSV file as a table with selection option
    edited_df = st.data_editor(df, use_container_width=True, editable=True)

    if select_all:
        edited_df['Select'] = True
    else:
        selected_rows = edited_df.index[edited_df['Select']].tolist()
        selected_df = edited_df.loc[selected_rows]

    st.write("Selected Rows:")
    st.write(selected_df.drop('Select', axis=1))  # Drop the 'Select' column before displaying

    if st.button("Export Selected Rows"):
        csv = selected_df.drop('Select', axis=1).to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="selected_rows.csv",
            mime="text/csv",
        )

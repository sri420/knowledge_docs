import pandas as pd
import streamlit as st

# Load the CSV data
df = pd.read_csv('data.csv')

# Session state variables
if 'page_num' not in st.session_state:
    st.session_state.page_num = 0
if 'page_size' not in st.session_state:
    st.session_state.page_size = 10

# Pagination
start = st.session_state.page_num * st.session_state.page_size
end = start + st.session_state.page_size
page_data = df.iloc[start:end]

# Display data for the current page
st.write(page_data)

# Form for page navigation
with st.form('page_nav'):
    page_num = st.number_input('Page Number', value=st.session_state.page_num + 1)
    page_size = st.number_input('Page Size', value=st.session_state.page_size, min_value=1)
    submitted = st.form_submit_button('Go')

    if submitted:
        st.session_state.page_num = page_num - 1
        st.session_state.page_size = page_size

# Editing data
edited_data = st.data_editor(page_data)
df.iloc[start:end] = edited_data

# Save button
if st.button('Save'):
    df.to_csv('edited_data.csv', index=False)
    st.success('Data saved successfully!')

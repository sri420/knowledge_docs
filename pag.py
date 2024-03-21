import streamlit as st
import pandas as pd

# Assuming you have a large Pandas DataFrame called 'data'
data = pd.DataFrame({ ... })

# Set the number of rows to display per page
rows_per_page = 20

# Get the current page and edited data from the session state
current_page = st.session_state.get('current_page', 0)
edited_data = st.session_state.get('edited_data', data.copy())

# Calculate the start and end indices for the current page
start_idx = current_page * rows_per_page
end_idx = start_idx + rows_per_page

# Display the data for the current page and allow editing
edited_page_data = st.data_editor(edited_data.iloc[start_idx:end_idx])

# Update the edited data in the session state
edited_data.iloc[start_idx:end_idx] = edited_page_data

# Create navigation buttons
prev_page, next_page = st.columns(2)

if prev_page.button("Previous", disabled=current_page == 0):
    current_page -= 1
if next_page.button("Next", disabled=end_idx >= len(edited_data)):
    current_page += 1

# Update the session state with the current page and edited data
st.session_state.current_page = current_page
st.session_state.edited_data = edited_data

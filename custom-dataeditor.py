import pandas as pd
import streamlit as st

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 28, 35],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)

# Render the DataFrame with a custom select all checkbox
st.markdown("""
<style>
.stDataEditor .custom-checkbox {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}
.stDataEditor .custom-checkbox input[type="checkbox"] {
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# Add a select all checkbox to the header
select_all = st.checkbox("Select All", key="select_all")

# Render the DataFrame
edited_df = st.data_editor(df, use_container_width=True, num_rows_per_page=10)


# Check the state of the select all checkbox
if select_all:
    # Select all rows
    edited_df = edited_df.assign(is_selected=True)
else:
    # Deselect all rows
    edited_df = edited_df.assign(is_selected=False)

# Display the updated DataFrame
st.data_editor(edited_df, use_container_width=True, num_rows_per_page=10)

import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Sarah', 'Tom', 'Emily', 'David', 'Jessica'] * 10,
    'Age': [25, 32, 41, 28, 35, 27, 38, 31, 42, 26] * 10,
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 'Sydney', 'Madrid', 'Amsterdam', 'Rome', 'Toronto'] * 10
})

# Add two additional columns
data['Select'] = False
data['Comment'] = ''

# Configure AG Grid options
gb = st.ag_grid_builder(
    data,
    height=350,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,
    configure_pagination=True,
    paging_page_size=20  # Number of rows per page
)

# Add a checkbox column
gb.configure_columns(['Select'], editable=True, checkbox_select=True)

# Add a text column
gb.configure_columns(['Comment'], editable=True)

# Display the grid
gridOptions = gb.to_dict()["gridOptions"]
grid_response = st.ag_grid(gridOptions)

# Get the selected rows
selected_rows = grid_response["selected_rows"]

# Add a "Save" button
if st.button('Save'):
    # Display the selected rows as JSON
    st.write('Selected Rows (JSON format):')
    st.json(selected_rows)

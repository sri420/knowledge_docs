import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode, JsCode

# Load data from CSV file
data = pd.read_csv('your_file.csv')

# Create an instance of GridOptionsBuilder
gb = GridOptionsBuilder.from_dataframe(data)

# Configure grid options
gb.configure_default_column(editable=True, resizable=True)
gb.configure_selection(selection_mode='multiple', use_checkbox=True)
gb.configure_pagination(paginationAutoPageSize=True)
grid_options = gb.build()

# Create an instance of AgGrid
ag_grid = AgGrid(data,
                 grid_options=grid_options,
                 update_mode=GridUpdateMode.MANUAL,
                 data_return_mode=DataReturnMode.AS_INPUT,
                 fit_columns_on_grid_load=True)

# Add a save button
if st.button('Save'):
    # Get the current grid state
    grid_response = ag_grid.data()

    # Get selected rows
    selected_rows = grid_response['selected_rows']

    # Process selected rows (e.g., save to a file or database)
    if selected_rows:
        selected_data = data.iloc[selected_rows]
        st.write('Selected Rows:')
        st.write(selected_data)
        # Perform additional operations with selected_data, if needed

# Display the AgGrid
ag_grid.data()

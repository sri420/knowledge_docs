import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, DataReturnMode

# Load data from CSV file
data = pd.read_csv('your_file.csv')

# Create an instance of AgGrid
ag_grid = AgGrid(data,
                 editable=True,
                 update_mode=GridUpdateMode.MANUAL,
                 data_return_mode=DataReturnMode.AS_INPUT,
                 fit_columns_on_grid_load=True)

# Display the AgGrid
grid_response = ag_grid.data()

# Get selected rows
selected_rows = grid_response['selected_rows']

# Display selected rows
if selected_rows:
    st.write('Selected Rows:')
    st.write(data.iloc[selected_rows])

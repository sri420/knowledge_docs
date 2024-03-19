import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 32, 41, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
})

# Define the options for the 'City' column
city_options = ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 'Sydney']

# Create a custom editor for the 'City' column
def city_editor(value):
    return st.selectbox('', city_options, index=city_options.index(value) if value in city_options else 0)

# Create a data editor instance
edited_data = st.data_editor(
    data,
    use_container_width=True,
    column_editors={
        'City': city_editor  # Use the custom editor for the 'City' column
    }
)

# Display the edited data
st.write(edited_data)

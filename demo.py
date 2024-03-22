import streamlit as st
import pandas as pd
import json

# Load data from CSV
def load_data():
    df = pd.read_csv('/content/sample_data/california_housing_test.csv')
    return df

# Save data to CSV
def save_data(df):
    df.to_csv('your_file.csv', index=False)

# Display data with pagination
def display_data(df, rows_per_page):
    total_rows = len(df)
    max_pages = -(-total_rows // rows_per_page)
    page_number = st.number_input(label="Page Number", min_value=1, max_value=max_pages, step=1)
    start_index = rows_per_page * (page_number - 1)
    end_index = start_index + rows_per_page
    return df.iloc[start_index:end_index], start_index

# Main
def main():
    if "data" not in st.session_state:
       st.session_state.data = load_data()


    df = st.session_state.data
    rows_per_page = 10

    st.title('Data Editor')
    df_displayed, start_index = display_data(df, rows_per_page)
    df_displayed = st.data_editor(df_displayed)

    # Update the original dataframe with the edited data
    df.iloc[start_index:start_index+len(df_displayed)] = df_displayed.values

    if st.button('SAVE'):
        #save_data(df)
        st.data_editor(df)
        #st.write(json.dumps(df.to_dict(), indent=4))

if __name__ == "__main__":
    main()

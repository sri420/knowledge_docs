import streamlit as st
from streamlit.state.session_state import SessionState

# Function to initialize data
def initialize_data():
    # You can initialize your data here
    return [{"id": i, "value": f"value_{i}"} for i in range(1, 101)]  # Example data with 100 records

# Function to display data editor for a specific page
def display_data_editor(data, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = min(start_index + page_size, len(data))
    page_data = data[start_index:end_index]
    edited_data = st.dataframe(page_data, height=400, width=500)
    return edited_data

def main():
    # Initialize session state
    session_state = SessionState.get(data=[], page_number=1)

    # Load data if not already loaded
    if not session_state.data:
        session_state.data = initialize_data()

    # Display pagination controls
    page_number = st.sidebar.number_input("Page Number", min_value=1, max_value=len(session_state.data) // PAGE_SIZE + 1, value=session_state.page_number)

    # Display data editor for the selected page
    edited_data = display_data_editor(session_state.data, PAGE_SIZE, page_number)

    # Update data in session state if changes are made
    if edited_data is not None:
        session_state.data[((page_number - 1) * PAGE_SIZE):((page_number - 1) * PAGE_SIZE + len(edited_data))] = edited_data

    # Save button to capture changes
    if st.button("Save Changes"):
        process_changes(session_state.data)

def process_changes(data):
    # Process changes made in st.data_editor here
    st.write("Changes captured and processed successfully!")

if __name__ == "__main__":
    PAGE_SIZE = 10  # Adjust page size as needed
    main()

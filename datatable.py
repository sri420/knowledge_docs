import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

# Sample data (replace with your actual DataFrame)
df = pd.DataFrame({'column1': [1, 2, 3, 4, 5], 'column2': ['A', 'B', 'C', 'D', 'E']})

# Define initial page size and current page
PAGE_SIZE = 10
current_page = 0

# Function to slice DataFrame for pagination
def slice_data(df, page_size, current_page):
    return df.iloc[current_page * page_size: (current_page + 1) * page_size]

# Function to capture edited data and update edited_df
def update_edited_data(data, row_id, col_id, edited_df):
    # Check if row or column doesn't exist, handle gracefully (e.g., log or display error message)
    if row_id is None or col_id is None:
        return edited_df

    # Update edited DataFrame
    edited_df.loc[row_id, col_id] = data
    return edited_df

# Initial empty DataFrame for edited data
edited_df = pd.DataFrame(columns=df.columns)

app.layout = html.Div([
    html.Div('Editable DataTable with Pagination'),
    dcc.Dropdown(
        id='page-size',
        options=[{'label': str(x), 'value': x} for x in [5, 10, 15]],
        value=PAGE_SIZE
    ),
    dash_table.DataTable(
        id='datatable',
        columns=[{'name': i, 'id': i, 'editable': True} for i in df.columns],
        data=slice_data(df.copy(), PAGE_SIZE, current_page).to_dict('rows'),
        page_size=PAGE_SIZE,
        page_current=current_page,
        style_table={'overflowX': 'auto'}  # Ensure horizontal scrolling for long columns
    ),
    html.Div(id='pagination-container'),
    html.Div([
        html.H3('Edited Data'),
        dash_table.DataTable(
            id='edited-datatable',
            columns=[{'name': i, 'id': i} for i in df.columns],
            data=edited_df.to_dict('rows'),
            style_table={'overflowX': 'auto'}  # Ensure horizontal scrolling for long columns
        )
    ])
])

@app.callback(
    [Output('datatable', 'data'), Output('datatable', 'page_current'), Output('edited-datatable', 'data')],
    [Input('datatable', 'data_changed'),
     Input('datatable', 'page_current'),
     Input('page-size', 'value'),
     Input('datatable', 'full_cell_edit'),
     State('datatable', 'data'),
     State('datatable', 'row_id'),
     State('datatable', 'col_id')]
)
def update_output(data, page_current, page_size, full_cell_edit, data_state, row_id, col_id):
    global edited_df

    if data is None:
        return slice_data(df.copy(), page_size, current_page).to_dict('rows'), current_page, edited_df.to_dict('rows')

    if full_cell_edit is None:
        return data, page_current, edited_df.to_dict('rows')

    # Update edited DataFrame and return updated data for both tables
    edited_df = update_edited_data(data[row_id][col_id], row_id, col_id, edited_df.copy())

    return slice_data(df.copy(), page_size, page_current).to_dict('rows'), page_current, edited_df.to_dict('rows')

if __name__ == '__main__':
    app.run_server(debug=True)

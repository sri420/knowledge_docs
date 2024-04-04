import dash
from dash import html, dcc, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('./data/test_data.csv')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_action='native',
        page_current=0,
        page_size=10,  # Change this to the number of rows you want per page
        editable=True
    ),
    dbc.Button("Save Changes", id="save-button"),
    dbc.Modal(
    [
        dbc.ModalHeader("Unsaved Changes"),
        dbc.ModalBody("You have unsaved changes. Do you want to save them before navigating away?"),
        dbc.ModalFooter([
            dbc.Button("Yes", id="confirm-save", className="ml-auto"),
            dbc.Button("No", id="cancel-save", className="ml-auto")
        ]),
    ],
    id="modal",
),
    dcc.Store(id='store-desired-page', storage_type='session'),
    dcc.Store(id='store', data=df.to_dict('records')),
    dcc.Store(id='store-page', data=0)  # Store to track the current page
])

import pandas as pd

@app.callback(
    [Output('modal', 'is_open'), Output('store', 'data'), Output('store-page', 'data'), Output('store-desired-page', 'data'), Output('table', 'data'), Output('table', 'page_current')],
    [Input('table', 'page_current'), Input('save-button', 'n_clicks'), Input('confirm-save', 'n_clicks'), Input('cancel-save', 'n_clicks')],
    [State('store', 'data'), State('store-page', 'data'), State('modal', 'is_open'), State('table', 'data'), State('table', 'page_current')],
    prevent_initial_call=True
)
def toggle_modal(desired_page, save_n, confirm_n, cancel_n, stored_data, stored_page, is_open, table_data, page_current):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('-----------------')

    print('trigger_id:' + trigger_id)
    print('is_open:' + str(is_open))
    #print('stored_data:' + str(stored_data))
    #print('table_data:' + str(table_data))
    print('desired_page:' + str(desired_page))
    #print('stored_page:' + str(stored_page))
    print('page_current:' + str(page_current))  
    print('save_n:' + str(save_n))
    print('confirm_n:' + str(confirm_n))    
    print('cancel_n:' + str(cancel_n))
    print('-----------------')
    
    if trigger_id == 'save-button' and stored_data != table_data:
        pd.DataFrame(table_data).to_csv('./data/test_data.csv', index=False)  # Save the data back to the CSV file
        return is_open, table_data, stored_page, dash.no_update, dash.no_update, desired_page
    #if trigger_id == 'save-button' and stored_data != table_data and not is_open:
        #return True, stored_data, stored_page, desired_page, dash.no_update, dash.no_update
    elif trigger_id == 'table' and stored_data != table_data and not is_open:
        return True, stored_data, stored_page, desired_page, dash.no_update, desired_page
        #return True, stored_data, stored_page, desired_page, dash.no_update, stored_page
    elif trigger_id in ['confirm-save', 'cancel-save'] and is_open:
        if trigger_id == 'confirm-save':
            pd.DataFrame(table_data).to_csv('./data/test_data.csv', index=False)  # Save the data back to the CSV file
        return False, table_data if trigger_id == 'confirm-save' else stored_data, stored_page, dash.no_update, stored_data if trigger_id == 'cancel-save' else dash.no_update, desired_page

    return is_open, stored_data, stored_page, dash.no_update, dash.no_update, dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)

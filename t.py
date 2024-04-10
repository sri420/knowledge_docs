import dash
from dash import html,Dash,Input, Output, callback
import dash_ag_grid as dag



def button_cell_renderer(params):
    return html.Button('Click Me', id=f'button_{params.data.id}', n_clicks=0)


columns = [
    {'field': 'id', 'headerName': 'ID'},
    {'field': 'name', 'headerName': 'Name'},
    {'field': 'age', 'headerName': 'Age'},
    {'field': 'button', 'headerName': 'Action', 'cellRenderer': button_cell_renderer}
]

app = Dash(__name__)

app.layout = html.Div([
    dag.AgGrid(
        id='my-ag-grid',
        columnDefs=columns,
        rowData=[
            {'id': 1, 'name': 'John', 'age': 30},
            {'id': 2, 'name': 'Jane', 'age': 25},
            {'id': 3, 'name': 'Bob', 'age': 35},
        ],
        style={'height': '400px', 'width': '100%'}
    )
])


@callback(
    Output('my-ag-grid', 'rowData'),
    [Input(f'button_{i}', 'n_clicks') for i in range(1, 4)])
def handle_button_click(*args):
    # Perform actions based on the button clicks
    # and update the row data if necessary
    return [
        {'id': 1, 'name': 'John', 'age': 30},
        {'id': 2, 'name': 'Jane', 'age': 25},
        {'id': 3, 'name': 'Bob', 'age': 35},
    ]



if __name__ == '__main__':
    app.run_server(debug=True)

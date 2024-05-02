import dash
from dash import dcc, html
import dash_ag_grid as dag
#from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc, Input, Output, callback ,State,ctx,no_update
import pandas as pd
import json
import dash_bootstrap_components as dbc

from DataService import getData

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

rows,columns = getData() # Assign returned tuple 

# Create a DataFrame from the rows and column names
df = pd.DataFrame(rows, columns=columns)

columnDefs = [
     {"field": "Select", "checkboxSelection": True},
     {
        "headerName": "Name",
        "field": "name"
    },
      {
        "headerName": "DOB",
        "field": "dob"
    },
    {
        "headerName": "CITY",
        "field": "city"
    },
     {
        "headerName": "DEPTNO",
        "field": "deptno"
    },
      {
        "headerName": "ROLE",
        "field": "role"
    },
    {
        "field": "EDIT",
        "cellRenderer": "Button",
        "cellRendererParams": {"className": "btn btn-success","value":"EDIT"},
    }
]

# Define the layout of the app
app.layout = html.Div([
    html.H2(" Set the Page Size.  Enter number of rows"),
    dcc.Input(id="input-page-size", type="number", min=1, max=len(df), value=10, debounce=True),
    dag.AgGrid(
        id='aggrid',
        rowData=df.to_dict("records"),
        defaultColDef={"filter": "agTextColumnFilter"},
        columnDefs=columnDefs,
        dashGridOptions={"rowHeight": 48,"pagination": True, "paginationPageSizeSelector": False, "animateRows": False,'rowSelection': 'single',"suppressRowClickSelection": True},
    ),
    dcc.Store(id='selected-row-data', data=None),

    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Edit Agent Information")),
        dbc.ModalBody(
            [
                dbc.Label("Column 1", className="mr-2"),
                dbc.Input(type="text", id="txtcolumn1"),
                dbc.Label("Column 2", className="mr-2"),
                dbc.Input(type="text", id="txtcolumn2")
            ]
        ),
        dbc.ModalFooter( [
            dbc.Button("Save", id="save", className="ml-auto"),
            dbc.Button("Close", id="close", className="ml-auto") ]
        )
    ], id="modal",
       keyboard=False,
       centered=True,
       backdrop="static"),

        
])


@callback(
    Output("aggrid", "dashGridOptions"),
    Input("input-page-size", "value"),
    State("aggrid", "dashGridOptions"),
)
def update_page_size(page_size, grid_options):
    page_size = 1 if page_size is None else page_size
    grid_options["paginationPageSize"] = page_size
    return grid_options

# Callback to store selected data in dcc.Store
@app.callback(
      Output('selected-row-data', 'data'),
      Input("aggrid", "selectedRows")

)
def update_selected_data(selected_data):
    print("START:  update_selected_data")
    if selected_data:
        print("update_selected_data: selected_data is AVAILABLE")
        #print(selected_data[0])
        return selected_data[0]  # Assuming single row selection
    return no_update 


@callback(

    Output("txtcolumn1", "value"),
    Output("txtcolumn2", "value"),
    Output("modal", "is_open"),
   
    
    Input("aggrid", "cellRendererData"),
    Input("close", "n_clicks"),
    Input("save", "n_clicks"),

    State('selected-row-data', 'data'),
    State("modal", "is_open"),
    State("txtcolumn1", "value"),
    State("txtcolumn2", "value")
)
def showChange(cellRenderData,closebtn,savebtn,selecteddata,is_open,txtcolumn1,txtcolumn2): 
    print("START: showChange...")
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print("showChange: trigger_id")
    print(trigger_id)
    if trigger_id == 'save':
        print('trigger is save')
        # Fetch the submitted values
        print("START: submitted values are:")
        print(txtcolumn1)
        print(txtcolumn2)
        print("END:  Submitted values")
        # Save the values to DB
        # ToDO

        # Close the modal
        return no_update,no_update,not is_open
    elif trigger_id == 'close':
        print('trigger is close')
        return no_update,no_update,not is_open
    elif trigger_id == 'aggrid':
        print("showChange: trigger is aggrid")
   
        if cellRenderData:
            print('showChange: cellRenderData is AVAILABLE...')
            if selecteddata:
                print('showChange: selecteddata is AVAILABLE...')
                return selecteddata['Column1'],selecteddata['Column2'],True
      

    return no_update,no_update,no_update





# Run the app,
if __name__ == '__main__':
    app.run(debug=True)

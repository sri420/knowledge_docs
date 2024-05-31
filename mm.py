import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Column1': ['Value1', 'Value2'],
    'Column2': ['Value3', 'Value4'],
})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create a list of dbc.Input components for each column in the DataFrame
# Create a list of dbc.Input components for each column in the DataFrame
form_fields = []
for column in df.columns:
    form_fields.append(dbc.Label(column))
    form_fields.append(dbc.Input(id=column, type="text"))

# Create a dbc.Modal component and add the form fields to the body of the modal
modal = dbc.Modal(
    [
        dbc.ModalHeader("Form"),
        dbc.ModalBody(form_fields),
        dbc.ModalFooter(
            [
                dbc.Button("Submit", id="submit-button", className="ml-auto"),
                dbc.Button("Close", id="close-button", className="ml-auto"),
            ]
        ),
    ],
    id="modal",
)

app.layout = html.Div([dbc.Button("Open form", id="open-button"), modal])

@app.callback(
    Output("modal", "is_open"),
    [Input("open-button", "n_clicks"), Input("submit-button", "n_clicks"), Input("close-button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, n3, is_open):
    if n1 or n2 or n3:
        return not is_open
    return is_open

@app.callback(
    Output("modal-body", "children"),
    Input("submit-button", "n_clicks"),
    [State(column, "value") for column in df.columns],
)
def update_output(n_clicks, *args):
    if n_clicks:
        # Do something with the form data
        form_data = dict(zip(df.columns, args))
        print(form_data)

if __name__ == "__main__":
    app.run_server(debug=True)

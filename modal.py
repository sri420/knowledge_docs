import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

# Assume you have a DataFrame `df`
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': ['qux', 'quux', 'quuz'],
    'C': ['corge', 'grault', 'garply']
})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

modal = dbc.Modal(
    [
        dbc.ModalHeader("Input Form"),
        dbc.ModalBody(
            [dbc.Input(id=column, placeholder=f"Enter {column}...", className="mb-3") for column in df.columns]
        ),
        dbc.ModalFooter(
            dbc.Button("Close", id="close", className="ml-auto")
        ),
    ],
    id="modal",
)

app.layout = html.Div([
    dbc.Button("Open Modal", id="open"),
    modal
])

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)

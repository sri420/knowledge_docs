def generate_form_layout(column_names):
    form_layout = []
    for col in column_names:
        form_layout.append(
            dbc.Row(
                [
                    dbc.Col(dbc.Label(col, className="col-md-2"), width=2),
                    dbc.Col(
                        dcc.Input(id={'type': 'form-input', 'value': col}, type='text'),
                        width=10,
                    ),
                ]
            )
        )
    return form_layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container(
    [
        dbc.Row(
            [dbc.Col(html.H1("Dynamic Form based on DataFrame"), width=12)],
            justify="center",
        ),
        dbc.Form(id='dynamic-form', children=generate_form_layout(df.columns)),
        dbc.Button("Submit", id="submit-button", color="primary", className="mt-3"),
    ],
    fluid=True,
)
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    prevent_initial_call=True,
)
def update_output(n_clicks):
    if n_clicks:
        submitted_data = {col: dash.callback_context.triggered[0]['prop_id'].split('.')[0].split('-')[-1] for col in df.columns}
        # Process submitted data (e.g., update DataFrame, send to server)
        return dbc.Alert(f"Submitted data: {submitted_data}", color="success")
    return None


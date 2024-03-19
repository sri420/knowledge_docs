import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# Define the CheckboxRenderer
checkbox_renderer = JsCode("""
class CheckboxRenderer{
    init(params) {
        this.params = params;
        this.eGui = document.createElement('input');
        this.eGui.type = 'checkbox';
        this.eGui.checked = params.value;
        this.checkedHandler = this.checkedHandler.bind(this);
        this.eGui.addEventListener('click', this.checkedHandler);
    }
    checkedHandler(e) {
        let checked = e.target.checked;
        let colId = this.params.column.colId;
        this.params.node.setDataValue(colId, checked);
    }
    getGui(params) {
        return this.eGui;
    }
    destroy(params) {
        this.eGui.removeEventListener('click', this.checkedHandler);
    }
}
""")

# Create Example DataFrame
data = {
    "Name": ["Luna", "Waldi", "Milo", "Pixie", "Nelly"],
    "Grade": [14.5, 13.1, 14.2, 11.7, 12.2],
}
df = pd.DataFrame(data)
df.insert(loc=1, column="Selected", value=True)

# Configure the grid
gob = GridOptionsBuilder.from_dataframe(df)
gob.configure_column('Selected', editable=True, cellRenderer=checkbox_renderer)
gridOptions = gob.build()

# Display the grid
AgGrid(df, gridOptions=gridOptions)

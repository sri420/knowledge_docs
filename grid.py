import gradio as gr
import pandas as pd

df = pd.read_csv("your_file.csv")

def update_data(data, row, col, value):
    data.iloc[row, col] = value
    return data

data = df.copy()  # Create a copy of the original DataFrame

with gr.Blocks() as demo:
    gr.RenderedDataFrame(
        data,
        headers="auto",
        max_rows_per_page=10,  # Set the number of rows per page
        enable_edit=True,
        update_mode=gr.UpdateMode.MANUAL,
    )
    with gr.Row():
        row_num = gr.Number(label="Row", value=0)
        col_num = gr.Number(label="Column", value=0)
        value_input = gr.Textbox(label="Value")
        update_btn = gr.Button("Update Cell")
    update_btn.click(
        fn=update_data,
        inputs=[data, row_num, col_num, value_input],
        outputs=data,
    )

demo.launch()

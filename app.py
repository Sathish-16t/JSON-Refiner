import json
import gradio as gr

def refine_json(text):

    lines = text.split("\n")
    data = {}

    for line in lines:
        if ":" in line:
            key, value = line.split(":",1)

            key = key.strip()
            value = value.strip()

            if value.isdigit():
                value = int(value)

            elif value.lower() == "true":
                value = True

            elif value.lower() == "false":
                value = False

            else:
                try:
                    value = float(value)
                except:
                    pass

            data[key] = value

    output = json.dumps(data, indent=4)

    stats = f"""
Top-level Keys: {len(data)}
Value Types: {set(type(v).__name__ for v in data.values())}
"""

    return output, stats


with gr.Blocks() as demo:

    gr.Markdown("# JSON Refiner")

    with gr.Row():
        inp = gr.Textbox(lines=10,label="Input Key-Value Text")
        out = gr.Code(label="Refined JSON")

    stats = gr.Textbox(label="JSON Statistics")

    btn=gr.Button('refine JSON')
    btn.click(refine_json,inputs=inp,outputs=[out,stats])
    demo.launch()

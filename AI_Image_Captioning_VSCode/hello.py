"""IBM Lab 2 Gradio quickstart (boilerplate that IBM supplies directly)."""
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

if __name__ == "__main__":
    # IBM uses 0.0.0.0 on Cloud IDE; localhost is safer on your own machine.
    demo.launch(server_name="127.0.0.1", server_port=7860)

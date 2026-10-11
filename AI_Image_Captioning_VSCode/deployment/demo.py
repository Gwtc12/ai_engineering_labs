"""IBM Lab 3's supplied simple Gradio application (PDF p. 6)."""
import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

if __name__ == "__main__":
    # IBM requires 0.0.0.0 in the container so Code Engine can reach port 7860.
    demo.launch(server_name="0.0.0.0", server_port=7860)

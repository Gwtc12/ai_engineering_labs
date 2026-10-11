"""IBM Lab 2, pages 13–15: YOUR image-captioning Gradio exercise.

This deliberately leaves the learning logic undone.
"""
import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

MODEL_ID = "Salesforce/blip-image-captioning-base"

# LAB STEP 2: load processor and BLIP model (PDF p. 13).
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)


def caption_image(input_image: np.ndarray):
    """Receive an image as a NumPy array; return a text caption."""
    raw_image = Image.fromarray(input_image).convert("RGB")
    text = "the image of"
    inputs = processor(images=raw_image, text=text, return_tensors = "pt")
    outputs = model.generate(**inputs, max_length=50)  # type: ignore[attr-defined]
    caption = processor.decode(outputs[0], skip_special_tokens = True)
    return caption


if __name__ == "__main__":
    # LAB STEPS 4–5 (p. 14): connect function to gr.Interface and launch.
    iface = gr.Interface(
        fn=caption_image,
        inputs=gr.Image(),
        outputs="text"
    )

    iface.launch()
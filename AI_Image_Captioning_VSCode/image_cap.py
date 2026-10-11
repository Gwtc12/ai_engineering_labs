"""IBM Lab 2, pages 5–9: first BLIP captioning exercise.

IMPORTANT: This is a LEARNING STARTER, not a completed solution.
Run after completing the TODOs: python image_cap.py images/your-photo.jpg
"""
import sys
from pathlib import Path
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

MODEL_ID = "Salesforce/blip-image-captioning-base"


def main(image_path: Path):
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)

    image = Image.open(image_path).convert("RGB")

    text = "the image of"
    inputs = processor(images=image, text=text, return_tensors="pt")

    outputs = model.generate(**inputs, max_length=50)

    caption = processor.decode(outputs[0], skip_special_tokens=True)
    print(caption)
   


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python image_cap.py images/your-photo.jpg")
    main(Path(sys.argv[1]))

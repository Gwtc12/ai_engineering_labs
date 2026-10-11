"""IBM Lab 2, pages 17–20: webpage-image captioning exercise.

IBM supplies the HTML/image downloading logic; you write the BLIP portion.
This starter uses the Wikipedia IBM article named in the PDF.
Only process public web pages you are allowed to access.
"""
from io import BytesIO
from typing import cast
import requests
from bs4 import BeautifulSoup
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration



MODEL_ID = "Salesforce/blip-image-captioning-base"
URL = "https://en.wikipedia.org/wiki/IBM"
HEADERS = {"User-Agent": "Mozilla/5.0"}

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = cast(
    BlipForConditionalGeneration,
    BlipForConditionalGeneration.from_pretrained(MODEL_ID),
)

def caption_image(raw_image: Image.Image) -> str:
    text = "The image of"
    inputs = processor(images=raw_image, text=text, return_tensors = "pt")
    outputs = model.generate(**inputs, max_length =50)
    captions = processor.decode(outputs[0], skip_special_tokens=True)
    return captions

    


def main():
    # The following webpage-scraping scaffold comes from IBM's example.
    response = requests.get(URL, headers=HEADERS, timeout=15)
    response.raise_for_status()
    print("Status:", response.status_code, "HTML size:", len(response.text))

    soup = BeautifulSoup(response.text, "html.parser")
    img_elements = soup.find_all("img")
    print(f"Found {len(img_elements)} <img> tags")

    with open("captions.txt", "w", encoding="utf-8") as caption_file:
        for idx, img_element in enumerate(img_elements, start=1):
            # bs4 attribute values may be str or a list of str; normalize to str.
            raw_url = img_element.get("src") or img_element.get("data-src")
            if not raw_url and img_element.has_attr("srcset"):
                raw_url = img_element["srcset"]
            if isinstance(raw_url, list):
                raw_url = " ".join(raw_url)
            img_url = str(raw_url).split()[0] if raw_url else ""
            if not img_url:
                continue
            if img_url.endswith(".svg") or ".svg" in img_url:
                continue
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                img_url = "https://en.wikipedia.org" + img_url
            elif not img_url.startswith("http"):
                continue

            try:
                r = requests.get(img_url, timeout=10, headers=HEADERS)
                r.raise_for_status()
                raw_image = Image.open(BytesIO(r.content))
                if raw_image.size[0] * raw_image.size[1] < 200:
                    continue
                raw_image = raw_image.convert("RGB")

                # The code below calls YOUR BLIP logic from above.
                caption = caption_image(raw_image)
                caption_file.write(f"{img_url}: {caption}\n")
                print(f"[{idx}] Caption saved")
            except NotImplementedError:
                # Do not accidentally hide an incomplete lab task.
                raise
            except OSError:
                # Some site images may not be supported by Pillow.
                continue
            except Exception as exc:
                print(f"[{idx}] Error: {exc}")
                continue


if __name__ == "__main__":
    main()

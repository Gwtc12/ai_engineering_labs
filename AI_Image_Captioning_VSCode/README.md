# AI Image Captioning — One VS Code Project

These two IBM labs are phases of one learning project:
1. **Build:** describe images with BLIP, add a Gradio interface, and caption images from a webpage.
2. **Deploy:** package and deploy a Gradio app using Docker and IBM Code Engine. IBM provides a *small greeting demo* for this part; we'll follow that exercise rather than silently changing it.

## Start in VS Code

Open **this folder** in VS Code. In Terminal → New Terminal, run **one command at a time**:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python hello.py
```

Use Python **3.10** if available (3.11 also works for many setups). **Stop after the version check and send me its output first** so we can avoid environment problems. On Windows, ask me for the corresponding activation command. The first BLIP run downloads pretrained weights from Hugging Face, so it needs internet and disk space.

## Files we'll use (in order)

- `image_cap.py` — first BLIP image caption (you complete the code).
- `hello.py` — IBM's supplied Gradio warm-up.
- `image_captioning_app.py` — your Gradio + BLIP app (you complete the code).
- `automate_url_captioner.py` — captions for images found on a webpage (you complete the BLIP part).
- `deployment/` — IBM's provided `demo.py`, `requirements.txt`, `Dockerfile`; test locally, then deploy with IBM Code Engine if you have cloud access.
- `lab_instructions/` — both original PDFs.

Put a test photo in `images/`. The starter code has TODOs deliberately: we implement **one step at a time** and test each step.

## Final interview (60–90 seconds)

Use this short template, **in your own words**:

1. **WHAT:** “I built ___.”
2. **WHY:** “It solves ___.”
3. **HOW:** “The input goes through ___, then ___, and produces ___.”
4. **TEST:** “I checked it worked by ___.”
5. **LEARNED:** “The most important engineering concept I learned was ___.”

I will interview you, score **technical accuracy, clarity, and conciseness** (each /10), explain what you missed or overexplained, and have you try again.

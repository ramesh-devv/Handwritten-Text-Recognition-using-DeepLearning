from PIL import Image
import torch

from preprocess import preprocess
from model_loader import processor, model, device


def predict_text(image_path):

    image_path = preprocess(image_path)

    image = Image.open(image_path).convert("RGB")

    pixel_values = processor(
        image,
        return_tensors="pt"
    ).pixel_values.to(device)

    generated_ids = model.generate(
        pixel_values,
        max_new_tokens=50
    )

    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return text, "High"
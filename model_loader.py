import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

MODEL_NAME = "microsoft/trocr-base-handwritten"

print("=" * 60)
print("Loading Microsoft TrOCR Handwritten Model...")
print("First run may take 5-10 minutes depending on internet speed.")
print("=" * 60)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = TrOCRProcessor.from_pretrained(
    MODEL_NAME,
    use_fast=False
)

model = VisionEncoderDecoderModel.from_pretrained(
    MODEL_NAME
)

model.to(device)
model.eval()

print("=" * 60)
print("Model Loaded Successfully!")
print("Running on:", device)
print("=" * 60)
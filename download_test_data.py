from dotenv import load_dotenv
from pathlib import Path
import os
import gdown
import sys
import re

load_dotenv()

DATA_DIR = Path(os.getenv("DATA_DIR"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

FILE_ID = os.getenv("FILE_ID")

output_file = DATA_DIR / "dataset.csv"

url = f"https://drive.google.com/uc?id={FILE_ID}"

print(f"Pobieranie do: {output_file}")
print(f"Używane ID pliku: {FILE_ID}")

gdown.download(url, str(output_file), quiet=False)

print("Pobrano pomyślnie.")
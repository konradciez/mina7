import csv
from pathlib import Path

DATA_FILE = Path("data/dataset.csv")

def test_every_email_has_at():
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            assert "@" in row["Email"]
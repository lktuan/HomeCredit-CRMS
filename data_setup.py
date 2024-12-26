import zipfile
import os
from pathlib import Path

if __name__ == "__main__":
    # Set paths
    zip_file = "home-credit-credit-risk-model-stability.zip"
    extract_path = "src/data"

    # Create extract directory if it doesn't exist
    Path(extract_path).mkdir(parents=True, exist_ok=True)

    # Unzip file
    print(f"Extracting {zip_file} to {extract_path}")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Delete zip file
    os.remove(zip_file)
    print("Zip file deleted")
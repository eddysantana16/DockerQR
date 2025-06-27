import qrcode
import argparse
import os
from datetime import datetime

def generate_qr(url, output_dir="qr_codes"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    img = qrcode.make(url)
    img.save(filepath)

    print(f"[INFO] QR code generated: {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("--url", type=str, required=True, help="URL to encode in the QR code")
    args = parser.parse_args()

    generate_qr(args.url)

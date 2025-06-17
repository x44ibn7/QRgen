# QRgen

A simple Python application that generates QR codes from URLs or text input.

## Description

QRgen is a straightforward QR code generator that creates QR code images from any text or URL input. The generated QR codes can be easily scanned with any QR code reader or smartphone camera.

## Features

- Generate QR codes from any text or URL input
- Save QR codes as PNG images
- Customizable output filename
- Simple command-line interface

## Requirements

- Python 3.x
- `qrcode` library

## Installation

1. Ensure you have Python installed on your system
2. Install the required package using pip:
   ```
   pip install qrcode[pil]
   ```

## Usage

Run the script and follow the prompts:

```
python qrgen.py
```

When prompted, enter the URL or text you want to convert to a QR code. The program will generate a QR code image named `qrcode.png` in the same directory.

You can also use the `generate_qr()` function in your own code:

```python
from qrgen import generate_qr

# Generate a QR code with default filename (qrcode.png)
generate_qr("https://example.com")

# Generate a QR code with custom filename
generate_qr("https://example.com", "my_qrcode.png")
```

## License

This project is open source and available for anyone to use and modify.

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

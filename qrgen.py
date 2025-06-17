import qrcode

def generate_qr(link, filename="qrcode.png"):
    """Generates a QR code for the given link and saves it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    link = input("Enter the link to generate QR code: ")
    generate_qr(link)

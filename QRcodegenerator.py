import qrcode

def generate_qr(data, filename='qrcode.png'):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR Code saved as {filename}")


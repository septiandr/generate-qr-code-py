import qrcode

def generate_qr(data, filename='qrcode.png'):
    # Buat QR Code
    qr = qrcode.QRCode(
        version=1,  # ukuran QR (1–40), atau gunakan None untuk otomatis
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Buat gambar QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Simpan ke file
    img.save(filename)
    print(f"QR code saved as: {filename}")

# Contoh penggunaan
# generate_qr("https://cp.hyundaimotor.co.id/public/cs/qr?evseid=ID*HYI*E7937")
generate_qr("https://cp.hyundaimotor.co.id/public/cs/ID*HYI*E7937")

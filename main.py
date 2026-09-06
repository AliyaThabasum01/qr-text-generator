from generator import create_qr

text = input("Enter text or URL: ").strip()
filename = input("Enter output filename: ").strip()

if not filename:
    filename = "qrcode.png"

create_qr(text, filename)

print(f"\n✅ QR code saved as {filename}")

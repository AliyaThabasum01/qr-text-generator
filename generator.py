import qrcode


def create_qr(text, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image()
    image.save(filename)

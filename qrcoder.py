import qrcode

data = "https://cozyportfolio.netlify.app/"

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")

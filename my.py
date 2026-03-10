import qrcode

# Apne HTML front page ka URL yaha daalo
url = "https://tanishshukla280810.github.io/jatin-qr-code-work/"  

# QR code generate karo
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("frontpage_qr.png")

print("QR Code bana liya! frontpage_qr.png file check karo.")

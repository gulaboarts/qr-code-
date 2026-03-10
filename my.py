import qrcode

url = "https://gulaboarts.github.io/qr-code-/"

img = qrcode.make(url)

img.save("gulabo_qr.png")

print("QR Code Ready")

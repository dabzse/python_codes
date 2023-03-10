from pyqrcode import create as qr


SITE = "http://dabzse.net"
NAME = "website.svg"

qr(SITE).svg(NAME, scale = 7)


print(f"QR code has been saved: {NAME}")

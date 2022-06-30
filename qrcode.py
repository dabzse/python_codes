import pyqrcode
from pyqrcode import QRCode


SITE = "http://dabzse.net"
NAME = "website.svg"


qr = pyqrcode.create(SITE)
qr.svg(NAME, scale = 7)

print(f"QR code has been saved: {NAME}")

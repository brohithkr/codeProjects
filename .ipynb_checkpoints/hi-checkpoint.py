import qrcode
import os

img = qrcode.make("https://www.FuckYou.com")

img.save("qr.png","PNG")

print("hello")
import qrcode
import qrcode.image.svg

img = qrcode.make("https://github.com/vroque19")

img.save("output.png")


import qrcode

img = qrcode.make("https://github.com/MSR-07")
img.save("gitHubQr.png")
img.show()

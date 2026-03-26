import qrcode
x = qrcode.QRCode()
msg = "have a good day!!!"
x.add_data(msg)
x.make(fit=True)
res = x.make_image(fill_color="black",back_color="white")
res.save("pooja.png")
print("created successfully")

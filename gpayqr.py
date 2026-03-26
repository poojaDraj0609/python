import qrcode
x = qrcode.QRCode()

upi_id = "poojadharmaraj73@oksbi"

name = "this is pooja"
note = "prem kudutha kasa anupu"
amount = "100"

link = f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"
x.add_data(link)
x.make(fit=True)
res = x.make_image(fill_color="black",back_color="white")
res.save("POOjA Gpay.png")
print("created successfully")
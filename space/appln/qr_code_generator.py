import qrcode

upi_url = " (upi url)"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(upi_url)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save("static/images/upi_payment_qr.png")


print("QR code generated and saved as 'static/images/upi_payment_qr.png'")

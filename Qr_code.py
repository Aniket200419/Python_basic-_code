import qrcode

# Your website/link
url = "https://www.linkedin.com/in/aniket-lande-539b8a2b1/"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code
img.save("my_link_qr.png")

print("QR Code created successfully!")
print("Saved as: my_link_qr.png")
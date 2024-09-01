import qrcode 

# Replacing this with your actual vercal link

portfolio_url = "https://myportfolio-q2t7yv434-aanand452s-projects.vercel.app/"


# create a qrcode  object

qr = qrcode.QRCode(
    version=1, # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Controls the error correction used for the QR Code
    box_size = 10, # Size of each box in pixels
    border = 4, # Thickness of the border
)


# Add your URL to the QR code

qr.add_data(portfolio_url)
qr.make(fit=True)

#create an image from the QR code instance

img = qr.make_image(fill="black",back_color='white')

# Save the image file
img.save("portfolio_qr_code.png")

print("QR Code generated and saved as portfolio_qr_code.png")
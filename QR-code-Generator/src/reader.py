from pyzbar.pyzbar import decode
from PIL import Image

def read_qr_code(image_path):
    img = Image.open(image_path)
    result = decode(img)
    for obj in result:
        print("Data:", obj.data.decode())
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
from PIL import ImageColor

def get_error_correction(level):
    return {
        "L": ERROR_CORRECT_L,
        "M": ERROR_CORRECT_M,
        "Q": ERROR_CORRECT_Q,
        "H": ERROR_CORRECT_H,
    }.get(level, ERROR_CORRECT_L)

def is_valid_color(color):
    try:
        ImageColor.getrgb(color)
        return True
    except ValueError:
        return False

def generate_qr_code(data, filename, file_format, fg_color, bg_color, box_size, error_level):
    # Validate colors
    if not is_valid_color(fg_color):
        print(f"Invalid foreground color '{fg_color}'. Using default 'black'.")
        fg_color = "black"
    if not is_valid_color(bg_color):
        print(f"Invalid background color '{bg_color}'. Using default 'white'.")
        bg_color = "white"

    qr = qrcode.QRCode(
        version=1,
        error_correction=get_error_correction(error_level),
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save(f"{filename}.{file_format}")
    print(f"QR code saved as {filename}.{file_format}")
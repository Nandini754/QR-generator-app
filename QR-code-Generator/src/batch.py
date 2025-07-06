from qr_generator import generate_qr_code
from history import log_history

def batch_generate():
    print("Batch mode: Enter each input on a new line. Enter a blank line to finish.")
    inputs = []
    while True:
        data = input("Input: ").strip()
        if not data:
            break
        inputs.append(data)
    for idx, data in enumerate(inputs, 1):
        filename = f"qr_code_{idx}"
        generate_qr_code(data, filename, "png", "black", "white", 10, "L")
        log_history(data, f"{filename}.png")
    print(f"Generated {len(inputs)} QR codes.")
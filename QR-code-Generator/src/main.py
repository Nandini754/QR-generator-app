from qr_generator import generate_qr_code
from batch import batch_generate
from history import log_history

def main():
    print("=== QR Code Generator ===")
    mode = input("Choose mode: (1) Single (2) Batch: ").strip()
    if mode == "2":
        batch_generate()
    else:
        data = input("Enter text or URL: ").strip()
        filename = input("Enter filename (without extension): ").strip() or "qr_code"
        file_format = input("Choose format (png/jpg/svg): ").strip().lower() or "png"
        print("You can use color names (e.g., 'red', 'blue') or hex codes (e.g., '#FF5733').")
        fg_color = input("Foreground color (default black): ").strip() or "black"
        bg_color = input("Background color (default white): ").strip() or "white"
        box_size = int(input("Box size (default 10): ").strip() or 10)
        error_level = input("Error correction (L/M/Q/H, default L): ").strip().upper() or "L"
        generate_qr_code(
            data, filename, file_format, fg_color, bg_color, box_size, error_level
        )
        log_history(data, f"{filename}.{file_format}")

if __name__ == "__main__":
    main()
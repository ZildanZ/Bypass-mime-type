import sys
import piexif
from PIL import Image

def embed_php(jpg_path, php_path, output_path):
    try:
        with open(php_path, "r") as f:
            php_code = f.read()
        
        exif_dict = piexif.load(jpg_path)
        exif_dict["0th"][piexif.ImageIFD.Make] = php_code.encode()
        exif_bytes = piexif.dump(exif_dict)
        
        image = Image.open(jpg_path)
        image.save(output_path, "jpeg", exif=exif_bytes)
        print(f"PHP script embedded successfully into {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def extract_php(jpg_path, output_php_path):
    try:
        exif_dict = piexif.load(jpg_path)
        php_code = exif_dict["0th"].get(piexif.ImageIFD.Make, b"").decode()
        
        if php_code:
            with open(output_php_path, "w") as f:
                f.write(php_code)
            print(f"PHP script extracted successfully to {output_php_path}")
        else:
            print("No PHP script found in EXIF metadata.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████████─██████████─██████─────────████████████───██████████████─██████──────────██████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░░░░░██─██░░░░░░██─██░░██─────────██░░░░░░░░████─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─████████████░░░░██─████░░████─██░░██─────────██░░████░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─
─────────████░░████───██░░██───██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────
───────████░░████─────██░░██───██░░██─────────██░░██──██░░██─██░░██████░░██─██░░██──██░░██──██░░██─██░░██████████─██░░██████████─██░░██─────────
─────████░░████───────██░░██───██░░██─────────██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────
───████░░████─────────██░░██───██░░██─────────██░░██──██░░██─██░░██████░░██─██░░██──██░░██──██░░██─██████████░░██─██░░██████████─██░░██─────────
─████░░████───────────██░░██───██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██████░░██─────────██░░██─██░░██─────────██░░██─────────
─██░░░░████████████─████░░████─██░░██████████─██░░████░░░░██─██░░██──██░░██─██░░██──██░░░░░░░░░░██─██████████░░██─██░░██████████─██░░██████████─
─██░░░░░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░██──██░░██─██░░██──██████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████████─██████████─██████████████─████████████───██████──██████─██████──────────██████─██████████████─██████████████─██████████████─
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")
        print("Usage:")
        print("  Embed PHP: python script.py embed image.jpg file.php output.jpg")
        print("  Extract PHP: python script.py extract image.jpg output.php")
        sys.exit(1)

    command = sys.argv[1].lower()
    
    if command == "embed" and len(sys.argv) == 5:
        embed_php(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "extract" and len(sys.argv) == 4:
        extract_php(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command or arguments.")

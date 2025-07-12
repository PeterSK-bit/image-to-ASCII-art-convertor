import argparse
from PIL import Image
from string import ascii_letters, digits

def sanitize_filename(name):
    safe_chars = ascii_letters + digits + "-_."
    return "".join(c for c in name if c in safe_chars)

def main():
    parser = argparse.ArgumentParser(description="Convert image to ASCII art.")
    parser.add_argument("image_path", nargs="?", help="Path to the input image (optional)")
    parser.add_argument("--output", "-o", help="Name of the output .txt file (optional)")

    args = parser.parse_args()

    # If not provided via CLI, ask interactively
    image_path = args.image_path or input("Path to image: ").strip()
    output_name = args.output or input("Output file name: ").strip()

    # Sanitize output file name
    output_name = sanitize_filename(output_name)
    if not output_name:
        print(f"INFO: After sanitazion filename end up empty, default filename asigned")
        output_name = "image"
    print(f"INFO: Sanitized filename: {output_name}")

    # Try to load image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"ERROR: Unable to load image: {e}")
        return

    pix = image.load()
    width, height = image.size
    symbols = " .:-=+*#%@"

    with open(f"{output_name}.txt", "w") as f:
        for y in range(height):
            for x in range(width):
                r, g, b = pix[x, y][:3]
                avg = (r + g + b) / 3
                idx = int(avg / (255 / (len(symbols) - 1)))
                char = symbols[idx]
                f.write(char + "  ")
            f.write("\n")

if __name__ == "__main__":
    main()
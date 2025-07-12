from PIL import Image
from string import ascii_letters, digits

def main():
    path = input("path to image: ")
    new_file_name = input("new file name: ").strip().replace(" ", "-")

    safe_chars = ascii_letters + digits + "-_."
    new_file_name = "".join(char for char in new_file_name if char in safe_chars)

    # if new_file_name is empty after sanitizing
    if not new_file_name:
        print("INFO: After sanitazion of your filename it came out empty, default filename assigned")
        new_file_name = "image"

    print(f"INFO: Sanitized filename: {new_file_name}")

    try:
        image = Image.open(path)
    except:
        print("ERROR: Unable to load image")
        return

    pix = image.load()

    width, height = image.size
    symbols=" .:-=+*#%@"

    with open(f"{new_file_name}.txt","w") as f:
        for y in range(height):
            for x in range(width):
                r, g, b = pix[x, y][:3]  # Extract RGB values
                average_brightness = (r + g + b) / 3
                symbol_index = int(average_brightness / (255 / (len(symbols) - 1)))
                ascii_char = symbols[symbol_index]
                f.write(ascii_char + "  ")  # Two spaces to preserve aspect ratio
            f.write("\n")

if __name__ == "__main__":
    main()
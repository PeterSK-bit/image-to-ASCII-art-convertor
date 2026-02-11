import argparse
from PIL import Image
from string import ascii_letters, digits
import sys
import logging

def sanitize_filename(name):
    safe_chars = ascii_letters + digits + "-_."
    return "".join(c for c in name if c in safe_chars)

def main() -> int:
    parser = argparse.ArgumentParser(description="Convert image to ASCII art.")
    parser.add_argument("image_path", nargs="?", help="Path to the input image (optional)")
    parser.add_argument("--output", "-o", help="Name of the output .txt file (optional)")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    logger = logging.getLogger(__name__)

    # Getting input
    image_path = args.image_path or input("Path to image: ").strip()
    output_name = args.output or input("Output file name: ").strip()

    # Sanitize output file name
    output_name = sanitize_filename(output_name)
    if not output_name:
        logger.warning("After sanitazion filename end up empty, default filename asigned")
        output_name = "image"
    logger.info("Sanitized filename: %s", output_name)

    # Try to load image
    try:
        image = Image.open(image_path)
        pix = image.load()
    except FileNotFoundError:
        logger.error("Input file not found.")
        return 1
    except PermissionError:
        logger.error("No permission to read input file.")
        return 1
    except Image.UnidentifiedImageError:
        logger.error("File is not a valid image.")
        return 1
    except OSError as e:
        logger.exception("OS error while opening image: %s", e)
        return 1
    except Exception as e:
        logger.exception("Unexpected error while loading input image: %s", e)

    width, height = image.size
    SYMBOLS = " .:-=+*#%@"
    
    # try to write output
    try:
        with open(f"{output_name}.txt", "w") as f:
            for y in range(height):
                for x in range(width):
                    r, g, b = pix[x, y][:3]
                    avg = (r + g + b) / 3
                    idx = int(avg / (255 / (len(SYMBOLS) - 1)))
                    char = SYMBOLS[idx]
                    f.write(char + "  ")
                f.write("\n")
    except PermissionError:
        logger.error("No permission to write output file.")
        return 2
    except OSError as e:
        logger.exception("OS error while writing output file: %s", e)
        return 2
    except Exception as e:
        logger.exception("Unexpected error while writing output: %s", e)
        return 2

    return 0

if __name__ == "__main__":
    sys.exit(main())
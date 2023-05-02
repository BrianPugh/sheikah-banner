import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="Text to translate.")
    parser.add_argument("--vertical", action="store_true")
    parser.add_argument(
        "--mode",
        type=str,
        default="L",
        help="Output mode. Recommended 'L' (default) or '1'.",
    )
    parser.add_argument("--size", type=int, default=36, help="Output font size")
    parser.add_argument("--padding", type=int, default=None)
    parser.add_argument("--output", "-o", type=Path, help="Output file to save to.")
    args = parser.parse_args()

    font_path = "font/sheikah-complete.ttf"

    if args.padding is None:
        args.padding = args.size

    if args.vertical:
        args.text = "\n".join(args.text)

    font = ImageFont.truetype(font_path, args.size)

    _, _, text_width, text_height = ImageDraw.Draw(Image.new("RGB", (0, 0))).textbbox(
        (0, 0), args.text, font=font
    )

    image_width = text_width + 2 * args.padding
    image_height = text_height + 2 * args.padding

    # Create an Image object and a Draw object
    img = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(img)
    draw.text((args.padding, args.padding), args.text, font=font, fill="black")

    img = img.convert(args.mode)

    if args.output:
        img.save(args.output)
    else:
        img.show()


if __name__ == "__main__":
    main()

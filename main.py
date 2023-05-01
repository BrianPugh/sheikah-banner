import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="Text to translate.")
    args = parser.parse_args()

    font_path = "font/sheikah-complete.ttf"
    font_size = 36
    padding = 20

    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = ImageDraw.Draw(Image.new("RGB", (0, 0))).textsize(
        args.text, font=font
    )

    image_width = text_width + padding
    image_height = text_height + padding

    # Create an Image object and a Draw object
    img = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(img)
    draw.text((padding // 2, padding // 2), args.text, font=font, fill="black")

    # Show the image
    img.show()


if __name__ == "__main__":
    main()

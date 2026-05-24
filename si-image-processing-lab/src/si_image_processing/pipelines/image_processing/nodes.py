from PIL import Image, ImageFilter, ImageDraw


def process_image(
    input_path: str,
    output_path: str,
    rotation_angle: int,
    filter_name: str,
    watermark_text: str,
):

    image = Image.open(input_path)

    rotated = image.rotate(rotation_angle)

    if filter_name == "EMBOSS":
        filtered = rotated.filter(ImageFilter.EMBOSS)

    elif filter_name == "FIND_EDGES":
        filtered = rotated.filter(ImageFilter.FIND_EDGES)

    else:
        filtered = rotated

    draw = ImageDraw.Draw(filtered)

    draw.text((20, 20), watermark_text, fill="white")

    filtered.save(output_path)

    return output_path
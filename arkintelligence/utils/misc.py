import base64
import os


def is_image(file_path: str) -> bool:
    """
    Check if the file is an image.
    :param file_path: Path to the file.
    :return: True if the file is an image, False otherwise.
    """
    if file_path.startswith("http"):
        return True
    # Validate the file path
    if not os.path.isfile(file_path):
        raise ValueError(f"File path {file_path} is not valid.")
    # List of valid image extensions
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    # Get the file extension
    _, ext = os.path.splitext(file_path)
    # Check if the extension is in the list of valid extensions
    return ext.lower() in valid_extensions


def encode_image(image_path):
    if image_path.startswith("http"):
        return image_path
    code = ""
    with open(image_path, "rb") as image_file:
        code = base64.b64encode(image_file.read()).decode("utf-8")
    _, ext = os.path.splitext(image_path)
    return f"data:image/{ext.lower().replace('.', '')};base64,{code}"

from PIL import ImageGrab
from generateNameWithTime import generate_name_with_time


def capturing_screenshot(x: int, y: int, width: int, height: int):
    ss_region = (x, y, width, height)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f"../image/capture/{generate_name_with_time('image')}")

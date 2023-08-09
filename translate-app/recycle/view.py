import pyautogui
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the coordinates of the rectangle you want to capture
x, y, width, height = 400, 100, 300, 200

# Capture the screen area
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Convert the screenshot to grayscale for better OCR
screenshot = screenshot.convert("RGB")

# Perform OCR on the screenshot
text = pytesseract.image_to_string(screenshot)

print("Extracted Text:")
print(text)
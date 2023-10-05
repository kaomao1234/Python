from PIL import Image, ImageDraw

# Open the image
image_path = "image/capture1.PNG"  # Replace with the path to your image
original_image = Image.open(image_path)

# Convert the image to RGB mode (removes the alpha channel)
original_image = original_image.convert("RGB")

# Create a draw object to draw on the image
draw = ImageDraw.Draw(original_image)

# Get the dimensions of the image
width, height = original_image.size

# Define the number of rows and columns for the grid
num_rows = 4
num_cols = 4

# Calculate the width and height of each grid cell
cell_width = width // num_cols
cell_height = height // num_rows

# Draw horizontal grid lines
for i in range(1, num_rows):
    y = i * cell_height
    draw.line([(0, y), (width, y)], fill=(0, 0, 0), width=2)

# Draw vertical grid lines
for i in range(1, num_cols):
    x = i * cell_width
    draw.line([(x, 0), (x, height)], fill=(0, 0, 0), width=2)

# Save the image with the grid
output_path = "output_image_with_grid.jpg"
original_image.save(output_path)

# Show or display the image
original_image.show()

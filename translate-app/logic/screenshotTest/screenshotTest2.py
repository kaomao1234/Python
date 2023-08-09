from PIL import ImageGrab
ss_region = (300, 300, 600, 600)
ss_img = ImageGrab.grab(ss_region)
ss_img.save("image/SS3.jpg")
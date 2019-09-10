import os
import pytesseract
from PIL import Image


image_path = os.path.join(os.getcwd(), "Images/a.jpg")
save_path = os.path.join(os.getcwd(), "Images/grayscale.jpg")

# Convert the image to grayscale
image = Image.open(image_path).convert('L')
image = image.point(lambda x: 0 if x<125 else 250, '1')
image.save(save_path)

# Convert the image to txt
custom_oem_psm_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(Image.open(save_path), config=custom_oem_psm_config))
import os
import pytesseract
import enchant
from PIL import Image

english_dict = enchant.Dict("en_US")
image_path = os.path.join(os.getcwd(), "Images/a.jpg")
save_path = os.path.join(os.getcwd(), "Images/grayscale.jpg")

score_tracker = []

for index in range(100):
    print("We are at iteration: ", index)
    # Convert the image to grayscale
    image = Image.open(image_path).convert('L')
    image = image.point(lambda x: 0 if x < (100 + index) else 250, '1')
    image.save(save_path)
    # Convert the image to txt
    custom_oem_psm_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(Image.open(save_path), config=custom_oem_psm_config).split(" ")
    
    score = 0

    for word in text:
        try:
            if english_dict.check(word):
                score += 1
        except:
            print("Something Went Wrong. Continue")
    score_tracker.append(score)

print(score_tracker)

import os
import emoji
from PIL import Image, ImageFont
from pilmoji import Pilmoji
import subprocess

# Get a list containing all the available emojis
emojis = list(emoji.EMOJI_DATA.keys())

print(len(emojis))

for size in [16, 32, 64, 128, 256]:

    directory = f"./png/{size}x{size}"
    os.makedirs(directory, exist_ok=True)

    for e in emojis:

        try:

            filename = f"{directory}/{e}.png"

            if os.path.exists(filename):
                continue

            with Image.new('RGBA', (size, size), (0, 0, 0, 0)) as image:
                font = ImageFont.truetype('Arial.ttf', size)

                with Pilmoji(image) as pilmoji:
                    pilmoji.text((0, 0), e, (0, 0, 0), font)

                # Save the image as a PNG file
                image.save(filename)
        
        except Exception as ex:
            print("Couldn't process emoji: ", e, ex)
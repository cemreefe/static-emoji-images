import os
from jinja2 import Environment, FileSystemLoader
import emoji 

base_dir = './'

images_dir = f"./png/128x128"

# Set the list of emojis
emoji_list = [ file.split('.')[0] for file in os.listdir(images_dir) if not file.startswith(".")]

f = open("gallery.html", "w")

# Set the available image sizes
sizes = ['16x16', '32x32', '64x64', '128x128', '256x256']

# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('jinja-template.html')

# Create a list of dictionaries containing the emoji names and image paths
emojis = []
for emoji in emoji_list:
    emoji_paths = {}
    for size in sizes:
        emoji_path = os.path.join(base_dir, 'png', size, f'{emoji}.png')
        if os.path.exists(emoji_path):
            emoji_paths[size] = emoji_path
    emojis.append({'name': emoji, 'paths': emoji_paths})

# Render the HTML template with the emoji data
html = template.render(emojis=emojis, sizes=sizes)

# Save the generated HTML file
with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
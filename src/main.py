from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

with open('players.csv', newline='') as players:
    for line in players:
        player = line.strip().split(',')
        if len(player) < 3:
            continue  # Skip lines that don't have enough data
        name, character, skin = player[0], player[1], player[2]
        
        # Load the character image
        character = Image.open(f'assets/{character}-{skin}.png')
        
        # Load the font
        font = ImageFont.truetype("assets/warownia-black-narrow.ttf", 64)
        
        # Draw the text on the image
        draw = ImageDraw.Draw(character)
        draw.text((20, 300), f'{name}', (255, 255, 255), font=font)
        
        # Save the modified image
        character.save(f'../output/doombox_{name}.png')

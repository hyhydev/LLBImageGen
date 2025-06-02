import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# if an output directory does not exist, create it
if not os.path.exists('../output'):
  os.makedirs('../output')

with open('players.csv', newline='') as players:
  for line in players:
    player = line.strip().split(',')
    if len(player) < 3:
      continue  # Skip lines that don't have enough data
    name, character_name, skin_name = player[0], player[1], player[2]

    print(f'Processing {name} with character {character_name} and skin {skin_name}')
    
    # Load the character image
    try:
      character = Image.open(f'assets/{character_name}/{character_name}_{skin_name}.png')
    except FileNotFoundError:
      print(f"Character image for {name} not found: assets/{character_name}/{character_name}_{skin_name}.png")
      continue

    # Create a semi-transparent overlay
    overlay = Image.new('RGBA', character.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle((0, 300, 400, 400), fill=(0, 0, 0, 60))

    # Composite the overlay onto the character image
    character = character.convert('RGBA')  # Ensure character image is in RGBA mode
    character = Image.alpha_composite(character, overlay)
    
    # Load the font
    fontsize = 80
    font = ImageFont.truetype("assets/warownia-black-narrow.ttf", fontsize)
    
    # Draw the text on the image
    draw = ImageDraw.Draw(character)

    while (width := font.getlength(f'{name}')) > 400:
      fontsize -= 1
      font = ImageFont.truetype("assets/warownia-black-narrow.ttf", fontsize)

    text_bbox = draw.textbbox((0, 0), f'{name}', font=font)
    text_height = text_bbox[3] - text_bbox[1]

    xoffset = (400 - width) // 2
    yoffset = 300 + (40 - text_height) // 2

    draw.text((xoffset+6, yoffset+6), f'{name}', (0, 0, 0), font=font)
    draw.text((xoffset, yoffset), f'{name}', (255, 255, 255), font=font)
    
    # Save the modified image
    character.save(f'../output/{character_name}_{name}.png')

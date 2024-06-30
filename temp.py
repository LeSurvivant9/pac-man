from PIL import Image

# Chargement du spritesheet d'origine
original_image = Image.open("maze_sprites.png")

# Dimensions des sprites et du nouveau spritesheet
sprite_width, sprite_height = 8, 8
sprites_per_row = 6
padding = 1
total_sprites = 30
rows = total_sprites // sprites_per_row

# Dimensions du nouveau spritesheet
new_width = sprites_per_row * (sprite_width + padding) - padding
new_height = rows * (sprite_height + padding) - padding

# Création de la nouvelle image
new_image = Image.new("RGBA", (new_width, new_height))

# Copie des sprites dans la nouvelle image
for i in range(total_sprites):
    sprite = original_image.crop((i * sprite_width, 0, (i + 1) * sprite_width, sprite_height))
    new_x = (i % sprites_per_row) * (sprite_width + padding)
    new_y = (i // sprites_per_row) * (sprite_height + padding)
    new_image.paste(sprite, (new_x, new_y))

# Sauvegarde du nouveau spritesheet
new_image.save("new_spritesheet.png")

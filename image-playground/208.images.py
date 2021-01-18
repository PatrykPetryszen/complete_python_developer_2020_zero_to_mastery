from PIL import Image, ImageFilter

img = Image.open('/Users/p.petryszen/Documents/VsCode/complete_python_developer_2020_zero_to_mastery/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.png', 'png')
from PIL import Image, ImageFilter

img = Image.open('/Users/p.petryszen/Documents/VsCode/complete_python_developer_2020_zero_to_mastery/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L') # Set to black & white
filtered_img = img.rotate(68).save('rotated.png', 'png')
# filtered_img.show()
resize = img.resize((300, 300))
resize.save('resized.png', 'png')
resize.show()
box = (100, 100, 400, 400)
resize = img.crop(box)
resize.save('cropped.png', 'png')
# filtered_img.save("blur.png", 'png')
from PIL import Image, ImageFilter

img = Image.open('/Users/p.petryszen/Documents/VsCode/complete_python_developer_2020_zero_to_mastery/image-playground/Pokedex/pikachu.jpg')

print(img.size)
print(img.mode)
print(dir(img))
print(img.getpixel)

filtered_img = img.filter(ImageFilter.BLUR) #SHARPEN, SMOOTH
filtered_img.save('blur.png', 'png' )
filtered_img.show()
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpen.png', 'png' )
filtered_img.show()
filtered_img = img.convert('L')
filtered_img.save('grey.png')
filtered_img.show()

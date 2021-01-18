from PIL import Image, ImageFilter

img = Image.open('/Users/p.petryszen/Documents/VsCode/complete_python_developer_2020_zero_to_mastery/image-playground/astro.jpg')
print(img.size)
new_img = img.resize((400, 200)) #If we resize big image it would be squished up 
new_img.save('thumbnail.jpg')
new_img.show()
img.thumbnail((400,200)) #thumbnail method doesn't return any image it edits the current one 
img.save('better_thumbnail.jpg') #thumbnail keeps the aspect ratio
img.show()
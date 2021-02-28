from PIL import Image

im = Image.open('Images/original_input.png')
width, height = im.size

scaling = input('Downscaling factor:')

scalingint = int(scaling)


widthnew = int(width/scalingint)
heightnew = int(height/scalingint)

new_im = im.resize((widthnew, heightnew))
new_im.save('Images/input_rescaled.png')

print(im.size)
print(new_im.size)

print('done')
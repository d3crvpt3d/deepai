from PIL import Image

im = Image.open('Images/original_input.png')
width, height = im.size

scaling = input('Downscaling factor:')

new_im = im.resize(( int(width/scaling), int(height/scaling) ))
new_im.save('Images/input_rescaled.png')

print(im.size)
print(new_im.size)

print('done')
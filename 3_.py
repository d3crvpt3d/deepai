from PIL import Image

file = open('tmp/test_output.ai_rgba','r')

im = Image.open('Images/original_input.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())

inputs = []
weight = []

output = []
for i in inputs:
    if i > 0:
        output.append(i)
    else:
        output.append(0)

print(output)

file.close

print('done')
from PIL import Image

im = Image.open('Images/input_rescaled.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())

print(im.mode)

x=0
y=0

done=False

file = open('tmp/test_output.ai_rgba','w')

tmp_values =''

while(done!=True):
    tmp_values = tmp_values + str(pixel_values[x+y])
    x=x+1
    if(x>=width):
        x=0
        file.write( tmp_values+'\n' )
        y=y+1
        tmp_values = ''
        if(y>=height):
            done=True

file.close

print('done')
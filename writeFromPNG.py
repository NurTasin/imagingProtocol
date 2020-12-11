from PIL import Image
im=Image.open("mkbhd.jpg")
im=im.convert("RGBA")


height=im.size[1]
width=im.size[0]

code = bytearray([])
for y in range(height):
	for x in range(width):
		r,g,b,a= im.getpixel((x,y))
		code= code + bytearray([r,g,b,a])

if height>255 and width>255:
    code = bytearray([(height^0b100000000),height>>8,(width^0b100000000),width>>8])+code
    print([(height^0b100000000),height>>8,(width^0b100000000),width>>8])
elif height>255:
    code = bytearray([(height^0b100000000),height>>8,width,0])+code
    print([(height^0b100000000),height>>8,width,0])
elif width>255:
    code = bytearray([height,0,(width^0b100000000),width>>8])+code
    print([height,0,(width^0b100000000),width>>8])
else:
    code = bytearray([height,0,width,0])+code
    print([height,0,width,0])

with open("mkbhdFullOptimized.bin","wb+") as file:
    file.write(code)
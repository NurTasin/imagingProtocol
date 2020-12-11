height=60
width=30

code=bytearray([255,0,0]*10*30)
code = code + bytearray([0,255,0]*10*30)
code = code + bytearray([0,0,255]*10*30)
code = code + bytearray([255,255,0]*10*30)
code = code + bytearray([255,0,255]*10*30)
code = code + bytearray([0,255,255]*10*30)

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

with open("exmpl60x30.bin","wb+") as file:
    file.write(code)
            

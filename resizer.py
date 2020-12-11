from PIL import Image
size_120=(480,480)
i=Image.open("CaptainAmerica.png")
i.thumbnail(size_120)
i.save("CaptainAmerica480x480.png")
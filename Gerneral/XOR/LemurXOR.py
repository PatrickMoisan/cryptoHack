from PIL import Image, ImageChops
pic1 = Image.open("/Users/patrickmoisan/Desktop/py /code\/cryptoHack-2/lemur.png")
pic2 = Image.open("/Users/patrickmoisan/Desktop/py /code\/cryptoHack-2/flag.png")
pic3 = ImageChops.add(ImageChops.subtract(pic2, pic1), ImageChops.subtract(pic1, pic2))
pic3.show()
pic3.save("/Users/patrickmoisan/Desktop/py /code/\cryptoHack-2/pic3.png")
from PIL import Image
mac = Image.open('example.jpg')
#print(type(mac))
#mac.show()
print(mac.size)
print(mac.format_description)
mac.crop((0,0,100,100)).show()
from PIL import Image

print "Enter Image Address"

addr=raw_input()
img = Image.open(addr)
img.show()

print "Enter X dimension"
x=int(raw_input())
print "Enter Y dimension"
y=int(raw_input())

size = x,y


im_resized = img.resize(size, Image.ANTIALIAS)
im_resized.save("image_resized.png", "PNG")

print "Image Converted"

from pyx import *
from PIL import Image

# Set the image resolution
im = Image.new("RGB", (1000, 1000))

# (x0, y0) denote centre of the circle
# r denotes radius of circle

def draw_circle(r, x0 = 0, y0 = 0):
# WARNING :- Please ensure that you select appropraite values for
# the x0, y0 and r so as to not cause index error. 
# The circle should lie within the image.
# Remember that an image is a 2D matrix .
	x = r - 1
	y = 0
	dx = 1
	dy = 1
	e = dx - (r << 1)

	while x >= y:
    
    # We exploit the symmetry of the circle
    # For sake of simplicity consider a circle centered at the origin
    # A circle centered at origin is symmetric about x axis, y axis
    # and about lines y = x and y = -x. This divides the circle regions into 
    # 8 octants. Moreover due to symmetry, what is true in any one octant 
    # will be true in other octants as well.
    
		im.putpixel((x0 + x, y0 + y),(255, 0, 0))
		im.putpixel((x0 + y, y0 + x),(255, 0, 0))
		im.putpixel((x0 - x, y0 + y),(255, 0, 0))
		im.putpixel((x0 - y, y0 + x),(255, 0, 0))
		im.putpixel((x0 - x, y0 - y),(255, 0, 0))
		im.putpixel((x0 - y, y0 - x),(255, 0, 0))
		im.putpixel((x0 + x, y0 - y),(255, 0, 0))
		im.putpixel((x0 + y, y0 - x),(255, 0, 0))

		if(e <= 0):
			y += 1
			e += dy
			dy += 2

		if(e > 0):
			x -= 1
			dx += 2
			e += dx - (r << 1)

draw_circle(256,500,500)

# Get the image in your directory in the following three formats
c = canvas.canvas()
c.insert(bitmap.bitmap(0, 0, im, height=0.8))
c.writeEPSfile("pil")
c.writePDFfile("pil")
c.writeSVGfile("pil")

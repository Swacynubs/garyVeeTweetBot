"""
File: tweetGen.py
Purpose: Generate fake tweets of Gary Vee for Stinky's Meme Stock Market Bot
Created: April 6th 2022
"""

from PIL import Image, ImageDraw, ImageFont

text1 = 'Create img'
text2 = 'With Python'

img_name = 'garyvee.png'

color = 'dark_blue' #grey,light_blue,blue,orange,purple,yellow,green

font = 'Roboto-Bold.ttf'

myImg = Image.open(img_name)

text = "Hello World"

draw = ImageDraw.Draw(myImg)
draw.text((10,10), "Hello World", fill=(255,255,0))
width,height = draw.textsize(text)

print(width)
print(height)

#myImg.show()


def createTweet(tweetText="No TEXT"):
	veeProfilePic = Image.open('images/veeProfilePic.png')
	draw = Image.new('RGB',(500,500), color = 'white')
	

	drawing = ImageDraw.Draw(draw)
	textW,textH = drawing.textsize(tweetText)
	vPPWidth,vPPHeight = veeProfilePic.size
	print("Width of text:",textW)
	print("Height of text:",textH)
	print("Width of PP:",vPPWidth)
	print("Height of PP:",vPPHeight)

	draw.paste(veeProfilePic)	



	drawing.text((100,100), tweetText,fill=(0,0,0))

	draw.show()


	pass

createTweet("Hello world! This text is awesome!")




def center_text(img,font,text1,text2,fill1,fill2):
    draw = ImageDraw.Draw(img) # Initialize drawing on the image
    w,h = img.size # get width and height of image
    t1_width, t1_height = draw.textsize(text1, font) # Get text1 size
    t2_width, t2_height = draw.textsize(text2, font) # Get text2 size
    p1 = ((w-t1_width)/2,h // 3) # H-center align text1
    p2 = ((w-t2_width)/2,h // 3 + h // 5) # H-center align text2
    draw.text(p1, text1, fill=fill1, font=font) # draw text on top of image
    draw.text(p2, text2, fill=fill2, font=font) # draw text on top of image
    return img

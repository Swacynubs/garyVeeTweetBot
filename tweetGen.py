"""
File: tweetGen.py
Purpose: Generate fake tweets of Gary Vee for Stinky's Meme Stock Market Bot
Created: April 6th 2022
"""
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import random
import markovify

# text1 = 'Create img'
# text2 = 'With Python'

# img_name = 'garyvee.png'

# color = 'dark_blue' #grey,light_blue,blue,orange,purple,yellow,green

# font = 'Roboto-Bold.ttf'

# myImg = Image.open(img_name)

# text = "Hello World"

# draw = ImageDraw.Draw(myImg)
# draw.text((10,10), "Hello World", fill=(255,255,0))
# width,height = draw.textsize(text)

# print(width)
# print(height)


#myImg.show()

def getTime():
	now = datetime.time.now()
	print(now)

def checkSizeOfText(tweetText,size=150):

	
	veeProfilePic = Image.open('images/veeProfilePic.png')
	draw = Image.new('RGB',(1000,size), color = 'white')
	
	font2 = ImageFont.truetype("SanFrancisco\\SFUIText\\SFUIText-Regular.otf", size=25)
	font2Bold = ImageFont.truetype("SanFrancisco\\SFUIText\\SFUIText-Semibold.otf", size=25)
	drawing = ImageDraw.Draw(draw)
	textW,textH = drawing.textsize(tweetText)
	vPPWidth,vPPHeight = veeProfilePic.size
	print("Width of text:",textW)
	print("Height of text:",textH)
	print("Width of PP:",vPPWidth)
	print("Height of PP:",vPPHeight)
	print("HH: ", size)
	

	#Check size
	widthFont2 = font2.getlength(tweetText)
	print("W:",widthFont2)
	# if widthFont2 > vPPWidth:
	# 	print("text too big")
	

	draw.paste(veeProfilePic)	

	offset=100
	# wrapText(draw,tweetText,font2)
	lines = textwrap.wrap(tweetText, width=65)
	print("len:",len(lines))
	for line in lines:
		drawing.text((110,offset), line, fill=(0,0,0), font=font2)
		offset+=35
	returnSize = size
	print("OFFSET!",offset,"| SIZE:",size)
	#Check if the text is too big and we need to make the picture bigger
	if(offset+125 > size):
		returnSize = checkSizeOfText(tweetText,size+50)
	return returnSize

def createTweet(tweetText="No TEXT",size=400):



	veeProfilePic = Image.open('images/veeProfilePic.png')
	draw = Image.new('RGB',(1000,size), color = 'white')
	
	font2 = ImageFont.truetype("SanFrancisco\\SFUIText\\SFUIText-Regular.otf", size=25)
	font2Bold = ImageFont.truetype("SanFrancisco\\SFUIText\\SFUIText-Semibold.otf", size=25)
	drawing = ImageDraw.Draw(draw)
	textW,textH = drawing.textsize(tweetText)
	vPPWidth,vPPHeight = veeProfilePic.size
	# print("Width of text:",textW)
	# print("Height of text:",textH)
	# print("Width of PP:",vPPWidth)
	# print("Height of PP:",vPPHeight)
	
	

	#Check size
	widthFont2 = font2.getlength(tweetText)
	# print("W:",widthFont2)
	# if widthFont2 > vPPWidth:
	# 	print("text too big")
	

	draw.paste(veeProfilePic)	

	offset=100
	# wrapText(draw,tweetText,font2)
	lines = textwrap.wrap(tweetText, width=65)
	for line in lines:
		drawing.text((110,offset), line, fill=(0,0,0), font=font2)
		offset+=35

	#Check if the text is too big and we need to make the picture bigger
	# if(offset > 400):
	# 	print("Too big! Need to resize image")

	heart = Image.open("images/heart.png","r")
	heartW, heartH = heart.size
	
	draw.paste(heart,(95,offset+10))

	#Randomly generate likes
	likes = random.randint(0,1000)
	likesD = random.randint(0,10)
	if(likesD == 0):
		likes = f"{likes}K"
	else:
		likes = f"{likes}.{likesD}K"




	drawing.text((95+heartW,offset+18),likes,fill=(100,100,100),font=font2Bold)
	
	#Spacing for the time
	xBlock = (95+heartW)+len(str(likes)*18)
	now = datetime.now()

	current_time = now.strftime("%I:%M %p")
	current_time += " " + datetime.today().strftime('- %b %d, %Y')




	drawing.text((xBlock,offset+18), current_time ,fill=(100,100,100),font=font2Bold)
	    

	#Border drawing
	drawing.line((0, 0) + (vPPWidth,0), fill=(150,150,150), width = 3)
	drawing.line((0, 0) + (0,offset+25+heartH+5), fill=(150,150,150), width = 2)
	drawing.line((0, offset+25+heartH+5) + (vPPWidth,offset+25+heartH+5), fill=(150,150,150), width = 2)
	drawing.line((vPPWidth, 0) + (vPPWidth,offset+25+heartH+5), fill=(150,150,150), width = 2)


	#Comments section
	offset = offset+25+heartH+5
	commentPic = Image.open('images/comment.png')
	draw.paste(commentPic,(100,offset+10))

	yOffset = commentPic.size[0] + 5
	randomNum = random.randint(0,10000)

	randomString = str(randomNum)
	if(randomNum >= 1000):
		#print("NUM:",randomNum)
		#randomString1 = randomString[0] + ","
		#print("OK:",randomString1)
		#randomString1.join([randomString[x] for x in range(1,len(randomString))])
		randomString = "{:,}".format(randomNum)
	randomString += " people are talking about this"
	drawing.text((100+commentPic.size[1]+10, offset + 10 + 3), randomString, fill=(0,0,200), font=font2)


	#Extra outline
	drawing.line((0, offset) + (0,offset+55), fill=(150,150,150), width = 2)
	drawing.line((0, offset+55) + (vPPWidth,offset+55), fill=(150,150,150), width = 2)
	drawing.line((vPPWidth, offset) + (vPPWidth,offset+55), fill=(150,150,150), width = 2)
	#drawing.line((vPPWidth, 0) + (vPPWidth,offset+18+heartH+5), fill=(150,150,150), width = 2)


	# margin = offset = 40
	# for line in textwrap.wrap(tweetText, width=40):
	#     draw.text((margin, offset), line, font=font, fill=(0,0,0))
	#     offset += font.getsize(line)[1]

	draw.show()
	draw.save("tmp.png")



def generateText():
	with open("GVQuotes.txt", encoding="utf8") as f:
		text = f.read()

	# Build the model.
	text_model = markovify.Text(text)

	#Return a tweet
	return (text_model.make_sentence())


#============================================
# Running the program
#============================================
genText = generateText()
mySize = checkSizeOfText(genText)
genText = "def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):def center_text(img,font,text1,text2,fill1,fill2):"
createTweet(genText,mySize)



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

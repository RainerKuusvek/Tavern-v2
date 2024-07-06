import os
from PIL import Image, ImageFont, ImageDraw

# directories
base_dir = 'C:\\Users\\kuusv\\Desktop\\Tavern V2'
template_dir = base_dir + '\\templates'
current_dir = os.getcwd()

# base dimensions (of playing card. Standard is 64mm x 89mm. Tabletopia is 10 px per mm)
cardwidth = 635
cardheight = 888
margin = [20, 20]
iconSize = [100, 100]


###################################


#Text Widths

titleWidth = 18
descriptionWidth=34
descriptionWidth2=30
halfDescriptionWidth=28
peeveTitleWidth = 20

#Spacings
textSpacingFactor=0.85

#all-use frame
nameFrame = Image.open("{}\\images\\icons\\nameFrame.png".format(base_dir))

bufferSize=300


lvlCoords = (cardwidth - 210, 200)


#Fonts
typeFontSize=40; font_type = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), typeFontSize)
titleTextSize = 90; font_title= ImageFont.truetype(r'{}\\fonts\\dusty.ttf'.format(base_dir), titleTextSize)#ImageFont.truetype(r'{}\\fonts\\dragon.otf'.format(base_dir), titleTextSize)

descriptionTextSize=32; font_description=ImageFont.truetype(r'{}\\fonts\\Frutiger.ttf'.format(base_dir), descriptionTextSize)
townsfolkDescriptionTextSize=40; font_townsfolkDescription=ImageFont.truetype(r'{}\\fonts\\Frutiger.ttf'.format(base_dir), townsfolkDescriptionTextSize)

raceclassTextSize = 40; font_raceclass = ImageFont.truetype(r'{}\\fonts\\western.otf'.format(base_dir), raceclassTextSize)
peeveTitleSize=80; font_peeveTitle = ImageFont.truetype(r'{}\\fonts\\dusty.ttf'.format(base_dir), peeveTitleSize)
peeveDescriptionSize=55; font_peeveDescription = ImageFont.truetype(r'{}\\fonts\\Frutiger.ttf'.format(base_dir), peeveDescriptionSize)
raceclassTextSize = 35;

#Icons
rage = Image.open("{}\\images\\icons\\rageIcon.png".format(base_dir))
fame = Image.open("{}\\images\\icons\\fame.png".format(base_dir))
plus = Image.open("{}\\images\\icons\\plus.png".format(base_dir))
drinkIcon=Image.open("{}\\images\\icons\\drinkIcon.png".format(base_dir))
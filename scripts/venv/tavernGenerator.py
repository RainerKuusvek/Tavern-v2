import numpy as np
import os, sys
from PIL import Image, ImageFont, ImageDraw
import textwrap
import csv
import requests
import googleSheetsInterface
from constants import *


def drawType(type, template):
    #Builds the template, type, and title of a card

    typeCoords = [margin[0], 5]

    cardBase = template.copy()
    I1 = ImageDraw.Draw(cardBase)

    #type
    I1.text([int((cardwidth - font_type.getbbox(type)[2]) * 0.5), typeCoords[1]], type, fill=(10, 10, 10), font=font_type)

    return cardBase


def buildCardStandard(type, template, col):
    #Builds the template, type, and title of a card

    typeCoords = [margin[0], 5]
    titleCoords = [margin[0], margin[1] + 65]

    cardBase = template.copy()
    I1 = ImageDraw.Draw(cardBase)

    #type
    I1.text([int((cardwidth - font_type.getbbox(type)[2]) * 0.5), typeCoords[1]], type, fill=col, font=font_type)
    #title
    text = textwrap.wrap("{}".format(card[1]), width=int(titleWidth))
    for nt in range(len(text)):
        I1.text(np.add(titleCoords, [0, nt * titleTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_title)

    return cardBase


def buildPeeve(card, i):
    if card[9]=="positive":
        cardPNG=Image.open("{}\\goodpeeveTemplate.png".format(template_dir)).copy()
    else:
        cardPNG = Image.open("{}\\badPeeveTemplate.png".format(template_dir)).copy()

    I1 = ImageDraw.Draw(cardPNG)

    peeveTitleCoords = [35, 30]

    # Title
    text = textwrap.wrap("{}".format(card[1]), width=int(peeveTitleWidth))
    for nt in range(len(text)):
        I1.text(np.add(peeveTitleCoords, [0, nt * peeveDescriptionSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_peeveTitle)



    # Description
    peeveDescriptionCoords = [30, 100]
    text = textwrap.wrap("{}".format(card[3]), width=int(22))
    peeveTextSquishFactor = 0.7
    for nt in range(len(text)):
        I1.text(np.add(peeveDescriptionCoords, [0, nt * (peeveDescriptionSize+8) * peeveTextSquishFactor]), text[nt], fill=(10, 10, 10), font=font_peeveDescription)
    rageSize=(66,88)
    alignX=550
    rageCoords=(alignX-int(rageSize[0]*0.25), 25)
    if card[9]=="negative":
        cardPNG.paste(rage.resize(rageSize), rageCoords, rage.resize(rageSize))

    #paste relevant icon
    newIconSize=(50,50)
    iconCoords = (alignX, 210)
    peeveWidth=600
    if card[4] != "null":
        string = card[4].split("/")
        if len(string) != 1:
            step = int((peeveWidth * 0.5) / (len(string) - 1))
        for j in range(len(string)):
            if os.path.isfile("{}\\images\\icons\\{}.png".format(base_dir, string[j])):
                iconPaste = Image.open("{}\\images\\icons\\{}.png".format(base_dir, string[j].lower()))
                xShift=int((j*0.5*newIconSize[0]-len(string)*newIconSize[0]*0.25))
                cardPNG.paste(iconPaste.resize(newIconSize), (iconCoords[0]+xShift, iconCoords[1]), iconPaste.resize(newIconSize))
    '''

    peeveTextSquishFactor = 0.7

    string=card[4].split("/")
    iconSize=(80,80)
    rageSize=(60,80)
    cardSplit=0.0

    #cardPNG.paste(plus.resize(iconSize), (rageCoords[0]-60, rageCoords[1]), plus.resize(iconSize))
    I1.text((rageCoords[0]+40, rageCoords[1]+5), " IF ", fill=(10, 10, 10), font=font_title)

    if card[4]!="null":
        print(string)

        step=int(peeveWidth*0.5)
        if len(string)!=1:
            step = int((peeveWidth*0.5) / (len(string) - 1))

        for j in range(len(string)):
            #xCoord=int(peeveWidth*cardSplit+(1-cardSplit)*peeveWidth*((i+1)/(2*len(string)))-iconSize[0]*0.5)
            xCoord=cardSplit+(1-cardSplit)*j/len(string)
            xCoord=int(peeveWidth*xCoord)+30
            yCoord=rageCoords[1]+110
            #print(string, i, string[0])

            if os.path.isfile("{}\\images\\icons\\{}.png".format(base_dir, string[j])):
                iconPaste=Image.open("{}\\images\\icons\\{}.png".format(base_dir,string[j].lower()))
                cardPNG.paste(iconPaste.resize(iconSize), (xCoord, yCoord),iconPaste.resize(iconSize))

            else:
                length=font_title.getbbox("{}".format(string[j]))[2]
                I1.text((xCoord-int(length*0.1), yCoord), string[j], fill=(10, 10, 10), font=font_title)

    '''
    cardPNG.save("{}\\Results\\peeves\\card_{}.png".format(base_dir, i + 1))


def buildModule(card, i):
    ModuleTemplate = Image.open("{}\\moduletemplate.png".format(template_dir))
    ModuleTemplate2 = Image.open("{}\\moduletemplate2.png".format(template_dir))
    ModuleTemplate3 = Image.open("{}\\moduletemplate3.png".format(template_dir))

    if card[3]=="extra table":
        template=Image.open("{}\\moduletemplate2.png".format(template_dir))
        shift=(140, 100)
        titleWidth=18
        moduleDescriptionWidth = descriptionWidth - 4 - shift[0] * 0.05
    elif card[3]=="coach":
        template = Image.open("{}\\moduletemplate3.png".format(template_dir))
        shift = (140, 100)
        titleWidth=18
        moduleDescriptionWidth=descriptionWidth - 4 - shift[0] * 0.05
    else:
        shift = (50, 30)
        titleWidth=16
        moduleDescriptionWidth = 25

        template = Image.open("{}\\moduletemplate.png".format(template_dir))
    #Builds the template, type, and title of a card
    cardPNG = template.copy()
    I1 = ImageDraw.Draw(cardPNG)

    builderIcon=icon=Image.open("{}\\images\\icons\\builder.png".format(base_dir, card[10])).resize([50,50])
    cardPNG.paste(builderIcon, (570,40), builderIcon)  # add ic

    # type
    I1.text([int((cardwidth - font_type.getbbox("MODULE")[2]) * 0.5), 5], "MODULE", fill=(200, 200, 200),font=font_type)
    # title
    text = textwrap.wrap("{}".format(card[1]), width=int(titleWidth+1))
    coords=(titleCoords[0]+shift[0], titleCoords[1]+shift[1])
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, nt * titleTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10),font=font_title)

    I1 = ImageDraw.Draw(cardPNG)

    #description
    coords=(margin[0]+shift[0], 350+shift[1])
    text = textwrap.wrap("{}".format(card[4]), width=int(moduleDescriptionWidth))
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, nt * townsfolkDescriptionTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_townsfolkDescription)


    #icon
    moduleIconSize=(200,200)
    icon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[8])).resize(moduleIconSize)

    coords=(int(cardwidth*0.5-moduleIconSize[0]*0.5), 550)
    cardPNG.paste(icon, coords, icon)  # add icon



    cardPNG.save("{}\\Results\\visitors\\card_{}.png".format(base_dir, i + 1))


def buildHero(card, i):
    cardPNG=drawType("HERO", Image.open("{}\\herotemplate.png".format(template_dir)))

    I1 = ImageDraw.Draw(cardPNG)

    #type
    #I1.text([int((cardwidth - font_type.getsize("HERO")[0]) * 0.5), typeCoords[1]], "HERO", fill=(10, 10, 10), font=font_type)

    #add character portraits
    portraitAspect=(641,641)
    characterPortrait = Image.open("{}\\images\\characterPortraits\\{}.jpg".format(base_dir, card[1])).convert("RGBA").resize(portraitAspect)
    #characterPortraitJPG.save("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1]))
    #characterPortrait = Image.open("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1])).resize(portraitSize)
    coords=(0, 35)
    portraitSize=(0, 0, 640, 535)
    characterPortrait=characterPortrait.crop(portraitSize)
    cardPNG.paste(characterPortrait, coords, characterPortrait)  # add icon

    #title

    titleCoords = [10, 410]
    text = textwrap.wrap("{}".format(card[1]), width=int(18))
    nameFrameCoords=(0, titleCoords[1]-7)
    backFrame=nameFrame.resize((641, int(110*np.sqrt(len(text)**1.5))))
    cardPNG.paste(backFrame, nameFrameCoords, backFrame)  # add icon

    for nt in range(len(text)):
        spacing=2
        I1.text(np.add(titleCoords, [-spacing, -spacing+nt * titleTextSize * textSpacingFactor]), text[nt], fill=(240, 240, 240), font=font_title)
        I1.text(np.add(titleCoords, [2*spacing, 2*spacing + nt * titleTextSize * textSpacingFactor]), text[nt], fill=(240, 240, 240),font=font_title)
    for nt in range(len(text)):
        I1.text(np.add(titleCoords, [0, nt * titleTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_title)


    font=font_raceclass
    raceIcon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[8])).resize(iconSize)
    classIconSize=(80,80)
    classIcon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[9])).resize(classIconSize)
    I1 = ImageDraw.Draw(cardPNG)
    #write Race
    descriptionCoordsA = (margin[0], 590)
    I1.text(descriptionCoordsA, card[8].upper(), fill=(10, 10, 10), font=font)
    cardPNG.paste(raceIcon, (descriptionCoordsA[0]+bufferSize, descriptionCoordsA[1]+7-int(iconSize[0]*0.15)), raceIcon)  # add icon
    raceLen=font.getbbox('{}'.format(card[8])+'   ')[0]

    #add hero icon
    heroIcon=icon=Image.open("{}\\images\\icons\\hero.png".format(base_dir, card[10])).resize([50,50])
    cardPNG.paste(heroIcon, (570,40), heroIcon)  # add ic

    #write Class

    I1.text([descriptionCoordsA[0], descriptionCoordsA[1]+raceclassTextSize], card[9].upper(), fill=(10, 10, 10), font=font)
    cardPNG.paste(classIcon, (descriptionCoordsA[0]+bufferSize+110, 7+descriptionCoordsA[1]-int(iconSize[0]*0.1)), classIcon)  # add icon

    #add Level
    lvlCoords = (descriptionCoordsA[0]+bufferSize+194, 7+descriptionCoordsA[1]-int(iconSize[0]*0.15))
    lvlScale=0.9;newLvlSize=(int(132*lvlScale), int(99))
    lvlIcon=Image.open("{}\\images\\icons\\lvl{}.png".format(base_dir, card[10])).resize(newLvlSize)
    cardPNG.paste(lvlIcon, lvlCoords, lvlIcon)  # add icon
    shift=font_title.getbbox('{}'.format(card[10]))
    I1.text((lvlCoords[0]+int(newLvlSize[0]*0.5-shift[2]*0.5), lvlCoords[1]+int(+newLvlSize[1]*0.5-shift[3]*0.5)), card[10], fill=(10, 10, 10), font=font_title)

    #Ability
    abilityCoords=(margin[0], 668)
    text = textwrap.wrap("ABILITY (x1    ): {}".format(card[3]), width=int(40))
    for na in range(len(text)):
        I1.text(np.add(abilityCoords, [0, (na + 1) * descriptionTextSize*textSpacingFactor]), text[na],fill=(10, 10, 10), font=font_description)
    drinkSize=(23,23)
    cardPNG.paste(drinkIcon.resize(drinkSize), (abilityCoords[0]+170, abilityCoords[1]+28), drinkIcon.resize(drinkSize),)  # add icon


    #Rage Effects
    rageCoords = (margin[0], 812)
    rageSpacing=15
    cardPNG.paste(rage, (rageCoords[0] + rageSpacing * 3, rageCoords[1]), rage)  # add icon
    cardPNG.paste(rage, (rageCoords[0] + rageSpacing * 2, rageCoords[1]), rage)  # add icon
    cardPNG.paste(rage, (rageCoords[0] + rageSpacing, rageCoords[1]), rage)  # add icon

    text = textwrap.wrap("{}".format(card[4]), width=int(35))
    for nr1 in range(len(text)):
        I1.text(np.add(rageCoords, [90, (nr1) * descriptionTextSize * textSpacingFactor]), text[nr1], fill=(10, 10, 10), font=font_description)




    cardPNG.save("{}\\Results\\visitors\\card_{}.png".format(base_dir, i + 1))


def buildQuest(card, i):

    cardPNG = buildCardStandard("QUESTGIVER", Image.open("{}\\questtemplate.png".format(template_dir)), (200, 200, 200))
    I1 = ImageDraw.Draw(cardPNG)
    questIconSize=(50,50)
    questIcon=Image.open("{}\\images\\icons\\questgiver.png".format(base_dir)).resize(questIconSize)
    cardPNG.paste(questIcon, (570,40),questIcon)

    '''
    titleCoords = [margin[0], margin[1] + 65]

    I1 = ImageDraw.Draw(cardPNG)

    #title
    text = textwrap.wrap("{}".format(card[1]), width=int(40))
    for nt in range(len(text)):
        I1.text(np.add(titleCoords, [0, nt * titleTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_title)
    '''


    #bufferSize=200
    #Requirements
    classCoords=(margin[0], 460)
    for iClass in range(2):
        classIcon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[8+iClass])).resize(iconSize)
        strLen=font_description.getbbox("{}".format(card[8+iClass].upper()))
        xCoord=int(cardwidth*(0.25+0.5*iClass)-iconSize[0]*0.5)
        yCoord=classCoords[1]
        cardPNG.paste(classIcon, (xCoord, yCoord + raceclassTextSize), classIcon)  # add icon
        #print("Card: ", card[1],  ", Class: ", card[8+iClass],", Cardwidth: ", cardwidth, ", Text Length: ", font_description.getbbox("{}".format(card[8+iClass]))[2], ", Coord:, ", iClass*cardwidth*0.5+cardwidth*0.25-int(0.5*font_description.getbbox("{}".format(card[8+iClass]))[2]))

        I1.text((xCoord-int(0.25*font_description.getbbox("{}".format(card[8+iClass]))[2]), yCoord), "{}".format(card[8+iClass]).upper(), fill=(10, 10, 10), font=font_description)

    #Questgiver Race
    raceIcon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[5])).resize(iconSize)
    raceCoords=(margin[0], 350)
    I1.text([raceCoords[0], raceCoords[1]], 'Questgiver: {}  '.format(card[5]),fill=(10, 10, 10), font=font_raceclass)
    cardPNG.paste(raceIcon, (int(cardwidth-bufferSize*0.4), int(raceCoords[1]-iconSize[1]*0.4)), raceIcon)  # add icon

    #lvl1Reward
    fameIconSize = 70
    lvl1RewardCoords=(margin[0]+20, 710)
    I1.text(lvl1RewardCoords, '1-HERO REWARD: ', fill=(10, 10, 10), font=font_raceclass)
    cardPNG.paste(fame.resize((fameIconSize, fameIconSize)), (int(cardwidth-bufferSize*0.3), int(lvl1RewardCoords[1]-fameIconSize*0.25)), fame.resize((fameIconSize, fameIconSize)))  # add icon
    I1.text((lvl1RewardCoords[0]+font_raceclass.getbbox('1-HERO REWARD     ')[2], lvl1RewardCoords[1]-20), '{}'.format(card[3]), fill=(10, 10, 10), font=font_title)




    #lvl2Reward
    lvl2RewardCoords=(lvl1RewardCoords[0], lvl1RewardCoords[1]+80)
    I1.text(lvl2RewardCoords, '2-HERO REWARD: ', fill=(10, 10, 10), font=font_raceclass)
    cardPNG.paste(fame.resize((fameIconSize, fameIconSize)), (int(cardwidth-bufferSize*0.3), int(lvl2RewardCoords[1]-fameIconSize*0.25)), fame.resize((fameIconSize, fameIconSize)))  # add icon
    I1.text((lvl2RewardCoords[0]+font_raceclass.getbbox('2-HERO REWARD     ')[2], lvl2RewardCoords[1]-20), '{}'.format(card[4]), fill=(10, 10, 10), font=font_title)

    cardPNG.save("{}\\Results\\visitors\\card_{}.png".format(base_dir, i + 1))


def buildTownsfolk(card, i, j):
    cardPNG=buildCardStandard("TOWNSFOLK", Image.open("{}\\townsfolkTemplate.png".format(template_dir)), (10, 10, 10))
    I1 = ImageDraw.Draw(cardPNG)

    #name
    coords = (margin[0], 250)
    names=card[8].split('/')
    I1.text((coords[0], coords[1]), names[j%len(names)], fill=(10, 10, 10), font=font_townsfolkDescription)

    # Description
    coords=(margin[0], 300)
    I1.text(coords, 'DESCRIPTION: ', fill=(10, 10, 10), font=font_townsfolkDescription)
    text = textwrap.wrap("{}".format(card[4]), width=int(30))
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, (1+nt) * townsfolkDescriptionTextSize * textSpacingFactor]),text[nt], fill=(10, 10, 10), font=font_townsfolkDescription)

    # Type
    coords=(coords[0], coords[1]+200)
    I1.text(coords, 'TYPE: ', fill=(10, 10, 10), font=font_townsfolkDescription)
    coords = (coords[0], coords[1] + 50)
    I1.text((coords[0], coords[1]), card[3], fill=(10, 10, 10), font=font_townsfolkDescription)
    typeIcon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[3])).resize(iconSize)
    cardPNG.paste(typeIcon, (coords[0]+bufferSize+40, int(coords[1]-0.25*iconSize[1])),typeIcon)  # add icon

    #  donation Rewards
    fameSize=(30, 30)
    coords = (coords[0], coords[1] + 200)
    cardPNG.paste(fame.resize(fameSize), (coords[0]  + 120, coords[1]+35), fame.resize(fameSize))  # add icon
    text = textwrap.wrap("Fame (   ) reward when donated to town un-enraged: {}".format(card[7]), width=int(30))
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, (1+nt) * townsfolkDescriptionTextSize * textSpacingFactor]),text[nt], fill=(10, 10, 10), font=font_townsfolkDescription)

    cardPNG.save("{}\\Results\\townsfolk\\card_{}.png".format(base_dir, i + 1))


def buildSeason(card, i):
    cardPNG=buildCardStandard("SEASON", Image.open("{}\\seasonsTemplate.png".format(template_dir)), (10, 10, 10))
    I1 = ImageDraw.Draw(cardPNG)


    portraitAspect=(641,641)
    seasonPortrait = Image.open("{}\\images\\seasonImages\\{}.jpg".format(base_dir, card[1])).convert("RGBA").resize(portraitAspect)
    #characterPortraitJPG.save("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1]))
    #characterPortrait = Image.open("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1])).resize(portraitSize)
    coords=(0, 35)
    portraitSize=(0, 0, 640, 535)


    seasonPortrait=seasonPortrait.crop(portraitSize)
    cardPNG.paste(seasonPortrait, coords, seasonPortrait)  # add icon

    text = textwrap.wrap("{}".format(card[1]), width=int(20))
    seasonLabel = Image.open("{}\\images\\icons\\seasonLabel.png".format(base_dir)).convert("RGBA").resize(portraitAspect).resize((cardwidth+10, 80*len(text)))
    cardPNG.paste(seasonLabel, (0,95), seasonLabel)  # add icon
    seasonTitleCoord=(margin[0], 100)
    for nt in range(len(text)):
        I1.text(np.add(seasonTitleCoord, [0, nt * titleTextSize * textSpacingFactor]), text[nt], fill=(10, 10, 10), font=font_title)



    # Description
    descriptionCoords=(margin[0], 580)
    text = textwrap.wrap("{}".format(card[4]), width=int(descriptionWidth2))
    for nt in range(len(text)):
        I1.text(np.add(descriptionCoords, [0, nt * townsfolkDescriptionTextSize * textSpacingFactor]), text[nt],fill=(10, 10, 10), font=font_townsfolkDescription)

    #Number of visitors
    coords=(margin[0], descriptionCoords[1]+100)

    I1.text([coords[0], coords[1]], 'NUMBER OF VISITORS TODAY: '.format(card[5]), fill=(10, 10, 10), font=font_raceclass)
    I1.text([int((cardwidth - font_title.getbbox('5')[2]) / 2), coords[1] + 40],'{}    ({})'.format(card[5], card[10]), fill=(10, 10, 10), font=font_title)

    coords=(coords[0], coords[1]+120)

    spacing=120
    iconSize=(120,120)
    if card[8] != "null":
        affectList = card[8].split("/")
        for ri in range(len(affectList)):
            circle=Image.open("{}\\images\\icons\\circle.png".format(base_dir)).resize(iconSize)
            cardPNG.paste(circle.resize(iconSize), (coords[0] + ri*spacing, int(coords[1]-390+iconSize[0]*0.25)),circle.resize(iconSize))  # add icon

        for ri in range(len(affectList)):
            I1.text((coords[0], coords[1]+ri*40), affectList[ri], fill=(10, 10, 10), font=font_description)
            icon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, affectList[ri])).resize(iconSize)
            cardPNG.paste(icon.resize(iconSize), (coords[0] + ri*spacing, int(coords[1]-390+iconSize[0]*0.25)),icon.resize(iconSize))  # add icon
    cardPNG.save("{}\\Results\\seasons\\card_{}.png".format(base_dir, i + 1))

'''
def buildUpgrade(card, i):
    cardPNG=buildCardStandard("TOWN UPGRADE", Image.open("{}\\upgradeTemplate.png".format(template_dir)), (10, 10, 10))
    I1 = ImageDraw.Draw(cardPNG)

    # Description
    descriptionCoords=(margin[0], 550)
    text = textwrap.wrap("{}".format(card[4]), width=int(descriptionWidth))
    for nt in range(len(text)):
        I1.text(np.add(descriptionCoords, [0, nt * descriptionTextSize * textSpacingFactor]), text[nt],fill=(10, 10, 10), font=font_townsfolkDescription)

    spacing=80
    textSize = 50;

    #Instruction
    coords=(margin[0], 600)
    text = textwrap.wrap("{}".format(card[5]), width=int(descriptionWidth2))
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, nt * townsfolkDescriptionTextSize * textSpacingFactor]), text[nt],fill=(10, 10, 10), font=font_townsfolkDescription)

    #Description
    coords=(margin[0], 700)
    text = textwrap.wrap("{}".format(card[3]), width=int(descriptionWidth2))
    for nt in range(len(text)):
        I1.text(np.add(coords, [0, nt * townsfolkDescriptionTextSize * textSpacingFactor]), text[nt],fill=(10, 10, 10), font=font_townsfolkDescription)


    iconDims=(300,300)
    coords=(int(cardwidth*0.5-iconDims[0]*0.5), 200)
    icon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[4])).resize((iconDims))
    cardPNG.paste(icon, (coords[0], coords[1]),icon)  # add ic


    cardPNG.save("{}\\Results\\visitors\\card_{}.png".format(base_dir, i + 1))
'''

def buildTownUpgrade(card, i):

    if card[5]!="null":
        cardPNG = drawType("TOWN UPGRADE", Image.open("{}\\notablesTemplate.png".format(template_dir)))
    else:
        cardPNG = drawType("TOWN UPGRADE", Image.open("{}\\notablesTemplate2.png".format(template_dir)))
    #cardPNG=drawType("TOWN UPGRADE", Image.open("{}\\notablesTemplate.png".format(template_dir)))
    I1 = ImageDraw.Draw(cardPNG)


    #townsfolkImage
    portraitAspect=(641,641)
    characterPortrait = Image.open("{}\\images\\upgradeImages\\{}.jpg".format(base_dir, card[1])).convert("RGBA").resize(portraitAspect)
    #characterPortraitJPG.save("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1]))
    #characterPortrait = Image.open("{}\\images\\characterPortraits\\{}.png".format(base_dir, card[1])).resize(portraitSize)
    coords=(0, 35)
    imageDims=(0, 50, 640, 520)
    characterPortrait=characterPortrait.crop(imageDims)
    cardPNG.paste(characterPortrait, coords, characterPortrait)  # add icon


    #name
    titleCoords = (margin[0], 520)
    text = textwrap.wrap("{}".format(card[1]), width=int(18))
    for nt in range(len(text)):
        I1.text(titleCoords, text[nt], fill=(10, 10, 10), font=font_title)



    #if owner exists
    iconDims=(80,80)
    ownerIcon=icon=Image.open("{}\\images\\icons\\benefactorIcon.png".format(base_dir, card[4])).resize((iconDims))
    typeIcon=icon=Image.open("{}\\images\\icons\\{}.png".format(base_dir, card[10])).resize((iconDims))

    ownerLabel=icon=Image.open("{}\\images\\icons\\benefactorLabel.png".format(base_dir, card[10]))
    ownerLoc=(455, 375)

    if card[5]!="null":
        cardPNG.paste(ownerLabel, [ownerLoc[0] -5, ownerLoc[1] -3], ownerLabel)  # add ic
        I1.text(ownerLoc, 'Benefactor', fill=(10, 10, 10), font=font_townsfolkDescription)
        cardPNG.paste(ownerIcon, [ownerLoc[0] + 45, ownerLoc[1] + 40], ownerIcon)  # add ic

    ### Writing
    # EFFECT WHEN DRAWN
    descriptionWidth = 40

    typeCoords=(545,520)
    cardPNG.paste(typeIcon, typeCoords, typeIcon)  # add ic

    # Action Effect
    coords = (margin[0], 580)
    text = textwrap.wrap("EFFECT: {}".format(card[3]), width=int(descriptionWidth))
    for na in range(len(text)):
        I1.text(np.add(coords, [0, (na + 1) * townsfolkDescriptionTextSize * textSpacingFactor]), text[na],fill=(10, 10, 10), font=font_description)


    '''
    if (card[5]!="null") and (card[5]!="static") :
        text = textwrap.wrap("EFFECT WHEN DRAWN:\n{}".format(card[5]), width=int(descriptionWidth))
        for na in range(len(text)):
            I1.text(np.add(coords, [0, (na + 1) * townsfolkDescriptionTextSize * textSpacingFactor]), text[na],fill=(10, 10, 10), font=font_description)
    
    # ACTIVATION CONDITION AND EFFECT
    coords=(coords[0], coords[1]+100)
    text = textwrap.wrap("ACTIVATION CONDITION:\n{}".format(card[7]), width=int(descriptionWidth))
    for na in range(len(text)):
        I1.text(np.add(coords, [0, (na + 1) * townsfolkDescriptionTextSize * textSpacingFactor]), text[na],fill=(10, 10, 10), font=font_description)
    '''
    # SPECIAL RULES
    coords=(coords[0], 710)
    if card[5]!="null":
        text = textwrap.wrap("SPECIAL RULES: \n{}".format(card[7]), width=int(descriptionWidth))
        for na in range(len(text)):
            I1.text(np.add(coords, [0, (na + 1) * townsfolkDescriptionTextSize * textSpacingFactor]), text[na],fill=(10, 10, 10), font=font_description)




    cardPNG.save("{}\\Results\\visitors\\card_{}.png".format(base_dir, i + 1))






if __name__ == "__main__":
    # import database
    cards = googleSheetsInterface.csv_from_google_sheet("https://docs.google.com/spreadsheets/d/1dwU_Z0NAUDviUeKY2951i9sxRpVGj7BZ2jmJZL2bP9M/edit#gid=1154421056")[2:]

    ######   Remove Existing Results   ######
    for f in os.listdir("{}\\results\\peeves".format(base_dir)):
        os.remove("{}\\results\\peeves\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\seasons".format(base_dir)):
        os.remove("{}\\results\\seasons\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\visitors".format(base_dir)):
        os.remove("{}\\results\\visitors\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\townsfolk".format(base_dir)):
        os.remove("{}\\results\\townsfolk\\{}".format(base_dir, f))


    # mysterious shift factors
    shiftFactor = 0.8

    # cardLocations
    #peeveTitleCoords = [35, 35]
    titleCoords = [margin[0], margin[1] + 65]
    typeCoords = [margin[0], margin[1] + 10]
    cardShift = 20
    raceCoords = (margin[0], 250 + cardShift)
    raceCoordsTownsfolk = (margin[0], 180)
    classCoords = (margin[0] + 150, raceCoords[1])
    descriptionCoords = (margin[0], 450 + cardShift)
    abilityCoords = (margin[0], 420 + cardShift)
    townsfolkDescriptionCoords = (margin[0], 360 + cardShift)

    rage1Coords = (margin[0], int(abilityCoords[1] + 210))
    rage2Coords = (margin[0], int(abilityCoords[1] + 280))
    notableIconCoords = (margin[0] + 180, 150)
    alignmentCoords = (margin[0] + 300, 270)
    townsfolkTypeCoords = (margin[0] + 180, 120)


    peeveDescriptionCoords = [30, 120]
    ###########################

    # mysterious shift factors

    # for every card
    i=0
    for card in (cards):
        print(card[1], card[6])
        print(card)
        '''
        if int(card[0])==10:
            exit()
        '''
        for j in range(int(card[6])):
            if card[2]=='peeve':
                buildPeeve(card, i)
            if card[2]=='module':
                buildModule(card, i)
            if card[2]=='Hero':
                buildHero(card, i)
            if card[2]=='Quest':
                buildQuest(card, i)
            if card[2]=='season':
                buildSeason(card, i)
            if card[2]=='townUpgrade':
                buildTownUpgrade(card, i)
            if card[2]=='townsfolk':
                buildTownsfolk(card, i, j)
            i=i+1



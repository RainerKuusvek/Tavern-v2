import numpy as np
import os, sys
from PIL import Image, ImageFont, ImageDraw
import textwrap
import csv


if __name__==    "__main__":

    #directories
    base_dir='C:\\Users\\kuusv\\Desktop\\Tavern V2'
    template_dir=base_dir+'\\templates'
    current_dir=os.getcwd()

    #import database
    cards=np.loadtxt(base_dir+'\\databases\\taverncards.csv',delimiter=",", dtype=str, skiprows=2)

    #base dimensions (of playing card. Standard is 64mm x 89mm. Tabletopia is 10 px per mm)
    cardwidth=635
    cardheight=888
    margin=[30, 30]
    iconSize=[100, 100]

    #Score Dictionary
    scoreDict={"warrior":2,
               "priest":3,
               "troubadour":3,
               "bandit":4,
               "champion":5,
               "mage":5,
               "cultist":6}

    # remove all existing
    for f in os.listdir("{}\\results\\peeves".format(base_dir)):
        os.remove("{}\\results\\peeves\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\seasons".format(base_dir)):
        os.remove("{}\\results\\seasons\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\visitors".format(base_dir)):
        os.remove("{}\\results\\visitors\\{}".format(base_dir, f))
    for f in os.listdir("{}\\results\\townsfolk".format(base_dir)):
        os.remove("{}\\results\\townsfolk\\{}".format(base_dir, f))


    #open template
    HeroTemplate = Image.open("{}\\herotemplate.png".format(template_dir))
    townsfolkTemplate=Image.open("{}\\townsfolkTemplate.png".format(template_dir))
    ModuleTemplate=Image.open("{}\\moduletemplate.png".format(template_dir))
    ModuleTemplate2=Image.open("{}\\moduletemplate2.png".format(template_dir))
    ModuleTemplate3=Image.open("{}\\moduletemplate3.png".format(template_dir))
    Questtemplate=Image.open("{}\\questtemplate.png".format(template_dir))
    NotableTemplate=Image.open("{}\\notablesTemplate.png".format(template_dir))
    seasonsTemplate=Image.open("{}\\seasonsTemplate.png".format(template_dir))
    goodPeeveTemplate = Image.open("{}\\goodpeeveTemplate.png".format(template_dir))
    badPeeveTemplate = Image.open("{}\\badpeeveTemplate.png".format(template_dir))


    ### open icons
        #races
    human=Image.open("{}\\images\\icons\\human.png".format(base_dir))
    dwarf=Image.open("{}\\images\\icons\\dwarf.png".format(base_dir))
    goblin=Image.open("{}\\images\\icons\\goblin.png".format(base_dir))
    orc=Image.open("{}\\images\\icons\\orc.png".format(base_dir))
    elf=Image.open("{}\\images\\icons\\elf.png".format(base_dir))

    #classes
    warrior=Image.open("{}\\images\\icons\\warrior.png".format(base_dir))
    mage=Image.open("{}\\images\\icons\\mage.png".format(base_dir))
    troubadour=Image.open("{}\\images\\icons\\troubadour.png".format(base_dir))
    bandit=Image.open("{}\\images\\icons\\bandit.png".format(base_dir))
    champion=Image.open("{}\\images\\icons\\champion.png".format(base_dir))
    cultist=Image.open("{}\\images\\icons\\cultist.png".format(base_dir))
    priest=Image.open("{}\\images\\icons\\priest.png".format(base_dir))
    any=Image.open("{}\\images\\icons\\any.png".format(base_dir))

    #requirements
    missionmod=Image.open("{}\\images\\icons\\missionmod.png".format(base_dir))
    auction=Image.open("{}\\images\\icons\\auction.png".format(base_dir))
    attack=Image.open("{}\\images\\icons\\attack.png".format(base_dir))
    defence=Image.open("{}\\images\\icons\\defence.png".format(base_dir))
    soother=Image.open("{}\\images\\icons\\soother.png".format(base_dir))
    activator=Image.open("{}\\images\\icons\\activator.png".format(base_dir))
    anticriminal = Image.open("{}\\images\\icons\\anticriminal.png".format(base_dir))

    #notables
    mayorIcon = Image.open("{}\\images\\icons\\mayor.png".format(base_dir))
    toughIcon = Image.open("{}\\images\\icons\\tough.png".format(base_dir))
    constableIcon = Image.open("{}\\images\\icons\\constable.png".format(base_dir))
    entertainerIcon = Image.open("{}\\images\\icons\\entertainer.png".format(base_dir))
    auditorIcon = Image.open("{}\\images\\icons\\auditor.png".format(base_dir))
    crierIcon = Image.open("{}\\images\\icons\\crier.png".format(base_dir))
    temperanceIcon = Image.open("{}\\images\\icons\\temperance.png".format(base_dir))
    envoyIcon = Image.open("{}\\images\\icons\\envoy.png".format(base_dir))
    recruiterIcon = Image.open("{}\\images\\icons\\recruiter.png".format(base_dir))
    nuisanceIcon = Image.open("{}\\images\\icons\\nuisance.png".format(base_dir))
    carpenterIcon = Image.open("{}\\images\\icons\\carpenter.png".format(base_dir))

    #alignment
    good = Image.open("{}\\images\\icons\\goodalignment.png".format(base_dir))
    evil = Image.open("{}\\images\\icons\\badalignment.png".format(base_dir))
    neutral = Image.open("{}\\images\\icons\\neutralalignment.png".format(base_dir))

    #level
    lvl1 = Image.open("{}\\images\\icons\\lvl1.png".format(base_dir))
    lvl2 = Image.open("{}\\images\\icons\\lvl2.png".format(base_dir))
    lvl3 = Image.open("{}\\images\\icons\\lvl3.png".format(base_dir))

    #rage
    rage = Image.open("{}\\images\\icons\\rageIcon.png".format(base_dir))
    plus = Image.open("{}\\images\\icons\\plus.png".format(base_dir))

    #textbox sizes
    descriptionWidth=32
    heroDescriptionWidth=32
    heroRageWidth=26
    nameWidth=12
    heroNameWidth=12
    townsfolkDescriptionWidth=21
    notableDescriptionWidth=31
    builderDescriptionWidth=26
    seasonDescriptionWidth=24
    peeveTitleWidth=20
    peeveDescriptionWidth=26
    peeveDescriptionTextSize=70

    #fonts
    titleSize=68; raceclassTextSize=55; heroDescriptionTextSize=57; seasonsDescriptionTextSize=68
    font_name = ImageFont.truetype(r'{}\\fonts\\dragon.otf'.format(base_dir), titleSize)
    font_raceclass = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), raceclassTextSize)
    font_herodescription = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), heroDescriptionTextSize)
    font_title = ImageFont.truetype(r'{}\\fonts\\dragon.otf'.format(base_dir), titleSize)
    font_type = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), 60)
    font_townsfolkDescription= ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), 80)
    font_number = ImageFont.truetype(r'{}\\fonts\\dungeon.ttf'.format(base_dir), 60)
    font_seasonsDescription = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), seasonsDescriptionTextSize)
    fontBuilderDescription=ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), 75)
    font_peeveTitle = ImageFont.truetype(r'{}\\fonts\\dragon.otf'.format(base_dir), 60)
    font_peeveDescription = ImageFont.truetype(r'{}\\fonts\\magical.ttf'.format(base_dir), peeveDescriptionTextSize)

    #mysterious shift factors
    shiftFactor=0.8

    #cardLocations
    peeveTitleCoords=[35, 35]
    titleCoords=[margin[0], margin[1]+65]
    typeCoords=[margin[0], margin[1]+10]
    cardShift=20
    raceCoords=(margin[0], 250+cardShift)
    raceCoordsTownsfolk=(margin[0], 180)
    classCoords=(margin[0]+150, raceCoords[1])
    descriptionCoords=(margin[0], 450+cardShift)
    abilityCoords=(margin[0], 420+cardShift)
    townsfolkDescriptionCoords=(margin[0], 360+cardShift)


    rage1Coords=(margin[0], int(abilityCoords[1]+210))
    rage2Coords = (margin[0], int(abilityCoords[1]+280))
    notableIconCoords=(margin[0]+180, 150)
    alignmentCoords=(margin[0]+300, 270)
    townsfolkTypeCoords=(margin[0]+180, 120)
    lvlCoords=(cardwidth-210, 200)

    peeveDescriptionCoords=[30, 120]

    #mysterious shift factors
    shiftFactor=0.8

    #determine card type. Hero, Quest, Module
    for card in (cards[:, 0]):
        card=int(card)-1
        for i in range(int(cards[card, 6])): #for every copy of each card
            ### Peeve
            if cards[card, 2]=='peeve':
                if cards[card, 9]=="positive":
                    cardPNG=goodPeeveTemplate.copy()
                elif cards[card, 9]=="negative":
                    cardPNG = badPeeveTemplate.copy()

                I1 = ImageDraw.Draw(cardPNG)
                # Title
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(peeveTitleWidth))
                for nt in range(len(text)):
                    I1.text(np.add(peeveTitleCoords, [0, nt * 20 * 0.9]), text[nt], fill=(10, 10, 10),font=font_peeveTitle)


                # Description
                text = textwrap.wrap("{}".format(cards[card, 3]), width=int(peeveDescriptionWidth))
                peeveTextSquishFactor=0.7
                for nt in range(len(text)):
                    I1.text(np.add(peeveDescriptionCoords,[0, nt*peeveDescriptionTextSize*peeveTextSquishFactor]), text[nt], fill=(10, 10, 10), font=font_peeveDescription)

                cardPNG.save("{}\\Results\\peeves\\card{}_{}.png".format(base_dir, card + 1, i + 1))

            ### Townsfolk
            if cards[card, 2]=='townsfolk':

                cardPNG=townsfolkTemplate.copy()
                I1 = ImageDraw.Draw(cardPNG)

                #TYPE
                I1.text([int((cardwidth - font_type.getsize('TOWNSFOLK')[0]) * 0.5), typeCoords[1]], 'TOWNSFOLK',
                        fill=(10, 10, 10), font=font_type)
                # Title
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords, [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)


                # Description
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(townsfolkDescriptionWidth))
                for nt in range(len(text)):
                    I1.text(np.add(townsfolkDescriptionCoords,[0, nt*heroDescriptionTextSize*shiftFactor*1.2]), text[nt], fill=(10, 10, 10), font=font_townsfolkDescription)

                # Type

                I1.text(rage2Coords, 'TYPE: ', fill=(10, 10, 10),font=font_raceclass)
                xCoord=cardwidth-150

                if cards[card, 5]=='mission modifier':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Mission Modifier', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(missionmod, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), missionmod)  # add icon
                if cards[card, 5]=='auction':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Auction  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(auction, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), auction)  # add icon
                if cards[card, 5]=='attack':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Attack  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(attack, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), attack)  # add icon
                if cards[card, 5]=='defence':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Defence  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(defence, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), defence)  # add icon
                if cards[card, 5]=='soother':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Soother  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(soother, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), soother)  # add icon
                if cards[card, 5]=='activator':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Ability Activator  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(activator, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), activator)  # add icon
                if cards[card, 5]=='anticriminal':
                    I1.text([rage2Coords[0], rage2Coords[1] + font_raceclass.getsize('TYPE: ')[1]], 'Anticriminal  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(anticriminal, (xCoord, int(rage2Coords[1]+0.75*font_raceclass.getsize('TYPE: ')[1]-iconSize[1]/2)), anticriminal)  # add icon

                # Add race of townsfolk
                raceArray=cards[card, 9].split("/")
                xCoord=cardwidth-150-120
                if raceArray[i%len(raceArray)]=='human':
                    I1.text(raceCoords, 'HUMAN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(human, (xCoord, raceCoordsTownsfolk[1]+raceclassTextSize), human)  # add icon
                    raceLen=font_raceclass.getsize('HUMAN ')
                elif raceArray[i%len(raceArray)]=='dwarf':
                    I1.text(raceCoords, 'DWARF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(dwarf, (xCoord, raceCoordsTownsfolk[1]+raceclassTextSize), dwarf)  # add icon
                    raceLen=font_raceclass.getsize('DWARF ')
                elif raceArray[i%len(raceArray)]=='goblin':
                    I1.text(raceCoords, 'GOBLIN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(goblin, (xCoord, raceCoordsTownsfolk[1]+raceclassTextSize), goblin)  # add icon
                    raceLen=font_raceclass.getsize('GOBLIN ')
                elif raceArray[i%len(raceArray)]=='orc':
                    I1.text(raceCoords, 'ORC', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(orc, (xCoord, raceCoordsTownsfolk[1]+raceclassTextSize), orc)  # add icon
                    raceLen=font_raceclass.getsize('ORC ')
                elif raceArray[i%len(raceArray)]=='elf':
                    I1.text(raceCoords, 'ELF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(elf, (xCoord, raceCoordsTownsfolk[1]+raceclassTextSize), elf)  # add icon
                    raceLen=font_raceclass.getsize('ELF ')

                if cards[card, 7]=='1':
                    #I1.text(raceCoords, 'ELF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(evil, (xCoord+120, raceCoordsTownsfolk[1]+raceclassTextSize), evil)  # add icon
                else:
                    cardPNG.paste(neutral, (xCoord+120, raceCoordsTownsfolk[1]+raceclassTextSize), neutral)  # add icon



                cardPNG.save("{}\\Results\\townsfolk\\card{}_{}.png".format(base_dir, card + 1, i + 1))

            ### QUEST
            if cards[card, 2]=='Quest':
                cardPNG = Questtemplate.copy()
                # Name
                I1 = ImageDraw.Draw(cardPNG)
                #TYPE
                I1.text([int((cardwidth - font_type.getsize('QUESTGIVER')[0]) * 0.5), typeCoords[1]], 'QUESTGIVER',
                        fill=(10, 10, 10), font=font_type)
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords, [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                #Requirement 1
                coords=np.add(raceCoords,np.array([0, 40]))
                if cards[card, 8]=='any':
                    I1.text(coords, 'ANY', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(any, (coords[0], coords[1]+raceclassTextSize), any)  # add icon
                    raceLen = font_raceclass.getsize('ANY')[0]
                if cards[card, 8]=='warrior':
                    I1.text(coords, 'WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (coords[0], coords[1]+raceclassTextSize), warrior)  # add icon
                    raceLen = font_raceclass.getsize('WARRIOR')[0]
                if cards[card, 8]=='bandit':
                    I1.text(coords, 'BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (coords[0], coords[1]+raceclassTextSize), bandit)  # add icon
                    raceLen = font_raceclass.getsize('BANDIT')[0]
                if cards[card, 8]=='priest':
                    I1.text(coords, 'PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (coords[0], coords[1]+raceclassTextSize), priest)  # add icon
                    raceLen = font_raceclass.getsize('PRIEST')[0]
                if cards[card, 8]=='troubadour':
                    I1.text(coords, 'MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (coords[0], coords[1]+raceclassTextSize), troubadour)  # add icon
                    raceLen = font_raceclass.getsize('MINSTREL')[0]
                if cards[card, 8]=='mage':
                    I1.text(coords, 'MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (coords[0], coords[1]+raceclassTextSize), mage)  # add icon
                    raceLen = font_raceclass.getsize('MAGE')[0]
                if cards[card, 8]=='champion':
                    I1.text(coords, 'CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (coords[0], coords[1]+raceclassTextSize), champion)  # add icon
                    raceLen = font_raceclass.getsize('CHAMPION')[0]
                if cards[card, 8]=='cultist':
                    I1.text(coords, 'CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (coords[0], coords[1]+raceclassTextSize), cultist)  # add icon
                    raceLen = font_raceclass.getsize('CULTIST')[0]



                # Requirement 2
                if cards[card, 9]=='any':
                    I1.text([coords[0]+raceLen, coords[1]], ', ANY', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(any, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), any)  # add icon
                if cards[card, 9]=='warrior':
                    I1.text([coords[0]+raceLen, coords[1]], ', WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), warrior)  # add icon
                if cards[card, 9]=='bandit':
                    I1.text([coords[0]+raceLen, coords[1]], ', BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), bandit)  # add icon
                if cards[card, 9]=='priest':
                    I1.text([coords[0]+raceLen, coords[1]], ', PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), priest)  # add icon
                if cards[card, 9]=='troubadour':
                    I1.text([coords[0]+raceLen, coords[1]], ', MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), troubadour)  # add icon
                if cards[card, 9]=='mage':
                    I1.text([coords[0]+raceLen, coords[1]], ', MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), mage)  # add icon
                if cards[card, 9]=='champion':
                    I1.text([coords[0]+raceLen, coords[1]], ', CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), champion)  # add icon
                if cards[card, 9]=='cultist':
                    I1.text([coords[0]+raceLen, coords[1]], ', CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (coords[0]+iconSize[0]+margin[0], coords[1]+raceclassTextSize), cultist)  # add icon

                # Race of Questgiver
                spacing = (descriptionCoords[0] + font_raceclass.getsize('Questgiver:        ')[0], descriptionCoords[1] +10 - int(iconSize[1] * 0.25))
                shift=15
                if cards[card, 10] == 'human':
                    I1.text([descriptionCoords[0], descriptionCoords[1]+shift], 'Questgiver: HUMAN  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(human, (spacing[0], spacing[1]), human)  # add icon
                if cards[card, 10] == 'dwarf':
                    I1.text([descriptionCoords[0], descriptionCoords[1]+shift], 'Questgiver: DWARF  ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(dwarf, (spacing[0], spacing[1]), dwarf)  # add icon
                if cards[card, 10] == 'goblin':
                    I1.text([descriptionCoords[0], descriptionCoords[1]+shift], 'Questgiver: GOBLIN ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(goblin, (spacing[0], spacing[1]), goblin)  # add icon
                if cards[card, 10] == 'elf':
                    I1.text([descriptionCoords[0], descriptionCoords[1]+shift], 'Questgiver: ELF ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(elf, (spacing[0], spacing[1]), elf)  # add icon
                if cards[card, 10] == 'orc':
                    I1.text([descriptionCoords[0], descriptionCoords[1]+shift], 'Questgiver: ORC ', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(orc, (spacing[0], spacing[1]), orc)  # add icon


                #alignment of Questgiver
                # Alignment
                if cards[card, 7] == '1':
                    cardPNG.paste(evil,(spacing[0]+110, spacing[1]), evil)  # add icon
                else:
                    cardPNG.paste(neutral, (spacing[0]+110, spacing[1]), neutral)  # add icon


                #LVL1 Reward
                I1.text(rage1Coords, '1-HERO REWARD: {}'.format(cards[card, 3]), fill=(10, 10, 10), font=font_raceclass)

                #LVL2 Reward
                if cards[card, 4]!='null':
                    I1.text(rage2Coords, '2-HERO REWARD: {}'.format(cards[card, 4]), fill=(10, 10, 10), font=font_raceclass)
                    #I1.text(np.add(rage2Coords, [0, raceclassTextSize]), '{}'.format(cards[card, 4]), fill=(10, 10, 10), font=font_raceclass)



                cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card + 1, i + 1))


            ### MODULE
            if cards[card, 2]=='module':
                if cards[card, 8]=='extratable':
                    cardPNG = ModuleTemplate2.copy()
                    # TYPE
                    I1 = ImageDraw.Draw(cardPNG)
                    I1.text([int((cardwidth - font_type.getsize('BUILDER')[0]) * 0.5), typeCoords[1]+50], 'BUILDER',
                            fill=(10, 10, 10), font=font_type)

                    #TITLE
                    text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth*0.8))
                    for nt in range(len(text)):
                        I1.text(np.add(np.add(titleCoords, [130, 120]), [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                    # Description
                    text = textwrap.wrap("{}".format(cards[card, 4]), width=int(builderDescriptionWidth))
                    for nt in range(len(text)):
                        I1.text(np.add(descriptionCoords,[130, nt*heroDescriptionTextSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_herodescription)

                    #icon
                    raceIndex=5
                    raceIconIndex=(450, 250)
                    if cards[card, raceIndex]=="human":
                        cardPNG.paste(human, raceIconIndex, human)  # add icon
                    if cards[card, raceIndex]=="dwarf":
                        cardPNG.paste(dwarf, raceIconIndex, dwarf)  # add icon
                    if cards[card, raceIndex]=="elf":
                        cardPNG.paste(elf, raceIconIndex, elf)  # add icon
                    if cards[card, raceIndex]=="orc":
                        cardPNG.paste(orc, raceIconIndex, orc)  # add icon
                    if cards[card, raceIndex]=="goblin":
                        cardPNG.paste(goblin, raceIconIndex, goblin)  # add icon

                    cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card + 1, i + 1))

                elif cards[card, 3]=='coach':
                    cardPNG = ModuleTemplate3.copy()
                    # TYPE
                    I1 = ImageDraw.Draw(cardPNG)
                    I1.text([int((cardwidth - font_type.getsize('BUILDER')[0]) * 0.5), typeCoords[1]+50], 'BUILDER',
                            fill=(10, 10, 10), font=font_type)

                    #TITLE
                    text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth*0.9))
                    for nt in range(len(text)):
                        I1.text(np.add(np.add(titleCoords, [130, 120]), [0, nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                    # Description
                    text = textwrap.wrap("{}".format(cards[card, 4]), width=int(builderDescriptionWidth*0.9))
                    for nt in range(len(text)):
                        I1.text(np.add(descriptionCoords,[130, nt*heroDescriptionTextSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_herodescription)

                    # Type
                    xCoord=cardwidth-120;yCoord=300
                    if cards[card, 5]=="bandit":
                        cardPNG.paste(bandit, (xCoord, yCoord), bandit)  # add icon
                    if cards[card, 5]=="champion":
                        cardPNG.paste(champion, (xCoord, yCoord), champion)  # add icon
                    if cards[card, 5]=="mage":
                        cardPNG.paste(mage, (xCoord, yCoord), mage)  # add icon
                    if cards[card, 5]=="cultist":
                        cardPNG.paste(cultist, (xCoord, yCoord), cultist)  # add icon
                    if cards[card, 5]=="troubadour":
                        cardPNG.paste(troubadour, (xCoord, yCoord), troubadour)  # add icon
                    if cards[card, 5] == "warrior":
                        cardPNG.paste(warrior, (xCoord, yCoord), warrior)  # add icon

                    cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card + 1, i + 1))


                else:
                    shift=40
                    cardPNG = ModuleTemplate.copy()
                    # TYPE
                    I1 = ImageDraw.Draw(cardPNG)
                    I1.text([int((cardwidth - font_type.getsize('BUILDER')[0]) * 0.5), typeCoords[1]+50], 'BUILDER',
                            fill=(10, 10, 10), font=font_type)

                    #TITLE
                    text = textwrap.wrap("{}".format(cards[card, 1]), width=int(nameWidth))
                    for nt in range(len(text)):
                        I1.text(np.add(titleCoords, [20, 10+shift+nt * titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                    #Race Boost
                    yCoord=int(rage2Coords[1]-0.5*font_raceclass.getsize('HUMAN MODULE ')[1])
                    if cards[card, 5]=='human':
                        I1.text([rage2Coords[0]+shift, yCoord+50], 'HUMAN MODULE', fill=(10, 10, 10), font=font_raceclass)
                        cardPNG.paste(human, (shift+raceCoords[0]+font_raceclass.getsize('HUMAN MODULE ')[0], yCoord), human)  # add icon
                    if cards[card, 5]=='dwarf':
                        I1.text([rage2Coords[0]+shift, yCoord+50], 'DWARF MODULE', fill=(10, 10, 10), font=font_raceclass)
                        cardPNG.paste(dwarf, (shift+raceCoords[0]+font_raceclass.getsize('DWARF MODULE ')[0], yCoord), dwarf)  # add icon
                    if cards[card, 5]=='goblin':
                        I1.text([rage2Coords[0]+shift, yCoord+50], 'GOBLIN MODULE', fill=(10, 10, 10), font=font_raceclass)
                        cardPNG.paste(goblin, (shift+raceCoords[0]+font_raceclass.getsize('GOBLIN MODULE ')[0], yCoord), goblin)  # add icon
                    if cards[card, 5]=='orc':
                        I1.text([rage2Coords[0]+shift, yCoord+50], 'ORC MODULE', fill=(10, 10, 10), font=font_raceclass)
                        cardPNG.paste(orc, (shift+raceCoords[0]+font_raceclass.getsize('ORC MODULE ')[0], yCoord), orc)  # add icon
                    if cards[card, 5]=='elf':
                        I1.text([rage2Coords[0]+shift, yCoord+50], 'ELF MODULE', fill=(10, 10, 10), font=font_raceclass)
                        cardPNG.paste(elf, (shift+raceCoords[0]+font_raceclass.getsize('ELF MODULE ')[0], yCoord), elf)  # add icon


                    # Description
                    text = textwrap.wrap("{}".format(cards[card, 4]), width=int(18))
                    for nt in range(len(text)):
                        I1.text(np.add(raceCoords,[shift+20, 70+shift+nt*heroDescriptionTextSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=fontBuilderDescription)

                    cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card + 1, i + 1))

            ### HERO
            if cards[card, 2]=='Hero':
                cardPNG = HeroTemplate.copy()
                I1 = ImageDraw.Draw(cardPNG)
                #TYPE
                I1.text([int((cardwidth-font_type.getsize('HERO')[0])*0.5), typeCoords[1]], 'HERO',fill=(10, 10, 10), font=font_type)

                #Name
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(heroNameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords,[0, nt*titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)


                if cards[card, 8]=='human':
                    I1.text(raceCoords, 'HUMAN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(human, (raceCoords[0], raceCoords[1]+raceclassTextSize), human)  # add icon
                    raceLen=font_raceclass.getsize('HUMAN ')


                if cards[card, 8]=='dwarf':
                    I1.text(raceCoords, 'DWARF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(dwarf, (raceCoords[0], raceCoords[1]+raceclassTextSize), dwarf)  # add icon
                    raceLen=font_raceclass.getsize('DWARF ')

                if cards[card, 8]=='goblin':
                    I1.text(raceCoords, 'GOBLIN', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(goblin, (raceCoords[0], raceCoords[1]+raceclassTextSize), goblin)  # add icon
                    raceLen=font_raceclass.getsize('GOBLIN ')

                if cards[card, 8]=='orc':
                    I1.text(raceCoords, 'ORC', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(orc, (raceCoords[0], raceCoords[1]+raceclassTextSize), orc)  # add icon
                    raceLen=font_raceclass.getsize('ORC ')

                if cards[card, 8]=='elf':
                    I1.text(raceCoords, 'ELF', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(elf, (raceCoords[0], raceCoords[1]+raceclassTextSize), elf)  # add icon
                    raceLen=font_raceclass.getsize('ELF ')

                ######


                #Class
                if cards[card, 9]=='warrior':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'WARRIOR', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(warrior, (classCoords[0], classCoords[1]+raceclassTextSize), warrior)  # add icon
                if cards[card, 9]=='bandit':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'BANDIT', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(bandit, (classCoords[0], classCoords[1]+raceclassTextSize), bandit)  # add icon
                if cards[card, 9]=='priest':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'PRIEST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(priest, (classCoords[0], classCoords[1]+raceclassTextSize), priest)  # add icon
                if cards[card, 9]=='troubadour':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'MINSTREL', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(troubadour, (classCoords[0], classCoords[1]+raceclassTextSize), troubadour)  # add icon
                if cards[card, 9]=='mage':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'MAGE', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(mage, (classCoords[0], classCoords[1]+raceclassTextSize), mage)  # add icon
                if cards[card, 9]=='champion':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'CHAMPION', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(champion, (classCoords[0], classCoords[1]+raceclassTextSize), champion)  # add icon
                if cards[card, 9]=='cultist':
                    I1.text([raceCoords[0]+raceLen[0], raceCoords[1]], 'CULTIST', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(cultist, (classCoords[0], classCoords[1]+raceclassTextSize), cultist)  # add icon

                # Ability

                I1.text(abilityCoords, 'ABILITY:', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 3]), width=int(heroDescriptionWidth))
                for na in range(len(text)):
                    I1.text(np.add(abilityCoords,[0, (na+1)*heroDescriptionTextSize*shiftFactor]), text[na], fill=(10, 10, 10), font=font_herodescription)



                #Rage 1
                #I1.text(rage1Coords, 'RAGE 1 EFFECT: ', fill=(10, 10, 10), font=font_herodescription)
                yShift = -5
                '''
                
                cardPNG.paste(rage, (rage1Coords[0], rage1Coords[1] + yShift), rage)  # add icon
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(heroRageWidth))
                for nr in range(len(text)):
                    I1.text(np.add(rage1Coords,[90, (nr)*heroDescriptionTextSize*shiftFactor]), text[nr], fill=(10, 10, 10), font=font_herodescription)
                '''
                # Rage 2
                #I1.text(rage2Coords, 'RAGE 2 EFFECT: ', fill=(10, 10, 10), font=font_herodescription)
                cardPNG.paste(rage, (rage1Coords[0] + 30, rage1Coords[1] + yShift), rage)  # add icon
                cardPNG.paste(rage, (rage1Coords[0]+15, rage1Coords[1] + yShift), rage)  # add icon
                cardPNG.paste(rage, (rage1Coords[0], rage1Coords[1] + yShift), rage)  # add icon
                #cardPNG.paste(plus, (rage1Coords[0] + 50, rage1Coords[1] + yShift+20), plus)  # add icon
                text = textwrap.wrap("{}".format(cards[card, 5]), width=int(heroRageWidth))
                for nr1 in range(len(text)):
                    I1.text(np.add(rage1Coords, [90, (nr1) * heroDescriptionTextSize*shiftFactor]), text[nr1], fill=(10, 10, 10), font=font_herodescription)

                if cards[card, 7]=='1':
                    cardPNG.paste(evil, (alignmentCoords[0], classCoords[1]+raceclassTextSize), evil)  # add icon
                if cards[card, 7] == '0':
                    cardPNG.paste(good, (alignmentCoords[0], classCoords[1]+raceclassTextSize), good)  # add icon


                #add Level

                if cards[card, 10] == '1':
                    shift = [90, 40]
                    cardPNG.paste(lvl1, lvlCoords, lvl1)  # add icon
                    I1.text(np.add(lvlCoords, shift), '1', fill=(10, 10, 10), font=font_number)
                if cards[card, 10] == '2':
                    shift = [87, 40]
                    cardPNG.paste(lvl2, lvlCoords, lvl2)  # add icon
                    I1.text(np.add(lvlCoords, shift), '2', fill=(10, 10, 10), font=font_number)
                if cards[card, 10] == '3':
                    shift = [87, 40]
                    cardPNG.paste(lvl3, lvlCoords, lvl3)  # add icon
                    I1.text(np.add(lvlCoords, shift), '3', fill=(10, 10, 10), font=font_number)


                #print(cards[card, 6])

                cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card+1, i + 1))
                #if card==1:
                    #sys.exit()

            ### Seasons
            if cards[card, 2] == 'Event':
                cardPNG = seasonsTemplate.copy()
                #TYPE
                I1 = ImageDraw.Draw(cardPNG)
                I1.text([int((cardwidth - font_type.getsize('SEASONS')[0]) * 0.5), typeCoords[1]], 'SEASONS',
                        fill=(10, 10, 10), font=font_type)
                #Title
                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(heroNameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords,[0, nt*titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                # Description
                text = textwrap.wrap("{}".format(cards[card, 4]), width=int(seasonDescriptionWidth))
                for nt in range(len(text)):
                    I1.text(np.add(descriptionCoords, [0, nt * seasonsDescriptionTextSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_seasonsDescription)

                #number of visitors today
                shift=65
                I1.text([raceCoords[0], raceCoords[1]+shift], 'NUMBER OF VISITORS TODAY: '.format(cards[card, 5]), fill=(10, 10, 10), font=font_raceclass)
                I1.text([int((cardwidth-font_title.getsize('5')[0])/2), raceCoords[1]+shift+50], '{}    ({})'.format(cards[card, 5], cards[card, 10]), fill=(10, 10, 10), font=font_title)


                if cards[card, 8]!="null":
                    affectList=cards[card, 8].split("/")
                    '''
                    if affectList[0] =='human' or affectList[0] =='dwarf' or affectList[0] =='elf' or affectList[0] =='orc' or affectList[0] =='goblin':
                        I1.text(rage1Coords + np.array([0, raceCoords[1] + 60]), 'Affects Races: ')
                    if affectList[0] =='warrior' or affectList[0] =='bandit' or affectList[0] =='mage' or affectList[0] =='troubadour' or affectList[0] =='priest' or affectList[0] =='cultist' or affectList[0] =='champion':
                        I1.text(rage1Coords + np.array([0, raceCoords[1] + 60]), 'Affects Classes: ')
                    '''
                    for ri in range(len(affectList)):
                        xCoord=int(rage1Coords[0])
                        yCoord=int(rage1Coords[1]+seasonsDescriptionTextSize+ 80*ri-60)

                        I1.text([xCoord, yCoord+25], affectList[ri], fill=(10, 10, 10),font=font_raceclass)

                        if affectList[ri]=='human':
                            cardPNG.paste(human, (xCoord+font_raceclass.getsize('human   ')[0], yCoord), human)  # add icon
                        if affectList[ri]=='dwarf':
                            cardPNG.paste(dwarf, (xCoord+font_raceclass.getsize('dwarf   ')[0], yCoord), dwarf)  # add icon
                        if affectList[ri]=='goblin':
                            cardPNG.paste(goblin, (xCoord+font_raceclass.getsize('goblin   ')[0], yCoord), goblin)  # add icon
                        if affectList[ri]=='elf':
                            cardPNG.paste(elf, (xCoord+font_raceclass.getsize('elf   ')[0], yCoord), elf)  # add icon
                        if affectList[ri]=='orc':
                            cardPNG.paste(orc, (xCoord+font_raceclass.getsize('orc   ')[0], yCoord), orc)  # add icon
                        if affectList[ri]=='warrior':
                            cardPNG.paste(warrior, (xCoord+font_raceclass.getsize('warrior   ')[0], yCoord), warrior)  # add icon
                        if affectList[ri]=='bandit':
                            cardPNG.paste(bandit, (xCoord+font_raceclass.getsize('bandit   ')[0], yCoord), bandit)  # add icon
                        if affectList[ri]=='priest':
                            cardPNG.paste(priest, (xCoord+font_raceclass.getsize('priest   ')[0], yCoord), priest)  # add icon
                        if affectList[ri]=='troubadour':
                            cardPNG.paste(troubadour, (xCoord+font_raceclass.getsize('troubadour   ')[0], yCoord), troubadour)  # add icon
                        if affectList[ri]=='champion':
                            cardPNG.paste(champion, (xCoord+font_raceclass.getsize('champion   ')[0], yCoord), champion)  # add icon
                        if affectList[ri]=='mage':
                            cardPNG.paste(mage, (xCoord+font_raceclass.getsize('mage   ')[0], yCoord), mage)  # add icon
                        if affectList[ri]=='cultist':
                            cardPNG.paste(cultist, (xCoord+font_raceclass.getsize('cultist   ')[0], yCoord), cultist)  # add icon


                cardPNG.save("{}\\Results\\seasons\\card{}_{}.png".format(base_dir, card + 1, i + 1))
            ### Notables
            if cards[card, 2] == 'notable':
                cardPNG = NotableTemplate.copy()
                I1 = ImageDraw.Draw(cardPNG)
                #Type
                I1.text([int((cardwidth - font_type.getsize('NOTABLE')[0]) * 0.5), typeCoords[1]], 'NOTABLE',
                        fill=(10, 10, 10), font=font_type)

                #title

                text = textwrap.wrap("{}".format(cards[card, 1]), width=int(heroNameWidth))
                for nt in range(len(text)):
                    I1.text(np.add(titleCoords,[0, nt*titleSize*shiftFactor]), text[nt], fill=(10, 10, 10), font=font_name)

                #image
                if cards[card, 9]=='mayor':
                    cardPNG.paste(mayorIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), mayorIcon)  # add ic
                if cards[card, 9] == 'constable':
                    cardPNG.paste(constableIcon, (notableIconCoords[0], notableIconCoords[1] + raceclassTextSize), constableIcon)  # add ic
                if cards[card, 9]=='carpenter':
                    cardPNG.paste(carpenterIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), carpenterIcon)  # add ic
                if cards[card, 9]=='auditor':
                    cardPNG.paste(auditorIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), auditorIcon)  # add ic
                if cards[card, 9]=='entertainer':
                    cardPNG.paste(entertainerIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), entertainerIcon)  # add ic
                if cards[card, 9]=='crier':
                    cardPNG.paste(crierIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), crierIcon)  # add ic
                if cards[card, 9]=='temperance':
                    cardPNG.paste(temperanceIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), temperanceIcon)  # add ic
                if cards[card, 9]=='envoy':
                    cardPNG.paste(envoyIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), envoyIcon)  # add ic
                if cards[card, 9]=='recruiter':
                    cardPNG.paste(recruiterIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), recruiterIcon)  # add ic
                if cards[card, 9]=='tough':
                    cardPNG.paste(toughIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), toughIcon)  # add ic
                if cards[card, 9]=='nuisance':
                    cardPNG.paste(nuisanceIcon, (notableIconCoords[0], notableIconCoords[1]+raceclassTextSize), nuisanceIcon)  # add ic

                if cards[card, 9] != 'mayor':
                    ownerLoc=(notableIconCoords[0]+300, notableIconCoords[1]+raceclassTextSize-20)
                    I1.text(ownerLoc, 'Owner', fill=(10, 10, 10), font=font_raceclass)
                    cardPNG.paste(any, [ownerLoc[0]+3, ownerLoc[1]+40], any)  # add ic


                #description
                I1.text(abilityCoords, 'DESCRIPTION:', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 3]), width=int(notableDescriptionWidth))
                for na in range(len(text)):
                    I1.text(np.add(abilityCoords,[0, (na+1)*heroDescriptionTextSize*shiftFactor]), text[na], fill=(10, 10, 10), font=font_herodescription)

                description2Coords=(margin[0], int(abilityCoords[1]+180))
                if cards[card, 9]!='mayor':
                    I1.text(description2Coords, 'APPOINTMENT BONUS:', fill=(10, 10, 10), font=font_herodescription)
                text = textwrap.wrap("{}".format(cards[card, 5]), width=int(notableDescriptionWidth))
                for na in range(len(text)):
                    I1.text(np.add(description2Coords,[0, (na+1)*heroDescriptionTextSize*shiftFactor]), text[na], fill=(10, 10, 10), font=font_herodescription)


                cardPNG.save("{}\\Results\\visitors\\card{}_{}.png".format(base_dir, card + 1, i + 1))
    #OLD CODE################################################################################################################
    ################################################################################################################################
    sys.exit()


    herotemplate=Image.open("{}\\herotemplate.png".format(base_dir))




    classrace_im=[warrior, bandit, priest, troubadour, mage,
                  champion, cultist, any, human, dwarf, goblin, orc, elf, elemental, good, evil]


    nHeroes = len(np.transpose(herodata)[0])
    for i in range(nHeroes):
        characters=len(herodata[i][1])
        if characters>=15:
            nameW=int(width*0.1)-int(((characters-12)**1.1)*0.6)
        else:
            nameW=int(width*0.1)
        font_name = ImageFont.truetype(r'{}}\\fonts\\arial.ttf'.format(base_dir), nameW)
        #font_t = ImageFont.truetype(r'C:\\Users\\kuusv\\Desktop\\TavernGame\\Jobs\\pythonCards\\arial.ttf', int(width*0.05))
        #font_d = ImageFont.truetype(r'C:\\Users\\kuusv\\Desktop\\TavernGame\\Jobs\\pythonCards\\arial.ttf', int(width*0.25))

        # Draw title
        templateCopy = herotemplate.copy()
        I1 = ImageDraw.Draw(templateCopy)
        I1.text((int(width*0.1), int(height*0.1)), "{}".format(herodata[i][1]), fill=(10, 10, 10), font=font_name)

        # Draw Drink Requirement
        I1.text((int(width*0.4), int(height*0.75)), "{}".format(herodata[i][9]), fill=(10, 10, 10), font=font_d)

        #Draw alignment
        aligncoords=[int(width*0.8), int(height*0.25)]
        if int(herodata[i][11])==0:
            templateCopy.paste(good.convert("RGBA"), aligncoords, good.convert("RGBA"))  # add icon
        elif int(herodata[i][11])==1:
            templateCopy.paste(evil.convert("RGBA"), aligncoords, evil.convert("RGBA"))  # add icon


        # Draw Race
        racecoords=[int(width*0.1), int(height*0.25)]

        if herodata[i][2]=='human':
            templateCopy.paste(classrace_im[8].convert("RGBA"), racecoords, classrace_im[8].convert("RGBA"))  # add icon
        elif herodata[i][2]=='dwarf':
            templateCopy.paste(classrace_im[9].convert("RGBA"), racecoords, classrace_im[9].convert("RGBA"))  # add icon
        elif herodata[i][2] == 'goblin':
            templateCopy.paste(classrace_im[10].convert("RGBA"), racecoords, classrace_im[10].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'orc':
            templateCopy.paste(classrace_im[11].convert("RGBA"), racecoords, classrace_im[11].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'elf':
            templateCopy.paste(classrace_im[12].convert("RGBA"), racecoords, classrace_im[12].convert("RGBA"))  # add icon

        elif herodata[i][2] == 'elemental':
            templateCopy.paste(classrace_im[13].convert("RGBA"), racecoords, classrace_im[13].convert("RGBA"))  # add icon

        # Draw Class
        classcoords=[int(width*0.1), int(height*0.4)]
        if herodata[i][3]=='warrior':
            templateCopy.paste(classrace_im[0].convert("RGBA"), classcoords, classrace_im[0].convert("RGBA"))  # add icon
        if herodata[i][3]=='bandit':
            templateCopy.paste(classrace_im[1].convert("RGBA"), classcoords, classrace_im[1].convert("RGBA"))  # add icon
        if herodata[i][3]=='priest':
            templateCopy.paste(classrace_im[2].convert("RGBA"), classcoords, classrace_im[2].convert("RGBA"))  # add icon
        if herodata[i][3]=='troubadour':
            templateCopy.paste(classrace_im[3].convert("RGBA"), classcoords, classrace_im[3].convert("RGBA"))  # add icon
        if herodata[i][3]=='mage':
            templateCopy.paste(classrace_im[4].convert("RGBA"), classcoords, classrace_im[4].convert("RGBA"))  # add icon
        if herodata[i][3]=='champion':
            templateCopy.paste(classrace_im[5].convert("RGBA"), classcoords, classrace_im[5].convert("RGBA"))  # add icon
        if herodata[i][3]=='cultist':
            templateCopy.paste(classrace_im[6].convert("RGBA"), classcoords, classrace_im[6].convert("RGBA"))  # add icon


        #Add Tantrum

        text=textwrap.wrap(herodata[i][10], width=30)
        I1.text((int(width*0.1), int(height*0.5)), "Tantrum:", fill=(10, 10, 10), font=font_t)
        for nt in range(len(text)):
            textheight=30
            I1.text((int(width*0.1), int(height*0.55)+nt*textheight), "{}".format(text[nt]), fill=(10, 10, 10), font=font_t)


        templateCopy.save("{}\\Results\\Heroes\\Hero{}.png".format(path, i + 1))




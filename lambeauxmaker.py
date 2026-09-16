"""
ça ça va juste créer une bannières avec des paramètres
de base le placeholder c'est who is he??
"""
import os 
from datetime import date
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PATH_MJS = "images/photosmjs/" 
FONT_MVP = ImageFont.truetype("fonts/Anton-Regular.ttf", size=620) 
SUBTEXT_COLOR = (100, 200, 250, 150)

def load_img(path:str)-> Image:
    return Image.open( path ).convert("RGBA")

class LambeauxMaker:
    def __init__(self, victoire:bool, scoreEq1:int, scoreEq2:int, nomMVP:str):  
        imgMVP = self.load_MVP(nomMVP)
        self.mvp = nomMVP

        winlooseIMG = self.load_MainText(victoire) 
        ScoreText = f"{scoreEq1}-{scoreEq2}"
        background = self.load_Background()

        self.merge(background, imgMVP, winlooseIMG ,ScoreText)

    def merge(self, backgroundIMG:Image, profileIMG:Image, mainTextIMG:Image, subText:str):
        pos_x = backgroundIMG.size[0]//32
        pos_y = backgroundIMG.size[1]//8
        draw = ImageDraw.Draw(backgroundIMG) 

        subtxtIMG = Image.new('RGBA', backgroundIMG.size, (255,255,255,0))
        d = ImageDraw.Draw(subtxtIMG)
        d.text( (pos_x,pos_y) , subText, fill=SUBTEXT_COLOR, font=FONT_MVP, stroke_width=4,stroke_fill=SUBTEXT_COLOR)
        blurred_subtext = subtxtIMG.filter(ImageFilter.GaussianBlur(radius=16))

        backgroundIMG =  Image.alpha_composite(backgroundIMG,blurred_subtext)
        backgroundIMG =  Image.alpha_composite(backgroundIMG,subtxtIMG)

        pos_x = backgroundIMG.size[0]//2 - profileIMG.size[0]//2
        pos_y = backgroundIMG.size[1]//2 - profileIMG.size[1]//2
        backgroundIMG.paste(profileIMG, (pos_x,pos_y) , profileIMG) 

        pos_x = backgroundIMG.size[0]//2 - mainTextIMG.size[0]//2
        pos_y = int(backgroundIMG.size[1]*1.05)- mainTextIMG.size[1]
        backgroundIMG.paste(mainTextIMG, (pos_x,pos_y) , mainTextIMG)  
        

        #sauvegarde
        backgroundIMG.convert("RGB").save(f"images/creations/{date.today()}=={self.mvp}==.jpg") 
    
    def load_MainText(self, win:bool):
        path = "images/win.png" if win else "images/loose.png"
        return load_img(path)

    def load_MVP(self, mj:str)-> Image:
        chemin = f"{PATH_MJS}{mj}.png"
        if not os.path.isfile(chemin):
            chemin= PATH_MJS+"placeholder.png"
            

        return load_img(chemin) 

    def load_Background(self):
        return load_img("images/background.png")

LambeauxMaker(True, 13, 11, "Mathydre")

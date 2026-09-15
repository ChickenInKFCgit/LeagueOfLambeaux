"""
ça ça va juste créer une bannières avec des paramètres
de base le placeholder c'est who is he??
"""
import os 
from PIL import Image, ImageDraw, ImageFont

PATH_MJS = "images/photosmjs/"
            
FONT_MAIN = ImageFont.truetype("segoeui.ttf", size=36)
FONT_SUB = ImageFont.truetype("segoeui.ttf", size=20)
SUBTEXT_COLOR = (100, 200, 100, 255)

def load_img(path:str)-> Image:
    return Image.open( path ).convert("RGBA")

class LambeauxMaker:
    def __init__(self, victoire:bool, scoreEq1:int, scoreEq2:int, nomMVP:str):  
        imgMVP = self.load_MVP(nomMVP)

        WorLText = "VICTOIRE" if victoire else "DÉFAITE"
        textcolor = (0, 255, 0, 255) if victoire else (255, 0, 0, 255)
        ScoreText = f"\ {scoreEq1} - {scoreEq2} /"
        background = self.load_Background()

        self.merge(background, imgMVP, WorLText ,ScoreText, textcolor)

    def merge(self, backgroundIMG:Image, profileIMG:Image, mainText:str, subText:str, text_color:tuple):
        backgroundIMG.paste(profileIMG, (0,0) , profileIMG) 

        draw = ImageDraw.Draw(backgroundIMG)  

        draw.text( (50,50) , mainText, fill=text_color, font=FONT_MAIN) 
        draw.text( (100,100) , subText, fill=SUBTEXT_COLOR, font=FONT_SUB)   

        #sauvegarde
        backgroundIMG.convert("RGB").save("creationsAJDDATEJSP.jpg") 
    

    def load_MVP(self, mj:str)-> Image:
        chemin = f"{PATH_MJS}{mj}.png"
        if not os.path.isfile(chemin):
            chemin= PATH_MJS+"placeholder.png"
            

        return load_img(chemin) 

    def load_Background(self):
        return load_img("images/background.png")

LambeauxMaker(True, 13, 11, "Mathydre")
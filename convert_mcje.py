from mcje.minecraft import Minecraft
import param_MCJE as param
import circle as cr
from ms_font import font_design,FONT_HEIGHT,FONT_WIDTH

MASS_HEIGHT = FONT_HEIGHT + 2
MASS_WIDTH = FONT_WIDTH + 4
STA_X = 50
STA_Y = 71
STA_Z = 50

class MCJESweeper():
    def __init__(self,mc):
        self.mass_x = STA_X
        self.mass_z = STA_Z
        self.mc = mc
    
    def setMass(self,w,h):
        self.mass_h = 0
        self.mass_w = 0
        while self.mass_w < w:
            while self.mass_h < h:
                self.mc.setBlocks(self.mass_x-3,STA_Y,self.mass_z-3,self.mass_x+3,STA_Y,self.mass_z+3,param.BLACK_CONCRETE)
                self.mc.setBlocks(self.mass_x-2,STA_Y,self.mass_z-2,self.mass_x+2,STA_Y,self.mass_z+2,param.STONE)
                self.mass_x -= 6
                self.mass_h += 1
            self.mass_x = STA_X
            self.mass_h = 0
            self.mass_z += 6
            self.mass_w += 1

    def cellOpen(self,j,i):
        self.mass_x = STA_X - j*6
        self.mass_z = STA_Z + i*6
        print(self.mass_x,self.mass_z)
        self.mc.setBlocks(self.mass_x-2,STA_Y,self.mass_z-2,self.mass_x+2,STA_Y,self.mass_z+2,param.CONCRETE)

    def raiseFrag(self,j,i):
        self.mass_x = STA_X - j*6
        self.mass_z = STA_Z + i*6
        print(self.mass_x,self.mass_z)
        self.mc.setBlocks(self.mass_x-2,STA_Y,self.mass_z-2,self.mass_x+2,STA_Y,self.mass_z+2,param.ORANGE_CONCRETE)
    
    def game_over(self):
        self.mc.postToChat("ばーかばーか地雷踏んでやんの～")

if __name__ == '__main__':
    BOARD_WIDTH, BOARD_HEIGHT = 20, 10
    mc = Minecraft.create(port=param.PORT_MC)
    mjs = MCJESweeper(mc)
    mjs.setMass(BOARD_WIDTH,BOARD_HEIGHT)




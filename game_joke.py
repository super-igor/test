import pygame as pg
import colors
import random 

class Window:
    w1 = 1000
    w2 = 600
#-------------------------------------------------------
class Button: 
    def __init__(self, text, color, width, height, x, y):
        self.text = text
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def jumpto(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
    def is_over(self, mouse_x, mouse_y):
        
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            return True
        else:
            return False
    
    def do(self):
        pass
    
    def set_text(self, text):
        self.text = text
        
    def set_color(self, color):
        self.color = color
        
    def set_size(self, size, width, height):
        self.width = width
        self.height = height
        

btn_yes = Button('yes', colors.RED, 150, 50, 550, 300)
btn_no = Button('no', colors.BLUE, 150, 50, 300, 300)

screen = pg.display.set_mode((Window.w1, Window.w2))

FPS = 30
pg.init()
clock = pg.time.Clock()

running = True
while running:
    screen.fill(colors.WHITE)
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            if btn_no.is_over(x, y) == True:
                new_x = random.randint(10,600)
                new_y = random.randint(10,600)
                btn_no.jumpto(new_x, new_y)
                
    
    btn_yes.draw(screen)
    btn_no.draw(screen)
    
    pg.display.update()
pg.quit()

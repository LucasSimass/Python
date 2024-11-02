import pygame 
import neat
import time
import os 
import random
pygame.font.init()

# defining the "Window board" size (1 = 1px)  
WIN_WIDTH = 500
WIN_HEIGHT = 700

# get the images of the bird
BIRD_IMGS = [
    # Default Bird Animation 

    # Bird with the wings up
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), 

    # Bird with the wings in the mid
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), 

    # Bird with the wings down
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))
]

# Get the image of the pipe 
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))

# Get the image of the base 
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))

# Get the image of the background 
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)


# Default Bird Object
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
       self.x = x
       self.y = y
       self.tilt = 0
       self.tick_count = 0
       self.vel = 0
       self.height = self.y
       self.img_count = 0
       self.img = self.IMGS[0]   

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count += 1

        # how much we´re moving up and how much we moving down
        d = self.vel * self.tick_count + 1.5 * self.tick_count**2

        if d >= 16:
            d = 16
        
        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y <  self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt < -90:
                self.tilt -= self.ROT_VEL
    
    def draw(self,win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2
        
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_react =  rotated_image.get_rect(center=self.img.get_rect(x=self.x, y=self.y).center)
        win.blit(rotated_image, new_react)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Pipe:
    GAP = 200
    VEL = 5
    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()
        self.img = BIRD_IMGS[0]
    
    def set_height(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = Bird.get_mask(self)
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
      
        return False

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.x2 < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG,(self.x1, self.y))
        win.blit(self.IMG,(self.x2, self.y))
        
def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))

    for pipe in pipes: 
        if pipe.collide(bird):
            pass
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)

    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(230,350)
    base = Base(630) #position of the base y position
    pipes = [Pipe(600)]
    score = 0
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # bird.move()
        add_pipe = False
        rem = []
        for pipe in pipes: 
            if pipe.collide(bird):
                pass
            pipe.move()

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                pass

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
                pass
        if add_pipe:
            score += 1
            pipes.append(Pipe(600)) 

        for r in rem:
            pipes.remove(random)

        if bird.y + bird.img.get_height() >= 730:
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)
    pygame.quit()
    quit()

main()
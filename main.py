# IMPORTS
import pygame
pygame.init()


#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
blue = (55, 149, 222)


# DEFINE CLASSES
class Level:
     def __init__(self, blocks, watches, door):
          self.blocks = blocks
          self.watches = watches
          self.door = door


# DEFINE VARIABLES/LISTS
x = 10
y = 300
w = 68
h = 188
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
player = pygame.Rect(x, y, w, h)

speed = 1
score = 0

pygame.display.set_caption("Run, Jiri, RUN!")

player_img = pygame.image.load("player.png")
watch_img = pygame.image.load("watch.png")

level1 = Level(
     [],
     [],
     pygame.Rect(350, 200, 200, 200)
)
level2 = Level(
     [
          pygame.Rect(100, 220, 10, 160),
          pygame.Rect(100, 220, 700, 10),
          pygame.Rect(800, 220, 10, 160),
          pygame.Rect(100, 380, 320, 10),
          pygame.Rect(530, 380, 280, 10)
          ],
     [
          # 1
          [pygame.Rect(50, 60, 36, 60), True],
          [pygame.Rect(150, 60, 36, 60), True],
          [pygame.Rect(250, 60, 36, 60), True],
          [pygame.Rect(350, 60, 36, 60), True],
          [pygame.Rect(450, 60, 36, 60), True],
          [pygame.Rect(550, 60, 36, 60), True],
          [pygame.Rect(650, 60, 36, 60), True],
          [pygame.Rect(750, 60, 36, 60), True],
          # 2
          [pygame.Rect(840, 150, 36, 60), True],
          [pygame.Rect(840, 250, 36, 60), True],
          [pygame.Rect(840, 350, 36, 60), True],
          # 3
          [pygame.Rect(50, 500, 36, 60), True],
          [pygame.Rect(150, 500, 36, 60), True],
          [pygame.Rect(250, 500, 36, 60), True],
          [pygame.Rect(350, 500, 36, 60), True],
          [pygame.Rect(450, 500, 36, 60), True],
          [pygame.Rect(550, 500, 36, 60), True],
          [pygame.Rect(650, 500, 36, 60), True],
          [pygame.Rect(750, 500, 36, 60), True]
          ],
     pygame.Rect(420, 230, 100, 10)
)
level3 = Level(
     [
          pygame.Rect(300, 300, 30, 30),
          pygame.Rect(500, 300, 30, 30),
          pygame.Rect(700, 300, 30, 30)
          ],
     [
          [pygame.Rect(400, 300, 36, 60), True],
          [pygame.Rect(600, 300, 36, 60), True]
          ],
     pygame.Rect(800, 300, 30, 30)
)
level4 = Level(
     [
          # 1
          pygame.Rect(100, 200, 10, 200),
          pygame.Rect(100, 200, 100, 10),
          pygame.Rect(200, 200, 10, 200),
          # 2
          pygame.Rect(300, 200, 10, 200),
          pygame.Rect(300, 390, 100, 10),
          pygame.Rect(400, 200, 10, 200),
          # 3
          pygame.Rect(500, 200, 10, 200),
          pygame.Rect(500, 200, 100, 10),
          pygame.Rect(600, 200, 10, 200),
          # 4
          pygame.Rect(700, 200, 10, 200),
          pygame.Rect(700, 390, 100, 10),
          pygame.Rect(800, 200, 10, 200)
          ],
     [
          [pygame.Rect(120, 220, 36, 60), True],
          [pygame.Rect(160, 220, 36, 60), True],
          [pygame.Rect(320, 320, 36, 60), True],
          [pygame.Rect(360, 320, 36, 60), True],
          [pygame.Rect(520, 220, 36, 60), True],
          [pygame.Rect(560, 220, 36, 60), True],
          [pygame.Rect(720, 320, 36, 60), True],
          [pygame.Rect(760, 320, 36, 60), True],
          [pygame.Rect(120, 290, 36, 60), True],
          [pygame.Rect(160, 290, 36, 60), True],
          [pygame.Rect(320, 250, 36, 60), True],
          [pygame.Rect(360, 250, 36, 60), True],
          [pygame.Rect(520, 290, 36, 60), True],
          [pygame.Rect(560, 290, 36, 60), True],
          [pygame.Rect(720, 250, 36, 60), True],
          [pygame.Rect(760, 250, 36, 60), True]
          ],
     pygame.Rect(40, 150, 20, 300)
)
level5 = Level(
     [
          # j
          pygame.Rect(200, 200, 10, 210),
          pygame.Rect(150, 400, 50, 10),
          pygame.Rect(150, 350, 10, 50),
          # i
          pygame.Rect(300, 200, 10, 210),
          # r
          pygame.Rect(400, 200, 10, 210),
          pygame.Rect(400, 200, 50, 10),
          pygame.Rect(450, 200, 10, 110),
          pygame.Rect(400, 300, 50, 10),
          pygame.Rect(430, 310, 10, 50),
          pygame.Rect(440, 360, 10, 50),
          # i
          pygame.Rect(550, 200, 10, 210)
          ],
     [
          [pygame.Rect(650, 70, 36, 60), True],
          [pygame.Rect(750, 70, 36, 60), True],
          [pygame.Rect(650, 170, 36, 60), True],
          [pygame.Rect(750, 170, 36, 60), True],
          [pygame.Rect(650, 270, 36, 60), True],
          [pygame.Rect(750, 270, 36, 60), True],
          [pygame.Rect(650, 370, 36, 60), True],
          [pygame.Rect(750, 370, 36, 60), True],
          [pygame.Rect(650, 470, 36, 60), True],
          [pygame.Rect(750, 470, 36, 60), True],
          ],
     pygame.Rect(850, 250, 30, 100)
)
level6 = Level([],[],pygame.Rect(1000, 700, 0, 0))
levels = [level1, level2, level3, level4, level5, level6]
level_num = 0
level = levels[level_num]


# DEFINE FUNCTIONS
def print_score():
     font = pygame.font.Font(None, 50)
     screen.blit(font.render(str(score), True, black), (850,10))

def collision():
     for block in level.blocks:
          if block.colliderect(player):
               return True

def off_screen():
     if x < 0 or y < 0 or x+w > 900 or y+h > 600:
          return True


# GAME LOOP
end = False
while not end:
     screen.fill(blue)
     if level_num == 5:
          font = pygame.font.Font(None, 100)
          screen.blit(font.render("score: 47", True, black), (300, 150))
          screen.blit(font.render("HAPPY BIRTHDAY!", True, white), (150, 300))
          font = pygame.font.Font(None, 15)
          screen.blit(font.render("made by LamaMilu", True, white), (800, 560))
          screen.blit(font.render("all rights reserved", True, black), (803, 575))
          screen.blit(player_img, player)
     else:
          for watch in level.watches:
               if watch[1]:
                    screen.blit(watch_img, watch[0])
          for block in level.blocks:  
               pygame.draw.rect(screen, black, block)
          pygame.draw.rect(screen, white, level.door)
          screen.blit(player_img, player)
          print_score()
     pygame.display.flip()
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

     keys = pygame.key.get_pressed()
     if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_a]:

          old_x = x
          old_y = y

          if keys[pygame.K_w]:
               y -= speed
               player = pygame.Rect(x, y, w, h)
               if collision() or off_screen():
                    y = old_y

          if keys[pygame.K_s]:
               y += speed
               player = pygame.Rect(x, y, w, h)
               if collision() or off_screen():
                    y = old_y

          if keys[pygame.K_d]:
               x += speed
               player = pygame.Rect(x, y, w, h)
               if collision() or off_screen():
                    x = old_x

          if keys[pygame.K_a]:
               x -= speed
               player = pygame.Rect(x, y, w, h)
               if collision() or off_screen():
                    x = old_x

     for watch in level.watches:
          if watch[0].colliderect(player) and watch[1]:
               score += 1
               watch[1] = False

     if level.door.colliderect(player):
          done = True
          for watch in level.watches:
               if watch[1]:
                    done = False
          if done:
               level_num += 1
               level = levels[level_num]
               x = 10
               y = 300

     clock.tick(200)
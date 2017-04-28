import pygame, sys, random, time

screen_size = (width, height) = (1900, 1000)

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0) 
GREEN = (0, 255, 0)
RED = (255,  0, 0)

speed = 7

class Block(pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Block, self).__init__()   #costruttore
		
		self.sprite_sheet = pygame.image.load(filename).convert()

		self.image = pygame.Surface((width, height))
                self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
		self.image.set_colorkey(GREEN) 
		
		self.rect = self.image.get_rect()
		
	def reset_pos(self):
		self.rect.x = (width /2 )
		self.rect.y =700
	
	def update(self):
		self.rect.y -= 10
		#if self.rect.y  < -10  :
	 		#self.reset_pos()


class Nemico(pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Nemico, self).__init__()   #costruttore
		
		self.sprite_sheet = pygame.image.load(filename).convert()

		self.image = pygame.Surface((width, height))
                self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
		self.image.set_colorkey(GREEN) 
		
		self.rect = self.image.get_rect()
		
	def reset_pos(self):
		self.rect.x = -80
		self.rect.y =10
		
	
	def update(self):
		
		self.rect.x += speed
		if self.rect.x  > width :
	 		self.reset_pos()


class Giocatore(pygame.sprite.Sprite):
	def __init__(self, filename,  width, height):
		super(Giocatore, self).__init__()   #costruttore
		
		self.sprite_sheet = pygame.image.load(filename).convert()

		self.image = pygame.Surface((width, height))
                self.image.blit(self.sprite_sheet, (0, 0), (0, 0, width, height))
		self.image.set_colorkey(GREEN) 
		
		self.rect = self.image.get_rect()
			
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("DRAGONBALL")

clock = pygame.time.Clock()

giocatore1 = "goku.png"
nemico1 = "freezer.png"
sfondo = "namec.png"

bg = pygame.image.load(sfondo).convert()



block_list = pygame.sprite.Group()
nemico_list = pygame.sprite.Group()
giocatore_list = pygame.sprite.Group()





block = Block("sferaverde.png",130, 130)
block.rect.x = (width /2 )
block.rect.y = 680
block_list.add(block)

nemico = Nemico(nemico1, 168, 298)
nemico.rect.x = 50
nemico.rect.y = 10
nemico_list.add(nemico)


giocatore = Giocatore (giocatore1 , 198, 272)
giocatore.rect.x = 910
giocatore.rect.y = 750
giocatore_list.add(giocatore)


done = False
spara = False
vita = 200
potere = 1000




font = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 150)
def score(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (100, 900))
def energia(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (10,  900))
def score_potere(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (1800,  900))
def text_potere(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (1650,  900))

def up(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (1000,  500))



def lose(message, color):
    text = font2.render(message, True, color)
    screen.blit(text, (750,  450))

gameOver = False

livello1 = True
livello2 = False
livello3 = False

UP=False


while not gameOver :


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameOver = True
		if event.type == pygame.KEYDOWN:   #se l'evento e' di pressione di     un tasto
                	if event.key == pygame.K_UP:
				numrand = random.randint(9 ,41)
				potere-= numrand
				block.reset_pos()
			if event.key == pygame.K_a:      #trucchi
				potere = 9999
			if event.key == pygame.K_s:
				vita = 10	
	hit_list = pygame.sprite.spritecollide(block, nemico_list, False)
	for hit in hit_list:
        	vita -= 1


	screen.blit(bg, (0, 0))		




	if livello1 == True:
		if vita <= 0:
			livello2 = True
			livello1 = False
			nemico.reset_pos()
			speed = 13
			vita = 250
 			time.sleep(3)

		
	if livello2 == True :
	
		if vita<=0:
			livello2=False
			livello3=True
			nemico.reset_pos()
			speed = 17
			vita = 300
 			time.sleep(3)

	if livello3 == True :
		if vita<=0:
			lose("HAI VINTO !",GREEN) 
			gameOver = True


	energia("Vita: ", GREEN)
	score(str(vita), WHITE)
	

		
	
	text_potere("Potere:" , GREEN)
	score_potere(str(potere), WHITE)

	if potere <= 0 :
		lose("GAME OVER", RED)
		gameOver = True

	block_list.update()
	nemico_list.update()
	giocatore_list.update()

	nemico_list.draw(screen)
	giocatore_list.draw(screen)
	block_list.draw(screen)



    	pygame.display.flip()
	clock.tick(30)

time.sleep(3)
pygame.quit()
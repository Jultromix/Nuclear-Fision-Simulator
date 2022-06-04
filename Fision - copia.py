import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import time

pygame.init()

# Constantes
size = (1000, 700)
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
BLUE =  (   0,   0, 255)
RED =   ( 255,   0,   0)
GREEN = (   0, 255,   0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("simlacion: Reacción Nuclear ")
ventana = pygame.display.set_mode(size)

#Section of event switches
Switch_A_motion = False
Switch_N_appear = False
Switch_N_speed = False

Switch_KrBa_appear = False
Switch_KrBa_speed = False

#Casos posibles Fision
UrKrBa=["Images/Uranio.png","Images/Bario.png", "Images/Kripton.png","Images/neutron.png"]
MgHNa = ["Images/Mg.png","Images/D.png", "Images/Na.png"]

#Casos posibles fusion
DTHe = ["Images/D.png","Images/T.png", "Images/He.png","Images/neutron.png"]
TTHe = ["Images/D.png","Images/T.png", "Images/He.png","Images/neutron.png"]
class Neutron(pygame.sprite.Sprite):

    def __init__(self,picture_path,coordx,coordy,speedx,speedy):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [coordx,coordy]
        self.speed_N = [speedx,speedy] 

    def update(self):
        global Switch_N_speed
        if Switch_N_speed == False:
            self.rect = self.rect.move(self.speed_N)
        else:
            self.rect = self.rect.move(self.speed_N[0],-self.speed_N[1])
        
        if self.rect.left <= 0 or self.rect.right >=1000:
            self.kill()
            # self.speed_N[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >=700:
            self.kill()
            # self.speed_N[1] *= -1

class Uranium(pygame.sprite.Sprite):
    def __init__(self,picture_path,coordx,coordy):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [coordx, coordy]
        self.speed_Ur = [0,0]
        self.in_motion = False
    
    def update(self):

        if Switch_A_motion == True:
            self.rect = self.rect.move(self.speed_A)

            if self.rect.left <= 0 or self.rect.right >=1000:
                self.speed_A[0] *= -1.06

            if self.rect.top <= 0 or self.rect.bottom >=700:
                self.speed_A[1] *= -1.06

class Kripton(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()
        self.image = pygame.image.load("Images/Kripton.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_Kr = [random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2))] 

    def update(self):
        self.rect = self.rect.move(self.speed_Kr)

        
        if self.rect.left <= 0 or self.rect.right >=1050:
            self.kill()

            
        # if self.rect.top <= 0 or self.rect.bottom >=700:
        #     self.speed_E[1] *= -1

class Barium(pygame.sprite.Sprite):

    def __init__(self,center):
        super().__init__()
        self.image = pygame.image.load("Images/Bario.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_Ba = [random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2))] 

    def update(self):
        self.rect = self.rect.move(self.speed_Ba)
        
        if self.rect.left <= 0 or self.rect.right >=1050:
            self.kill()

        # if self.rect.top <= 0 or self.rect.bottom >=700:
        #     self.speed_E[1] *= -1
# ---------------------------------------------------------------------

# Funciones
#Agregar/mostrar neutrones

# Grupo de Neutrones
default_N = Neutron("Images/neutron.png",100, 350,random.randint(1,7),0)
neutron_group = pygame.sprite.Group()
neutron_group.add(default_N)

# Grupo-Atomos de uranio
uranium_group = pygame.sprite.Group()
default_uranium = Uranium("Images/Uranio.png",random.randint(120,800), 350)
uranium_group.add(default_uranium)
for atom in range(0,11):
    new_atom = Uranium("Images/Uranio.png",random.randint(50,900), random.randint(0,600))
    uranium_group.add(new_atom)

#Grupos-Atomos de Kripton y Bario
kripton_group = pygame.sprite.Group()
barium_group = pygame.sprite.Group()

clock = pygame.time.Clock()



all_sprites = pygame.sprite.Group()
all_sprites.add(neutron_group)
all_sprites.add(uranium_group)
all_sprites.add(kripton_group)
all_sprites.add(barium_group)


running = True
while True:       
    #movimiento del neutron (por elmomento ciclico)
    for evento in GAME_EVENTS.get():
        if evento.type == GAME_GLOBALS.QUIT:
            sys.exit(0)
        if evento.type == GAME_GLOBALS.KEYDOWN:
            if evento.key == GAME_GLOBALS.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    all_sprites.update() 

    
    #Activates the atoms' motion once collision is produced
    # if pygame.sprite.groupcollide(uranium_group,neutron_group,True,True):
    hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
    for hit in hits:
        print(hit)
        for n in range(0,1):
            barium = Barium(hit.rect.center)
            kripton = Kripton(hit.rect.center)

            barium_group.add(barium)
            all_sprites.add(barium)
            kripton_group.add(kripton)
            all_sprites.add(kripton)

        for n in range(0,10):
            new_neutron = Neutron("Images/neutron.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
            neutron_group.add(new_neutron)
            all_sprites.add(new_neutron)

    # if len(all_sprites)==0:
    #     pygame.quit()
    # else:
    #     continue
    pygame.display.flip()
    clock.tick(60)
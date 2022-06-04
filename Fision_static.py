import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import time

pygame.init()
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("simlacion: Reacción Nuclear ")
# Constantes

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
BLUE =  (   0,   0, 255)
RED =   ( 255,   0,   0)
GREEN = (   0, 255,   0)
font = pygame.font.SysFont(None, 20)
#Section of event switches
Switch_A_motion = False
Switch_N_appear = False
Switch_N_speed = False

Switch_KrBa_appear = False
Switch_KrBa_speed = False
click = False

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

        if self.rect.top <= 0 or self.rect.bottom >=700:
            self.kill()


class Uranium(pygame.sprite.Sprite):
    def __init__(self,picture_path,coordx,coordy):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [coordx, coordy]
        self.speed_Ur = [0,0]
        self.in_motion = False
    
    def update(self):


        self.rect = self.rect.move(self.speed_Ur)

        if self.rect.left <= 0 or self.rect.right >=1000:
            self.speed_Ur[0] *= -1

        if self.rect.top <= 0 or self.rect.bottom >=700:
            self.speed_Ur[1] *= -1

class Kripton(pygame.sprite.Sprite):
    
    def __init__(self,picture_path, center):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_Kr = [random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2))] 

    def update(self):
        self.rect = self.rect.move(self.speed_Kr)

        
        if self.rect.left <= 0 or self.rect.right >=1050:

            self.kill()

            
        if self.rect.top <= 0 or self.rect.bottom >=700:
          self.kill()
          
class Barium(pygame.sprite.Sprite):

    def __init__(self,picture_path,center):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_Ba = [random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2))] 

    def update(self):
        self.rect = self.rect.move(self.speed_Ba)
        
        if self.rect.left <= 0 or self.rect.right >=1050:
 
            self.kill()

        if self.rect.top <= 0 or self.rect.bottom >=700:
         
          self.kill()
# ---------------------------------------------------------------------

# Funciones
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    clock = pygame.time.Clock()
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        
        pygame.draw.rect(screen,(0,255,0), button_1)
        pygame.draw.rect(screen,(0,0,255), button_2)
        if button_1.collidepoint((mx, my)):
            if click:
                simulacion_MgHNa()
        if button_2.collidepoint((mx, my)):
            if click:
                simulacion_UrKrBa()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
            if evento.type == GAME_GLOBALS.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def simulacion_UrKrBa():

    # Grupo de Neutrones
    default_N = Neutron("Images/neutron.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Images/Uranio.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,30):
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
    while running:       

        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                sys.exit(0)
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False
                    

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
                barium = Barium("Images/Bario.png",hit.rect.center)
                kripton = Kripton("Images/Kripton.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            for n in range(0,10):
                new_neutron = Neutron("Images/neutron.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
                neutron_group.add(new_neutron)
                all_sprites.add(new_neutron)

        pygame.display.flip()
        clock.tick(60)

def simulacion_MgHNa():
    # Grupo de Neutrones
    default_N = Neutron("Images/neutron.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Images/Mg.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,11):
        new_atom = Uranium("Images/Mg.png",random.randint(50,900), random.randint(0,600))
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
    while running:       
        #movimiento del neutron (por elmomento ciclico)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                sys.exit(0)
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False
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
                barium = Barium("Images/D.png",hit.rect.center)
                kripton = Kripton("Images/Na.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            for n in range(0,5):
                new_neutron = Neutron("Images/neutron.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
                neutron_group.add(new_neutron)
                all_sprites.add(new_neutron)

        pygame.display.flip()
        clock.tick(60)

def simulacion_DTHe():
    # Grupo de Neutrones
    default_N = Neutron("Images/D.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Images/T.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,11):
        new_atom = Uranium("Images/T.png",random.randint(50,900), random.randint(0,600))
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
    while running:       
        #movimiento del neutron (por elmomento ciclico)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                sys.exit(0)
            
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False
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
                barium = Barium("Images/He.png",hit.rect.center)
                kripton = Kripton("Images/neutron.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            for n in range(0,1):
                new_neutron = Neutron("Images/D.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
                neutron_group.add(new_neutron)
                all_sprites.add(new_neutron)

        pygame.display.flip()
        clock.tick(60)

def simulacion_TTHe():
    # Grupo de Neutrones
    default_N = Neutron("Images/T.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Images/T.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,11):
        new_atom = Uranium("Images/T.png",random.randint(50,900), random.randint(0,600))
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

    running =True
    while running:       
        #movimiento del neutron (por elmomento ciclico)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                sys.exit(0)
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False

        pygame.display.flip()
        screen.fill(BLACK)
        
        all_sprites.draw(screen)
        all_sprites.update() 

        hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
        for hit in hits:
            print(hit)
            for n in range(0,1):
                barium = Barium("Images/He.png",hit.rect.center)
                kripton = Kripton("Images/neutron.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)
            for b in range(0,2):    
                kripton = Kripton("Images/neutron.png",hit.rect.center)
                kripton_group.add(kripton)
                all_sprites.add(kripton)
            for n in range(0,1):
                new_neutron = Neutron("Images/T.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
                neutron_group.add(new_neutron)
                all_sprites.add(new_neutron)

        pygame.display.flip()
        clock.tick(60)

# simulacion_UrKrBa()
# simulacion_MgHNa()
# simulacion_DTHe()
# simulacion_TTHe()
main_menu()
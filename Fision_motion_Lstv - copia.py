#import cx_Freeze
import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import time

pygame.init()
tamaño = (1000, 700)
screen = pygame.display.set_mode(tamaño)
pygame.display.set_caption("simulacion: Reacción Nuclear ")
# Constantes

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
BLUE =  (   0,   0, 255)
RED =   ( 255,   0,   0)
GREEN = (   0, 255,   0)


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
            # self.kill()
            self.speed_N[0] *= -1
        if self.rect.top <= 0 or self.rect.bottom >=700:
            # self.kill()
            self.speed_N[1] *= -1

class Uranium(pygame.sprite.Sprite):
    def __init__(self,picture_path,coordx,coordy):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [coordx, coordy]
        self.speed_Ur = [random.randint(-4,4),random.randint(-4,4)]
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

        
        if self.rect.left <= 0 or self.rect.right >=1000:
            self.speed_Kr[0] *= -1
            # self.kill()

            
        if self.rect.top <= 0 or self.rect.bottom >=700:
            self.speed_Kr[1] *= -1
          # self.kill()
          
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
            self.speed_Ba[0] *=-1
            # self.kill()

        if self.rect.top <= 0 or self.rect.bottom >=700:
            self.speed_Ba[1] *= -1
          # self.kill()

# Funciones
def draw_text(text,size, color, surface, x, y):
    font = pygame.font.SysFont(None, size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    global click
    clock = pygame.time.Clock()
    
    base_font = pygame.font.Font(None,50)
    user_text = ""
    react1= pygame.image.load("react1.png")
    react2 = pygame.image.load("react2.png")
    react3 = pygame.image.load("react3.png")
    react4 = pygame.image.load("react4.png")
    settings = pygame.image.load("settings.png")
    while True:
 
        screen.fill((174,197,190))

        draw_text('Reacciones Nucleares',75, (252, 237, 0), screen, 20, 20)
        draw_text('Fisión',50, (245, 241, 189), screen, 230, 240)
        draw_text('Fusión',50, (245, 241, 189), screen, 680, 240)
        draw_text('Cantidad de colisiones: ',50, (245, 241, 189), screen, 106, 150)
        mx, my = pygame.mouse.get_pos()
        
        
        button_1 = pygame.Rect(106, 301, 349, 89)
        button_3 = pygame.Rect(556, 301, 349, 89)
        button_4 = pygame.Rect(556, 501, 349, 89)
        button_2 = pygame.Rect(106, 501, 349, 89)
        button_opt = pygame.Rect(911, 0, 89, 89)

        pygame.draw.rect(screen,(0,255,0), button_1)
        pygame.draw.rect(screen,(0,0,255), button_2)
        pygame.draw.rect(screen,(255,0,0), button_3)
        pygame.draw.rect(screen,(255,255,255), button_4)
        pygame.draw.rect(screen,(156,126,108), button_opt)
        if button_1.collidepoint((mx, my)):
            if click:
                simulacion_UrKrBa(user_text)
                calculatorUrKr(user_text)
        if button_2.collidepoint((mx, my)):
            if click:
                simulacion_MgHNa(user_text)
                calculatorMgNa(user_text)
        if button_3.collidepoint((mx, my)):
            if click:
                simulacion_DTHe(user_text)
                calculatorTD(user_text)
        if button_4.collidepoint((mx, my)):
            if click:
                simulacion_TTHe(user_text)
                calculatorTT(user_text)
        if button_opt.collidepoint((mx, my)):
            if click:
                pofis()
        pygame.draw.rect(screen, (0,255,0), button_1)
        pygame.draw.rect(screen, (0,0,255), button_2)
        pygame.draw.rect(screen, (255,0,0), button_3)
        pygame.draw.rect(screen, (255,255,255), button_4)
        pygame.draw.rect(screen, (156,126,108), button_opt)
 
        click = False
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_TAB:
                    pygame.quit()
                    sys.exit()
                if evento.key == GAME_GLOBALS.K_DELETE:
                    user_text = ""
            if evento.type == GAME_GLOBALS.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True
            if evento.type == GAME_GLOBALS.KEYDOWN:
                user_text += evento.unicode
            
        screen.blit(pygame.transform.scale(react1,(380,90)),(100, 300))
        screen.blit(pygame.transform.scale(react2,(380,90)),(100, 500))
        screen.blit(pygame.transform.scale(react3,(380,90)),(550, 300))
        screen.blit(pygame.transform.scale(react4,(380,90)),(550, 500))
        screen.blit(pygame.transform.scale(settings,(89,89)),(911, 0))
        text_surface = base_font.render(user_text,True,(255,255,255))
        screen.blit(text_surface,(520, 152))
        pygame.display.update()
        clock.tick(60)

def simulacion_UrKrBa(num_col): 
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 
    # Grupo de Neutrones
    default_N = Neutron("neutron.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)
    for atom in range(0,int(num_col)):
        new_atom = Neutron("neutron.png",random.randint(50,900), random.randint(0,600),random.randint(-5,6),random.randint(-5,6))
        neutron_group.add(new_atom)
    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Uranio.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,int(num_col)):
        new_atom = Uranium("Uranio.png",random.randint(50,900), random.randint(0,600))
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

    Bgnd= pygame.image.load("Reactor_bk.png")
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
                    num_col = 0
        
        
        #Activates the atoms' motion once collision is produced
        hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
        for hit in hits:
            print(hit)

            for n in range(0,1): 
                barium = Barium("Bario.png",hit.rect.center)
                kripton = Kripton("Kripton.png",hit.rect.center)
    
                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            for n in range(0,3):
                new_neutron = Neutron("neutron.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
                neutron_group.add(new_neutron)
                all_sprites.add(new_neutron)
        
        
        screen.blit(pygame.transform.scale(Bgnd,(1000,700)),(0,0))
          
        all_sprites.draw(screen)
        all_sprites.update()    
        pygame.display.flip()  
        clock.tick(60)

def simulacion_MgHNa(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 

    # Grupo de Neutrones
    default_N = Neutron("neutron.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)
    for atom in range(0,int(num_col)):
        new_atom = Neutron("neutron.png",random.randint(50,900), random.randint(0,600),random.randint(-7,6),random.randint(-7,6))
        neutron_group.add(new_atom)
    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("Mg.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,int(num_col)):
        new_atom = Uranium("Mg.png",random.randint(50,900), random.randint(0,600))
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

    Bgnd= pygame.image.load("Reactor_bk.png")
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
        
        

        
        #Activates the atoms' motion once collision is produced
        # if pygame.sprite.groupcollide(uranium_group,neutron_group,True,True):
        hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
        for hit in hits:
            print(hit)
            for n in range(0,1):
                barium = Barium("D.png",hit.rect.center)
                kripton = Kripton("Na.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            # for n in range(0,5):
            #     new_neutron = Neutron("neutron.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
            #     neutron_group.add(new_neutron)
            #     all_sprites.add(new_neutron)
        screen.blit(pygame.transform.scale(Bgnd,(1000,700)),(0,0))
        all_sprites.draw(screen)
        all_sprites.update() 
        pygame.display.flip()
        clock.tick(60)

def simulacion_DTHe(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 

    # Grupo de Neutrones
    default_N = Neutron("D.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)
    for atom in range(0,int(num_col)):
        new_atom = Neutron("D.png",random.randint(50,900), random.randint(0,600),random.randint(-6,6),random.randint(-5,5))
        neutron_group.add(new_atom)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("T.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,int(num_col)):
        new_atom = Uranium("T.png",random.randint(50,900), random.randint(0,600))
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
    Bgnd= pygame.image.load("Reactor_bk.png")
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
        
        

        
        #Activates the atoms' motion once collision is produced
        # if pygame.sprite.groupcollide(uranium_group,neutron_group,True,True):
        hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
        for hit in hits:
            print(hit)
            for n in range(0,1):
                barium = Barium("He.png",hit.rect.center)
                kripton = Kripton("neutron.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

            # for n in range(0,1):
            #     new_neutron = Neutron("D.png",hit.rect.centerx,hit.rect.centery,random.choice((-5,-4,-3,-2,2,3,4,5)),random.choice((-2,-1,1,2)))
            #     neutron_group.add(new_neutron)
            #     all_sprites.add(new_neutron)
        screen.blit(pygame.transform.scale(Bgnd,(1000,700)),(0,0))
        all_sprites.draw(screen)
        all_sprites.update() 
        pygame.display.flip()
        clock.tick(60)

def simulacion_TTHe(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 

    # Grupo de Neutrones
    default_N = Neutron("T.png",100, 350,random.randint(1,7),0)
    neutron_group = pygame.sprite.Group()
    neutron_group.add(default_N)
    for atom in range(0,int(num_col)):
        new_atom = Neutron("T.png",random.randint(50,900), random.randint(0,600),random.randint(-6,6),random.randint(-6,6))
        neutron_group.add(new_atom)

    # Grupo-Atomos de uranio
    uranium_group = pygame.sprite.Group()
    default_uranium = Uranium("T.png",random.randint(120,800), 350)
    uranium_group.add(default_uranium)
    for atom in range(0,int(num_col)):
        new_atom = Uranium("T.png",random.randint(50,900), random.randint(0,600))
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
    Bgnd= pygame.image.load("Reactor_bk.png")
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
        
       

        hits =  pygame.sprite.groupcollide(uranium_group,neutron_group,True,True)
        for hit in hits:
            print(hit)
            for n in range(0,1):
                barium = Barium("He.png",hit.rect.center)

                barium_group.add(barium)
                all_sprites.add(barium)

            for b in range(0,2):    
                kripton = Kripton("neutron.png",hit.rect.center)
                kripton_group.add(kripton)
                all_sprites.add(kripton)

        
        screen.blit(pygame.transform.scale(Bgnd,(1000,700)),(0,0))
        all_sprites.draw(screen)
        all_sprites.update() 
        pygame.display.flip()
        clock.tick(60)

#Calculadoras
def calculatorUrKr(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('La energía liberada es:',100, (11, 235, 167), screen, 0, 0)
        
        Energy = round((int(num_col)+1)*((1.008665+235.043939)-((3*1.008665)+141.9164+90.923))*931.48,4)
        Result = str(Energy)+" MeV"+" (Exotermica)"
        draw_text(Result, 70, (255, 255, 45), screen, 150, 350)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False


                    

        pygame.display.update()
        clock.tick(60)

def calculatorMgNa(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass  
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('La energía liberada es:',100, (11, 235, 167), screen, 0, 0)
        Q = (int(num_col)+1)*((1.008665+24.98583)-(2.014102+23.99096))
        Energy = str(round(Q*931.48,5))
        Result = Energy+" MeV"+" (Endotermica)"
        draw_text(Result, 70, (255, 255, 45), screen, 50, 350)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False


                    

        pygame.display.update()
        clock.tick(60)

def calculatorTD(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('La energía liberada es:',100, (11, 235, 167), screen, 0, 0)
        Q = (int(num_col)+1)*((2.014102+3.016030)-(4.00263+1.008665))
        Energy = str(round(Q*931.48,5))
        Result = Energy+" MeV"+" (Exotermica)"
        draw_text(Result, 70, (255, 255, 45), screen, 150, 350)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False         

        pygame.display.update()
        clock.tick(60)

def calculatorTT(num_col):
    try:
        try:
            num_col =int(num_col)
        except:       
            print("fallo") 
            if num_col == "":
                num_col =0
            if num_col.isdigit()==False:
                num_col = 0
                print(num_col)
            if int(num_col)>300:
                num_col = 0
    except:
        pass 
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('La energía liberada es:',100, (11, 235, 167), screen, 0, 0)
        Q = (int(num_col)+1)*((2*3.016030)-(4.00263+2*1.008665))
        Energy = str(round(Q*931.48,5))
        Result = Energy+" MeV"+" (Exotermica)"
        draw_text(Result, 70, (255, 255, 45), screen, 125, 350)
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False   

        pygame.display.update()
        clock.tick(60)

#Instrucciones e informacion personal:
def pofis():
    
    clock = pygame.time.Clock()
    inst = pygame.image.load("Instructions.png")
    running = True
    while running:
        screen.fill((255,255,255))

        
        
        for evento in GAME_EVENTS.get():
            if evento.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == GAME_GLOBALS.KEYDOWN:
                if evento.key == GAME_GLOBALS.K_ESCAPE:
                    running = False   
        screen.blit(pygame.transform.scale(inst,(800,600)),(0,0))
        pygame.display.update()
        clock.tick(60)
main_menu()

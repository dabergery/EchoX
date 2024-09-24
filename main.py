import pygame
import sys
from pygame import mixer
import cv2
import numpy as np

pygame.init()
Running = True
screen = pygame.display.set_mode((600, 1080))
pygame.display.set_caption("echoX Game Musique")
icon = pygame.image.load("Icon.ico")
pygame.display.set_icon(icon)
# Représentation des touches de jeu, info de position, de couleur, et etat de pression
class Key:
    def __init__(self, x, y, color1, color2, key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pygame.Rect(self.x, self.y, 80, 25)
        self.handled = False
keys = [
    Key(100, 800, (255, 153, 187), (255, 34, 119), pygame.K_q),
    Key(200, 800, (119, 255, 255), (68, 170, 255), pygame.K_s),
    Key(300, 800, (255, 153, 255), (255, 102, 221), pygame.K_d),
    Key(400, 800, (119, 255, 204), (0, 221, 170), pygame.K_f),
]
class Button:
    def __init__(self, x, y, img, img_br):
        self.img = img
        self.img_br = img_br
        self.button = self.img.get_rect(center=(x, y))
    def draw(self, pos):
        mouse = pygame.mouse.get_pos()
        self.highlighted = self.button.collidepoint(mouse)
        if self.highlighted:
            pos.blit(self.img_br, self.button)
        else:
            pos.blit(self.img, self.button)
    def is_clicked(self, pos):
        return self.button.collidepoint(pos)
Tx_St = pygame.image.load('Start.png').convert_alpha()
Tx_St_Br = pygame.image.load('Start_Br.png').convert_alpha()
Tx_Se = pygame.image.load('Settings.png').convert_alpha()
Tx_Se_Br = pygame.image.load('Settings_Br.png').convert_alpha()
Tx_Qu = pygame.image.load('Quit.png').convert_alpha()
Tx_Qu_Br = pygame.image.load('Quit_Br.png').convert_alpha()
Tx_Pa = pygame.image.load('Pause.png').convert_alpha()
Tx_Pa_Br = pygame.image.load('Pause_Br.png').convert_alpha()
Tx_Re = pygame.image.load('Retour.png').convert_alpha()
Tx_Re_Br = pygame.image.load('Retour_Br.png').convert_alpha()
Tx_Me = pygame.image.load('Menu.png').convert_alpha()
Tx_Me_Br = pygame.image.load('Menu_Br.png').convert_alpha()
Tx_One_Br = pygame.image.load('Music_One_Br.png').convert_alpha()
Tx_One = pygame.image.load('Music_One.png').convert_alpha()
Tx_Two = pygame.image.load('Music_Two.png').convert_alpha()
Tx_Two_Br = pygame.image.load('Music_Two_Br.png').convert_alpha()
Tx_Three = pygame.image.load('Music_Three.png').convert_alpha()
Tx_Three_Br = pygame.image.load('Music_Three_Br.png').convert_alpha()
Tx_Four = pygame.image.load('Music_Four.png').convert_alpha()
Tx_Four_Br = pygame.image.load('Music_Four_Br.png').convert_alpha()
Tx_Five = pygame.image.load('Music_Five.png').convert_alpha()
Tx_Five_Br = pygame.image.load('Music_Five_Br.png').convert_alpha()
Start = pygame.transform.scale(Tx_St, (100, 100))
Start_Br = pygame.transform.scale(Tx_St_Br, (100, 100))
Settings = pygame.transform.scale(Tx_Se, (100, 100))
Settings_Br = pygame.transform.scale(Tx_Se_Br, (100, 100))
Pause = pygame.transform.scale(Tx_Pa, (100, 100))
Pause_Br = pygame.transform.scale(Tx_Pa_Br, (100, 100))
Quit = pygame.transform.scale(Tx_Qu, (100, 100))
Quit_Br = pygame.transform.scale(Tx_Qu_Br, (100, 100))
Retour = pygame.transform.scale(Tx_Re, (100, 100))
Retour_Br = pygame.transform.scale(Tx_Re_Br, (100, 100))
Menu = pygame.transform.scale(Tx_Me, (100, 100))
Menu_Br = pygame.transform.scale(Tx_Me_Br, (100, 100))
w75 = 75
Music_One = pygame.transform.scale(Tx_One, (w75, w75))
Music_One_Br = pygame.transform.scale(Tx_One_Br, (w75, w75))
Music_Two = pygame.transform.scale(Tx_Two, (w75, w75))
Music_Two_Br = pygame.transform.scale(Tx_Two_Br, (w75, w75))
Music_Three = pygame.transform.scale(Tx_Three, (w75, w75))
Music_Three_Br = pygame.transform.scale(Tx_Three_Br, (w75, w75))
Music_Four = pygame.transform.scale(Tx_Four, (w75, w75))
Music_Four_Br = pygame.transform.scale(Tx_Four_Br, (w75, w75))
Music_Five = pygame.transform.scale(Tx_Five, (w75, w75))
Music_Five_Br = pygame.transform.scale(Tx_Five_Br, (w75, w75))
button_Start = Button(200, 300, Start, Start_Br)
button_Settings = Button(300, 300, Settings, Settings_Br)
button_Quit = Button(400, 300, Quit, Quit_Br)
button_Pause = Button(300, 300, Pause, Pause_Br)
button_Retour = Button(540, 590, Retour, Retour_Br)
button_Menu = Button(300, 400, Menu, Menu_Br)
button_Music_One = Button(90, 220, Music_One, Music_One_Br)
button_Music_Two = Button(340, 220, Music_Two, Music_Two_Br)
button_Music_Three = Button(90, 320, Music_Three, Music_Three_Br)
button_Music_Four = Button(340, 320, Music_Four, Music_Four_Br)
button_Music_Five = Button(90, 420, Music_Five, Music_Five_Br)
g = {
    "Actual_Song": 'BGM_Error.mp3',
    "Actual_Map": 'map5.txt',
    "Actual_BG": 'BG_Error.png',
    "Actual_Vid": 'acat.mp4',
    "Actual_Map_data": ['test', 'test2', None],
    "started": True,
    "Paused": False,
    "reload": 0,
}
def Error():
    print("Get Error")
    screen.blit(pygame.image.load(g["Actual_BG"]), (0, 0))
    mixer.music.load('BGM_Error.mp3')
    mixer.music.play()
    pygame.display.flip()
    pygame.time.delay(1000)
    Select_level(g["Actual_Song"], g["Actual_Map"], g["Actual_BG"])
def Select_level(Actual_Song, Actual_Map, Actual_BG):
    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_BG"])
    g["Paused"] = False
    while True:
        screen.blit(pygame.image.load('BG_Pistes.png'), (0, 0))
        screen.blit(pygame.image.load('color.png'), (60, 470))
        button_Music_One.draw(screen)
        button_Music_Two.draw(screen)
        button_Music_Three.draw(screen)
        button_Music_Four.draw(screen)
        button_Music_Five.draw(screen)
        button_Retour.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_Music_One.is_clicked(event.pos):
                    g["Actual_Song"] = 'BGM_Electric_Angel.mp3'
                    g["Actual_BG"] = 'BG_Electric_Angel.png'
                    g["Actual_Map"] = 'map1.txt'
                    g["Actual_Vid"] = 'Vid_Ele.mp4'
                    mixer.music.load('NoBGM_Ele.mp3')
                    mixer.music.play(-1)
                    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_Vid"])
                elif button_Music_Two.is_clicked(event.pos):
                    g["Actual_Song"] = 'BGM_Psychedelic_Void.mp3'
                    g["Actual_BG"] = 'BG_Psychedelic_Void.png'
                    g["Actual_Map"] = 'map2.txt'
                    g["Actual_Vid"] = 'Vid_Psy.mp4'
                    mixer.music.load('NoBGM_Psy.mp3')
                    mixer.music.play(-1)
                    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_Vid"])
                elif button_Music_Three.is_clicked(event.pos):
                    g["Actual_Song"] = 'BGM_Germany.mp3'
                    g["Actual_BG"] = 'BG_Germany.png'
                    g["Actual_Map"] = 'map3.txt'
                    g["Actual_Vid"] = 'Vid_Dan.mp4'
                    mixer.music.load('NoBGM_Dan.mp3')
                    mixer.music.play(-1)
                    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_Vid"])
                elif button_Music_Four.is_clicked(event.pos):
                    g["Actual_Song"] = 'BGM_Break_the_rules.mp3'
                    g["Actual_BG"] = 'BG_Break_the_rules.png'
                    g["Actual_Map"] = 'map4.txt'
                    g["Actual_Vid"] = 'Vid_Bre.mp4'
                    mixer.music.load('NoBGM_Bre.mp3')
                    mixer.music.play(-1)
                    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_Vid"])
                elif button_Music_Five.is_clicked(event.pos):
                    g["Actual_Song"] = 'BGM_Plants_Vs_Zombies.mp3'
                    g["Actual_BG"] = 'BG_Plants_Vs_Zombies.png'
                    g["Actual_Map"] = 'map5.txt'
                    g["Actual_Vid"] = 'Vid_Pla.mp4'
                    mixer.music.load('NoBGM_Pla.mp3')
                    mixer.music.play(-1)
                    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_BG"]), g["Actual_Song"]
                elif button_Retour.is_clicked(event.pos):
                    mixer.music.stop()
                    main_menu(0)
        pygame.display.flip()

def load():
    map = g["Actual_Map"]
    rects = []
    f = open(map, "r")
    data = f.readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25, y * -100, 50, 25))
    return rects
map_rect = load()
def Pause():
    mixer.music.pause()
    while Running:
        g["Paused"] = True
        screen.blit(pygame.image.load('BG_Pause.png'), (0, 0))
        button_Start.draw(screen)
        button_Quit.draw(screen)
        button_Menu.draw(screen)
        for event in pygame.event.get():
            # Bouton Start
            if event.type == pygame.MOUSEBUTTONDOWN and button_Start.is_clicked(event.pos):
                screen.blit(pygame.image.load(g["Actual_BG"]), (0, 0))
                mixer.music.unpause()
                Start_Level(g["Actual_Map"], True)
            # Touche Echap
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                screen.blit(pygame.image.load(g["Actual_BG"]), (0, 0))
                mixer.music.unpause()
                Start_Level(g["Actual_Map"], True)
            # Bouton Quitter
            if event.type == pygame.MOUSEBUTTONDOWN and button_Quit.is_clicked(event.pos):
                pygame.quit()
                sys.exit()
            # Bouton Menu
            if event.type == pygame.MOUSEBUTTONDOWN and button_Menu.is_clicked(event.pos):
                g["Paused"] = False
                main_menu(0)
        pygame.display.update()

def Level_Setings():
    g["Actual_BG"] = 'BG_Level_Options'
    screen.blit(pygame.image.load(g["Actual_BG"]), (0, 0))
    button_Start.draw(screen)
    pygame.display.update()
def Start_Level(map, Paused):
    if g["Actual_BG"] == 'BG_Error.png':
        Error()
    if Paused:
        mixer.music.unpause()
    else:
        mixer.music.load(g["Actual_Song"])
        mixer.music.play()
    print("Paused=", g["Paused"])
    cap = cv2.VideoCapture(g["Actual_Vid"])
    while Running:
        screen.blit(pygame.image.load(g["Actual_BG"]), (0, 0))
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            frame = pygame.transform.scale(frame, (600, 1080))
            screen.blit(frame, (0, 0))

        for rect in map_rect:
            if not g["reload"]:
                g["reload"] = (rect.y)
            pygame.draw.rect(screen, (200, 0, 0), rect)
            rect.y += 20
            for key in keys:
                if key.rect.colliderect(rect) and not key.handled:
                    map_rect.remove(rect)
                    break

        k = pygame.key.get_pressed()
        for key in keys:
            if k[key.key]:
                pygame.draw.rect(screen, key.color1, key.rect)
                key.handled = False
            else:
                pygame.draw.rect(screen, key.color2, key.rect)
                key.handled = True
        pygame.display.flip()
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Pause()
    cap.release()
    cv2.destroyAllWindows()
    fade(g["Actual_Song"], 'Pasmal.png')
    main_menu(0)
def fade(img1, img2):
    fade = pygame.Surface((600, 1080))
    fade.fill((0, 0, 0))
    opacity = 0
    img1 = pygame.image.load('fade1.png')
    img2 = pygame.image.load('fade2.png')
    screen.blit(pygame.image.load('fade1.png'), (0, 0))
    pygame.display.update()
    pygame.time.delay(500)
    for r in range(0, 300):
        opacity += 1
        fade.set_alpha(opacity)
        screen.blit(img1, [0, 0])
        screen.blit(fade, (0, 0))
        pygame.display.update()
    for r in range(0, 300):
        opacity -= 1
        fade.set_alpha(opacity)
        screen.blit(img2, [0, 0])
        screen.blit(fade, (0, 0))
        pygame.display.update()
    pygame.time.delay(2000)


def main_menu(s):
    if s:
        fade('fade1.png', 'fade2.png')
    # Boucle principale
    print("\nGlobal\n", g["Actual_Song"], "\n", g["Actual_Map"], "\n", g["Actual_Vid"])
    while True:
        screen.fill((0, 0, 0))
        screen.blit(pygame.image.load('BG_Menu.png'), (0, 0))
        button_Start.draw(screen)
        button_Settings.draw(screen)
        button_Quit.draw(screen)
        pygame.display.flip()
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_Start.is_clicked(event.pos):
                Start_Level(g["Actual_Song"], False)
            if event.type == pygame.MOUSEBUTTONDOWN and button_Settings.is_clicked(event.pos):
                Select_level(g["Actual_Song"], g["Actual_Map"], g["Actual_BG"])
            if event.type == pygame.MOUSEBUTTONDOWN and button_Quit.is_clicked(event.pos):
                pygame.quit()
                sys.exit()
main_menu(1)
Error()

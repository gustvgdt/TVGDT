﻿import pygame as pg
import globals
from helper import *
import math

class Personnage(pg.sprite.Sprite):
    """Classe générant le héros"""
    
    def __init__(self, image_path, position, max_life, atk, max_speed) :
        
        pg.sprite.Sprite.__init__(self)
        try:
            print(load_image)
            self.image_all = load_image(image_path, -1)[0] #sprite sheet
        except:
            print("Impossible de charger l'image du personnage")
        rect_tab = [[pg.Rect(32*i, 48*j, 32, 48) for j in range(4)] for i in range(4)]
        self.images = [[self.image_all.subsurface(rect_tab[i][j]) for i in range(4)] for j in range(4)]
        self.image = self.images[0][0]
        self.position = position
        self.rect = pg.rect.Rect(position[0],position[1], 32, 48)
        self.speed = max_speed
        self.life = max_life
        self.atk = atk #attaque de l'entité
        self.state = 0 #Défini l'état de l'entité (0 : immobile, 1: mouvement, 2: attaque, 3: touché)
        self.aim = 0 #"angle" de visé de l'entité
        self.cpt = 40
        self.i_image = 0
        self.j_image = 0

    def update(self):
        vertical_move = 1 if globals.keyPressed['down'] else -1 if globals.keyPressed['up'] else 0
        horizontal_move = 1 if globals.keyPressed['right'] else -1 if globals.keyPressed['left'] else 0
        if vertical_move != 0 or horizontal_move != 0:
            globals.hero.move((horizontal_move, vertical_move))
            self.cpt -= 1
            if self.cpt == 0:
                self.cpt = 40
        else:
            
            self.image = self.images[self.i_image][0]

    def turn(self, angle):
        """Permet à l'entité de tourner sur elle-même d'un angle"""
        if self.aim != angle:
            self.aim = angle
            self.state = 1
            #Penser à modifier l'image du perso
        

    def get_env(self):
        """Récupère le "statut" des 9 cases entourant l'entité, renvoie un dict avec comme clés les coordonnées des cases.
        Ce dict contient des bool selon que la case est occupée par un elt du décors ou par une autre entité"""

        return env


    def collision(self, direction, env):
        """Détecte"""
        return pg.sprite.spritecollide
    
    def move(self, direction, collision = False):
        """Déplace l'entité d'une case dans la direction choisie(tableau de 2 entiers contenus dans {-1; 0; 1})
        si le test de collision renvoi False"""

        if direction[0] != 0 and direction[1] == 0:
            new_x = self.position[0] + self.speed*direction[0]
            new_y = self.position[1]
        elif direction[1] != 0 and direction[0] == 0:
            new_y = self.position[1] + self.speed*direction[1]
            new_x = self.position[0]
        elif direction[1] != 0 and direction[0] != 0:
            speed = math.ceil(self.speed/math.sqrt(2))
            new_x = self.position[0] + speed*direction[0]
            new_y = self.position[1] + speed*direction[1]
        
        t=self.cpt
        if t>30:
            self.j_image = 0
        elif t>20:
            self.j_image = 1
        elif t>10:
            self.j_image = 2
        else:
            self.j_image = 3

        if collision != True:

            if new_y > self.position[1]:
                self.image = self.images[0][0]
                self.i_image = 0
                
            elif new_x < self.position[0]:
                self.image = self.images[1][0]
                self.i_image = 1
            elif new_x > self.position[0]:
                self.image = self.images[2][0]
                self.i_image = 2
            elif new_y < self.position[1]:
                self.image = self.images[3][0]
                self.i_image = 3
                
            self.position = [new_x, new_y]
##            print("moves to: ", self.position)
            self.rect.move_ip(direction[0], direction[1])
            self.state = 1
            self.image = self.images[self.i_image][self.j_image]

    def reset_state(self):
                            
        if self.state != 0:
            self.state = 0

    def attack(self):
        """Renvoi une liste avec coordonnées de la case vers laquelle le personnage attaque
        ainsi que les points d'attaque infligés"""
        dir_x = self.position[0] + self.angle[0]
        dir_y = self.position[1] + self.angle[1]
        cible = [dir_x, dir_y]
        #Eventuellement ajouter une fonction aléatoire pour déterminer, à partir de self.atk, les points d'attaque
        pt_atk = self.atk
        self.state = 2
        return [cible, pt_atk]

    def getHit(self, pnj_atk):
        self.life -= pnj_atk
        self.state = 3




    

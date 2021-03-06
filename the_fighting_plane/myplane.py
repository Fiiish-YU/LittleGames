# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:44:54 2020

@author: xun
"""
import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image1 = pygame.image.load("images/plane1.png").convert_alpha()
        self.image2 = pygame.image.load("images/plane2.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left,self.rect.top = \
                                       (self.width - self.rect.width) // 2,\
                                       self.height - self.rect.height - 60
        self.speed = 4
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)
    
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
    
    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60
    
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
            
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width
            
    def reset(self):
        self.rect.left,self.rect.top = \
                                       (self.width - self.rect.width) // 2,\
                                       self.height - self.rect.height - 60
        self.active = True
        self.invincible = True                          
            
            
            
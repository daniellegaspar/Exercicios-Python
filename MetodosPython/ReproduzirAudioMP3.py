'''Faça um programa em python que abra e reproduza o áudio
de um arquivo MP3'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar... ')
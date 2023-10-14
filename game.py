import pgzrun
import pygame
import random

pygame.mouse.set_visible(False)

WIDTH = 1200
HEIGHT = 700

target = Actor('target_red1')
target.x = 100
target.y = 200

duck = Actor('duck_brown')
duck.x = 500
duck.y = 200

duck2 = Actor('duck_yellow')
duck2.center = WIDTH/2, HEIGHT-50

cursor = Actor('crosshair_outline_large')
cursor.score = 0

def on_mouse_move(pos):
    cursor.pos = pos

def on_mouse_down(pos):
    sounds.biggun.play()
    cursor.score -= 1
    if cursor.colliderect(target):
        target.right = 0
        target.y = random.randint(0, HEIGHT)
        cursor.score += 11
    
    if cursor.colliderect(duck):
        duck.right = 0
        duck.y = random.randint(0, HEIGHT)
        cursor.score -= 9

    if cursor.colliderect(duck2):
        duck2.left = WIDTH
        duck2.y = random.randint(0, HEIGHT)
        cursor.score -= 19

def update():
    duck.x += 5
    if duck.left> WIDTH:
        duck.right = 0
        
        
    duck2.x -= 5
    if duck2.right< 0:
        duck2.left = WIDTH

    target.x += 5
    if target.left> WIDTH:
        target.right = 0

def draw():
    screen.clear()
    screen.draw.text(f"Score: {cursor.score}",
                    (10,10), color = "white", fontsize = 30)
    target.draw()
    duck.draw()
    duck2.draw()
    cursor.draw()

pgzrun.go()
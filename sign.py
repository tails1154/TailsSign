print("TailsSign v1.0 Pre-Init");
import pygame
import tkinter as tk
import requests
import time
import sys
import traceback
import os
print("[ OK ] Pre-Init Finished");
print("TailsSign v1.0 Init");
pygame.init();
pygame.font.init()
text = pygame.font.SysFont("Comic Sans MS", 150)
print("Loading config.txt");
windownamenext=False
conf = open("configsign.txt", "rt")
print("[ OK ] Opened configsign.txt")
print("Loading Config")
for x in conf:
    if x == "window=True\n":
        window=True
    elif x == "debug=True\n":
        debug=True
    elif x == "debug=False\n":
        debug=False
    elif x == "window=False\n":
        window=False
    elif x == "audio=True\n":
        audio=True
    elif x == "audio=False\n":
        audio=False
    elif x == "end":
        print("end of config reached");
print("Loading confighostsign.txt")
conf2 = open("confighostsign.txt", "rt")
host=conf2.read()
print("[ OK ] Read confighost.txt");
flags = pygame.FULLSCREEN
if window:
    screen = pygame.display.set_mode((1280, 720))
else:
    screen = pygame.display.set_mode((1280, 720), flags)
clock = pygame.time.Clock()
running = True
introPlaying = False
connected = False
pygame.display.set_caption("TailsSign")

print("[ OK ] Window Created")
print("[ OK ] Init Complete")
screen.fill("lightblue")
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Shutting Down TailsSign");
                pygame.quit()
        try:
            def connect():
                try:
                    text_surface = text.render("Connecting...", False, (0, 0, 0))
                    screen.blit(text_surface, (500, 500))
                    pygame.display.flip();
                    pygame.mixer.music.load("audio/connect.mp3", "mp3")
                    if audio: pygame.mixer.music.play(-1);
                    time.sleep(1)
                    request = requests.get(host + "connect")
                    if request.status_code == 200:
                        print("connected")
                        connected=True
                        pygame.mixer.music.stop()
                        return True
                    else:
                        return False
                except:
                        print("[ ERR ] Error Occoured while connecting! Exiting");
                        print("Error! Shutting down...")
                        traceback.print_exc()
                        return False

                    
            def showsign():
                screen.fill("lightblue");
                request = requests.get(host + "getsign")
                if request.status_code == 200:
                    content = request.content.decode()
                    text_surface = text.render(content, False, (0, 0, 0))
                    screen.blit(text_surface, (0, 360))
                    pygame.display.flip();
                else:
                    print("[ ERR ] did not get 200 status code");
            if connected:
                showsign()
            else:
                if connect():
                    connected = True
                
        except:
            print("Error! Shutting down...")
            traceback.print_exc()
            running = False

        
        
        
pygame.quit()


import pygame
from pygame.sprite import Group 
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
      #  Initialize pygame,settings and create a screen object.
      pygame.init()
      ai_settings = Settings()
      screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
      ai_settings.screen_width = screen.get_rect().width
      ai_settings.screen_height = screen.get_rect().height
      pygame.display.set_caption("Alien Invasion")	
      
      # Made the Play button.
      play_button = Button(ai_settings, screen, "Play")
           
      # Created an instance to store game statistics and created a scoreboard.
      stats = GameStats(ai_settings)    
      sb = Scoreboard(ai_settings, screen, stats)
      # Set the background color.
      bg_color = (230, 230, 230) 
         
      # Made a ship.
      ship = Ship(ai_settings, screen)
      # Made a group to store bullets in.
      bullets = Group()     
      # Made a group of aliens.
      aliens = Group()
      # Created the fleet of aliens.
      gf.create_fleet(ai_settings, screen, ship, aliens)
           
      
      # Start the main loop for the game.
      while True:         	
         gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
         if stats.game_active: 
             ship.update()  
             gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
             gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
             
         gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
                       
run_game() 

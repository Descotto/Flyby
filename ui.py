import pygame
from settings import *

class UI:
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont(UI_FONT, UI_FONT_SIZE)

        # bar setup
        self.hp_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.support_bar_rect = pygame.Rect(10, 30, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.shield_bar_rect = pygame.Rect(10, 50, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        


    def show_bar(self, current, max_amount,bg_rect,color):
        # draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        # convert stats to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # draw the bar
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect,3)

        # Display current and max health text
        health_text = f"{int(current)}/{int(max_amount)}"
        small_font = pygame.font.Font(None, 24)  
        text_surf = small_font.render(health_text, False, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=(bg_rect.centerx, bg_rect.centery))

        self.display_surface.blit(text_surf, text_rect)

    def show_support_bar(self, support_available):
        

        # Check if support is available
        if support_available:
            text = "Support Ready!"
            color = (0, 255, 0)   
        else:
            text = "Wait"
            color = (128, 128, 128)  
        # draw bg
        pygame.draw.rect(self.display_surface,color,self.support_bar_rect)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,self.support_bar_rect,3)

        # Display the text
        small_font = pygame.font.Font(None, 24)
        text_surf = small_font.render(text, False, (0,0,0))
        text_rect = text_surf.get_rect(center=(self.support_bar_rect.centerx, self.support_bar_rect.centery))

        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.support_bar_rect, 3)

    def show_shield_bar(self, shield_active, shield_ready, charging, current_hp, max_hp, bg_rect):
        # Check if the shield is active
        if shield_active:
            # Check if the shield is fully charged
            if shield_ready:
                text = "Shield Full"
                color = (0, 255, 0)
            else:
                # Check if the player is charging the shield
                if charging:
                    text = "Charging"
                else:
                    text = f"{int(current_hp)}/{int(max_hp)}"  # Display current and max shield HP
                color = (0, 128, 0)  # Green color for shield bar
        else:
            text = "Shields Depleted"
            color = (128, 128, 128)  # Gray color for inactive shield

        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert shield stats to pixel
        ratio = current_hp / max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # draw the shield bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect, 3)

        # Display text
        small_font = pygame.font.Font(None, 24)
        text_surf = small_font.render(text, False, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=(bg_rect.centerx, bg_rect.centery))

        self.display_surface.blit(text_surf, text_rect)

    def display(self,player):
        self.show_bar(player.hp,10,self.hp_bar_rect, HEALTH_COLOR)
        self.show_support_bar(player.support_available)
        self.show_shield_bar(player.shield_active, player.shield_ready, player.shield_charging, player.shield_hp, 10, self.shield_bar_rect)

        

import random
import  pygame

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.slow import Slow


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = random.randint(200,300)

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and score >= self.when_appers:
            self.power = random.randint(0,2)
            self.when_appers += random.randint(200,300)
            if self.power == 0:
                self.power_ups.append(Shield())
            elif self.power == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Slow())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if self.power == 0:
                    game.player.shield = True
                    game.player.hammer = False
                    game.player.slow = False
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 500)
                elif self.power == 1: 
                    game.player.shield = False
                    game.player.hammer = True
                    game.player.slow = False
                    game.game_speed += 15
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                else:
                    game.player.hammer = False
                    game.player.shield = False
                    game.game_speed -= 10

                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appers = random.randint(200,300)

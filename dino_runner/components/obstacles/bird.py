from dino_runner.utils.constants import BIRD
import random
from dino_runner.components.obstacles.obstacle import Obstacle

RandomBird = [225, 250, 300]

class Bird(Obstacle):
    def __init__(self):
        self.type = random.randint(0, 1)
        super().__init__(BIRD, 0)
        self.rect.y = random.choice(RandomBird)
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
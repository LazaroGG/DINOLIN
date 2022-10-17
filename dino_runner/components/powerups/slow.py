from dino_runner.utils.constants import SLOW, DEFAULT_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Slow(PowerUp):
    def __init__(self):
        self.image = SLOW
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)
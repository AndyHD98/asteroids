class Player(pygame.sprite.Circleshape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
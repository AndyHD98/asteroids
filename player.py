import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0


    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE] and self.shoot_timer == 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (forward * PLAYER_SPEED * dt)


    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.directon = pygame.math.Vector2(0,0)

        self.gravity= 0.8
        self.jump_speed = -16
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.directon.x = -1
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= 30
        elif keys[pygame.K_d]:
            self.directon.x = 1
            if keys[pygame.K_LSHIFT]:
                self.rect.x += 30
        else:
            self.directon.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
    
    def ApplyGravitiy(self):
        self.directon.y += self.gravity
        self.rect.y += self.directon.y

    def jump(self):
        self.directon.y = self.jump_speed

    def update(self):
        self.get_input()
        
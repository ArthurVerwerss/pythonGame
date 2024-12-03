import pygame
from spritesheet.spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('spritesheet.png').parse_sprite('chick.png')
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.12
        self.position, self.velocity = pygame.math.Vector2(
            0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    # To draw our player
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    # Update the player position
    def update(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionx(tiles)
        self.vertical_movement(dt)
        self.checkCollisiony(tiles)

    # acceleration for left and right
    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .9
        elif self.RIGHT_KEY:
            self.acceleration.x += .9
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + \
            (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

    # Juming movement and a check to not fall out of the screen
    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7:
            self.velocity.y = 7
        self.position.y += self.velocity.y * dt + \
            (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01:
            self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionx(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.x > 0:  # Makes the rect hit the right side of the block/tile
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif self.velocity.x < 0:
                self.position.x = tile.rect.right
                self.rect.x = self.position.x

    def checkCollisiony(self, tiles):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:  # Hits tile/block from the top
                self.on_ground = True
                self.on_jumping = False
                self.velocity.y = 0
                self.position.y = tile.rect.top
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:
                self.position.y = tile.rect.bottom + tile.rect.h
                self.rect.bottom = self.position.y

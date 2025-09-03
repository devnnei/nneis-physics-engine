import pygame, sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soft Blocks with Static Collision")

WHITE = (255,255,255)
BLUE = (0,0,255)
GRAY = (100,100,100)
RED = (200,50,50)
GREEN = (50,200,50)

clock = pygame.time.Clock()

player = pygame.Rect(100,200,60,40)
player_vel = pygame.Vector2(0,0)
acc = 0.5
friction = 0.9
max_speed = 6

blocks = [
    pygame.Rect(300,200,100,100),
    pygame.Rect(500,100,150,100)
]

class RedBlock:
    def __init__(self, rect):
        self.rect = rect
        self.vel = pygame.Vector2(0,0)
    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        self.vel *= 0.85
        if self.vel.length() < 0.05:
            self.vel = pygame.Vector2(0,0)
        self.rect.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))

red_blocks = [RedBlock(pygame.Rect(200,300,60,60)),
              RedBlock(pygame.Rect(600,300,80,80))]

class GreenBlock:
    def __init__(self, rect):
        self.rect = rect
        self.vel = pygame.Vector2(0,0)
    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        self.vel *= 0.95
        if self.vel.length() < 0.01:
            self.vel = pygame.Vector2(0,0)
        self.rect.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))

green_blocks = [GreenBlock(pygame.Rect(400,350,60,60)),
                GreenBlock(pygame.Rect(650,150,50,50))]

def soft_collide(a_rect, a_vel, b_rect, b_vel=None, strength=0.2):
    delta = pygame.Vector2(a_rect.center) - pygame.Vector2(b_rect.center)
    overlap_x = (a_rect.width + b_rect.width)/2 - abs(delta.x)
    overlap_y = (a_rect.height + b_rect.height)/2 - abs(delta.y)
    if overlap_x > 0 and overlap_y > 0:
        if overlap_x < overlap_y:
            push = pygame.Vector2(overlap_x * (1 if delta.x>0 else -1), 0)
        else:
            push = pygame.Vector2(0, overlap_y * (1 if delta.y>0 else -1))
        a_vel += push * strength
        if b_vel is not None:
            b_vel -= push * strength
        return True
    return False

def block_collide(a_rect, a_vel, b_rect):
    """Prevent going through static grey blocks."""
    if a_rect.colliderect(b_rect):
        dx1 = b_rect.right - a_rect.left
        dx2 = a_rect.right - b_rect.left
        dy1 = b_rect.bottom - a_rect.top
        dy2 = a_rect.bottom - b_rect.top
        min_dx = dx1 if abs(dx1) < abs(dx2) else -dx2
        min_dy = dy1 if abs(dy1) < abs(dy2) else -dy2
        if abs(min_dx) < abs(min_dy):
            a_rect.x += min_dx
            if a_vel is not None:
                a_vel.x = 0
        else:
            a_rect.y += min_dy
            if a_vel is not None:
                a_vel.y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel.x -= acc
    if keys[pygame.K_RIGHT]:
        player_vel.x += acc
    if keys[pygame.K_UP]:
        player_vel.y -= acc
    if keys[pygame.K_DOWN]:
        player_vel.y += acc

    player_vel *= friction
    if player_vel.length() > max_speed:
        player_vel = player_vel.normalize() * max_speed

    player.x += player_vel.x
    player.y += player_vel.y

    for b in blocks:
        block_collide(player, player_vel, b)

    for r in red_blocks:
        soft_collide(player, player_vel, r.rect, r.vel, strength=0.1) 

    for g in green_blocks:
        soft_collide(player, player_vel, g.rect, g.vel, strength=0.15)

    for r in red_blocks:
        for b in blocks:
            block_collide(r.rect, r.vel, b)

    for i, r1 in enumerate(red_blocks):
        for j, r2 in enumerate(red_blocks):
            if i<j:
                soft_collide(r1.rect, r1.vel, r2.rect, r2.vel, strength=0.1)

    for r in red_blocks:
        for g in green_blocks:
            soft_collide(r.rect, r.vel, g.rect, g.vel, strength=0.1)

    for i, g1 in enumerate(green_blocks):
        for j, g2 in enumerate(green_blocks):
            if i<j:
                soft_collide(g1.rect, g1.vel, g2.rect, g2.vel, strength=0.15)

    for r in red_blocks:
        r.update()
    for g in green_blocks:
        g.update()

    player.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))

    screen.fill(WHITE)
    for b in blocks:
        pygame.draw.rect(screen, GRAY, b)
    for r in red_blocks:
        pygame.draw.rect(screen, RED, r.rect)
    for g in green_blocks:
        pygame.draw.rect(screen, GREEN, g.rect)
    pygame.draw.rect(screen, BLUE, player)

    pygame.display.flip()
    clock.tick(60)

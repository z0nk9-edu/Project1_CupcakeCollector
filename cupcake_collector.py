import pygame
pygame.init()


WIDTH = 600
HEIGHT = 400


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("100 Bouncing Circles")
clock = pygame.time.Clock()

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]

player_image = pygame.image.load("player.png").convert_alpha()
cupcake_image = pygame.image.load(
    "cupcake.png"
).convert_alpha()

cupcake_image = pygame.transform.scale(
    cupcake_image,
    (30, 30)
)


player_image = pygame.transform.scale(
    player_image,
    (50, 50)
)

cupcakes = [
    pygame.Rect(150, 230, 30, 30),
    pygame.Rect(400, 180, 30, 30),
    pygame.Rect(520, 310, 30, 30)
]

player_dy = 0
gravity = 0.5
jump_speed = -10
on_ground = True


score = 0

player_rect = pygame.Rect(
        50,
        300,
        50,
        50
    )

running = True

while running:
    player_dy += gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_dy > 0:  
                player_rect.bottom = platform.top
                player_dy = 0
                on_ground = True
            elif player_dy < 0:  
                player_rect.top = platform.bottom
                player_dy = -.5
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5

    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    if player_rect.y >= 300:
        player_rect.y = 300
        player_dy = 0
        on_ground = True

    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False

    
    player_rect = pygame.Rect(
        player_rect.x,
        player_rect.y,
        50,
        50
    )

    for cupcake in cupcakes[:]:
        if player_rect.colliderect(cupcake):
            cupcakes.remove(cupcake)
            score += 1

    player_rect.y += player_dy
    screen.fill((0,0,0))
    screen.blit(player_image, (player_rect.x, player_rect.y))

    for cupcake in cupcakes:
        screen.blit(
            cupcake_image,
            (cupcake.x, cupcake.y)
        )

    for platform in platforms:
        pygame.draw.rect(
            screen,
            (100, 180, 100),
            platform
        )
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.font.init()
czcionka = pygame.font.SysFont("Comic Sans MS",15)
koordy=[]
middle=[0.0,0.,0.0,0.0]
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP:
                position=(pygame.mouse.get_pos())
                koordy.append(list(position))
                middle[0] += koordy[-1][0]
                middle[1] += koordy[-1][1]
                middle[2]=middle[0]/len(koordy)
                middle[3] = middle[1] / len(koordy)
            screen.fill([0,0,0])
            for items in range(0,len(koordy)):
                pygame.draw.circle(screen,[255,255,255],koordy[items],10)
            pygame.draw.circle(screen, [255, 0, 0], [middle[2],middle[3]], 10)
            pygame.display.flip()
        clock.tick(60)

main()

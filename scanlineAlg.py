import pygame, sys

def desenhaPixel(x, y):
  screen.set_at((round(x), round(y)), (255, 255, 255))

class Aresta:
    def __init__(self, y_min, y_max, x_yMin, incInversa):
        self.y_min = y_min
        self.y_max = y_max
        self.x_yMin = x_yMin
        self.incInversa = incInversa

def scanline(poligono):
    edgeTable = []
    for i in range(len(poligono)):
        pontoIni = poligono[i]
        if (i == (len(poligono) - 1)):
            pontoFim = poligono[0]
        else:
            pontoFim = poligono[i + 1]
        if (pontoIni[1] != pontoFim[1]):
            if (pontoIni[1] < pontoFim[1]):
                y_min  = pontoIni[1]
                x_yMin = pontoIni[0]
            else:
                y_min = pontoFim[1]
                x_yMin = pontoFim[0]
            y_max = max(pontoIni[1], pontoFim[1])
            varX = pontoFim[0] - pontoIni[0]
            varY = pontoFim[1] - pontoIni[1]
            incInversa = varX / varY
            edgeTable.append(Aresta(y_min, y_max, x_yMin, incInversa))

    activeEdgeTable = []

    for y in range(min(aresta.y_min for aresta in edgeTable), max(aresta.y_max for aresta in edgeTable) + 1):
        for aresta in edgeTable:
            if (aresta.y_min == y):
                activeEdgeTable.append(aresta)

        activeEdgeTable = [aresta for aresta in activeEdgeTable if aresta.y_max > y]

        activeEdgeTable.sort(key=lambda x: x.x_yMin)

        for aresta in activeEdgeTable:
            aresta.x_yMin += aresta.incInversa

        for i in range(0, len(activeEdgeTable), 2):
            x_aresta1 = int(activeEdgeTable[i].x_yMin)
            x_aresta2 = int(activeEdgeTable[i + 1].x_yMin)
            for x in range(x_aresta1, x_aresta2 + 1):
                desenhaPixel(x, y)

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))

poligono = ((50, 270), (100, 270), (100, 325), (50, 325))
scanline(poligono)
poligono = ((25, 30), (400, 30), (450, 100), (400, 200), (50, 150), (10, 55))
scanline(poligono)
poligono = ((300, 450), (474, 450), (387, 276))
scanline(poligono)

pygame.display.flip()

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
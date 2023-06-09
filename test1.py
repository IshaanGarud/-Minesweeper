import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()


#---------------------------GRID_settings-------------------------------
class Grid:
    def __init__(self):
        self.n_tiles = 4
        self.tile_size = WIDTH//self.n_tiles

        self.offset = 10
        self.tiles = {}

    def make_grid(self):
        for y in range(self.offset, HEIGHT, self.tile_size):
            for x in range(self.offset, WIDTH, self.tile_size):
                tile_rect = pygame.Rect(x, y, self.tile_size - self.offset, self.tile_size - self.offset)
                self.new_tile_size = tile_rect.size

                # if random.randint(0, self.n_tiles) == 1:
                #     isBomb = True
                # else:
                #     isBomb = False

                isBomb = False
                self.tiles[ str(tile_rect.x), str(tile_rect.y) ] = tile_rect, isBomb    # (x, y) : tile, isBomb
    

    def get_neighbors(self, tile):
        neighbors = []
        tile_x, tile_y = int(tile[0]), int(tile[1])
        temp1 = self.new_tile_size[1] + self.offset

        for y in range( tile_y - temp1, tile_y + temp1*2, self.tile_size):
            for x in range( tile_x - temp1, tile_x + temp1*2, self.tile_size ):

                # outofBounds = (x < 10 or x > )
                neighbors.append( (str(x), str(y)) )
        return neighbors

    def paint_neighbor(self, tile):
        tile_neigh = self.get_neighbors(tile)


    def draw_grid(self, base_color, mpos):
        neighbours = grid.get_neighbors(test_tile)       #('276', '276')

        for tile in self.tiles:
            tile_rect = self.tiles[tile][0]

            if tile_rect.collidepoint(*mpos):    # Click detection
                color = (255, 0, 0)
            elif self.tiles[tile][1] == True or tile == ('10', '210'):
                color = (0, 0, 255)
            if tile in neighbours:
                color = (255, 255, 0)
            else:
                color = base_color

            pygame.draw.rect(screen, color, tile_rect)

        
#-----------------------------MAIN_LOOP----------------------------------
grid = Grid()
grid.make_grid()
mpos = (0, 0)
test_tile = ('10', '210')


# for temp in grid.tiles:
#     print(grid.tiles[temp])

neigh = grid.get_neighbors(test_tile)       #('276', '276')
print(neigh)
print( ('10', '10') in neigh)


while True:
    screen.fill((30, 30, 30))

    keys = pygame.key.get_pressed()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()

    grid.draw_grid((255, 255, 255), mpos)

    pygame.display.flip()
    clock.tick(30)

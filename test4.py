import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
clock = pygame.time.Clock()


#---------------------------GRID_settings-------------------------------
class Grid:
    def __init__(self):
        self.n_tiles = 7
        self.tile_size = WIDTH//self.n_tiles
        self.offset = 10
        self.font = pygame.font.SysFont('Times New Roman', 10)

        self.tiles = []

    def make_grid(self):
        for y in range(self.offset, HEIGHT, self.tile_size):
            for x in range(self.offset, WIDTH, self.tile_size):
                tile_rect = pygame.Rect(x, y, self.tile_size - self.offset, self.tile_size - self.offset)
                self.new_tile_size = tile_rect.size
                
                isalive = None
                isBomb = False
                color = (255, 255, 255)
            
                if random.randint(1, self.n_tiles) == 1:
                    isalive = False                   
                else:
                    isalive = True
                    # isBomb = True
                self.tiles.append( [tile_rect, color, isBomb, isalive] ) 
          # [rect , color, isBomb, isalive]

    def get_neighbors(self, tile):
        tile_rect = tile[0]
        neighbors = []
        tile_x, tile_y = tile_rect.x, tile_rect.y
        temp1 = self.new_tile_size[1] + self.offset

        for y in range( tile_y - temp1, tile_y + temp1*2, self.tile_size):
            for x in range( tile_x - temp1, tile_x + temp1*2, self.tile_size ):
                outofBounds = (x < 10 or x > 798) or (y < 10 or y > 798)
                same = (x == tile_x and y == tile_y)
                for neigh_tile in self.tiles:   #list of tiles with info
                    if (neigh_tile[0].x == x and neigh_tile[0].y == y) and neigh_tile[3] == True and not same:
                        neighbors.append( neigh_tile )  # returns list of Neighboring Rects
        return neighbors
    
    def show_number(self, tile):
        neighbors = self.get_neighbors(tile)
        print(len(neighbors))

    def draw_grid(self, base_color, mpos):
            # tile[0] = tile_rect
            # tile[1] = color
            # tile[2] = isBomb (bool)
            # tile[3] = isalive (bool)
        for tile in self.tiles:
            tile_rect = tile[0]     # TILE IS A LIST >>>> [rect, color isbomb]
            if tile[3] == True:
                pygame.draw.rect(screen, tile[1], tile_rect)    #DRAW FIRST
                if tile_rect.collidepoint(*mpos):    # Click detection
                    self.selected_tile = tile
                    neighbors = self.get_neighbors(self.selected_tile)
                    
                    for n in neighbors:
                        self.tiles[ self.tiles.index(n) ][1] = (200, 200, 50)
                    tile[1] = (200, 50,50)

                else:
                    tile[1] = base_color
                
        
#-----------------------------MAIN_LOOP----------------------------------
grid = Grid()
grid.make_grid()
mpos = (0, 0)

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

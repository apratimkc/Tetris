from Box import *
        
class GameGrid:
    def __init__(self, width, height):
        self.hor_cells_count = width
        self.ver_cells_count = height
        self.verticies = []
        self.containers = []
        self.box_groups = []
        self.init_grid()
        
    def init_grid(self):
        self.verticies = [[Vector2(0,0) for _ in range(self.hor_cells_count+1)] 
                          for _ in range(self.ver_cells_count+1)]
        
        for i in range(self.ver_cells_count+1):
            for j in range(self.hor_cells_count+1):
                self.verticies[i][j].set_val(j,i)
                
        self.containers = [[BoxContainer() for _ in range(self.hor_cells_count)] 
                          for _ in range(self.ver_cells_count)]
        
    def add_box_group(self, bg):
        bg.shift_group_to(self.hor_cells_count//2,0)
        self.box_groups.append(bg)
        b_cos = bg.get_box_cos()
        for i in range(len(b_cos)):
            self.containers[b_cos[i][1]][b_cos[i][0]].box = bg.boxes[i]
        
    def __str__(self):
        s = "="*(self.hor_cells_count+4) + '\n'
        for i in range(self.ver_cells_count):
            s +='||'
            for j in range(self.hor_cells_count):
                v = self.containers[i][j].get_box_val()
                if v<1:
                    s += ' '
                else:
                    s += str(v)
            s += '||\n'
        s += "="*(self.hor_cells_count+4) 
        return s

def TestFun():
    grid = GameGrid(10,12)
    bg = BoxGroup(Vector2(0,0), 
                  [[0,0],
                   [1,0],
                   [-1,0],
                   [0,1]],1)
    grid.add_box_group(bg)
    print(grid)
    
if __name__ == '__main__':
    TestFun()

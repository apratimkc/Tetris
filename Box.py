from Vec2 import Vector2

class Box:
    def __init__(self, pivot, value):
        self.pivot = pivot
        self.value = value
        self.verticies = []
        self.update_verticies()
        
    def update_verticies(self):
        x = self.pivot.x
        y = self.pivot.y
        self.verticies = [Vector2(x,y) , Vector2(x+1,y) , Vector2(x+1,y+1) , Vector2(x,y+1)]
        
class BoxGroup:
    def __init__(self, center, rel_xy, val):
        self.center = center
        self.boxes = []
        self.add_boxes(rel_xy, val)
        self.rel_xy = rel_xy
        
    def add_boxes(self, rel_xy, val):
        for xy in rel_xy:
            self.add_box(xy[0], xy[1], val)
            
    def add_box(self, rel_x, rel_y, val):
        x = self.center.x + rel_x
        y = self.center.y + rel_y
        b = Box(Vector2(x,y), val)
        self.boxes.append(b)
        
    def shift_group_to(self, x,y):
        self.center.set_val(x, y)
        for b in self.boxes:
            b.update_verticies()
            
    def translate_to(self, dx, dy):
        pass
            
    def get_box_cos(self):
        cos = [[c[0]+self.center.x,c[1]+self.center.y] for c in self.rel_xy]
        return cos
        
        
class BoxContainer:
    def __init__(self, box=None):
        self.box = box
        
    def get_box_val(self):
        if self.box != None:
            return self.box.value
        else:
            return -1
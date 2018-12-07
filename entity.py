
# generic object to represent players, enemies, items, etc.
class Entity:

    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move entity by given amount
        self.x += dx
        self.y += dy

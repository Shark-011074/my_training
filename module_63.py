class Horse:
    def __init__(self, x_dist=0, sound='frr'):
        self.x_dist = x_dist
        self.sound = sound
        super().__init__()

    def run(self, dx):
        self.dx = dx
        self.x_dist += dx


class Eagle:
    def __init__(self, y_dist=0, sound='I train, eat, sleep, and repeat'):
        self.y_dist = y_dist
        self.sound = sound

    def flu(self, dy):
        self.dy = dy
        self.y_dist += dy


class Pegasus(Horse, Eagle):#В этом методе должны запускаться наследованные методы run и fly соответственно.


    def move(self,dx,dy):
        super().run(dx)
        super().flu(dy)
    def get_pos(self):#возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        return (self.x_dist,self.y_dist)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

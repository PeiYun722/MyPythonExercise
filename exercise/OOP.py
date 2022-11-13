class Car:
    def __init__(self,color):
        self.color=color
        self.seat=5
    def print_color(self):
        print("我的車子是",self.color)
    def print_seat(self):
        print("我的車子有",self.seat,"個座位")
    def set_seat(self,seat):
        self.seat=seat
        
aaa=Car("yellow")
aaa.set_seat(6)
aaa.print_seat()
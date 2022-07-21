## Simple example:
class rect:
   def __init__(self, length, base):
       self.l = length
       self.b = base
   def area(self):
        return self.l * self.b

r = rect(10.52,22.3)
print(f"Area is {r.area()} sqm")


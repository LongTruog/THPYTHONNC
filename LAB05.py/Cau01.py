class LAB05 :
    def __init__(self,name,population,area):
        self.name =  name 
        self.population = population
        self.area = area
    def is_larger (self,objLAB05 ):
        if self.area >= objLAB05.area:
            return True
        else:
            return False
canada = LAB05('Canada', 34482779, 9984670)
print(canada.name)
print(canada.population)
print(canada.area)
usa = LAB05('United States of America', 313914040, 9826675)
print(usa.name)
print(usa.population)
print(usa.area)
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""



class Classy(object):
    def __init__(self):
        self.items = []
        self.classiness = 0

    def getclassiness(self):
        return self.classiness

    def createlist(self):
        self.items.append(item)

    def additem(self, item):

        if item=="tophat":
            self.classiness+=2
        elif item=="bowtie":
            self.classiness+=4
        elif item=="monocle":
            self.classiness+=5
        else:
            self.classiness+=0
            
 
# Test cases
me = Classy()

# Should be 0
print(me.getclassiness())

me.additem("tophat")
# Should be 2
print(me.getclassiness())

me.additem("bowtie")
me.additem("jacket")
me.additem("monocle")
# Should be 11
print(me.getclassiness())

me.additem("bowtie")
# Should be 15
print(me.getclassiness())         
            
            
            

import pygame
import time
import random



##########
# COLORS #
##########



class color:

    white = (255, 255, 255)

    black = (0, 0, 0)

    red = (222, 60, 60)

    grey = (115, 115, 115)

    green = (43, 204, 94)



###################
# BUTTON CREATION #
###################



class Button:

    def __init__( self, x, y, width, height, color, text ):
        
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
        self.text = text

        self.show()
    
    def show(self):

        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height),0)
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, 1, (0,0,0))
        display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def clicked(self, x, y):

        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                return True
        return False



#########
# ARRAY #
#########



class Array:

    def __init__(self):
        self.array = [ i for i in range(1,101) ]
        self.found = False
        self.checked = []
        self.speed = 0
        self.newTarget()
    
    def newTarget(self): 
        self.target = self.array[ random.randint(0, 99) ]
        self.show()

    def reset(self): 
        self.array = [ i for i in range(1, 101) ]
        self.checked = []
        self.found = False
        array.show()
    
    def show(self):
        rect = pygame.Rect(0, 240, 1000, 600)
        pygame.draw.rect(display, color.white, rect)

        for i in range(0, 100):
            height = self.array[i] * 6
            rect = pygame.Rect(i*10, 840-height, 10, height)

            if self.array[i] in self.checked: pygame.draw.rect(display, color.grey, rect)

            elif self.array[i] == self.target: 
                if self.found: pygame.draw.rect(display, color.green, rect)
                else: pygame.draw.rect(display, color.red, rect)
            
            else: pygame.draw.rect(display, color.black, rect)
            
        
        pygame.display.update()
        time.sleep(self.speed)



##############
# ALGORITHMS #
##############



class Algorithms:

    running = False

    def linearSearch(arr):

        array.speed = 0.2
        Algorithms.running = True
        
        for element in arr:

            if element == array.target:

                array.found = True
                array.show()
                Algorithms.running = False
                return

            else:

                array.checked.append(element)
                array.show()

    
    def binarySearch(arr):
        
        array.speed = 1
        Algorithms.running = True

        high = len(arr) - 1
        low = 0
        
        while low <= high:
 
            mid = low + (high - low) // 2
    
            if arr[mid] == array.target:
                array.found = True
                array.show()
                Algorithms.running = False
                break

            array.checked.append(arr[mid])
            array.show()
    
            if arr[mid] < array.target:
                for i in range(low, mid): array.checked.append(arr[i])
                low = mid + 1
                array.show()
    
            else:
                for i in range(mid + 1, high + 1): array.checked.append(arr[i])
                high = mid - 1
                array.show()

    
    
    def ternarySearch(arr, low, high):

        array.speed = 1
        Algorithms.running = True

        target = array.target
 
        if (high >= low):
    
            left_mid = low + (high - low) // 3
            right_mid = high - (high - low) // 3
    
            if (arr[left_mid] == target):
                array.found = True
                array.show()
                Algorithms.running = False
                return
            
            if (arr[right_mid] == target):
                array.found = True
                array.show()
                Algorithms.running = False
                return
            
            array.checked.append(arr[left_mid])
            array.checked.append(arr[right_mid])
            array.show()
            
            if (target < arr[left_mid]):
                for i in range(left_mid + 1, high + 1): array.checked.append(arr[i])
                array.show()
                return Algorithms.ternarySearch(arr, low, left_mid - 1)
            
            elif (target > arr[right_mid]):
                for i in range(low, right_mid): array.checked.append(arr[i])
                array.show()
                return Algorithms.ternarySearch(arr, right_mid + 1, high)
            
            else:
                for i in range(low, left_mid): array.checked.append(arr[i])
                for i in range(right_mid + 1, high + 1): array.checked.append(arr[i])
                array.show()
                return Algorithms.ternarySearch(arr, left_mid + 1, right_mid - 1)
            
        Algorithms.running = False
    

    def bogoSearch(arr):

        array.speed = 0.2
        Algorithms.running = True
        checked = []

        while True:

            value = arr[ random.randint(0,99) ]

            if value in checked: continue

            if value == array.target:
                array.found = True
                array.show()
                break
            
            checked.append(value)
            array.checked.append(value)
            array.show()
            
        Algorithms.running = False        
    


#########
# CLICK #
#########



def click(pos):

    x, y = pos[0], pos[1]

    if reset.clicked(x,y):
        array.reset()
        return

    if target.clicked(x,y):
        array.newTarget()
        return

    if linearSearch.clicked(x,y):
        Algorithms.linearSearch(array.array)
        return
    
    if binarySearch.clicked(x,y):
        Algorithms.binarySearch(array.array)
        return
    
    if ternarySearch.clicked(x,y):
        Algorithms.ternarySearch(array.array, 0, 99)
        return
    
    if bogoSearch.clicked(x,y):
        Algorithms.bogoSearch(array.array)
        return



############
# MAINLOOP #
############



def mainloop():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if Algorithms.running: continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1: click(pygame.mouse.get_pos())



##############
# INITIALIZE #               
##############



pygame.init()
display = pygame.display.set_mode((1000, 840))
pygame.display.set_caption('Searching Algorithms')
display.fill(color.white)
pygame.draw.rect( display , color.grey , (0,0,1000,80) )

array = Array()

reset = Button( 10, 20, 155, 40, color.white, 'Reset' )
target = Button( 175, 20, 155, 40, color.white, 'Target' )
linearSearch = Button( 340, 20, 155, 40, color.white, 'Linear Search' )
binarySearch = Button( 505 , 20, 155, 40, color.white, 'Binary Search' )
ternarySearch = Button( 670 , 20, 155, 40, color.white, 'Ternary Search' )
bogoSearch = Button( 835 , 20, 155, 40, color.white, 'Bogo Search' )


pygame.display.update()


mainloop()

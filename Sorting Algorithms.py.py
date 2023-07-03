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

    grey = (200, 200, 200)



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



#################
# VISUALIZATION #
#################



class show:

    def array(arr):

        rect = pygame.Rect(0, 240, 1000, 600)
        pygame.draw.rect(display, color.white, rect)

        for i in range(0, 100):

            height = arr[i] * 6
            rect = pygame.Rect(i*10, 840-height, 10, height)
            pygame.draw.rect(display, color.red, rect)
        
        pygame.display.update()
        time.sleep(speed)



#########
# ARRAY #
#########



class Array:

    def __init__(self):
        self.array = [ i for i in range(1,101) ]
    
    def shuffle(self): 
        random.shuffle(self.array)
        show.array(array.array)

    def reset(self): 
        self.array = [ i for i in range(1, 101) ]
        show.array(array.array)



##############
# ALGORITHMS #
##############



class Algorithms:

    running = False

    def bubbleSort(arr):

        Algorithms.running = True

        n = len(arr)
        
        swapped = False
        
        for i in range(n-1):
        
            for j in range(0, n-i-1):
    
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    show.array(arr)
        
            if not swapped:
                array.array = arr
                Algorithms.running = False
                return

        array.array = arr
        Algorithms.running = False

    
    def insertionSort(arr):
        
        Algorithms.running = True

        for i in range(1, len(arr)):
        
            key_item = arr[i]

            j = i - 1

            while j >= 0 and arr[j] > key_item:
                arr[j + 1] = arr[j]
                show.array(arr)
                j -= 1

            arr[j + 1] = key_item
            show.array(arr)

        array.array = arr
        Algorithms.running = False
    
    
    def heapSort(arr):

        Algorithms.running = True

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            functions.heapify(arr, n, i)
    
 
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            show.array(arr)
            functions.heapify(arr, i, 0)

        array.array = arr
        Algorithms.running = False
    

    def quickSort(array, low, high):

        Algorithms.running = True
  
        if low < high:

            pi = functions.partition(array, low, high)
            
            Algorithms.quickSort(array, low, pi - 1)
            Algorithms.quickSort(array, pi + 1, high)
        
        Algorithms.running = False



#############
# FUNCTIONS #
#############



class functions:

    
    def heapify(array, n, i):
        largest = i  
        l = 2 * i + 1 
        r = 2 * i + 2 
     
        if l < n and array[i] < array[l]:
            largest = l
    
        if r < n and array[largest] < array[r]:
            largest = r
    
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            show.array(array)
            functions.heapify(array, n, largest)

    
    def partition(array, low, high):

  
        pivot = array[high]

        
        i = low - 1

        
        for j in range(low, high):
            if array[j] <= pivot:
            
                i = i + 1

                
                array[i], array[j] = array[j], array[i]
                show.array(array)
        
        array[i + 1], array[high] = array[high], array[i + 1]
        show.array(array)
        
        return i + 1



#########
# CLICK #
#########



def click(pos):

    x, y = pos[0], pos[1]

    if reset.clicked(x,y):
        array.reset()
        return

    if shuffle.clicked(x,y):
        array.shuffle()
        return

    if bubbleSort.clicked(x,y):
        Algorithms.bubbleSort(array.array)
        return
    
    if heapSort.clicked(x,y):
        Algorithms.heapSort(array.array)
        return
    
    if insertionSort.clicked(x,y):
        Algorithms.insertionSort(array.array)
        return
    
    if quickSort.clicked(x,y):
        Algorithms.quickSort(array.array, 0, 99)
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
            
            if Algorithms.running: return
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1: click(pygame.mouse.get_pos())



##############
# INITIALIZE #               
##############



pygame.init()
display = pygame.display.set_mode((1000, 840))
pygame.display.set_caption('Algorithm Visualizer')
display.fill(color.white)
pygame.draw.rect( display , color.grey , (0,0,1000,80) )

array = Array()
speed = 0.01

reset = Button( 10, 20, 155, 40, color.white, 'Reset' )
shuffle = Button( 175, 20, 155, 40, color.white, 'Shuffle' )
bubbleSort = Button( 340, 20, 155, 40, color.white, 'Bubble Sort' )
heapSort = Button( 505 , 20, 155, 40, color.white, 'Heap Sort' )
insertionSort = Button( 670 , 20, 155, 40, color.white, 'Insertion Sort' )
quickSort = Button( 835 , 20, 155, 40, color.white, 'Quick Sort' )

show.array(array.array)
pygame.display.update()


mainloop()
        

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



#########
# ARRAY #
#########



class Array:

    def __init__(self):
        self.array = [ i for i in range(1,101) ]
        self.speed = 0
    
    def shuffle(self): 
        random.shuffle(self.array)
        array.show(array.array)
    
    def show(self, arr):

        rect = pygame.Rect(0, 240, 1000, 600)
        pygame.draw.rect(display, color.white, rect)

        for i in range(0, 100):

            height = arr[i] * 6
            rect = pygame.Rect(i*10, 840-height, 10, height)
            pygame.draw.rect(display, color.red, rect)
        
        pygame.display.update()
        time.sleep(self.speed)



##############
# ALGORITHMS #
##############



class Algorithms:

    running = False

    def mergeSort(arr, low, high):

        array.speed = 0.01

        if low < high:
    
            m = low + ( high - low) // 2

            Algorithms.mergeSort(arr, low, m)
            Algorithms.mergeSort(arr, m + 1, high)
            functions.merge(arr, low, m, high)

        array.show(arr)
        array.array = arr
        Algorithms.running = False

    def bubbleSort(arr):

        Algorithms.running = True
        array.speed = 0.005
        n = len(arr)
        
        swapped = False
        
        for i in range(n-1):
        
            for j in range(0, n-i-1):
    
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    array.show(arr)
        
            if not swapped:
                array.array = arr
                Algorithms.running = False
                return

        array.array = arr
        Algorithms.running = False

    
    def insertionSort(arr):
        
        array.speed = 0.005
        Algorithms.running = True

        for i in range(1, len(arr)):
        
            key_item = arr[i]

            j = i - 1

            while j >= 0 and arr[j] > key_item:
                arr[j + 1] = arr[j]
                array.show(arr)
                j -= 1

            arr[j + 1] = key_item
            array.show(arr)

        array.array = arr
        Algorithms.running = False
    
    
    def heapSort(arr):

        array.speed = 0.01
        Algorithms.running = True

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            functions.heapify(arr, n, i)
    
 
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            array.show(arr)
            functions.heapify(arr, i, 0)

        array.array = arr
        Algorithms.running = False
    

    def quickSort(arr, low, high):

        array.speed = 0.02
        Algorithms.running = True
  
        if low < high:

            pi = functions.partition(arr, low, high)
            
            Algorithms.quickSort(arr, low, pi - 1)
            Algorithms.quickSort(arr, pi + 1, high)
        
        if arr == array.array:
            Algorithms.running = False
            return



#############
# FUNCTIONS #
#############



class functions:


    def merge(arr, low, mid, high):

        n1 = mid - low + 1
        n2 = high - mid
    
        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0, n1):
            L[i] = arr[low + i]
    
        for j in range(0, n2):
            R[j] = arr[mid + 1 + j]
    
        i = 0     
        j = 0    
        k = low     
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                array.show(arr)
                i += 1
            else:
                arr[k] = R[j]
                array.show(arr)
                j += 1
            k += 1
    
        while i < n1:
            arr[k] = L[i]
            array.show(arr)
            i += 1
            k += 1
    
        while j < n2:
            arr[k] = R[j]
            array.show(arr)
            j += 1
            k += 1

    
    def heapify(arr, n, i):
        largest = i  
        l = 2 * i + 1 
        r = 2 * i + 2 
     
        if l < n and arr[i] < arr[l]:
            largest = l
    
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            array.show(arr)
            functions.heapify(arr, n, largest)

    
    def partition(arr, low, high):

  
        pivot = arr[high]

        
        i = low - 1

        
        for j in range(low, high):
            if arr[j] <= pivot:
            
                i = i + 1

                
                arr[i], arr[j] = arr[j], arr[i]
                array.show(arr)
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        array.show(arr)
        
        return i + 1



#########
# CLICK #
#########



def click(pos):

    x, y = pos[0], pos[1]

    if shuffle.clicked(x,y):
        array.shuffle()
        return

    if mergeSort.clicked(x,y):
        Algorithms.mergeSort(array.array, 0, 99)
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

        if Algorithms.running: continue

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1: click(pygame.mouse.get_pos())



##############
# INITIALIZE #               
##############



pygame.init()
display = pygame.display.set_mode((1000, 840))
pygame.display.set_caption('Sorting Algorithms')
display.fill(color.white)
pygame.draw.rect( display , color.grey , (0,0,1000,80) )

array = Array()

shuffle = Button( 10, 20, 155, 40, color.white, 'Shuffle' )
mergeSort = Button( 175, 20, 155, 40, color.white, 'Merge Sort' )
bubbleSort = Button( 340, 20, 155, 40, color.white, 'Bubble Sort' )
heapSort = Button( 505 , 20, 155, 40, color.white, 'Heap Sort' )
insertionSort = Button( 670 , 20, 155, 40, color.white, 'Insertion Sort' )
quickSort = Button( 835 , 20, 155, 40, color.white, 'Quick Sort' )

array.show(array.array)
pygame.display.update()


mainloop()

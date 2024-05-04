import matplotlib.pyplot as plt
from Sorting_tester import Tester
from bubble_sort import Bubble_Sort
from selection_sort import Selection_Sort


class Sorting_Algorithms:
    def __init__(self,num_amount) -> None:
        self.num_amount = num_amount
        self.figure, self.ax = plt.subplots()
        self.num_list = Tester.generate_list(self.num_amount)
        self.rects = self.ax.bar(range(num_amount),self.num_list)
        
    
    def run(self):
        num_list_copy = self.num_list.copy()
        num_list_copy.sort()
        
        plt.title("Selection Sort")
        out_list = Selection_Sort(self.num_list.copy(),self).Sort()
        Tester.test(out_list,num_list_copy)
        
        plt.title("Bubble Sort")
        out_list = Bubble_Sort(self.num_list.copy(),self).Sort()
        Tester.test(out_list,num_list_copy)
        
        
    def display(self,num_list):
        for rect,h in zip(self.rects,num_list):
            rect.set_height(h)
        self.figure.canvas.draw()
        plt.pause(0.0001)

while True:
    try:
        num = int(input("How many numbers do you want to sort: "))
        break
    except:
        print("Not a valid number")

Sorting_Algorithms(num).run()
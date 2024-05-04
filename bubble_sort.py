from Sorting_tester import Tester

class Bubble_Sort:
    def __init__(self,num_list,runner) -> None:
        self.num_list = num_list
        self.runner = runner
    
    def Sort(self):
        index_number = 0
        while True:
            self.runner.display(self.num_list)
            change = False
            for i in range(len(self.num_list)):
                try:
                    if self.num_list[i] > self.num_list[i+1]:
                        change = True
                except:
                    pass
            if change == False:
                break
            try:
                if self.num_list[index_number] > self.num_list[index_number + 1]:
                    self.num_list[index_number] , self.num_list[index_number + 1] = self.num_list[index_number + 1] , self.num_list[index_number]
                
                index_number += 1
            except:
                index_number = 0
                
            
            
            
        return self.num_list
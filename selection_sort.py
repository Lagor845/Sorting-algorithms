from Sorting_tester import Tester


class Selection_Sort:
    def __init__(self,num_list,runner) -> None:
        self.num_list = num_list
        self.runner = runner

    def Sort(self):
        smallest_num = [0,self.num_list[0]]
        starting_num = 0
        while True:
            self.runner.display(self.num_list)
            change = False
            for i in range(starting_num,len(self.num_list)):
                if self.num_list[i] <= smallest_num[1]:
                    smallest_num = [i,self.num_list[i]]

            for i in range(len(self.num_list)):
                try:
                    if self.num_list[i] > self.num_list[i+1]:
                        change = True
                except:
                    pass
            if change == False:
                break

            self.num_list[starting_num] , self.num_list[smallest_num[0]] = smallest_num[1] , self.num_list[starting_num]
            smallest_num = [starting_num,self.num_list[starting_num+1]]
            starting_num += 1
        
        return self.num_list
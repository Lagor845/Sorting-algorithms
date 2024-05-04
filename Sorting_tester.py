import random

class Tester:
    def generate_list(numbers):
        num_list = []
        for i in range(numbers):
            num_list.append(random.randint(0,numbers))
        return num_list
    
    def test(num_list,num_list_copy):
        passing = True
        for i in range(len(num_list_copy)):
            if num_list[i] != num_list_copy[i]:
                passing = False

        if passing:
            print("Passed")
            
        else:
            print("Failed")
from Sorting_tester import Tester

num_list = Tester.generate_list(1000)
num_list_copy = num_list.copy()
num_list_copy.sort()

index_number = 0
while True:
    try:
        if num_list[index_number] > num_list[index_number + 1]:
            num_list[index_number] , num_list[index_number + 1] = num_list[index_number + 1] , num_list[index_number]
        
        index_number += 1
        change = False
        for i in range(len(num_list)):
            try:
                if num_list[i] > num_list[i+1]:
                    change = True
            except:
                pass
        if change == False:
            break
    except:
        index_number = 0

Tester.test(num_list,num_list_copy)
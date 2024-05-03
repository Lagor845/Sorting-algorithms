from Sorting_tester import Tester

num_list = Tester.generate_list(1000)
num_list_copy = num_list.copy()
num_list_copy.sort()

smallest_num = [0,num_list[0]]
starting_num = 0
while True:
    change = False
    for i in range(starting_num,len(num_list)):
        if num_list[i] <= smallest_num[1]:
            smallest_num = [i,num_list[i]]

    for i in range(len(num_list)):
        try:
            if num_list[i] > num_list[i+1]:
                change = True
        except:
            pass
    if change == False:
        break

    print(f"Swapping: {num_list[starting_num]} with: {smallest_num[1]}")
    num_list[starting_num] , num_list[smallest_num[0]] = smallest_num[1] , num_list[starting_num]
    smallest_num = [starting_num,num_list[starting_num+1]]
    starting_num += 1
    
Tester.test(num_list,num_list_copy)
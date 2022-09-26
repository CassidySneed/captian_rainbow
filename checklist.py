
#create our checklist 
checklist = list()

#create items in the list 
def create(item):
    checklist.append(item)

#reads item in list 
def read(index):
    print(checklist[index])
    return checklist[index]

#updates item in list 
def update(index, item):
    checklist[index]= item

#detetes item from list 
def destroy(index):
    checklist.pop(index)


#all_items
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1


#adds checkmark to item 
def mark_completed(index):
    checklist[index] = ("{} {}".format("√"+checklist[index]))

#user input 
def user_input(prompt):
    user_input = input(prompt)
    return user_input  

#select
def select(function_code): 
    #create item
    if function_code.lower() == "c": 
        input_item = user_input("Input item:")
        create(input_item)

    #read item
    elif function_code.lower() == "r": 
        item_index = user_input("Index Number?")
        read(int(item_index))

    #print all items 
    elif function_code.lower() == "p": 
        list_all_items()
    
    elif function_code.lower() == "q":
        global running
        running = False
        return 

    elif function_code.lower() == "u":
        input_index = user_input("Input index to update: ")
        input_item = user_input("Input item to update: ")
        update(int(input_index), input_item)

    elif function_code.lower() == "d":
        input_index = user_input("Input index to destroy")
        destroy(int(input_index))

    #catch all 
    else: 
        print("Unknown Option")




# #testing code 
# def test():
#     #previous testiing code 
#     create("purple sox")
#     create("red cloak")

#     print(read(0))
#     print(read(1))

#     update(0, "purple socks")
#     destroy(1)

#     print(read(0))

#     list_all_items()

#     #call and display funtion C
#     select ("C")
#     list_all_items()

#     #call and display function R
#     select("R")
#     list_all_items()

#     #call and display function R
#     select ("P")
#     list_all_items()
    

# #run test
# # test()

#whileloop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, D to destory item, U to update item, and Q to quit")
    select(selection)
    # print(selection)
    # print(running)
    

#user_value = user_input("Please Enter a Value:")
    #print(user_value)



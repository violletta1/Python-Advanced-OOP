data = input()

indexes = []

for i in range(len(data)):
    ch = data[i] #create data for every element

    if ch == "(": #check if element is (
        indexes.append(i) #add the index of the element to your stack
    elif ch == ")": #check if the element is )
        l = indexes.pop() #save the last element rom the stack
        print(data[l:i+1]) #print the elements from last element in stack to the current index + 1 from our data
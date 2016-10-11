def main() :
    comm = input("Please specify a command [list, add, mark, archive]:  ")
    data={}
    index=reading(data)

    if comm == "add" :
        add(data,index)
        save(data)
    if comm == "list" :
        listw(data) 
        save(data) 
    if comm == "mark" :
        mark(data)
        save(data)
    if comm == "archive" :
        archive(data)
        

    #save(data)

def reading(data):
    f=open("todolist",'r')
    i=1
    for line in f:
        #item=[line]
        data[i]=line
        #data[i][1]=item[1]
        i= i+1
    f.close()
    #print(data)
    return i

def add(data,i):
    element = input(('Add an item: '))
    data[i]=element+'\n'
    print(data)
    return i+1

def listw(data):
    i=1
    for each in data:
        if data[each][0] == 'x':
            print(str(i)+". [X] "+data[each][1:])
        else:
            print(str(i)+". [ ] "+data[each])
        i=i+1
        

def mark(data):
    listw(data)
    task = input("Which one want to mark as completed: ")
    for each in data:
        if int(each) == int(task):
            #print(each)
            new=data[each]
            data[each]="x"+new
            #print(data[each])


def save(data):
    f=open('todolist','w')
    for each in data:
        f.write(str(data[each]))
    f.close()

def archive(data):
    f=open('todolist','w')
    for each in data:
        if data[each][0] != 'x':
            f.write(str(data[each][1:]))
    f.close()
    print("All completed tasks got deleted.")


main()
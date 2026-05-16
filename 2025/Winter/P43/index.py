#Q2
#(a)
global queue
queue = [""] * 100
global head 
head = -1
global tail
tail = -1
global itemnum 
itemnum = 0

#(b)
def enqueue(data):
    global queue,head,tail,itemnum
    if itemnum == 100: # QUEUE FULL
        return False
    else:
        if tail == -1 and head == -1:
            tail = 0
            head = 0
            
        else:
            tail = tail + 1
            
        queue[tail] = data
        itemnum = itemnum + 1
        return True
    
#(c)
def dequeue():
    global queue,head,tail,itemnum
    if itemnum == 0: #QUEUE EMPTY
        return False
    else:
        data = queue[tail]
        tail = tail - 1
        itemnum = itemnum - 1
        return True
    
#(d)
def readdata():
    try:
        myfile = open("2025/Winter/P43/BinaryData.txt", mode = "r")
        digit = myfile.readline().strip()
        enqueue(digit)
    except IOError:
        print("file not found")

readdata()
print(queue)

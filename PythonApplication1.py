list = [1,1,0,1]
steps = 8
def xor(bit1, bit2):
    if bit1 == bit2:
        return 0
    elif bit1 != bit2:
        return 1

def printList():
    for bit in list:
        print(bit,end=",")

for i in range(0,9):
    print("\nStep: ", i , "\n", printList(), "\n")
    list.insert(0,xor(xor(list[2],list[3]),list[1]))
    



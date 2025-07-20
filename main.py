# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    pass# Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#def binaryCheat(num,size):
#    binnum=0
#    for i in range(size,0,-1):
#        binnum += (num>> (i-1))*10**size
#        num = num - (num>>(i-1))
#       print(num>>(i-2))
#    return binnum
def binary(num,size):
    stringNum=0
    goodsize = size
    size = size-1
    while (num!=0):
        p = 2**size
        if (num // (2** size)%10==1):
            num = num-(2**size)
            stringNum += 1*10**(size)
        else:
            stringNum +=0 * 10 **(size)
        size -=1
    return sined(stringNum,goodsize)
def sined(num,size):
    for i in range (size,-1,-1):
        p = (10**i)
        c= num//p
        if (num//(10**i)%10==1):
            num -=10**i
        else:
            num +=10**i
    return plus(num,size)
def plus(num,size):
    for i in range (size):
        if (num//(10**i)%10==1):
            num -=10**i
        else:
            num +=10**i
            return num
    return num+1
# Press the green button inb the gutter to run the script.
if __name__ == '__main__':
    #print(binaryCheat(42,8))
    print(binary(42,8))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def list2int(mylist,bits_per_value):
    myint = 0
    for ii,val in enumerate(mylist): myint |=  val << ii*bits_per_value
    return myint
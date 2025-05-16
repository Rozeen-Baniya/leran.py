# local varaible
# varaibles inside a function is locals varaible

# global varaible
# variables outside a function is global varaible

i = 10
def add():
    global i
    i = 15
    print (i)

add()
print(i)
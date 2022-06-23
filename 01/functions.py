def my_function():
    print("This is my function")
    print("Functions are very cool")

# my_function()

def my_function_with_arguments(parameter_one, parameter_two):
    print(parameter_one)
    print(parameter_two)

# my_function_with_arguments("hello","there")


def average(a,b):
    print((a+b)/2)

# average(3,7)

# def roundfun(a)


def add_two(my_num):
    return my_num+2

# print(add_two(5))

def can_i_sleep_in(weekend, morning_plans):
    return weekend and (not morning_plans)

# print(can_i_sleep_in(True,False))



def can_i_go_to_the_beach(sunny, temp_over_80, windy):
    return sunny and temp_over_80 and not windy


# print(can_i_go_to_the_beach(True, True, False), "should be True")
# print(can_i_go_to_the_beach(False, True, False), "should be False")
# print(can_i_go_to_the_beach(True, True, True), "should be False")
# print(can_i_go_to_the_beach(True, False, False), "should be False")




def should_i_go_outside(temp):
    return temp>=80


def has_teen(a, b, c):
    # Return true if one of these numbers is a teen
    # if any of them are not, return false
    return (a>=13 and a<=19) or (b>=13 and b<=19) or (c>=13 and c<=19)


# print(has_teen(10,13,19)==True)
# print(has_teen(16,13,19)==True)
# print(has_teen(15,13,20)==True)
# print(has_teen(16,13,19)==True)
# print(has_teen(20,20,16)==True)
# print(has_teen(9,10,20)==False)
# print(has_teen(45,99,2)==False)


def fround(morbius):
    if (morbius>0):
        print("it's morbin time")
        if (morbius-int(morbius)<0.5):
            return int(morbius)
        else:
            return int(morbius)+1
    elif (morbius==0):
        print("number is equal to morbin time")
        return(0)
    else:
        if (morbius-int(morbius)>-0.5):
            return int(morbius)
        else:
            return int(morbius)-1
        #later
    # return int(morbius/1) if morbius % 1 == 0 else (morbius-morbius%1)+1
    

    # This function should return a rounded integer
    
    
    
    #return ...

# print(fround(1.5))
# print(fround(-1.5))
# print(fround(-1.4))
# print(fround(1.4))
# print(fround(0))

# print(fround(1.5)==2)
# print(fround(-1.5)==-2)
# print(fround(-1.4)==-1)
# print(fround(1.4)==1)
# print(fround(0)==0)

def hello(name):
    if name=='jacob':
        return ""
    else:
        return 'Hello' + ' ' + name + '!'

# print(hello('bob')=='Hello bob!')
# print(hello('ben')=='Hello ben!')
# print(hello('joshua')=='Hello joshua!')
# print(hello('jacob')=='')

# number = 0

# # if example
# if number>1:
#     print("Im in the first if")

# if number>2:
#     print("Im in the second if")
# else:
#     print("Im in the else (Jackson)")


# number = 2

# # elif example
# if number==1:
#     print("Im in the first if")
# elif number==2:
#     print("Im in the second? elif")
# elif number<3:
#     print("im in the third? elif")
# else:
#     print("Im in the else (Jackson)")



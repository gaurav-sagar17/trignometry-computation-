def sin(angle) :
    pi = 3.14159265359
    angle = angle * (pi/180)
    p = 1 
    sign = 1
    res = 0
    count = 1
    while (count<=12)  : 
        num = (angle ** p)
        f = 1
        end = p 
        while(end >= 1) :
            f *= end 
            end -= 1
        # print("curretn term factotial is : ",f, end =" ")

        term = (num/f)*sign 
        # print("term is : ",term,end=" ")
        res += term 
        # print("current sum :",res)
        p += 2
        sign *= -1
        count += 1

    return res


def cos(angle) :
    pi = 3.14159265359
    angle = angle * (pi/180)
    p = 0
    sign = 1
    res = 0
    count = 1
    while (count<=11)  : 
        num = (angle ** p)
        f = 1
        end = p 
        while(end >= 1) :
            f *= end 
            end -= 1
        # print("curretn term factotial is : ",f, end =" ")

        term = (num/f)*sign 
        # print("term is : ",term,end=" ")
        res += term 
        # print("current sum :",res)
        p += 2
        sign *= -1
        count += 1

    return res

def main() :
    angle = float(input("enter the viewing angle  of the person :   "))
    base = float(input("enter the distance between the man and the pole : ")) 
    hyp = base/(cos(angle)) 
    per = hyp*(sin(angle)) 
    print("the base is : ",base) 
    print("the hypotenuse  is : ",hyp) 
    print("the perpendicualr is : ",per) 
    

if(__name__ == "__main__") :
    main() 
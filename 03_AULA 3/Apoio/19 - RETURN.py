

def menor(*args):
    omenor = 9999999999999
    for x in args:
        if(omenor >= x):
            omenor = x

    return omenor



print(menor(1,4,5,5,587,578,54,))
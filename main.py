def function1 (*args):
        l=len(args)
        s=0
        c=0
        while c<l:
            if type(args[c]) == int or type(args[c]) == float:
                s=s+args[c]
                c=c+1
            else:
                return "Error"
        return s
print(function1(1, 3, 10))





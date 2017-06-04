#william Dreese, hw6

def new_split_iter(expr):
    expr = expr + ";";
    pos = 0;
    while expr[pos] != ';':
        if expr[pos].isdigit():
            start = pos
            while expr[pos].isdigit():
                pos = pos+1
            yield expr[start:pos]
        elif expr[pos].isalpha():
            start = pos
            while expr[pos].isalpha():
                pos = pos+1
            yield expr[start:pos]
        elif expr[pos] in {'<', '>', '!', '='}:
            token = expr[pos]
            pos += 1
            if expr[pos] == '=':
                token += expr[pos]
                pos = pos+1
            yield token     
        else:
            if expr[pos] != ' ':
                yield expr[pos]
            pos = pos+1
        
if __name__ == "__main__":
    print (list(new_split_iter("deffn sqr(x) = x*x")))
    #evaluate("deffn abs(x) = x > 0 ? x : 0-x")
    print( list( new_split_iter("deffn fact(n) = n <= 1 ? 1 : n * fact(n-1)")))
    print (list(new_split_iter("sqr(4)")))
    #evaluate("abs(3-5)")
    #evaluate("fact(5)")

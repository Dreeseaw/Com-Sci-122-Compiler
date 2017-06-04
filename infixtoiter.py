from newsplit import new_split_iter
from peekable import Peekable, peek
import itertools

#has to return a peekable iter in postfix
def to_postfix( expr ):
    return Peekable ( postfix_sum(Peekable(new_split_iter(expr))) )

def next_op( i ): #finds the next operator
    while peek(i) is not None:
        if peek(i) in [")","("]:
            return None
        elif peek(i) in ["*","/","^","&","+","-"]:
            return peek(i)
        next(i)
            
        
def postfix_sum( it ):
    #accounts for unary negation
    if peek(it) is "-":
        n = next(it)
        nn = next(it)
        yield str(int(nn)*(-1))

    #main loop
    while peek(it) is not None:
        n = next(it)
        if n in [")","("]:
            if n == "(":
                adder = Peekable(postfix_sum( it ))
                while peek(adder) is not None: yield next(adder)
            else: break
        elif n in ["^"]:
            i,it = itertools.tee(it); i = Peekable(i); it = Peekable(it)
            nO = next_op(i)
            if nO is None:
                adder = Peekable(postfix_sum( it ))               
                while peek(adder) is not None: yield next(adder)
            else: yield next(it)
            yield n
        elif n in ["*","/","&"]:
            i,it = itertools.tee(it); i = Peekable(i); it = Peekable(it)
            nO = next_op(i)
            if nO not in ["+","-","*","/","&"]:
                adder = Peekable(postfix_sum( it ))               
                while peek(adder) is not None: yield next(adder)
            else: yield next(it)
            yield n
        elif n in ["+","-"]:
            i,it = itertools.tee(it); i = Peekable(i); it = Peekable(it)
            nO = next_op(i)
            if nO not in ["+","-"]:
                adder = Peekable(postfix_sum( it ))               
                while peek(adder) is not None: yield next(adder)
            else: yield next(it)
            yield n
        else: yield n
            
    

from vartree import VarTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree
from machine import Print

class Program:
    def __init__(self):
        self.first_stmt = -1        # 'main' not yet found
        self.last_temp  = 0         # no registers yet claimed
        self.functions = VarTree()  # no functions yet
        self.variables = VarTree()  # no global variables yet
        self.code = []              # no instructions yet
    def next_reg(self):
        self.last_temp += 1
        return self.last_temp

def compile_line(program,expr):
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        """
        name, parms, body = define_func(iterator)
        local_variables = VarTree()
        code_line = len(program.code)
        program.functions.assign(name, (parms, body, code_line, local_variables))
        body.comp( local_variables, program )
        """
        pass
    else:
        if program.first_stmt == -1:        # if 'main' not yet assigned
            program.first_stmt = len(program.code)  #    start executing here
        to_expr_tree(expr).comp( program.variables, program )
        program.code.append( Print( program.code[-1].get_temp() ) )
        
def run_program(program):
    """run the program that has been compiled into the prog array
    starting at the first line that is not within any function
    after setting aside enough space for temporary registers and stack
    """
    print()
    for i in range(len(program.code)):
        print(i,':',program.code[i])
    print()
    temps = 100*[0]                 # a 'large' number of registers
    stack = 200*[0]                 # a 'large' stack in case of recursion
    pc = program.first_stmt         # start at the first statement
    sp = 100                        # initialize stack pointer (unused here)
    while pc < len(program.code):   # run to the bottom
        inst = program.code[pc]     #     fetch an instruction
        pc += 1                     #     increment to refer to next
        chg = inst.execute(temps, stack, pc, sp)  #     execute the instruction
        if chg is not None:         # see if anything new was returned
            pc, sp = chg            # only if either changed (extra credit)

def run_file(filename):
    """Run the program stored in the given file"""
    program = Program() 
    for line in open(filename):
        print(line,end='')
        compile_line(program,line)
    run_program(program)

if __name__ == "__main__":
    testfile = open("test.txt","w")

    print("a = 3",file=testfile)
    print("b = a+2",file=testfile)
    print("(b+1)*(b+1)+a",file=testfile)

    testfile.close()
    run_file("test.txt")

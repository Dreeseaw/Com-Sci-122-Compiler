class Instruction:
    """Simple instructions representative of a RISC machine

    These instructions are mostly immutable -- once constructed,
    they will not be changed -- only displayed and executed
    """
    def __init__(self, t):      # default constructor
        self._temp = t          # every instruction has a register
    def get_temp(self):         #     which holds its answer
        return self._temp

class Print(Instruction):
    """A simple non-RISC output function to display a value"""
    def __str__(self):
        return "print T" + str(self._temp)
    def execute(self,temps,stack, p,s):
        print( temps[self._temp] )

class Initialize(Instruction):
    """T1 = 2"""
    def __init__(self, t, v):
        self._temp = t
        self._val = v
    def __str__(self):
        return "T" + str(self._temp) + " = " + str(self._val)
    def execute(self,temps,stack,p,s):
        temps[self._temp] = self._val

class Load(Instruction):
    """T1 = stack[0]"""
    def __init__(self, t, s):
        self._temp = t
        self._s = s
    def __str__(self):
        return "T" + str(self._temp) + " = stack[" + str(self._s) + "]"
    def execute(self,temps,stack,p,s):
        temps[self._temp] = stack[self._s]

class Store(Instruction):
    """stack[0] = T1"""
    def __init__(self, t, s):
        self._temp = t
        self._s = s
    def __str__(self):
        return "stack[" + str(self._s) + "] = T" + str(self._temp)
    def execute(self,temps,stack,p,s):
        stack[self._s] = temps[self._temp]

class Perform(Instruction):
    """T3 = T1+T2"""
    def __init__(self, t, t1, op, t2):
        self._temp = t
        self._temp1 = t1
        self._temp2 = t2
        self._op = op
    def __str__(self):
        return "T" + str(self._temp) + " = T" + str(self._temp1) + str(self._op)+"T"+str(self._temp2)
    def execute(self,temps,stack,p,s):
        temps[self._temp] = eval(str(temps[self._temp1])+str(self._op)+str(temps[self._temp2]))

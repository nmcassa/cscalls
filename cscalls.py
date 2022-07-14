import sys
import stack

#One at ___ (add var)
#___ is lit(var = __)
#___ is hacking (remove var from stack)
#Please watch
#I can drop (move up var stack)
#Drop AWP (move down var stack)
#PEEK (print)
def interpret(lines):
    var_stack = stack.Stack()

    for line in lines:
        if line == "PEEK":
            var_stack.print()

        if line[:7] == "One at ":
            var_stack.push(line.split(' ')[2])
        
if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nPlease give .cscall file as an second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        interpret(s.splitlines())

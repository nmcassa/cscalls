import sys
import stack

#One at ___ (add var)
#hacking istg pls report(remove var from stack)
#Tagged ____ times (move pointer to index)
#I'm loaded I can drop (move up var stack)
#GRAB AWP (move down var stack)
#HELP ___ (Label)
#Why is no one ___ (Goto)
#PEEK (print)
#WHERES MY TEAM (print stack)
def interpret(lines):
    var_stack = stack.Stack()
    curr = 0

    while curr < len(lines):
        line = lines[curr]
        
        if 'PEEK' in line:
            var_stack.print()

        if 'WHERES MY TEAM' in line:
            var_stack.print_stack()

        if line[:7] == "One at ":
            var_stack.push(line[7:])

        if 'hacking istg pls report' in line:
            var_stack.remove()

        if 'I\'m loaded I can drop' in line:
            var_stack.up()

        if 'GRAB AWP' in line:
            var_stack.down()

        curr += 1
        
if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nPlease give .cscall file as an second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        interpret(s.splitlines())

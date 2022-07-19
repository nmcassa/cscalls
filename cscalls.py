import sys
import stack
import hand
import label

#One at ___ (add var)
#hacking istg pls report(remove var from stack)
#Tagged ____ times (move pointer to index)
#I'm loaded I can drop (move up var stack)
#GRAB AWP (move down var stack)

#HELP ___ (Label)
#Why is no one ___ (Goto)
#save pls i have $_(compare pointer and held goto if true)

#What skin is that? (set hand to pointer)
#Drop me AK (get hand)
#YO INSPECT (print hand)

#You see him (Look)
#PEEK (print)
#WHERES MY TEAM (print stack)
#team? (input)
def interpret(lines):
    labels = []
    var_stack = stack.Stack()
    held_var = hand.Hand()
    curr = 0

    for line in lines:
        if 'HELP' in line:
            labels.append(label.Label(line[5:], curr-1))
        curr += 1

    curr = 0

    while curr < len(lines):
        line = lines[curr]
        
        if 'PEEK' in line:
            var_stack.print()

        elif 'WHERES MY TEAM' in line:
            var_stack.print_stack()

        elif 'team?' in line:
            var_stack.push(input())

        elif line[:7] == "One at ":
            var_stack.push(line[7:])

        elif 'hacking istg pls report' in line:
            var_stack.remove()

        elif 'I\'m loaded I can drop' in line:
            var_stack.up()

        elif 'GRAB AWP' in line:
            var_stack.down()

        elif 'You see him' in line:
            var_stack.look()

        elif 'Tagged ' in line:
            var_stack.index(int(line.split(' ')[1]))

        elif 'What skin' in line:
            held_var.set(var_stack.look())

        elif 'Drop me AK' in line:
            held_var.get()

        elif 'YO INSPECT' in line:
            held_var.print()

        elif 'Why is no one ' in line:
            for item in labels:
                if item.name == line[14:]:
                    curr = item.index

        elif 'save pls i have $' in line:
            if var_stack.look() is held_var.get():
                if int(line[17:]) >= 0:
                    curr = int(line[17:])-1

        curr += 1
        
if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('\n\nPlease give .cscall file as an second arg')
    else:
        h = open(sys.argv[1], 'r')
        s = h.read()
        h.close()
        interpret(s.splitlines())

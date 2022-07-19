# cscalls
 A stack based esoteric programming language that is made up of CS:GO callouts
 Contains a hand object, like a held piece in tetris, for comparisons

## Syntax

| cscall | action |
| --- | --- |
| One at ___ | Add var to stack |
| hacking istg pls report | Remove var at pointer |
| I'm loaded I can drop | move up var stack |
| GRAB AWP | move down var stack |
| Tagged ____ times | move pointer to index |
| HELP ___ | Label |
| Why is no one ___ | Goto |
| save pls i have $___ | compare pointer and held, goto if truthy |
| What skin is that? | set hand to pointer | 
| Drop me AK | get hand | 
| YO INSPECT | print hand |
| You see him | look (peek) |
| PEEK | print |
| WHERES MY TEAM | print stack |
| team? | input |

### Hello World
```
One at Hello World!
PEEK
```

### Cat
```
team?
PEEK
```

### Truth Machine
```
One at 0
What skin is that?
One at 1
team?
save pls i have $6
Why is no one A
PEEK
Why is no one END
HELP A
GRAB AWP
What skin is that?
save pls i have $13
Why is no one END
HELP B
PEEK
Why is no one B
HELP END
```


### Running a file example:

```
python cscalls.py example/hello.cscall
```

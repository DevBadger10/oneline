# Coding language idea
<!-- This was taken directly from my phone, which is where I first wrote it down.> <!-->
Assembly but in one line. Called Oneline.

It has the classic commands like:
- lbl
- jmp
- cjmp
- mov
- add
- sub

and then some customs like:
- cpy
- rjmp
- ret
- cat
- swp

It has the registers A, B, C, D, E and F, along with some more specials like Z for temporary storage of values, X for the terminal output, and M for the user's input.

All code is one line long and seperated by colons :.

Registers have special commands. ! then a register wipes that registers value.

For additional registers, they have another special command via the | symbol. For Z, it sets all other registers values to itself. For X, it ends the program. For M, it waits till the user presses enter on the input. And that's it!
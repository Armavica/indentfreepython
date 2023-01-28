"""A simple implementation of Brainfuck in idiomatic Python."""

def jump_map(code):
    """
    Compute the mapping from every '[' to its corresponding ']' and reversely.
    """
    jump = {}
    pos = []
    for i, instr in enumerate(code):
        if instr == "[":
            pos.append(i)
        if instr == "]":
            j = pos.pop()
            jump[i] = j
            jump[j] = i
    return jump


def eval_bf(code):
    """
    Interpret the Brainfuck code passed in argument.
    """
    jump = jump_map(code)

    tape = [0] * 30000
    ptr = 0
    pc = 0

    while pc < len(code):
        c = code[pc]
        if c == "+":
            tape[ptr] += 1
        elif c == "-":
            tape[ptr] -= 1
        elif c == "<":
            ptr -= 1
        elif c == ">":
            ptr += 1
        elif c == ".":
            print(chr(tape[ptr]), end="")
        elif c == ",":
            tape[ptr] = ord(input()[0])
        elif c == "[" and tape[ptr] == 0:
            pc = jump[pc]
        elif c == "]":
            pc = jump[pc] - 1
        pc += 1

"""
An implementation of Brainfuck in idiomatic Python, closely following the
indent-free implementation.
"""

def jump_map(code):
    """
    Compute the mapping between opening/closing and closing/opening delimiters.
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

def update_tape(tape, ptr, instr):
    """
    Update the state of the tape.
    """
    if instr == ",":
        tape[ptr] = ord(input()[0])
    else:
        tape[ptr] += {"+": 1, "-": -1}.get(instr, 0)
    return tape

def update_ptr(ptr, instr):
    """
    Update the pointer.
    """
    return ptr + {">": 1, "<": -1}.get(instr, 0)

def update_pc(pc, x, instr, jump):
    """
    Update the program counter.
    """
    if instr == "[" and x == 0:
        pc = jump[pc]
    if instr == "]":
        pc = jump[pc] - 1
    return pc + 1

def instruction(tape, ptr, pc, jump, code):
    """
    Execute the instruction located at `pc`.
    """
    if code[pc] == ".":
        print(chr(tape[ptr]), end="")
    tape = update_tape(tape, ptr, code[pc])
    ptr = update_ptr(ptr, code[pc])
    pc = update_pc(pc, tape[ptr], code[pc], jump)
    return tape, ptr, pc, jump, code

def eval_bf(code):
    """
    Interpret the Brainfuck code passed in argument.
    """
    jump = jump_map(code)
    tape = [0] * 30000
    ptr = 0
    pc = 0
    while pc < len(code):
        tape, ptr, pc, _, _ = instruction(tape, ptr, pc, jump, code)

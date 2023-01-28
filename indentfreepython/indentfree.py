"""
An implementation of Brainfuck in pure Python, without any indentation.

Because Brainfuck is Turing-complete, this proves that one can program any
computable function in indent-free Python.

To make things a little harder, this implementation doesn't use any `for`,
`while`, `if`, function definition, list/dict/set comprehension, or ternary
operator (`a if c else b`).
"""

jump_map1 = lambda jump, pos, i, code: {"[": (jump, pos + [i]), "]": not pos or (jump | {pos[-1]: i, i: pos[-1]}, pos[:-1])}.get(code[0], (jump, pos))

jump_map = lambda jump, pos, i, code: (code and [jump_map(*jump_map1(jump, pos, i, code), i + 1, code[1:])] or [(jump, pos, i, code)])[0]

update_tape = lambda tape, ptr, c: tape[:ptr] + [c == "," and ord(input()[0]) or tape[ptr] + {"+": 1, "-": -1}.get(c, 0)] + tape[ptr+1:]

update_ptr = lambda ptr, c: ptr + {">": 1, "<": -1}.get(c, 0)

update_pc = lambda pc, x, c, jump: {"[": [pc, jump.get(pc)][x == 0], "]": jump.get(pc, 0) - 1}.get(c, pc) + 1

update = lambda ntape, nptr, pc, jump, code: (ntape, nptr, update_pc(pc, ntape[nptr], code[pc], jump), jump, code)

instruction = lambda tape, ptr, pc, jump, code: print(end=code[pc] == "." and chr(tape[ptr]) or "") or update(update_tape(tape, ptr, code[pc]), update_ptr(ptr, code[pc]), pc, jump, code)

program = lambda tape, ptr, pc, jump, code: pc >= len(code) or program(*instruction(tape, ptr, pc, jump, code))

eval_bf = lambda code: program([0] * 30000, 0, 0, jump_map({}, [], 0, code)[0], code)

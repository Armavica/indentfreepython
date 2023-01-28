from indentfreepython import simple
from indentfreepython import indent
from indentfreepython import indentfree
from indentfreepython import programs

print("Simple implementation")
simple.eval_bf(programs.HELLOWORLD)

print()

print("Indent implementation")
indent.eval_bf(programs.HELLOWORLD)

print()

print("Indent-free implementation")
indentfree.eval_bf(programs.HELLOWORLD)

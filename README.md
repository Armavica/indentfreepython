# Indent-free Python

Many serious programmers are understandably frustrated with the bigoted
approach of Python to nesting code blocks[^1].  While all proper programming
languages employ some kind of opening and closing separators to unambiguously
delimit code blocks (from LaTeX's familiar `{`/`}`, to bash's elegant `if`/`fi`
or MATLAB's efficient `for`/`end`, `while`/`end` `switch`/`end`, `try`/`end`,
`if`/`end` and `parfor`/`end`), in their worst lapse of judgement, the Python
designers chose the most ridiculous "solution" to this problem: to give a
semantic meaning to whitespace.

Here, we propose a cure to this nonsense, by showing that indentation in Python
is as egregious as it is superfluous: indeed, as we demonstrate, any computable
function can be programmed in Python without using any indentation.

[^1]: `from __future__ import braces`

## Motivation

Although the absurdity of Python's indentation design will immediately appear
to even the most novice and inexperienced programmer, let us take a moment to
fully comprehend the implications of this cruel and unfunny joke.

### A literal joke

[Whitespace](https://en.wikipedia.org/wiki/Whitespace_\(programming_language\))
is actually the name of an esoteric programming language using only spaces,
tabulations, and line breaks, created as a joke.  By giving spaces a semantic
meaning, the Python designers borrowed a whole third of the characters of
Whitespace.  With what kind of seriousness do the Python designers expect to be
taken, when they proudly rely on an entire third of the functionalities of an
**esoteric** language created as a **joke**?

### Debilitating brittleness

The idea of attributing a meaning to invisible characters must only have come
to someone ignorant of elementary typography, for they would otherwise be
acquainted with the fact that not all spaces are equivalent.  Damned be the
fool who, by distraction or clumsiness, instead of the space bar, should err to
press the keyboard key that inputs a `U+00A0` No-Break Space, a `U+2009` Thin
Space, a `U+2007` Figure Space, a `U+2004` Three-Per-Em Space, or one of the 17
types of spaces easily available in modern computing environments.  This poor
soul is condemned to guess which of the thousands of invisible characters in
his file is unlike all of the others, or to replace them all one by one until
he or she finds the cause of his or her misfortune.

Alas, ancient input methods with only one or a couple of available space types
are not shelters from this draconian rigidity, for their user must exert
themselves to remain excruciatingly alert at all time, lest an unfortunate jest
of their hand or of other parts of their anatomy in the vicinity of the space
bar should randomly sprinkle their file with invisible characters that will
change the meaning of their program in ways that will make debugging extremely
arduous.

### Crushing inefficiency

The question needs to be asked: what do the Python designers find so attractive
about the space bar for designing a language that relies so heavily upon it?
What kind of bizarre satisfaction do they draw from pressing it so many times
in a row, at the beginning of each line of code?  We evaluate that in real
Python code bases, the average line sees the first fourth to third of its
length filled with useless spaces.  Imposing such hardship to oneself can be
considered harmful eccentricity, but designing a language to intentionally
force millions of developers to spend a third of their time programming
pressing the space key is misanthropy of hardly conceivable proportions.

### Accessibility nightmare

This lack of foresight is a revolting affront to partially sighted and visually
impaired people, who rely on screen readers to read digital text.  Clearly, not
only spaces cannot be seen, they also cannot be heard, which makes
understanding a Python code by ear simply impossible.  Besides, the rare screen
readers that can be configured to spell out every character, visible or not,
will impose an unbearable litany of "SPACE, SPACE, SPACE, SPACE" to their
users, at the start of every single line of code.


## The cure

The need to interface with existing Python code bases forces some of us to use
this language, filling novices with the heart-crushing prospect of having to
deal with imposed significant indentation.  Fortunately, not everything needs
to be indented in Python.  One must ask then: what ever can possibly be done,
by limiting oneself to the severely restricted subset of indentation-free
Python?

We show that Python without any indentation Turing-complete.  That is, given
any program written in any language (actually any computable function), one can
always write an equivalent program in Python without using any indentation.

We show this by implementing an interpreter of
[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) in Python, without using
any indentation.  Brainfuck being a Turing-complete language, successfully
implementing a Brainfuck interpreter in a given language is one of the most
entertaining ways to prove that this language is itself Turing-complete.

To translate any program into an indent-free Python program, it suffices to
translate it into a Brainfuck program, and evaluate it with this interpreter.

In the timeless style of some of the most venerable programming languages,
every line starts on the first column with a visible character.  It is to note
that our implementation doesn't rely on the cheap tricks that consist of
placing the body of a `for` or `while` loop on its first line, in fact, it
doesn't use any `for` or `while` loop at all.  Conditionals,
`list`/`dict`/`set` comprehensions, ternary expressions (`a if c else b` and
function definitions with `def` are also banned.

For reference, and to show how nasty code following traditional misguided
Python conventions can look, we also provide two other implementations:

- `indent` contains indented code that closely follows the `indentfree`
  implementation;
- `simple` contains a naive implementation of a Brainfuck interpreter.

The three functions `indentfree.eval_bf`, `indent.eval_bf` and `simple.eval_bf`
should be functionally identical.

Some examples of Brainfuck programs are provided in the module `programs.py`.

Note that due to hostile efforts from the Python designers to aggressively
discourage programmers not willing to submit to imposed indentation, you might
need to raise Python's recursion limit to run the `ROT13` program with the
indent-free implementation, for example with `import sys;
sys.setrecursionlimit(10000)`.

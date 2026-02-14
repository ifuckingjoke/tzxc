![tzxc](https://raw.githubusercontent.com/ifuckingjoke/tzxc/refs/heads/main/logo.svg)

[RU](README.md)

# tzxc

Terminal module with a controlled reverse subtraction loop and
configurable execution behavior.

------------------------------------------------------------------------

## Installation

``` bash
pip install tzxc
```

------------------------------------------------------------------------

## Quick Start

``` python
from tzxc import Tourter

game = Tourter()
game.zxc(delay=1)
```

------------------------------------------------------------------------

## Description

The `zxc()` method starts a loop beginning at `1000` and subtracts `7`
on each iteration.

The loop stops when the value reaches `6`, unless infinite mode is
enabled.

Total iterations with default settings: **143**.

------------------------------------------------------------------------

## API

### Class

``` python
Tourter()
```

When instantiated, the class stores the current system username (using
`getpass.getuser()`), which is used for output in automatic mode.

------------------------------------------------------------------------

### Method

``` python
zxc(
    delay: int,
    infinity: bool = False,
    hard_mode: bool = False,
    ctrl_off: bool = False,
    crazy_mode: bool = False,
    lang: str = "ru"
)
```

------------------------------------------------------------------------

## Parameters

**delay** (`int`, required)\
Delay between actions in seconds.\
In normal mode, one iteration takes approximately `delay * 2` seconds.

------------------------------------------------------------------------

**infinity** (`bool`, default `False`)\
If `True`, once the value reaches `6`, the loop restarts from `1000`.

------------------------------------------------------------------------

**hard_mode** (`bool`, default `False`)

Enables manual mode:

-   The user must input the result of `x - 7`
-   Incorrect answers are counted
-   After 5 incorrect answers, the system reboot command is executed
-   A correct answer resets the error counter

------------------------------------------------------------------------

**ctrl_off** (`bool`, default `False`)\
Intercepts the `SIGINT` signal (Ctrl+C) and prevents interruption.\
The original signal handler is restored after execution.

------------------------------------------------------------------------

**crazy_mode** (`bool`, default `False`)\
Reserved for future updates. Currently not used in execution logic.

------------------------------------------------------------------------

**lang** (`"ru"` \| `"eng"`, default `"ru"`)\
Defines the language of messages.

------------------------------------------------------------------------

## Behavior

### Normal Mode

1.  Automatic execution\
2.  Displays the expression and the calculated result\
3.  No user input required

### Hard Mode

1.  Requires user input\
2.  After 5 incorrect answers, a system reboot command is triggered:

-   Windows → `shutdown /r /t 0`
-   Linux → `sudo reboot`

------------------------------------------------------------------------

## Complexity

When `infinity=False`:

-   143 iterations\
-   Time complexity: `O(1)`\
-   Space complexity: `O(1)`

In an abstract model (if the initial value is replaced with `n`) →
`O(n)`.

------------------------------------------------------------------------

## Architecture

The module relies on:

-   system calls (`os`, `sys`)
-   signal handling (`signal`)
-   execution delays (`time`)
-   username detection (`getpass.getuser()`)

------------------------------------------------------------------------

## Initialization Details

On start:

``` python
x = 1000
uncorrect_answers = 0
```

The loop is implemented using:

``` python
while True:
```

Termination is controlled manually using `break`.

------------------------------------------------------------------------

## Iteration Count

Calculation:

    (1000 - 6) / 7 = 142

Since the final condition also passes through the loop, the total number
of iterations is **143**.

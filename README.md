## extprint

- **prints with color and background color**

- **prints lists and their indexes line by line**


## Install

```sh
pip install extprint
```

## Usage

```python
from extprint import printlist,printcolored,set_default_print_options
```

```python
list = [1,2,3,4,5,6,7,8,9,0]

printlist(list, seperator="----->", start_index=0, color="GREEN", bold=True)

printcolored("HELLO", color="BLUE", bold=True)

set_default_print_options(seperator="=",color="VIOLET",bold=True)

printlist(list)

printcolored("HI")
```
```
0 -----> 1
1 -----> 2
2 -----> 3
3 -----> 4
4 -----> 5
5 -----> 6
6 -----> 7
7 -----> 8
8 -----> 9
9 -----> 0
HELLO
1 = 1
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 = 0
HI
```


## Available colors-options

```python
printcolored("", color="?")

```

- **BLACK**
- **RED**
- **GREEN**
- **YELLOW**
- **BLUE**
- **VIOLET**
- **BEIGE**
- **WHITE**

- **BOLD**
- **ITALIC**



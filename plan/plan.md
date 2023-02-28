

## Project task assignments


At the very top of the source files should be name of the team and name of the team-member who worked on this file.
```py
# Tripple-Double
# @author xlogin00
```

> **Note**
> Each member of the team must have his own branch. Every source file must contain doxygen comments and header, defined above. Deadline for each member is 1 week (ends 01.03.2023)

### Design (xpodho08)
Implement drafts in `/mock` using [tkinter](https://docs.python.org/3/library/tkinter.html).

**Requirements**
Design implementation should be written in `/src/view/view.py`. Folder `view` has to contain all the necessary files for `view.py`.

- Interface must contain following buttons:
	- Operations:
		- plus (+)
		- minus (-)
		- multiply (*)
		- divide (/)
		- factorial (!)
		- exponentiation (^)
		- equals (=) *after clicking "equals" expression from display is sent to parser*
		- clear *clears display*
		- brackets (()) *both brackets should be separate buttons for now*
	- Tooltips
		- Implement button with question mark (in top left corner, circle) , which you can click to show tooltip for each button for 3 seconds.
- Keyboard
	- User should be able to type in any symbol using keyboard only.

### Expression parser (xturyt00)
Parser implementation should be written in `/src/parser/parser.py`. Folder `parser` has to contain all the necessary files for `parser.py`. 

**Requirements**
Parsing rules:
E -> E + E
E -> E - E
E -> -E
E -> E * E
E -> E / E
E -> E ^ E
E -> !E
E -> (E)
E -> e

Create priority table and parser. Parser must use functions implmented by `xkolia00 `. After input is validated, parsed and calculated, return result back to view.

### Math (xkolia00 )
Math implementation should be written in `/src/math/math.py`. Folder `math` has to contain all the necessary files for `math.py`.

**Requirements**
- Implement functions:
	- plus (+)
	- minus (-)
	- multiply (*)
	- divide (/)
	- factorial (!)
	- exponentiation (^)

Each function takes parameters *a* and *b*, with type of number and returns result.
Test all math functions with various inputs, using [unit testing](https://www.javatpoint.com/python-unit-testing#:~:text=What%20is%20the%20Python%20unittest,detect%2C%20and%20fix%20the%20errors.) in python. Test folder should be created next to `math.py`.


### Profiling (xbuten00)
Profiling implementation should be written in `/src/profiling/profiling.py`. Folder `profiling` has to contain all the necessary files for `profiling.py`.

**Requirements**
Profiling must use math library, written by `xkolia00`. If it's not done yet, use your custom functions, then replace them.

Profiling takes sequence of random digits `1, 2, 3, 4, 5, 6 ...` min. 1000.
Using formula below, it outputs $s$.

$s = \sqrt{\frac{1}{N-1}(\sum_{i=1}^{N}x_i^2-N\overline{x}^2)}$

$\overline{x} = \frac{1}{N}\sum_i^Nx_i$

### User documentation (xbuten00)

## Communication
Team uses for communication **Telegram** and **Discord**.

## Version control system
As VCS, we use github.com

**Repository access**
Email to xturyt00@stud.fit.vutbr.cz with subject "repository access" and github username to get access to our repo.


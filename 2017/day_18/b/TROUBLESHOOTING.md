Greetings and thank you for using PRESENT PRINTER 3000!
If you are reading this, you are probably experiencing problems with our
product. We are deeply sorry for your troubles and try our best to support you.

Some of our customers mentioned problems starting the program because in some
instances not all required initial checks could be completed so the program
could not run. In most of these cases this was due to an error during the
installation process.

Fortunately those can be easily fixed since the problem lies within incorrect
information in the check files not an incorrect program behaviour.

To fix this you can adjust the files, that are read by the check to the correct
value.

Every check consists of two files: a .in file and a .ans file. Those files can
be found in the check directory of your installation.
The .ans file must contain the correct information that is needed by the
program. This file is read and checked in order to assure its functionality.
The .in file contains the input the program assumes in order to check the
content in the .ans file. There is no point in changing this file since it is
not actually read by the program. It just exists for troubleshooting so its
easier to understand what is happening.

Every check uses a specific algorithm to transform the input to the required
output format. Those algorithms are described below. In order to fix the checks,
simply update the .ans files with the correct values and run the program again.

If you are still having troubles starting the program, feel free to contact our
support team at:

Holle & Stern Inc.
Georg-Herder-Str. 42
18055 Rostock


age
===

This check was not yet reported to fail. If it does, the value from the .in
file must be written into the .ans file. The .ans file must contain a single
two digit number.


name
====

Again, this check was never reported to fail. If it does, the value from the .in
file must be written into the .ans file. The .ans file must contain a value
representing a full name.


location
========

The programm has to determine the best route to the nearest present printer
available. This is done by spanning a grid of coordinates over the area,
starting with the current location. The grid is rotated in the general direction
of the nearest printer, so only positive coordinates are considered. 

To determine whether a specific coordinate is accessible and can be used for the
route, the following algorithm is used:

- calculate x*x + 3*x + 2*x*y + y + y*y from the coordinate
- Add the number from the .in file to the result
- transform the result into the binary representation
- conunt the number of bits that are 1
-- if this number is even, the coordinate is accessible
-- if this number is odd, the coordinate is inaccessible

For example consider the number in the .in file is 10, the map of the area would
look like this (accessible coordinates are written with a ., inaccessible are
written with a _)

  0123456789
0 ._.____.__
1 .._.._..._
2 _....__...
3 ___._.___.
4 .__.._.._.
5 ..__...._.
6 _...__.___

The programm considers (1,1) to be the current location of the user. It tries to
find the shortest path to a specific coordinate (which is also written in the 
.in file). Only horizonal und vertical movements are allowed. Moving diagonally
is not possible.

The .ans file must contain the length if the shortest path to the specified
coordinate.

Given the example above and a goal of (7,4) the shortest path would look like
this (with x describing the path taken).

  0123456789
0 ._.____.__
1 .x_.._..._
2 _xxx.__...
3 ___x_.___.
4 .__xx_xx_.
5 ..__xxx._.
6 _...__.___

So the shortest path would have a length of 11.


present
=======

This check determines which kind of present will be printed for the birthday
child. This is done through an eliminatation algorithm.

First all possible presents that can be printed are determined and numbered
starting with 1. The total number of availbe presents can be found in the .in
file. Then, all numbers are arranged in a circle structure, e.g. like this:

  1
5   2
 4 3

This circle is then reduced to exactly one present. Starting with present 1, and
then in clockwise order, the present directly opposite of the current present is
eliminated. If there are two presents opposite the current present, the left one
is eliminated (from the point of view of the current present).

Given the example above with 5 presents, this is how the eliminatation will
occur (the current present is marked with a dot).

  1.         1         1   2        2.   
5   2  ->  5   2.  ->         ->        ->  2
 4 3         4           4.         4

3 is on the left as viewed from 1, and 1 is in the left as viewed from 4, so they
get eliminated instead of 4 and 2.

The .ans file must contain the number of the present that will survive the
eliminatation process.


printer
=======

To check whether the printer is working correctly, the computer and the printer
run a synchronizing checking routine. The checking routine consists of several
instructions that are run sequentially. The instructions can be found in the .in
file. It consists of different types of instructions and it uses named registers
to store values during its run. Each routine has its own registers, so registers
on the computer will not influence the registers on the printer and vice versa.

The possible instructions are as following:

- ist R V, sets the value of register R to the value V
- plu R V, adds the value V to the current value of register R
- mal R V, multiplies the current value of register R by V and stores the result
  in register R
- mod R V, performs the modulu operation of the current value of register R and
  the value V (so R % V) and stores the result in register R
- spr R V, jumps V steps within the instruction list, but only if the current
  value of register R is greater than zero. Otherwise the routine continues
  normally. V might be negative.
- sen R, Sends the current value of register R to the other programm. Send
  messages are stored in queues until the other programm can receive them. So
  sen instructions are non-blocking.
- erh R, receives a value from the other program and stores the result in
  register R. If there is already a value in the send queue of the other program
  it will take the first value and remove it from the queue. Otherwise the
  program will wait until a value is send by the other program.

All registers start with a value of 0, except for register p. The program run
on the computer sets register p to 0 while the program run on the printer sets
register p to 1.

If both programs reach a erh instruction without any data waiting for them in a
queue, a deadlock is reached and both programms will terminate.

The .ans file must contain the value of successful sen instructions from the
program on the printer.

An example program might look like this:

ist a 1
plu a 2
mal a a
mod a 5
sen a
ist a 0
erh a
spr a -1

- first the value of register a is set to 1. Then 2 is added to its value. Then
  its multiplied with itself and set to itself modulo 5. So the value will be
  4 (((1 + 2) * 3) % 5)
- Then the programm sends the value of a to the oher program and resets a to 0.
  It will now wait until the other program reaches the sen instruction and
  receive its value (which will be 5). Register a is set to this value.
- The spr instruction can be applied, since a is greater than zero and the
  instruction pointer jumps one step back to the erh instruction.
- Both programs will reach the erh instruction without any further sends, so the
  deadlock is reached and both programs terminate. The final result would be 1
  since only one send command was issued.

The programs are not required to run at the same speed. The sen and erh
instructions are specifically designed to synchronize both. This means that the
host program could already have reached the first erh instruction without the
printer program even starting yet.
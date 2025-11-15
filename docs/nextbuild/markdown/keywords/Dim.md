# DIM

## Syntax

```
DIM variable_name[,variable_name...] [AS type] [= value]
```

## Description

DIM is used in Sinclair BASIC to declare arrays. In ZX BASIC, its usage has been extended to declare any variable and its type. A type is a name for the kind of data (Integer, Byte, String, etc.) it holds.

Where can be one of INTEGER, BYTE, FLOAT, etc. See the list of available types. If type is not specified, FLOAT will be used, unless you use a suffix (usually called sigil) like $ or %.

**Default variable values**

ZX BASIC will initialize any numeric variable to 0 (like most BASIC flavors), and any string variable to an empty string, so you don't need to initialize them, though it's recommended.

***Undeclared variables***

ZX BASIC allows you to use undeclared variables. In Sinclair BASIC, using an unassigned variable triggered the error Variable not found, but in ZX BASIC it will default to 0 value.

You can enforce variable declaration using the *--explicit* command line option. When it's used, the compiler will require every variable to be declared with DIM before being used for the 1st time.
You can also enforce explicit type declaration using the --strict command line option. This way, if you use DIM you will be required to declare also the type needed.

	'Declares 'a' as a 16 bit signed integer variable
	DIM a AS INTEGER

	'Declares 'b' as a Float because no type is specified
	DIM b

	'Declares 'c' as String, because of the '$' suffix
	DIM c$

	'Declares d as String, using an explicit type
	DIM d as STRING

	'Declares x, y as 32bit unsigned integers in a single line
	DIM x, y as ULONG

	'Here S is declared as String, because R has a $
	DIM R$, S

	'initialize an unsigned byte with 5
	DIM b as UBYTE = 5

	'warning: Using default implicit type float for a

	DIM a = 5

	'No warning here, because the compiler knows it is an integer (% suffix)

	DIM c% = 5

**Variable mapping**

You can declare a variable at a fixed memory address. This is called *variable mapping.*
E.g. in ZX Spectrum Sinclair's ROM address 23675 contains a system variable which points to UDG address. You could traditionally read this content by doing:

	PRINT "UDG memory address is "; PEEK 23675 + 256 * PEEK 23676

It is a 16 bit unsigned integer value (Uinteger). We can map a variable on that address:

	DIM UDGaddr AS Uinteger AT 23675
	PRINT "UDG memory address is "; UDGaddr

This is more readable. Also, setting a value to this variable changes UDG address.

**Variable aliasing**

A variable is just a memory position containing data. In same cases you might find useful a variable having more than one name, for the sake of code readability:

	DIM a AS Float = PI
	'REM Now let's declare an alias of 'a', called 'radians'
	DIM radians AS Float AT @a
	PRINT "radians = "; radians
	LET radians = 1.5
	PRINT "a = "; a

As you can see, both *radians* and a can be used interchangeably.

***Array Declaration***

**DIM a([*lower_bound* TO] *upper_bound* [, ...]) AS *type***

**Description**

By default, array indexes starts from 0, not from 1 as in Sinclair BASIC. You can change this behavior setting a different array base index using either a #pragma option or a command line option.

**Examples**

	'REM 'a' is an array of 11 floats, from a(0) to a(10)
	DIM a(10)

	''b' has the same size
	DIM b(0 TO 10)

**Initialized arrays**

You can also use DIM to declare an array, and promptly fill it with data. At the moment, this is not valid for string arrays, only numerical arrays. One handy way to use this would be to use an array to store a table, such as user defined graphics:

	'udg will be an array of 8 UBytes
	'Remember, the default in ZX Basic is for arrays to begin at zero, so 0-7 is 8 bytes
	DIM udg(7) AS uByte => {0,1,3,7,15,31,63,127}

	'This sets the System UDG variable to point to the 1st array element:
	POKE UINTEGER 23675,@udg(0): ' udg(0) is the 1st array element

Arrays of 2 or more dimensions can be initialized using this syntax:

	DIM udg(1, 7) AS uByte => {{0,1,3,7,15,31,63,127}, _
								{1,2,4,7,15,31,63,127}}

Each row contains an UDG. All bytes are stored in a continuous memory block

Note the usage of @variable to denote the location in memory the variable is stored into. Also see the extensions to POKE.

more info : https://zxbasic.readthedocs.io/en/docs/dim

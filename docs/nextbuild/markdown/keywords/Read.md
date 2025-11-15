# READ

## Syntax

```
READ *var or array_elem*[, *var or array_elem*, *var or array_elem*...]
```

## Description

**READ** gets the next data expression available from a DATA line definition and stores it into a variable (not arrays) or an array element. Instead of using INPUT() function or LET assignments, you can write a sequence (or several of them) of **READ** which might result in a compact and more readable code to initialize data variables.

READ gets the items one after another. This order can be changed using RESTORE.

  

**Example**

	DIM a(9) as UByte

	FOR i = 0 TO 9: REM 0 TO 9 => 10 elements
		READ a(i)
		PRINT a(i)
	NEXT i

	'notice the a(n) data entries
	DATA 2, 4, 6 * i, 7, 0
	DATA a(0), a(1), a(2), a(3), a(4)

This will output:

	2
	4
	12
	7
	0
	2
	4
	12
	7
	7
	0

Expressions are read and evaluated one by one, **when the READ sentence is executed**. When a **DATA** line is finished, the next one in the listing will be read. Traditionally if there's no more data to read, an *OUT of Data* error happened. In ZX Basic, the read sequence restarts from the beginning. The reading sequence can be altered with RESTORE  

**Remarks**

- This statement is Sinclair BASIC compatible.

More info : https://zxbasic.readthedocs.io/en/docs/read/

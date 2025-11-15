# LoadSDBank

## Syntax

```
LoadSDBank("filenname",nn,ss,oo,b)

nn = address (0000-1fff) offset in bank
ss = size to load 
oo = offset into file 
b  = bank to start 
```

## Description

LoadSDBank() can load files of any size (depending on RAM available) into the ZX Next's RAM banks. 
The routine will handle all required paging and loading, normally a startbank is all that is required.

- filename = filename to load
- address = 0 to $1fff and would be an offset into the start bank
- size = amount of data to load, 0 will the entire file.
- offset = Skip offset from the start of the file
- startbank = start 8kb bank

**Examples**

Load "mytiles.til" which is 16kb into bank 34 and 35

	LoadSDBank("mytiles.til",0,0,0,34)

To load the second 4kb from a file into bank 10

	LoadSDBank("test.dat",0,4096,4096,10)

Load a100kb file into banks 40 on onwards

	LoadSDBank("monty.mod",0,0,0,40)

When used with #DEFINE NEX the routine will become a macro and data will be included inside of the
NEX creating a self contained file. When this happens LoadSDBanks commands will be ignored, you can 
use LoadSD() or LoadSDBankRes() for loading once the application has started. 

**Remarks**

LoadSDBank is the way to store all your datafiles inside a finalized NEX file. Make sure you use 
#DEFINE NEX before #INCLUDE <nextlib.bas> to disable the code for LoadSDBank.

**Links**

- [LoadSD()](LoadSD.md)	
- [SaveSDBank()](SaveSDBank.md)
- [SaveSD()](SaveSD.md)
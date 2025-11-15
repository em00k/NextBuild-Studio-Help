# LoadSD

## Syntax

```
LoadSD("filenname",address,size,offset)
```

## Description

Loads a file from the filesystem. Size must be specified if the size is unknown you can use a size to set the maximum amount of data you want to load. Offset is how many bytes to skip from the start of the file.

**Examples**

To load a file called "myscreen.scr" into memory address $4000 with the length of 6912 bytes. 

	LoadSD("myfile.scr",$4000,6912,0)

To load the second 4kb from file "test.dat"

	LoadSD("test.dat",$4000,4096,4096)

**Remarks**

If you want to load larger files consider using **LoadSDBank()**

**Links**

- [LoadSDBank()](LoadSDBank.md)	
- [SaveSD()](SaveSD.md)
- [SaveSDBank()](SaveSDBank.md)
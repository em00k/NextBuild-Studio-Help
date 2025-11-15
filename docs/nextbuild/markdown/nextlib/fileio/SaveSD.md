# SaveSD

## Syntax

```
SaveSD("filenname",address,size)
```

## Description

Saves a file from memory to the filesystem. Size must be specified if the size is unknown you can use a size to set the maximum amount of data you want to load `0-65535`. Obviously the realistic size of the file you will want to save will be less than this.

**Examples**

To save a file called "myscreen.scr" from memory address `$4000/16384` with the length of `$1b00/6912` bytes. 

	SaveSD("myfile.scr",$4000,6912)

**Remarks**

If you want to save larger files consider using **SaveSDBank()**

**Links**

- [SaveSDBank()](SaveSDBank.md)
- [LoadSD()](LoadSD.md)	
- [LoadSDBank()](LoadSDBank.md)


## File IO

### File Management

NextBuild Studio supports the following file management commands:

- `LoadSDBank` - Load a file into a bank
- `LoadSD` - Load a file into RAM 
- `SaveSD` - Save a file from RAM

### LoadSDBank

```nextbuild
LoadSDBank(filename as string, address as uinteger, length as uinteger, offset as ulong, bank as ubyte)
``` 

`LoadSDBank` is used to load a file into a bank. It is a special commands because wheen used with the precompiler directive `#define NEX` changes the way the file is loaded into the bank.

NextBuild Studio will scan the main source file for `LoadSDBank` and construct a list of files to be included in the final `.nex` file. These will be included inside the `nex` and the files will not need to loaded into the bank at runtime. The `LoadSDBank` code will then be turned into an empty function.

`LoadSD` and `SaveSD` are used to load and save files from the SD card. 

### LoadSD 

```nextbuild
LoadSD(filename as string, address as uinteger, length as uinteger, offset as ulong)
```

### SaveSD

```nextbuild
SaveSD(filename as string, address as uinteger, length as uinteger)
```

## Example 1 - Loading a file into a bank
```nextbuild
    ' load 1024 bytes from the start of the file "myfile.txt" at address $c000
    LoadSD("myfile.txt", $c000, 1024, 0)

    ' save 1024 bytes from address $c000 to the file "myfile.txt"
    SaveSD("myfile.txt", $c000, 1024)
```

## Example 2 - Loading a file into a bank
```nextbuild
    ' tell NextBuild to include your file in the final .nex file
    #define NEX
    ' Specify the file to include
    ' load 1024 bytes from the start of the file "myfile.txt" at address $c000
    LoadSDBank("myfile.txt", $c000, 1024, 0, 32)
```

If you omit the `#define NEX` directive, the file will be loaded into the bank at runtime. This will affect all the ``LoadSDBank`` commands in the project.

## Related Functions

 - [LoadSDBank](LoadSDBank.md)
 - [LoadSD](LoadSD.md)
 - [SaveSD](SaveSD.md)

[Index](index.md)
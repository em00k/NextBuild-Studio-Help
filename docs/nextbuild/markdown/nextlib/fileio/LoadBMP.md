# LoadBMP(filename)

## Syntax

```
LoadBMP(filename)
```

## Description

Loads a bitmap file from the filesystem, directly into the screen buffer. The image will be automatically flipped vertically, this is because of the odd way BMP files are stored with a negative height. This is a very simplistic way to load an image into the screen buffer, and probably best to load the converted `.nxi` into a bank then point Layer2 RAM to it.

**Examples**

To load a file called "myscreen.bmp" into the screen buffer. 

```
LoadBMP("myscreen.bmp")
```

**Example using LoadSDBank()**

```
InitLayer2(MODE256X192)   	 
LoadSDBank("sanity_1_exported_256.nxi",0,0,0,38)             ' load the image into bank 38
NextReg(LAYER2_RAM_BANK_NR_12,38>>1)                         ' set the layer2 ram bank to 38
ShowLayer2(TRUE)                                             ' show the layer2
```
Because memory banks are 8KB in size, [LAYER2_RAM_BANK_NR_12](LAYER2_RAM_BANK_NR_12.md) uses 16KB paging which is why we need to halve the bank number with `>>1`.

**Remarks**

If you want to load larger files consider using **LoadSDBank()**

**Links**

- [Layer2RamBanks](LAYER2_RAM_BANK_NR_12.md)
- [LoadSDBank()](LoadSDBank.md)	
- [SaveSD()](SaveSD.md)
- [SaveSDBank()](SaveSDBank.md)
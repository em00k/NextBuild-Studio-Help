# InitSprites2(nr, address, bank)

## Syntax

```
InitSprites2(nr, address, bank)
```

## Description

Used to upload sprite data from a bank with offset *address* to sprite ram. This routine takes a bank number as an argument, which will be used to upload the data to sprite ram. This routine manages the memory paging for you.

The routine will page in the banks to slots 0 & 1 ``$0000-$3FFF``, then upload to the data to the sprite ram, then restore the default banks.

You can leave *address* as 0 to upload to upload from the start of the specified bank.

**Example**

```
' Say we want to upload 64 sprites with the data at $c000 (bank 1 is in slot 7 by default)
InitSprites2(63,$c000,1)
```

```
' Upload 64 sprites from bank 38 
InitSprites2(63,0,38)
```

Once upload the data in ram can be discarded

## Links 

- [InitSprites()](InitSprites.md)
- [UpdateSprite()](UpdateSprite.md)
- [NextRegister](_registers.md)
- [NextReg()](NextReg.md)
- [NextRegA()](NextRegA.md)



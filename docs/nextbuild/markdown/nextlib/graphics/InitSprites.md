# InitSprites(nr, address)

## Syntax

```
InitSprites(*nr*,*address*)
```

## Description

Used to upload sprite data from *address* to sprite ram. It is recommended to use [InitSprites2()](InitSprites2.md) instead.

**Example**
```
' Say we want to upload 64 sprites with the data at $c000
InitSprites(63,$c000)
```
Once upload the data in ram can be discarded. 

## Links 

- [InitSprites2()](InitSprites2.md)
- [UpdateSprite()](UpdateSprite.md)
- [NextRegister](_registers.md)
- [NextReg()](NextReg.md)
- [NextRegA()](NextRegA.md)



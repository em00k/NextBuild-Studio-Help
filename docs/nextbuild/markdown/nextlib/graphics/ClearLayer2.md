# ClearLayer2(nColour)

## Syntax

```
ClearLayer2(nColour)
```

## Description

Clears Layer2 with colour n. This routine will take the screen mode set by [InitLayer2](INITLAYER2.md). 

**Example**

```
InitLayer2(MODE320X256)     ' Set screen mode to 320x256
ClearLayer2($ff)            ' Clear Layer2 with palette index $ff, default is white.
ShowLayer2(TRUE)            ' Show Layer2

```

## See also

* [InitLayer2()](INITLAYER2.md)
* [ShowLayer2()](SHOWLAYER2.md)

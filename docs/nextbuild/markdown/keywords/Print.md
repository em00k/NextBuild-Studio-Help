# PRINT

## Syntax

```
PRINT [string][expression][value], | PRINT AT y,x; [string][expression][value]
```

## Description

Uses the ROM to PRINT text on to ULA. Can be used in conjunction with AT to set position

**Examples**

PRINT "HELLO NEXTBUILD"

	PRINT AT 10,4;"HELLO ZX BASIC"

You can also set attribute modifiers

	PRINT INK 2;"THIS TEXT IS RED"

**Remarks**

- This statement is Sinclair BASIC compatible.
- This function extends the Sinclair BASIC version.
- This statement also allows parenthesis and FreeBASIC syntax

More info : https://zxbasic.readthedocs.io/en/docs/

# TO

## Syntax

```
a TO b
```

## Description

TO can be used with FOR as follows:

**Examples**

	FOR n = 0 TO 10
	PRINT n
	NEXT n

It can also be use to select a portion of a string

	a$ = "NextBuild"
		PRINT a$(0 TO 3) : REM will print "Next"

	PRINT a$(4 TO ) : REM will print "Build"

**Remarks**

- This function is almost 100% Sinclair BASIC Compatible.

More info : https://zxbasic.readthedocs.io/en/docs/

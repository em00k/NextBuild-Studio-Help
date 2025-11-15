# PAUSE

## Syntax

```
PAUSE n
```

## Description

PAUSE CPU for n frames (0-65535) if n=0 means PAUSE forever until a keypress.

**Examples**

	PAUSE 0 : REM This will wait for a keypress
	PAUSE 1 : REM this will wait 1 frame

**Remarks**

- Using PAUSE will call ROM routine which may cause issues writing code for the NEX which can page out any part of memory. Use **WaitRetrace2(n)** and **WaitKey()** instead.

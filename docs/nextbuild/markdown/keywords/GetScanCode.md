# GETKEYSCANCODE

## Syntax

```
*scancode*=GETKEYSCANCODE()
```

## Description

Detects if a single key has been pressed

**Example**

	do
		if GetKeyScanCode()=KEYA
			END ' quits if A is pressed
		end if
	loop

**Remarks**

Requires: 

	#INCLUDE <keys.bas>

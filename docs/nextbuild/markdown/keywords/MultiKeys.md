# MULTIKEYS

## Syntax

```
MultiKeys(*scancode*)
```

## Description

Returns true if *scancode* key was detected

**Example**

	do
		if MultiKeys(KEYA) AND MultiKeys(KEYS)
			END ' quits if both A and S are pressed
		end if
	loop

**Remarks**

Requires: 

	#INCLUDE <keys.bas>

# USER_STORAGE_0_NR_7F

## Syntax

```
USER_STORAGE_0_NR_7F = $7F
```

## Description

**USER STORAGE 0 REGISTER** (R/W)

8-bit storage for user

These bits don't affect the HW in any way, the user can write any value to them and read it back.

May be useful for syncing with running copper code or whatever else you can think of.

Value is set to $FF upon soft reset.

Requires: 

	#INCLUDE <nextlib.bas>

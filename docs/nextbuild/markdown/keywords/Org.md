# ORG

## Syntax

```
'!org=*address*
```

## Description

Sets the start address of the program. If no org is set *32768* is used.

**Example**

	'!org=24576		' starts the program at 24576
	'!org=$6000		' starts the program at $6000

**Requires**

	#INCLUDE <nextlib.bas>

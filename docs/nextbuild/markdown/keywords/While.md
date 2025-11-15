# WHILE

## Syntax

```
WHILE ... END WHILE
```

## Description

WHILE is a compound statement used to perform loops. The code within a WHILE statement will repeat while the given condition is true. If the given condition is false the first time the inner sentences are never executed.

**Syntax**

	WHILE expression
		sentences
	END WHILE

Or

	WHILE expression
		sentences
	WEND

**Example**

	While a < b
		a = a + 1
		POKE a, 0
	END WHILE

An infinite loop:

	WHILE 1
		REM An infinite loop. This will issue a warning
		PRINT "HELLO WORLD"
	END WHILE

**Note:** For infinite loops use DO...LOOP

**Remarks**

- This statement does not exist in Sinclair Basic.
- **WHILE** can also be used with DO ... LOOP.

More info : https://zxbasic.readthedocs.io/en/docs/while/

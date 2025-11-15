# FOR

## Syntax

```
FOR n = n1 to n3 [ STEP n4 ] ... NEXT n
```

## Description

A For...Next loop initializes iterator to startvalue, then executes the sentences, incrementing iterator by stepvalue until it reaches or exceeds endvalue. If stepvalue is not explicitly given it will set to 1.

**Examples**

	FOR i = 1 TO 10: PRINT i: NEXT

**Differences From Sinclair Basic**

- The variable name after the NEXT statement is not required.
- Note that variable types can cause issues with ZX Basic For...Next Loops. If the upper limit of the iterator exceeds the upper limit of the variable type, the loop may not complete. For example


	DIM i as UByte

	FOR i = 1 to 300
		PRINT i
	NEXT i

Clearly, since the largest value a byte can hold is 255, it's not possible for i in the above example to exceed 300. The variable will "wrap around" to 0 and as a result, the loop will not ever terminate. This can happen in much more subtle ways when STEP is used. There has to be "room" within the variable type for the iterator to exceed the terminator when it is being incremented by "STEP" amounts. 

More info : https://zxbasic.readthedocs.io/en/docs/for/

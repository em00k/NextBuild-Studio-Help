# UBOUND

## Syntax

```
UBOUND (*array variable*), UBound(*array variable*, *dimension*)
```

## Description

Returns the array upper bound of the given . If the is not specified, it defaults to 1. If the specified is 0, then total number of dimensions is returned.

**Examples**

	DIM a(3 TO 5, 2 TO 8)
	PRINT UBound(a, 2) : ' Prints 8
	PRINT Ubound(a) : ' Prints 35, because dimension defaults to 1

The result is always a 16bit integer value.

If the is 0, then the number of dimension in the array is returned (useful to guess the number of dimensions of an array):

	DIM a(3 TO 5, 2 TO 8)
	PRINT UBound(a, 0): ' Prints 2, since 'a' has 2 dimensions

**Remarks**

- This function does not exists in Sinclair BASIC.

More info : https://zxbasic.readthedocs.io/en/docs/lbound/

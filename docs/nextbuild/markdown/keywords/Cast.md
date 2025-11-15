# CAST

## Syntax

```
CAST (*type,numeric value*), CAST (*type*,*variable*), CAST (*type*,function(*data*))
```

## Description

Returns a value of the type specified with a value equivalent to the item specified, if that is possible.

**Example**

	dim a as uinteger
	dim b,c as ubyte
	a = 32768
	b = 10
	c = b+cast(ubyte,a)

For most cases it can prove useful : 

	add = 32750 
	for x = 0 100
		print peek (add+cast(x,uinteger))		
		' in this case x will be cast as a ubyte by the compiler
		' which means when it is added add with being recast it 
		' will roll over 0-255
	next x 
    
Remarks

- This function can lose precision if used indiscriminately. For example, CAST(Integer,PI) returns 3, losing precision on the value of PI.
- This function is NOT Sinclair Compatible.

More info : https://zxbasic.readthedocs.io/en/docs/cast/

# SAVE

## Syntax

```
SAVE "xxx" CODE START, LENGTH
```

## Description

The below commands work in a manner identical to Sinclair Basic.

**Example**

	SAVE "xxx" CODE 32768, 6912

Saves to TAP a block of memory 6912 in length from address 32768.



**Remarks**

- This statement is Sinclair BASIC compatible.
- This DOES NOT WORK with the Next's SD, use SaveSD() instead.

More info : https://zxbasic.readthedocs.io/en/docs/return/

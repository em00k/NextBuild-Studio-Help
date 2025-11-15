# CONST

## Syntax

```
CONST *var* [AS *type*] = *value*
```

## Description

CONST declares a non-modifiable variable.

*type* can be something like Integer, Byte, Float, etc. See the list of available types. If type is not specified, Float will be used, unless you use a modifier like $ or %.

**Example**

	CONST screenAddress as uInteger = 16384

More info : https://zxbasic.readthedocs.io/en/docs/const/

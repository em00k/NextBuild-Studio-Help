# GetMMU

## Syntax

```
GetMMU(byval slot as ubyte) as ubyte
```

## Description

A function that returns the current memory bank in numerical slot

**Examples**

dim a as ubyte 
a = GetMMU($4)				; read bank paged into slot 4
Print a 				; print the value

## Links

* [NextRegister](NextRegister)

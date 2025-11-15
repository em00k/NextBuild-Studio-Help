# GetReg(register)

## Syntax

```
n = GetReg(register)
```

## Description

A function that returns the current value of a register. 

**Examples**
```
dim n as ubyte 
n = GetReg(MMU1_2000_NR_51)				' read bank paged into slot 1, $2000-$3fff, register $51
Print n 				                ' print the value
```

## Links

* [NextRegister](_registers.md)
* [NextReg()](NextReg.md)
* [NextRegA()](NextRegA.md)

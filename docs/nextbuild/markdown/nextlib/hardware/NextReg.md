# NextReg(register,constant)

## Syntax

```
NextReg(register,constant)
```

## Description

Sets Next register reg with a constant value. 
```
NextReg(MMU1_2000_NR_51,38)			'Sets register $51 in bank 1, $2000-$3fff to bank 38
```
Note that at compilation time this becomes a macro so will only work with constant values, if you want to use a variable you must use [NextRegA()](NextRegA.md)

## Links

* [NextRegA()](NextRegA.md)
* [NextRegisters](_registers.md)

# ASM

## Syntax

```
ASM ... END ASM
```

## Description

Starts immediate inline assembly context using standard z80n opcodes. Use with caution.

**Syntax**

	asm
		; (Z80n assembly code)
		ld	a, 10
		out ($fe), a 
	end asm
    
    ... rest of program 

More info https://zxbasic.readthedocs.io/en/docs/asm/

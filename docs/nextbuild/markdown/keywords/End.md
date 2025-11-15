# END

## Syntax

```
END, END SUB, END ASM, END FUNCTION
```

## Description

Used for ending a program, an asm block, sub or function

**Syntax**

To END the program

	END

To end an asm block

	asm
		; Z80n assembly code
	end asm

And similar is used after a SUB or FUNCTION

	sub mysub()
		'..code
	end sub

	function hello()
		'..code
	end function

More info : https://zxbasic.readthedocs.io/en/docs/if/

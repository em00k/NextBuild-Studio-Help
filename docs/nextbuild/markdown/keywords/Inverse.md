# INVERSE

## Syntax

```
INVERSE *value*,PRINT INVERSE *value*;
```

## Description

This can be used to change the permanent print settings, or the temporary ones. When used as a direct command:

	INVERSE n

where n is either 0 (false) or 1 (true), then the subsequent print statements will have their INK and PAPER values swapped from the current settings for INK and PAPER.

Just as in Sinclair basic, this command can be used as temporary colours by combining them with a print statement:

	Print INK 0;PAPER 7; INVERSE 1; "This WHITE text on BLACK background"

Note that the INK and PAPER are swapped because of the INVERSE 1 This format does not change the permanent colour settings and only affects the characters printed within that print statement.

**Remarks**

- This function is 100% Sinclair BASIC compatible.

More info : https://zxbasic.readthedocs.io/en/docs/inverse/

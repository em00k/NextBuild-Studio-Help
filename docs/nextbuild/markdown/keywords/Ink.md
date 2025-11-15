# INK

## Syntax

```
INK *value*, PRINT INK *value*;
```

## Description

This can be used to change the permanent print settings, or the temporary ones. When used as a direct command:

**Example**

	INK 2
- 0 - Black
- 1 - Blue
- 2 - Red
- 3 - Magenta
- 4 - Green
- 5 - Cyan
- 6 - Yellow
- 7 - White
- 8 - Transparent (Does not change paper value in square being printed)
- 9 - Contrast

Just as in Sinclair basic, this command can be used as temporary colours by combining them with a print statement:

	Print ink 2; "This is red text"

This format does not change the permanent colour settings and only affects the characters printed within that print statement.

**Remarks**

- This function is Near Sinclair BASIC compatible.

More info : https://zxbasic.readthedocs.io/en/docs/ink/

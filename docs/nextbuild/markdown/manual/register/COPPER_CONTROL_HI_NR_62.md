# COPPER_CONTROL_HI_NR_62

## Syntax

```
COPPER_CONTROL_HI_NR_62 = $62
```

## Description

**COPPER CONTROL HIGH BYTE** (R/W)

More info : https://wiki.specnext.dev/Copper_Control_High_Byte

Holds high byte of [Copper](https://wiki.specnext.dev/Copper) control flags.

**Bit**

	7-6  'Control Mode
	5-3  'Reserved must be 0
	2-0  'High three bits of Copper list index (value-2047)

When "Control mode" bits are identical with previously set ones, they are ignored - allowing for index change without restarting currently running Copper program.

Copper has internally 10 bit "program counter" register (**CPC**), going through 0-1023 values, executing Copper instruction from the list at memory position (CPC*2). This will cause the Copper program to loop automatically. To "halt" program (avoiding possible loop), use WAIT instruction with non-existent horizontal line, like "**WAIT 63,511 = 0xFF, 0xFF**".

**Bits 7-6**

	%00 'STOP Copper (CPC is kept at current value)
	%01 'Reset CPC to 0 and START Copper
	%10 'START Copper (does resume at current CPC)
	%11 'Reset CPC to 0 and START Copper, reset CPC at each video frame at (0,0) (top left pixel of PAPER area)

Requires: 

	#INCLUDE <nextlib.bas>

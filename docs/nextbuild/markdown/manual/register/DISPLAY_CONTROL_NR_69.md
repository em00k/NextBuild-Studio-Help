# DISPLAY_CONTROL_NR_69

## Syntax

```
DISPLAY_CONTROL_NR_69 = $69
```

## Description

**DISPLAY CONTROL 1 REGISTER** (R/W)

More info : https://wiki.specnext.dev/Display_Control_1_Register

Layer2, ULA shadow, Timex $FF port

**Bit**

	7	' Enable the Layer 2 (alias for Layer 2 Access Port ($123B / 4667) bit 1)
	6	' Enable ULA shadow (bank 7) display alias (for Memory Paging Control ($7FFD / 32765) bit 3]
	5-0  ' alias for Timex Sinclair Video Mode ($xxFF / 255) bits 5:0Control

ULA shadow screen from Bank 7 has higher priority than Timex modes, setting bit 6 to "1" together with one of the extended Timex graphic modes will result into classic ZX128 ULA mode using Bank 7 data.

Requires: 

	#INCLUDE <nextlib.bas>

# NEXT_RESET_NR_02

## Syntax

```
NEXT_RESET_NR_02 = $02
```

## Description

**NEXT RESET REGISTER** More info : https://wiki.specnext.dev/Next_Reset_Register

Identifies type of last reset. Can be written to force reset.

**Read**

	'bit 7 = Indicates the reset signal to the expansion bus and esp is asserted
	'bits 6:2 = Reserved
	'bit 1 = Indicates the last reset was a hard reset
	'bit 0 = Indicates the last reset was a soft reset
	* Only one of bits 1:0 will be set

**Write**

	'bit 7 = Assert and hold reset to the expansion bus and the esp wifi (hard reset = 0)
	'bits 6:2 = Reserved, must be 0
	'bit 1 = Generate a hard reset (reboot)
	'bit 0 = Generate a soft reset
	* Hard reset has precedence   

Requires: 

	#INCLUDE <nextlib.bas>

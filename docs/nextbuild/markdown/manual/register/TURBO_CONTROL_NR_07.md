# TURBO_CONTROL_NR_07

## Syntax

```
TURBO_CONTROL_NR_07 = $07
```

## Description

**CPU SPEED REGISTER** More info : https://wiki.specnext.dev/CPU_Speed_Register

Sets CPU Speed, reads actual speed.

**Bit Read**

	7-6  'Reserved
	5-4  'Current actual CPU speed
	3-2  'Reserved
	1-0  'Programmed CPU speed

**Bit Write**

	7-2  'Reserved must be 0
	1-0  'Set CPU speed (%00 on reset)
		%00	' 3.5MHz
		%01	' 7MHz
		%10	' 14MHz
		%11	' 28MHz

The CPU throttling from 14MHz to 7MHz is not happening in core 3.0+ any more (but if any configuration would require it, or 28MHz mode will be implemented with throttling, it can be seen by reading bits 5-4). The 3.5MHz speed limit when Expansion Bus is enabled is of course visible in bits 5-4 too.

The 28MHz with core 3.0.5 is adding extra wait state to every instruction opcode fetch and memory read (i.e. instruction like NOP will take 5T instead of regular 4T and DMA transfer configured to 2T+2T will take 3T+2T instead), there is some chance this may be improved in the future.   

Requires: 

	#INCLUDE <nextlib.bas>

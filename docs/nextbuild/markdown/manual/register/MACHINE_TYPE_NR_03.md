# MACHINE_TYPE_NR_03

## Syntax

```
MACHINE_TYPE_NR_03 = $03
```

## Description

**MACHINE TYPE REGISTER** More info : https://wiki.specnext.dev/Machine_Type_Register

Identifies timing and machine type.

A write to this register disables the bootrom in config mode

A write with bit 7 set will be accepted in any mode to change only display timing (bits 6-4).

**Bits**

	7	'(W) 1 to allow changes to bits 6:4
	7	'(R) Next write to Enhanced ULA Palette Extension ($44) will affect colour byte: 0 = RRRGGGBB, 1 = p000000B
	6-4  'Display timing affects I/O port decoding (since core 3.1.1)):
		%000: 'internal usage
		%001: 'ZX 48k
		%010: 'ZX 128k/+2 Grey
		%011: 'ZX +2A/B/+3e/Next Native
		%100: 'Pentagon
	3	'1 to toggle user lock on display timing (hard reset = 0) (since core 3.1.0)
	2-0	'Machine type (determines roms loaded and multiface type (since core 3.1.1)):
		%000: 'Config mode
		%001: 'ZX 48k
		%010: 'ZX 128k/+2 (Grey)
		%011: 'ZX +2A-B/+3e/Next Native
		%100: Pentagon.
		'Writable only in config mode.

Core 3.1.1 change: port-decoding now depends on the selected display-mode, not machine-type. So while machine is still in Next type, by changing to 128 display the port decoding does change too (for example $7FFD port is decoded differently on ZX128 vs ZX128+3 machines).

Requires: 

	#INCLUDE <nextlib.bas>

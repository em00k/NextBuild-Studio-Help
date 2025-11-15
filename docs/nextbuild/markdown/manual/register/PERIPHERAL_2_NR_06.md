# PERIPHERAL_2_NR_06

## Syntax

```
PERIPHERAL_2_NR_06 = $06
```

## Description

**PERIPHERAL 2 REGISTER** More info : https://wiki.specnext.dev/Peripheral_2_Register

Enables CPU Speed key, DivMMC, Multiface, Mouse and AY audio.

**Bit**

	7	'Enable CPU speed mode key "F8", 0 = disabled (1 after Soft-reset)
	6	'core3.1.2: Divert BEEP-only to internal speaker (hard reset = 0)
	5	'Enable "F3" key (50/60 Hz switch) (1 after Soft-reset)
	4	'Enable DivMMC automap and DivMMC NMI by DRIVE button (0 after Hard-reset)
	3	'Enable multiface NMI by M1 button (hard reset = 0)
	2	'PS/2 mode (primary device: 0 = keyboard, 1 = mouse), exchanges the keyboard/mouse pins on the PS/2 connector (writeable only in config mode)
	1	'Audio chip mode (%00 = YM, %01 = AY, %1x = Disabled)
	0	'(core 3.0) %11 hold all AY in reset

The bit 7 doesn't prevent SW from setting up different CPU speed by writing into CPU Speed Register ($07), it is used only to enable/disable the "F8" key toggle, similarly bit 5 enables "F3" key.

Requires: 

	#INCLUDE <nextlib.bas>

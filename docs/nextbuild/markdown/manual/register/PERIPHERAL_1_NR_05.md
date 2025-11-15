# PERIPHERAL_1_NR_05

## Syntax

```
PERIPHERAL_1_NR_05 = $05
```

## Description

**PERIPHERAL 1 REGISTER** More info : https://wiki.specnext.dev/Peripheral_1_Register

Sets joystick mode, video frequency and Scandoubler.

**Bit**		**Function**

	7-6	'Joystick 1 mode (LSB)
	5-4	'Joystick 2 mode (LSB)
	3	'Joystick 1
	2	'50/60 Hz mode (0 = 50Hz, 1 = 60Hz) (0 after a PoR or Hard-reset)
	1	'Joystick 2 mode (MSB)
	0	'Enable Scandoubler (1 = enabled) (1 after a PoR or Hard-reset) mode (MSB)  

Requires: 

	#INCLUDE <nextlib.bas>

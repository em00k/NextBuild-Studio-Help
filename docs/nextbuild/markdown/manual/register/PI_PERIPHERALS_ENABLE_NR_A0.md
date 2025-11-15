# PI_PERIPHERALS_ENABLE_NR_A0

## Syntax

```
PI_PERIPHERALS_ENABLE_NR_A0 = $A0
```

## Description

**PI PERIPHERAL ENABLE REGISTER** (R/W)

More info : https://wiki.specnext.dev/Pi_Peripheral_Enable_Register

Enable Pi peripherals: UART, Pi hats, I2C, SPI

**Bit**

	7-6  'Reserved, must be 0
	5	'Enable UART on GPIO 14,15 (overrides GPIO) (soft reset = 0)
	4	%0 'to connect Rx to GPIO 15, Tx to GPIO 14 (for comm with Pi hats) (soft reset = 0)
		%1 '1 to connect Rx to GPIO 14, Tx to GPIO 15 (for comm with Pi)
	3	Enable I2C on GPIO 2,3 (overrides GPIO) (soft reset = 0)
	2-1  'Reserved, must be 0
	0	Enable SPI on GPIO 7,8,9,10,11 (overrides GPIO) (soft reset = 0)

*(note: Next registers with number higher than $7F are inaccessible from Copper code)* 

Requires: 

	#INCLUDE <nextlib.bas>

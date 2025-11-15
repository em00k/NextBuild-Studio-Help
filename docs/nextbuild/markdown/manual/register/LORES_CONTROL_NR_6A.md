# LORES_CONTROL_NR_6A

## Syntax

```
LORES_CONTROL_NR_6A = $6A
```

## Description

**LORES CONTROL REGISTER** (R/W)

More info : https://wiki.specnext.dev/LoRes_Control_Register

LoRes Radastan mode

**Bit**

	7-6  ' Reserved, must be 0
	5	 ' 1 = LoRes is Radastan mode (128x96x4, 6144 bytes) (soft reset = 0)
	4	 ' 1 = LoRes Radastan Timex display file xor (soft reset = 0)
	3-0  ' LoRes Radastan palette offset (bits 1:0 apply in ULA+ mode) (soft reset = 0)

Requires: 

	#INCLUDE <nextlib.bas>

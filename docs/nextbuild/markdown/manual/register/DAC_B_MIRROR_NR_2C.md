# DAC_B_MIRROR_NR_2C

## Syntax

```
DAC_B_MIRROR_NR_2C = $2C
```

## Description

**DAC B (LEFT) MIRROR REGISTER**

More info : https://wiki.specnext.dev/DAC_B_(left)_mirror_Register

DAC B mirror, read current I2S left MSB

**Write**

	bits 7:0 ' 8-bit sample written to left side DAC B (soft reset = $80)

**Read**

	bits 7:0 ' MSB of current I2S (Pi:NextPi) left side sample

the LSB is latched and can be read from DAC A+D (mono) mirror Register ($2D) later

Requires: 

	#INCLUDE <nextlib.bas>

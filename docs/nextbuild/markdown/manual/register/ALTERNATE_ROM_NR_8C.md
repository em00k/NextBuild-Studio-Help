# ALTERNATE_ROM_NR_8C

## Syntax

```
ALTERNATE_ROM_NR_8C = $8C
```

## Description

Enable alternate ROM or lock 48k ROM

```
(R/W) (hard reset = 0)
IMMEDIATE
  bit 7 = 1 to enable alt rom
  bit 6 = 1 to make alt rom visible only during writes, otherwise replaces rom during reads
  bit 5 = 1 to lock ROM1 (48K rom)
  bit 4 = 1 to lock ROM0 (128K rom) AFTER SOFT RESET (copied into bits 7-4)
  bit 3 = 1 to enable alt rom
  bit 2 = 1 to make alt rom visible only during writes, otherwise replaces rom during reads
  bit 1 = 1 to lock ROM1 (48K rom)
  bit 0 = 1 to lock ROM0 (128K rom)
```  
The locking mechanism also applies if the alt rom is not enabled. For the +3 and Next, if the two lock bits are not zero, then the corresponding rom page is locked in place. Other models use the bits to preferentially lock the corresponding 48K rom or the 128K rom.

## Remarks 

More info : https://wiki.specnext.dev/Board_feature_control

Requires: 
```
#INCLUDE <nextlib.bas>
```
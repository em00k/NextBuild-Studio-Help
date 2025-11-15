# LOAD

## Syntax

```
LOAD "xxx" CODE, LOAD "xxx" CODE START, LOAD "xxx" CODE START, LENGTH, LOAD "xxx" SCREEN$
```

## Description

The below commands work in a manner identical to Sinclair Basic. These do NOT load from SD card, please check LoadSDBank and LoadSD.

	 LOAD "file" CODE 32768, 2048

	 LOAD "xxx" CODE
	 LOAD "xxx" CODE START
	 LOAD "xxx" CODE START, LENGTH
	 LOAD "xxx" SCREEN$

**Remarks**

- The save command should save bytes in a format that is 100% Sinclair BASIC Compatible
- For LOAD and VERIFY, when a R-Tape Loading error occurs, the program will not stop.
- You have to check PEEK 23610 (ERR_NR) for value 26. If that value exists, then the LOAD/VERIFY operation failed.
- At this moment, LOAD/SAVE/VERIFY can be interrupted by the user by pressing BREAK/Space, which exits the program and returns to the ROM BASIC. 
- This may be changed in the future to behave like the previous point (signaling the break in ERR_NR and returning).
- When using LOAD "xxx" DATA... you won't see the message "Number array:" or "Char array:", but "Bytes:" instead. 
- This is because ZX BASIC always uses bytes (LOAD/SAVE ... CODE) for storing user variables (ZX BASIC is machine code, so the idea of BASIC variables doesn't apply).

More info : https://zxbasic.readthedocs.io/en/docs/load/

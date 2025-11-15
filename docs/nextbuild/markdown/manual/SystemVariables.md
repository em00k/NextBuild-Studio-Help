# System variable for NextZXOS

The following system variables have been changed (same format as +3 manual):
```
1 5B5FH (23391) INKL INK colour for lo-res mode (was BAUD)
1 5B60H (23392) INK2 INK colour for layer2 mode (was BAUD+1)
1 5B61H (23393) ATTRULA Attributes for standard mode (was SERFL)
1 5B62H (23394) ATTRHR Attributes for hi-res mode (only paper
colour in bits 3..5 is used) (was SERFL+1)
1 5B63H (23395) ATTRHC Attributes for hi-colour mode (was COL)
1 5B64H (23396) INKMASK Softcopy of ULANext inkmask(or 0)(was WIDTH)
N1 5B65H (23397) LSBANK Temp bank in LOAD/SAVE & others (was TVPARS)
X1 5B68H (23400) FLAGN Flags for the NextZXOS system (was XLOC)
1 5B69H (23401) MAXBNK Maximum available RAM bank (was YLOC)
1 5B73H (23411) TILEBNKL Tiles bank for lo-res (was RC LINE)
1 5B74H (23412) TILEML Tilemap bank for lo-res (was RC LINE+1)
1 5B75H (23413) TILEBNK2 Tiles bank for layer2 (was RC START)
1 5B76H (23414) TILEM2 Tilemap bank for layer2 (was RC START+1)
X1 5B77H (23415) NXTBNK Bank containing NXTLIN (was RC STEP)
X1 5B78H (23416) DATABNK Bank containing DATADD (was RC STEP+1)
N1 5B7BH (23419) L2SOFT Softcopy of layer2 port (was DUMPLF)
X1 5C7FH (23679) GMODE Graphical layer/mode flags (was P POSN)
1 5C81H (23681) STIMEOUT Screensaver control (was unused)
2 5CB0H (23728) unused (was NMIADD)
```

The following system variables have been inserted where STRIP1 and STRIP2 were,
within the temporary TSTACK area. This means that there are now a guaranteed 117
bytes of TSTACK when calling +3DOS:

```
2 5B7CH (23420) TILEWL Width of lo-res tilemap
2 5B7EH (23422) TILEW2 Width of layer2 tilemap
2 5B80H (23424) TILEOFFL Offset in bank for lo-res tilemap
2 5B82H (23426) TILEOFF2 Offset in bank for layer2 tilemap
2 5B84H (23428) COORDSX x coord of last point plotted (layer 1/2)
2 5B86H (23430) COORDSY y coord of last point plotted (layer 1/2)
1 5B88H (23432) PAPERL PAPER colour for lo-res mode
1 5B89H (23433) PAPER2 PAPER colour for layer2 mode
Nx 5B8AH (23434) TMPVARS Base of temporary system variables (space shared with bottom of TSTACK)
```
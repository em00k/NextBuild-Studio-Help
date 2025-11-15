# NEXT_VERSION_NR_01

## Syntax

```
NEXT_VERSION_NR_01 = $01
```

## Description

**CORE VERSION REGISTER** https://wiki.specnext.dev/Core_Version_Register

Identifies core (FPGA image) version.

Most significant nibble holds major version number; least significant nibble holds minor version number.

See Core Version Register/**NEXT_VERSION_MINOR_NR_0E** (sub minor) ($0E) for sub-minor version number.

Requires: 

	#INCLUDE <nextlib.bas>

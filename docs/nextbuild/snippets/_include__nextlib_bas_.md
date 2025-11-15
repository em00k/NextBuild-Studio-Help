---
name: '#include <nextlib.bas>'
prefix: '#include'
description: >-
  Include the nextlib or other zxb lib, make sure this is after any #DEFINEs for
  NEX, DEBUG, IM2
---

```
#include ${1|<nextlib.bas>,<keys.bas>,<memcopy.bas>,<string.bas>,<print42.bas>,<print64.bas>,<printfzx.bas>,<megalz.bas>|}
$0
```

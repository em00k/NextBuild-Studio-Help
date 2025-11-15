---
name: LoadSDBank(...)
prefix: LoadSDBank
description: >-
  Loads a file into specified memory banks. Disable this when you create your
  final NEX by putting #Define NEX before the nextlib
---

```
LoadSDBank("${1:Filename}",${2:Address},${3:Length},${4:Offset},${5:Start bank})
$0
```

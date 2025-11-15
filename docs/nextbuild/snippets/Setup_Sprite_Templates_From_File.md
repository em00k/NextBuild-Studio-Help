---
name: Setup Sprite Templates From File
prefix: Template
description: >-
  This code loads a sprite file, pages in relevant banks and then uploads ending
  with putting back the default banks. This is intended ot be run in the load
  block of code.
---

```

' -- Load block 
LoadSDBank("${1:fname}",0,0,0,${2:bank})
InitSprites2(63,\$0000,${2:bank})       ' 63 nr of sprites to upload from bank 
' -- 
```

---
name: Simple timer snippet
prefix: Template
description: This code creates a simple timer that triggers on a set value
---

```
if  ${1:timername} =  ${2:0}
    ' timer triggered 
     ${1:timername} = 0
else 
     ${1:timername} =  ${1:timername} - 1 
endif 
```

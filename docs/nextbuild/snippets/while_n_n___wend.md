---
name: 'while n=n : wend'
prefix: while
description: |-
  Create a WHILE : WEND eg:
  While a < b
    Let a = a + 1
   Poke a, 0
  End While
---

```
while ${1:0} 
	$0
wend
```

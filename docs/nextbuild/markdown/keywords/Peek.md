# PEEK

## Syntax

```
PEEK (address), PEEK (typeToRead, address)
```

## Description

Returns the memory content (byte) stored at *address* position. If *address* is not a 16 bit unsigned integer, it will be converted to such type before reading the memory.

When *typeToRead* is specified, the given type is read from memory; otherwise the type of the read value is supposed to be *ubyte* (8 bit unsigned integer).

The type of the returning value is the *typeToRead* specified, or *ubyte* if no type is specified.

**Examples**

The following example reads a 16 bit unsigned integer at position 23675 (this is the System Variable for UDG in Sinclair BASIC systems):

	PRINT "Address of UDG is "; peek(23675) + 256 * peek(23676)

But it's faster to specify the type of the value:

	PRINT "Address of UDG is "; peek(uinteger, 23675)  

**Remarks**

- This function is Sinclair BASIC compatible.
- This function extends the Sinclair BASIC version.

More info : https://zxbasic.readthedocs.io/en/docs/peek/

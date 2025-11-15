# IF

## Syntax

```
IF ... END IF
```

## Description

IF is a very powerful control flow sentence that allows you to make decisions under specified conditions.

**Syntax**

	IF expression [THEN] sentences [: END IF]

Or

	IF expression [THEN]
		sentences
	 [ELSEIF expression [THEN] sentences]
	 [ELSEIF expression [THEN] sentences]
	 ...
	 [ELSE sentences]
	END IF

**Examples**

	IF a < 5 THEN PRINT "A is less than five" ELSE PRINT "A is greater than five"

Sentences might be in multiple lines:

	If a < 5 Then
        Print "A is less than five"
			a = a + 5
	Else
        Print "A is greater than five"

Since **IF** is a *sentence*, it can be nested; however, remember that *every* **IF** *must be closed with* **END IF** when the line is split after **THEN** (multiline **IF**):

	If a < 5 Then
        Print "A is less than five"
		If a > 2 Then
			Print "A is less than five but greater than 2"
		End If
	Else If a < 7 Then
			Print "A is greater or equal to five, but lower than 7"
		Else
			Print "A is greater than five"
		End if
	End if

**Using ELSEIF**

In the example above, you see that nesting an IF inside another one could be somewhat verbose and error prone. It's better to use the ELSEIF construct. So the previous example could be rewritten as:

	If a < 5 Then
		Print "A is less than five"
		If a > 2 Then
			Print "A is less than five but greater than 2"
		ElseIf a < 7 Then
			Print "A is greater or equal to five, but lower than 7"
		Else
			Print "A is greater than five"
	End If

**Remarks**
- This sentence is extended allowing now multiline IFs and also compatible with the Sinclair BASIC version.
- Starting from version 1.8 onwards the trailing END IF is not mandatory for single-line IFs, for compatibility with Sinclair BASIC

- The THEN keyword can be omitted, but keep in mind this might reduce code legibility.

More info : https://zxbasic.readthedocs.io/en/docs/if/

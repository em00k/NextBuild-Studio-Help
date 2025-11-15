# DO

## Syntax

```
DO ... LOOP
```

## Description

DO ... LOOP is a compound statement used to perform loops. The code within the DO ... LOOP statement will be repeated if the given condition is true

**Syntax**

The DO ... LOOP construct is a very powerful sentence and can be used in up to 5 different ways: 

**Infinite loops**

Sometimes we want a loop to repeat forever, no matter what, because we need to exit the loop when an external event happens. For example, we want to repeat forever waiting for a key press. Traditionally we use GOTO for this in Sinclair BASIC. Other languages use WHILE (1), etc. The best way to do this in ZX BASIC is this one:

	DO
		sentences
	LOOP : 'This loop repeats forever.

This form **loops forever**. It's better to use this form instead of using **STEP** 0 in a **FOR** loop, or a **WHILE** 1 condition loop. The generated code is more efficient.

**Looping UNTIL**

	DO
		sentences
	LOOP UNTIL condition

You can also put the condition at the beginning, this way:

	DO UNTIL condition
		sentences
	LOOP

In this case, the condition is checked first, and the program won't enter to the inner sentences if the condition is not satisfied at first.

**Example of using UNTIL**

Example: *Loop until the user press a Key*

	'in a single line!
	DO LOOP UNTIL INKEY$ <> ""

**Looping WHILE**

	DO
		sentences
	LOOP WHILE condition

This form repeats *while* the given condition is true. The difference with the WHILE sentence is the latter won't execute the inner sentences if condition is false at the start. Remember: **DO...LOOP** will execute sentences at least once regardless of the condition upon entry to the loop - it is only evaluated at the end of the first loop.

You can also put the condition at the beginning, this way:

	DO WHILE condition
			sentences
	LOOP

In this case, the condition is checked first, and the program won't enter to the inner sentences if the condition is not satisfied at first.

**Example using WHILE**

Example: *Loop while there is no key pressed*

	'in a single line!
	DO LOOP WHILE INKEY$ = ""

**Remarks**
- This statement does not exist in Sinclair Basic.
- **WHILE** can also be used with WHILE ... END WHILE loops.

More info : https://zxbasic.readthedocs.io/en/docs/do/

# RND

## Syntax

```
RND() | RND
```

## Description

Returns a number of type float in the range [0, 1) (i.e. 0 <= RND < 1), based on a random seed (see RANDOMIZE).

**Examples**

	'Function to a random number in the range [first, last), or {first <= x < last}.
	Function rnd_range (first As Double, last As Double) As Float
		Function = Rnd * (last - first) + first
	End Function

	'seed the random number generator, so the sequence is not the same each time
	RANDOMIZE

	'prints a random number in the range [0, 1], or {0 <= x < 1}.
	PRINT RND

	'prints a random number in the range [0, 10], or  {0 <= x < 10}.
	PRINT RND * 10

	'prints a random integer number in the range [1, 11), or  {1 <= x < 11}.
	'with integers, this is equivalent to [1, 10], or {1 <= n <= 10}.
	PRINT INT(RND * 10) +1

	'prints a random integer number in the range [69, 421], or {69 <= x < 421}.
	'this is equivalent to [69, 420], or {69 <= n <= 420}.
	PRINT INT(RND_RANGE(69,421)) 

**Remarks**

- ZX BASIC RND is much faster than Sinclair BASIC RND, and produces different random sequences.
- Its randomness is also much better (try plotting points at random x,y coords, and they look really random whilst in Sinclair BASIC diagonal lines begin to appear: this means there's a correlation between x, y points hence not very random).
- Also, Sinclair BASIC RND has a periodicity of 2^16 (65536), whilst ZX BASIC RND has a periodicity of 2^32 (4,294,967,296).

More info : https://zxbasic.readthedocs.io/en/docs/rnd/

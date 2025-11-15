# SPRITE_CONTROL_NR_15

## Syntax

```
NextReg(SPRITE_CONTROL_NR_15,n)
```

## Description

**SPRITE AND LAYERS SYSTEM REGISTER**

Enables/disables Sprites and Lores Layer, and chooses priority of sprites and Layer 2. Setting a value of [n] with the desired settings.

**Bits**
```
7	'Enable Lores Layer
6	'If 1, the sprite rendering priority is flipped, i.e. sprite 0 is on top of other sprites (0 after reset)
5	'If 1, the clipping works even in "over border" mode (doubling X-axis coordinates of clip window) (0 after reset)
4-2  'Layers priority and mixing(below)
1	'Enable sprites over border (0 after reset)
0	'Enable sprite visibility (0 after reset)
```
**Bits 4-2**
```
%000	S L U '(Sprites are at top, Layer 2 under, Enhanced_ULA at bottom)
%001	L S U
%010	S U L
%011	L U S
%100	U S L
%101	U L S
%110	(U|T)S(T|U)(B+L) 'Blending layer and Layer 2 combined, colours clamped to [0,7]
%111	since core3.1.1: (U|T)S(T|U)(B+L-5) 'Blending layer and Layer 2 combined, colours clamped to [0,7]
```

## Remarks

In layer mixing modes (%110 and %111) the "priority bit 7" of Layer 2 colour is propagated through the calculation, i.e. such pixel will raise above sprites even in mixing modes. If either U|T or L layer contains transparent colour pixel, the other layer pixel is drawn unchanged (skipping mixing calculation) (modified in 3.1.1, precise description to be added).

Since core3.1.1 the blending modes allow for layer non-contributing-to-blending (use ULA Control Register ($68) to configure blending sub-mode) to show independently in front of sprites, but modifies the transparency handling rules (to be documented soon)

When both "over border" (bit 1) and "clipping over border" (bit 5) is enabled, the Sprite clipping window Clip Window Sprites Register ($19) X-axis coordinates are "doubled", and coordinates origin is moved from pixel [0,0] position to sprite [0,0] position ([-32,-32] pixel position). For example: setting clip coordinates as {x1:5, x2:155, y1:7, y2:248} will make sprites visible in area [10,7]..[311,248] (inclusively) in sprite coordinates, i.e. the first visible pixel is at X1\*2 coordinate, and last visible pixel is at X2\*2+1 coordinate.

**SEE MORE** [https://wiki.specnext.dev/Sprite_and_Layers_System_Register](https://wiki.specnext.dev/Sprite_and_Layers_System_Register)

## Requires: 
```
#INCLUDE <nextlib.bas>
```
[Sprites](Sprites.md)
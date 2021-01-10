LDX #0

start:

right:
LDA $FF
CMP #$64
BNE left
LDA #$00
STA $200,X
STA $FF
INX
JMP display

left:
LDA $FF
CMP #$61
BNE display
LDA #$00
STA $200,X
STA $FF
DEX
JMP display

display:
LDA $fe
STA $200,X

JMP start

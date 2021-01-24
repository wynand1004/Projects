10 REM Intro to BASIC Programming by @TokyoEdtech
20 PRINT "BASIC Programming for Beginners by @TokyoEdtech"
30 REM INTEGERS AND FLOATS
40 LET x = 42
50 PRINT x
60 PRINT "The answer is " + x + "."
70 LET y = 1.21
80 PRINT y + " gigawatts!"
90 PRINT abs(y)
100 PRINT int(y)
110 PRINT round(y)
120 PRINT sqr(y)
130 PRINT rnd()
140 PRINT val("3.14159")
150 PRINT int(rnd()*10) + 1
160 REM Strings
170 LET name = "TokyoEdtech"
180 PRINT len(name)
190 PRINT "Hi, my name is " + name + "."
200 REM String Functions
210 PRINT LEFT(name, 2)
220 PRINT RIGHT(name, 2)
230 PRINT MID(name, 5, 2)
240 REM Conditional Statements
250 IF x = 42 THEN PRINT "Forty-two" ELSE PRINT "Not Forty-two"
260 REM Loops
270 FOR I = 1 TO 10
280 PRINT I + " * 2 = " + I*2
290 NEXT I
300 REM Arrays
310 ARRAY scores
320 scores[0] = 75
330 scores[1] = 85
340 scores[2] = 95
350 PRINT scores[1]
360 REM Subroutines
370 GOSUB 1000
380 PRINT "Back to the main program."
390 REM User input
400 INPUT "What is your name? > "; name
410 PRINT "Hi, " + name + ". Nice to meet you."
420 INPUT "Would you like to continue? Y/N > "; cont
430 if cont = "Y" THEN GOTO 20
990 END
1000 PRINT "This is a subroutine."
1010 RETURN

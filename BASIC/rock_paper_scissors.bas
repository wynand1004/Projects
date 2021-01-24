5 REM Rock, Paper, Scissors in BASIC by @TokyoEdtech
10 CLS
20 PRINT "Rock, Paper, and Scissors!"
30 INPUT "R)ock, P)aper, or S)cissors? > "; player
40 LET r = int(rnd()*3) + 1
50 IF r = 1 THEN computer = "R"
60 IF r = 2 THEN computer = "P"
70 IF r = 3 THEN computer = "S"
80 PRINT "The computer chose " + computer + "."
90 REM Tie Game
100 IF player = computer THEN PRINT "Tie!"
110 REM Player wins
120 IF player = "R" and computer = "S" THEN PRINT "Player wins!"
125 IF player = "S" and computer = "P" THEN PRINT "Player wins!"
130 IF player = "P" and computer = "R" THEN PRINT "Player wins!"
140 REM Computer wins
150 IF comptuer = "R" and player = "S" THEN PRINT "Computer wins"
160 IF computer = "S" and player = "P" THEN PRINT "Comptuer wins!"
170 IF computer = "P" and player = "R" THEN PRINT "Computer wins!"
180 INPUT "Play again? > "; playagain
190 if playagain = "Y" THEN GOTO 10
200 PRINT "OK. Thanks for playing!"

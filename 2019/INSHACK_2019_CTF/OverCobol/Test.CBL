       IDENTIFICATION DIVISION.
       PROGRAM-ID. HackMe.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
         01 SUBPRG.
           02 TMPNAME PIC X(10).
           02 TMPSCORE PIC 99.
           02 SUBPRGARG PIC X(20).
           02 SUBPRGNAME PIC X(20).
         01 TMPNAME2 REDEFINES SUBPRG PIC X(40).

         01 G.
          02 MATCHS OCCURS 10.
           03 PLAYER1 PIC X(10).
           03 PLAYER2 PIC X(10).
           03 SCORE1 PIC 99.
           03 SCORE2 PIC 99.
         01 NBMATCH PIC 99 VALUE 0.

         01 CHOICE PIC 9.
           88 ONE VALUE "1".
           88 TWO VALUE "2".
           88 THREE VALUE "3".
           88 QUIT VALUE "4".
        
         01 IDX PIC 99.

       PROCEDURE DIVISION.
         
         DISPLAY "################################"
         DISPLAY "# WELCOME IN THE COBOL GAME !  #"
         DISPLAY "################################".

       MENU-LAB.
         DISPLAY " "
         DISPLAY "1. Register a match."
         DISPLAY "2. View matchs."
         DISPLAY "3. Send match to the cloud."
         DISPLAY "4. Quit."
         DISPLAY "What do you want to do ? " NO ADVANCING
         ACCEPT CHOICE

         IF QUIT
           GOBACK
         END-IF

         IF ONE
           PERFORM REGISTER-MATCH
         ELSE
           IF TWO
             PERFORM VIEW-MATCH
           ELSE
             IF THREE
               PERFORM SEND-CLOUD
             END-IF
           END-IF
         END-IF
         
         GO TO MENU-LAB.

       REGISTER-MATCH.
         IF NBMATCH = 10
           DISPLAY "TOO MUCH MATCH."
           GO TO MENU-LAB
         END-IF

         DISPLAY "PLAYER1: " NO ADVANCING
         ACCEPT TMPNAME
         MOVE TMPNAME TO PLAYER1(NBMATCH + 1)

         DISPLAY "PLAYER2: " NO ADVANCING
         ACCEPT TMPNAME2
         MOVE TMPNAME TO PLAYER2(NBMATCH + 1)

         DISPLAY "SCORE1: " NO ADVANCING
         ACCEPT TMPSCORE
         MOVE TMPSCORE TO SCORE1(NBMATCH + 1)

         DISPLAY "SCORE2: " NO ADVANCING
         ACCEPT TMPSCORE
         MOVE TMPSCORE TO SCORE2(NBMATCH + 1)
         
         ADD 1 TO NBMATCH.

       END-REGISTER-MATCH.
         EXIT.

       VIEW-MATCH.
         IF NBMATCH = 0
           DISPLAY "No match are registered yet."
           GO TO MENU-LAB
         END-IF

         MOVE 1 TO IDX
         PERFORM UNTIL IDX = NBMATCH + 1
           DISPLAY PLAYER1(IDX) " vs " PLAYER2(IDX)
                   " : "SCORE1(IDX)"-"SCORE2(IDX)
           ADD 1 TO IDX
         END-PERFORM.
       END-VIEW-MATCH.
         EXIT.

       SEND-CLOUD.
         IF SUBPRGNAME = SPACE
           MOVE "send" TO SUBPRGNAME
           MOVE "matchs" TO SUBPRGARG
         END-IF
          DISPLAY SUBPRGNAME " " SUBPRGARG
          CALL SUBPRGNAME USING SUBPRGARG.
       END-SEND-CLOUD.
         EXIT.

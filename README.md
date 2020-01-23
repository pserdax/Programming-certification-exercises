# Programming-certification-exercises

Problem 1 - Casino

A famous casino from Bucharest wishes to detect card cheaters faster. Using an image recogntion
software one can detect the cards played by each player at a certain table and one wishes to find if
any player used cards extracted from its pockets. The card game that is monitored uses two classic
card decks (52 cards each deck, without the Joker).

Requirement:
Write a software that can help detect cheaters. If one detect that one card appears too often, the
software will display the card and will stop the game.

Input data:
One will read from the keyboard (the stdin stream) the following data:
• On the first line is the number n, representing the maximal number of hands to be played;
• On the following n lines is the played card, in the format:
<card_number> <card_sign>

Output data:
If no one tries to cheat, the text "JOC OK" will be displayed. If someone tries to cheat, the software
will display the cheated card in the same format as the one for the input (the card number and the card
sign, separated by space).

ATTENTION to the compliance to the problem requirements: the display of results must be
done EXACTLY as required! In other words, on the standard output stream there will be
nothing displayed in addition to the problem requirements; following the automatic evaluation,
any supplemental character displayed, or any display different than the requirements, will
produce an eroneous result and will lead to the „Reject” of the solution.

Restrictions and remarks:
1. 2<n<100
2. The sign of the cards can be: trefla, caro, cupa, pica.
3. The number of the cards is an integer number within [2; 14] (ace has value 11).
4. Warning: According to the chosen programming language, the file containing the code must
have one of the extensions .c, .cpp, .java, or .m. The web editor does not add automatically
these extensions and the lack of the extensions leads to the impossibility of program
compilation!
5. Warning: The source file must be named by the candidate as: <name>.<ext> where name is
the family name (last name) of the candidate and the extension is the one chosen according to
the previous warning. Attention to the restrictions imposed by the Java language regarding
the class name and the file name!




Problem 2 - Scholarships

The University’s secretary must determine the number of students who earned the merit scholarship
next academic year and to identify the student who earned performance scholarship (there is only one
performance scholarship). She has provided a list of all students and the marks obtained by them at
various disciplines. The performance scholarship is granted to the student who passed all exams and
has the highest average grade. Merit scholarships are awarded in descending order of average grade,
to students who passed all exams, whose average grades are over 8.00, but to a specified maximum
number of scholarships.

Requirement:
Determine which student has earned the performance scholarship and how many students will get
scholarships of merit in the next academic year.

Input data:
The following data is available via keyboard (stdin stream):
• Three positive integers m, n, p separated by spaces, representing:
o m - number of students,
o n - number of disciplines,
o p - the number of merit scholarships available;
• 2 * m lines that are read in sequence in the format:
o <NS>, a string representing the name of the student;
o <N1> <N2> ... <Nn> n integers in the range 1-10 separated by spaces, representing the
grades of the student;
All lines containing inputs end with the newline character (Enter key).

Output data:
The program will display on the screen (standard output stream)
• One the first line: the number of students who earned the merit scholarship;
• On the second line: the name of the student who earned the performance scholarship and his
average grade (fractional number with two decimal places) separated by space.

ATTENTION to the compliance to the problem requirements: the display of results must be
done EXACTLY as required! In other words, on the standard output stream there will be
nothing displayed in addition to the problem requirements; following the automatic evaluation,
any supplemental character displayed, or any display different than the requirements, will
produce an eroneous result and will lead to the „Reject” of the solution.

Restrictions and remarks:
1. 0 <m, n, p <100
2. We guarantee that there will be no students with equal average grades.
3. Warning: According to the chosen programming language, the file containing the code must
have one of the extensions .c, .cpp, .java, or .m. The web editor does not add automatically
these extensions and the lack of the extensions leads to the impossibility of program
compilation!
4. Warning: The source file must be named by the candidate as: <name>.<ext> where name is
the family name (last name) of the candidate and the extension is the one chosen according to 
the previous warning. Attention to the restrictions imposed by the Java language regarding
the class name and the file name!

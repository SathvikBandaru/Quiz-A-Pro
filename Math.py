
class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

easy=[QA("The necessary and sufficient condition differential equations to be exact is:" , "∂M/∂y = ∂N/∂x" , ["∂M/∂X = ∂N/∂Y", "∂M/∂y  ≠ ∂N/∂x", "∂M/∂y  ≠ ∂N/∂x"]),
        QA("what is the integrating factor if given differential eaquation is non exact and homogeneous:" ,"1/Mx+Ny" , ["1/Mx-Ny", "Mx+Ny", "Mx-Ny"]),
        QA("what is the integrating factor if given differential equation is non exact and in yf(xy)dx+xg(xy)dy=0   form:" , "1/Mx-Ny" ,["1/Mx+Ny", "Mx+Ny", "Mx-Ny"]),
        QA("The integrating factor in   xdy/dx-y=2xcosec2x is:" , "1/x" ,["2/x", "-1/x", "x"]),
        QA("The integrating factor in dy/dx+y=x is e^p where p=" , "x" , ["-x", "y", "2x"]),
        QA("The  particular  solution of ((D+1)^2)y=x is " , "x+2" ,["x+4", "x+3", "-x+3"]),
        QA("the particular solution of the equation (1/D-2)sinx is -1/5(P).Then p =" , "cosx+2sinx", ["cosx-2sinx", "sinx+cos2x", "sinx-cos2x"]),
        QA("The complementary solution of (D^2+5D+6)y=0 is" ,"c1(e^-2x)+c(2e^-3x)", ["c1(e^-2x)+c(2e^3x)", "c1(e^2x)+c(2e^-3x)", "c1(e^2x)+c(2e^3x)"]),
        QA("The particular solution of (D^2+D)y=X^2+2X is" , "x^3/3", ["x^3", "x^2/2", "x^2"]),
        QA("The particular solution the equation (D^2+1)y=X^3", "x^3-6x" ,["x^3+6x", "-x^3+6x", "-x^3-6x"]),
        QA("The particular solution of (D^2+a^2)y=cosax" , "xsinax/2a" ,["-2xsinax/2a", "2xsinax/2a", "-xsinax/2a"]),
        QA("The differential equation (dy/dx)+(ycosx+siny+y/sinx+xcosy+x)=0  is:" ,"exact",["non exact", "homogeneous", "linear differential equation"]),
        QA("What will be the fraction of 20%" ,"1/5", ["1/4", "1/5", "none of these"]),
        QA("A fruit seller had some apples. He sells 40% apples and still has 420 apples. Originally, he had:", "700 apples" ,["588 apples", "600 apples", "672 apples"]),
        QA("In an election between two candidates, one got 55% of the total valid votes, 20% of the votes were invalid. If the total number of votes was 7500, the number of valid votes that the other candidate got, was :" , "2700" ,["2500", "2900", "3100"]),
        QA("Two students appeared at an examination. One of them secured 9 marks more than the other and his marks was 56% of the sum of their marks. The marks obtained by them are:" ,"(42, 33)" ,["(39,30)", "(41,32)", "(43, 34)"]),
        QA("The price of sugar having gone down by 10%, a consumer can buy 5 kg more sugar for Rs 270. The difference between the original and reduced price per kg is" , "60 paise" ,["62 paise", "75 paise", "53 paise"]),
        QA("A shopkeeper bought 600 oranges and 400 bananas. He found 15% of oranges and 8% of bananas were rotten. Find the percentage of fruits in good condition" , "87.8%" , ["23.4%", "54.8%", "64.5%"]),
        QA("Three candidates contested an election and received 1136, 7636 and 11628 votes respectively. What percentage of the total votes did the winning candidate got" , "57%",["55%", "56%", "59%"]),
        QA("2.09 can be expressed in terms of percentage as", "209%" , ["2.09%", "20.09%", "0.209%"]),
        QA("A reduction of 10% in the price of wheat enables a man to buy 50 g of wheat more for a rupee. How much wheat could originally be had for a rupee?" , "450g" , ["400g", "500g", "350g"]),
        QA("75 g of sugar solution has 30% sugar in it. Then, the quantity of sugar that should be added to the solution to make the quantity of the sugar 70% in the solution, is" , "120g" , ["125g", "100g", "130g"]),
        QA("Half of 1 percent written as decimal is" ,"0.005", ["5", "0.5", "0.05"]),
        QA("A student has to obtain 33% of the total marks to pass. He got 125 marks and failed by 40 marks. The maximum marks are :" , "500", ["600", "800", "1000"]),
        QA("A man spends 35% of his income on food, 25% on children's education and 80% of the remaining on house rent. What percent of his income he is left with?" , "8%", ["6%", "10%", "12%"]),
        QA("If A = x% of y and B = y% of x, then which of the following is true" ,"none of these", ["A is smaller than B", "A is greater than B", "The relationship between A and B cannot be determined"]),
        QA("A student has to obtain 33% of the total marks to pass. He got 125 marks and failed by 40 marks. The maximum marks are :" , "500" , ["600", "800", "1000"]),
        QA("A man spends 35% of his income on food, 25% on children's education and 80% of the remaining on house rent. What percent of his income he is left with?" , "8%", ["6%", "10%", "12%"]),
        QA("If y exceeds x by 20%, then x is less than y by?" , "16 2/3 %" ,["16%", "16 1/3 %", "16 3/5 %"]),
        QA("What is 15 percent of 34?" , "5.10" , ["4.10", "3.10", "2.10"]),
        QA("In a certain school, 20% of students are below 8 years of age. The number of students above 8 years of age is 2/3 of the number of students of 8 years of age which is 48. What is the total number of students in the school?" , "100" , ["72", "80", "120"]),
        QA("1/9 % of 900?" , "81",["100", "20", "none of these"]),
        QA("What will be the fraction of 4%","1/25" , ["1/20", "1/50", "1/75"])]

moderate=[
          QA("What percent is 70 of 280?" , "50%" , ["25%", "75%", "none of these"]),
          QA("If A's height is 40% less than that of B, how much percent B's height is more than that of A?" , "96.66%" ,["66.66%", "76.66%", "86.665"]),
          QA("A number is decreased by 10% and then increased by 10%. The number so obtained is 10 less than the original number. What was the original number?" , "3000" ,["100", "2000", "4000"]),
          QA("The ratio 5:20 expressed as percent equals to" , "50%" , ["125%", "25%", "none of these"]),
          QA("Sam and Joan are playing a tennis match. If the probability of Sam's win is 0.59, then find the probability of Joan's win." , "0.25", ["0.47", "0.36", "0.41"]),
          QA("Let A and B be events on the same sample space, with P (A) = 0.6 and P (B) = 0.7. Can these two events be disjoint?" ,"all of the above" ,["yes", "no", "none of the above"]),
          QA("A family has two children. find the probability that both the children are girls given that at least one of them is a girl?" ,"2/3" ,["1/4", "1/3", "3/4"]),
          QA("In a lottery, there are 10 prizes and 25 blanks. A lottery is drawn at random. What is the probability of getting a prize?" , "5/7" , ["1/10", "2/5", "2/7"]),
          QA("Determine the probability that a digit chosen at random from the digits 1, 2, 3, …12 will be odd." , "1/9", ["1/2", "5/9", "4/9"]),
          QA("Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?" , "9/20",["1/2", "2/5", "8/15"]),
          QA("Which of these numbers cannot be a probability?" , "-0.0001", ["0.5", "0.001", "1"]),
          QA("A pack contains 4 blue, 2 red and 3 black pens. If 2 pens are drawn at random from the pack, NOT replaced and then another pen is drawn. What is the probability of drawing 2 blue pens and 1 black pen?" , "2/14" ,["1/15", "6/7", "8/12"]),
          QA("In a throw of dice what is the probability of getting number greater than 5" , "1/2" , ["1/3", "1/5", "1/6"]),
          QA("The probability that Soumya will get marry within 365 days is 'a' and the probability that her colleague Alma get marry within 365 days is 'b'. Find the probability that only one of the two gets marry at the end of 365 days." ,"ab-a-b" , ["a-b-2ab", "a+b-2ab", " a-b+2ab"]),
          QA("Three unbiased coins are tossed. What is the probability of getting at most two heads?" ,"1/4" , ["3/4", "3/8", "7/8"]),
          QA("Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?" , "3/5",["1/2", "9/20", "8/20"]),
          QA("In a lottery, there are 10 prizes and 25 blanks. A lottery is drawn at random. What is the probability of getting a prize?", "5/7" , ["2/7", "1/5", "1/2"]),
          QA("A bag contains 12 white and 18 black balls. Two balls are drawn in succession without replacement. What is the probability that first is white and second is black?" , "36/135" , ["18/145", "18/29", "37/135"]),
          QA("A bag contains 5 red and 3 green balls. Another bag contains 4 red and 6 green balls. If one ball is drawn from each bag. Find the probability that one ball is red and one is green ", "19/20", ["17/20", "8/10", "21/40"]),
          QA("A college has 10 basketball players. A 5-member team and a captain will be selected out of these 10 players. How many different selections can be made?" , "1260" , ["210", "10C6 * 6!", "10C5 * 6"]),
          QA("Out of 7 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?" , "25200", ["24400", "21300", "210"]),
          QA("A boy has nine trousers and 12 shirts. In how many different ways can he select a trouser and a shirt?" , "108", ["21", "12", "9"]),
          QA("Find the sum of all the 4 digit numbers that can be formed with the digits 3, 4, 5 and 6" , "119988", ["11988", "191988", "none of these"]),
          QA("In how many different ways can the letters of the word 'LEADING' be arranged in such a way that the vowels always come together?" , "720", ["520", "700", "750"]),
          QA("How many combinations of students are possible if the group is to consist of exactly 3 freshmen?" , "4500" , ["5000", "4000", "3550"]),
          QA("Find the number of words, with or without meaning, that can be formed with the letters of the word ‘SWIMMING?" , "10080" , ["4569", "9800", "2748"]),
          QA("A five-digit number is formed using digits 1, 3, 5, 7 and 9 without repeating any one of them. What is the sum of all such possible numbers?" , "666600" , ["6666660", "6666666", "none of these"]),
          QA("An intelligence agency forms a code of two distinct digits selected from 0, 1, 2, …., 9 such that the first digit of the code is nonzero. The code, handwritten on a slip, can however potentially create confusion, when read upsidedown-for example, the code 91 may appear as 16. How many codes are there for which no such confusion can rise?" , "71" , ["80", "78", "69"]),
          QA("A college has 10 basketball players. A 5-member team and a captain will be selected out of these 10 players. How many different selections can be made?" , "1260", [ "4000", "1250", "1600"]),
          QA("How many words can be formed by using all letters of TIHAR?" , "120" , ["100", "140", "160"]),
          QA("How many 3-letter words with or without meaning, can be formed out of the letters of the word, 'LOGARITHMS', if repetition of letters is not allowed?" , "720" , ["420", "none of these", "5040"]),
          QA("In how many different ways can the letters of the word 'DETAIL' be arranged such that the vowels must occupy only the odd positions?" ,"36" , ["none of these", "64", "120"]),
          QA("In how many different ways can the letters of the word 'CORPORATION' be arranged so that the vowels always come together?" , "50400" , ["810", "1440", "2880"]),
          QA("Find the sum of all the 4 digit numbers that can be formed with the digits 3, 4, 5 and 6" , "119988", ["119988", "11988", "none of these"]),]

tough=[QA("When four fair dice are rolled simultaneously, in how many outcomes will at least one of the dice show 3?"  , "671", ["155", "620", "625"]),
       QA("Four dice are rolled simultaneously. What is the number of possible outcomes in which at least one of the die shows 6?" , "671" , ["6! / 4!", "625", "1296"]),
       QA("If the sides of a triangle are 26 cm, 24 cm and 10 cm, what is its area?" , "120" , ["130", "312", "315"]),
       QA("In a cricket championship, there are 21 matches. If each team plays one match with every other team, the number of teams is" , "7", ["9", "10", "none of these"]),
       QA("A committee has 5 men and 6 women. What are the number of ways of selecting 2 men and 3 women from the given committee?" , "200" , ["150", "250", "300"]),
       QA("There are 18 stations between Hyderabad and Bangalore. How many second class tickets have to be printed, so that a passenger can travel from any station to any other station?" ,"380", ["200", "190", "100"]),
       QA("Shopping mall has a Rectangle shaped childrens play area. The play area measures 30x20m. Laying of tiles would cost Rs.60 Per Sq.m. Find the total cost?" , "36000" , ["54000", "24000", "73637"]),
       QA("The length of a rectangular plot is 5 1/3, times that of its breadth. If the area of the plot is 270 square metres, then what is its length?" , "120" , ["130", "125", "none of these"]),
       QA("The sides of a rectangle are in the ratio 4:3 and its area is 972sq.m find the perimeter of rectangle?" , "126" , ["120", "122", "124"]),
       QA("The four walls and ceiling of a room of length 25 ft., breadth 12 ft. and height 10 ft. are to be painted. Painter A can Paint 200 sqr.ft in 5 days, painter B can paint 250sqr.ft in 2 days. If A & B work together, in how many days do they finish the job?" , "7 6/11" , ["5 8/13", "5 11/12", "6 10/33"]),
       QA("A right angled isosceles triangle is inscribed in a semicircle of radius 7 cm . The area enclosed by the semicircle but exterior to the triangle is", "28 sq cm" , ["14 sq cm", "44 sq cm", "68 sq cm"]),
       QA("A baby crawls randomly in a Rectangle shaped room. Mother discovers the dimensions of the room to be 35x25m. To protect the child against fall, parents decide to lay play mat on the floor. Play mat costs Rs.38 per Sq.m. How much do parents need to spend to make the floor childproof?" , "Rs. 33250" , ["Rs.46550", "Rs.23750", "Rs. 65831.58"]),
       QA("If each side of a square is increased by 25%, find the percentage change in its area" , "56.25" , ["62.25", "59.52", "58.75"]),
       QA("A Rectangle shaped wooden plate has a measurement of 20x10m. To Varnish the plate, painter charges Rs.18 Per Sq.m. Find the cost to varnish top side of the plate?" , "Rs. 3600" , ["Rs.7200", "Rs.1800", "Rs.3444"]),
       QA("The ratio of the length and the breadth of a rectangle is 4 : 3 and the area of the rectangle is 6912 sq cm. Find the ratio of the breadth and the area of the rectangle?" , "1 : 96" , ["1 : 48", "1 : 84", "1 : 68"]),
       QA("Find the roots of the quadratic equation: 2x^2 + 3x - 9 = 0?" , "(3/2, -3)" , ["(3, -3/2)", "(-3/2, -3)", "(3/2, 3)"]),
       QA("The sum and the product of the roots of the quadratic equation x^2 + 20x + 3 = 0 are?" , "None of these" , ["(10,3)", "(-10,3)", "(20,-3)"]),
       QA("Solve (x + 1)(x – 3) = 0" , "(-1,3)", ["(2,3)", "(-1,5)", "(-1,6)"]),
       QA("Solve for x: x^2-3x-10 = 0" , "(5,-2)" , ["(2,5)", "(4,7)", "(8,9)"]),
       QA("Simplify x: 3x^2+2x =1", "(1/3, -1)" , ["(2,5)", "(3,7)", "(8,9)"]),
       QA("I. 3x^2 – 5x – 12 = 0,II. 3y^2 – 8y – 16 = 0" , "If x ≤ y" , ["If x > y", "If x < y", "If x ≥ y"]),
       QA("Solve x^2 = 24 – 10x?" , "(2,-12)", ["(2,8)", "(3,8)", "(8,5)"]),
       QA("Solve 8x^2 = 15 -14x" , "(3/4, -5/2)" , ["(1/2, -1/2)", "(6/8, 5/8)", "(7/4, 8/5)"]),
       QA("I. 4x^2 + 3x – 27 = 0,II. 3y^2 – 20y + 32 = 0" , "If x < y" , ["If x > y", "If x ≥ y", "If x ≤ y"]),
       QA("How many real roots does the equation have?x^2+3x+4=0" , "0" , ["1", "2", "3"]),
       QA("3, 5, 11, 14, 17, 21" , "14", ["21", "17", "3"]),
       QA("Find the odd man out. 1, 3, 9, 12, 19, 29" , "12", ["9", "1", "3"]),
       QA("Find the odd man out: 3, 7, 15, 17, 22, 27, 29.", "22" ,["15", "17", "27"]),
       QA("Find the Missing Number 2, 6, 12, 20, 30, 42, 56, __" , "72" , ["60", "64", "70"]),
       QA("The average of runs of a cricket player of 10 innings was 32. How many runs must he make in his next innings so as to increase his average of runs by 4?" , "76" , ["79", "85", "89"]),
       QA("Average of all prime numbers between 30 to 50" , "39.8" , ["37", "37.8", "39"]),
       QA("The captain of a cricket team of 11 members is 26 years old and the wicketkeeper is 3 years older. If the ages of these two are excluded, the average age of the remaining players is one year less than the average age of the whole team. What is the average age of the team?" , "23 years" ,["24", "25", "none of these"]),
       QA("Average of 10 matches is 32, How many runs one should score to increase his average by 4 runs." , "76" , ["70", "78", "80"])]












### NATIONAL UNIVERSITY OF SINGAPORE

### CS1231 - DISCRETE STRUCTURES

### (Semester 1: AY2017/18)

```
Time Allowed: 2 Hours
```
### INSTRUCTIONS TO CANDIDATES

1. This assessment paper contains EIGHTEEN (18)questions inTWO (2) parts and
    comprisesTHIRTEEN (13)printed pages, including this page.
2. AnswerALLquestions.
3. This is anOPEN BOOKassessment.
4. You are allowed to useNUS APPROVED CALCULATORS.
5. You are to submit two documents: TheOCR formand theAnswer Sheet. You may
    keep this question paper.
6. ShadeandwriteyourStudent Numbercompletely and accurately on the OCR form.
7. You must use 2B pencil for the OCR form.
8. WriteyourStudent Numberon the Answer Sheet.Do not write your name.
9. You may use pen or pencil to write your answers, but please erase cleanly, and write
    legibly. Marks may be deducted for illegible handwriting.


## Part A: (30 marks) MCQ. Answer on the OCR form.

For each multiple choice question, choose the best answer andshadethe corresponding
choice on the OCR form. Remember toshadeandwriteyourStudent Number(check that
it is correct!) on the OCR form. Each multiple choice question is worth 2 marks. No mark is
deducted for wrong answers. You should use a2B pencil.

Q1. Given four words “eye”, “can”, “zoo” and “eat”, in how many ways can you arrange
these words and the letters within each word?
A. 4!× 32 × 62
B. 4!× 64
C. 4× 32 × 62
D. 4!×3!
E. 12!

Q2. In how many ways can you pair up 8 boys and 8 girls?
(A pair consists of a boy and a girl.)
A. 8^2
B. 8!
C. 4! + 4!
D. 8! + 8!
E. 16!

Q3. Given the predicates below:

```
M(x) = (xis a male student ).
F(x) = (xis a female student ).
CM(x,y) = (xandytake a common module ).
```
```
Which of the following quantified statements means “Every female student takes some
common module with every male student”? (The domain is the set of all students and is
omitted in the quantified statements below.)
(I). ∀x∀y(M(x) ∧ F(y) → CM(x,y) ).
(II).∀x(F(x) → ∀y(M(y) ∧ CM(x,y) ) ).
(III).∀x(F(x) → ∀y(M(y) → CM(x,y) ) ).
(IV).∀x∀y(M(x) ∧ F(y) ∧ CM(x,y) ).
```
```
A. (I) only.
B. (IV) only.
C. (I) and (III) only.
D. (II) and (IV) only.
E. None of A, B, C, or D.
```

Q4. Given the following three pairs of graphs:

```
Figure 1A Figure 1B
```
```
Figure 2A Figure 2B
```
```
Figure 3A Figure 3B
```
```
Which of the following statements are TRUE?
(I). The graphs in Figures 1A and 1B are isomorphic.
(II). The graphs in Figures 2A and 2B are isomorphic.
(III). The graphs in Figures 3A and 3B are isomorphic.
```
```
A. (I) only.
B. (II) only.
C. (I) and (II) only.
D. (II) and (III) only.
E. All of (I), (II) and (III).
```

Q5. Which of the following statements are TRUE?

```
(I). The Tietze’s graph shown in Figure 1A in Q4 is an Eulerian graph.
(II). The number of edges in a complete graphKnisn^2 /2.
(III). If a simple connected graph onnvertices does not contain a cycle, then it must have
exactlyn−1 edges.
```
```
A. (I) only.
B. (II) only.
C. (III) only.
D. All of (I), (II) and (III).
E. None of (I), (II) and (III).
```
Q6. In a game of chance, you are required to draw one ball from a bag containing 4 red balls,
7 green balls, and 9 blue balls. You win $20 if you draw a red ball, $15 if you draw a green
ball, or nothing if you draw a blue ball. You pay $10 for each game. After each game, the
ball drawn is returned to the bag.
If Aiken plays this game 100 times, how much would you expect her to lose?
A. $9.25.
B. $75.
C. $92.50.
D. $100.
E. None of the above.

Q7. Figure 4 below shows a graph on three vertices. DefineW3(vi) to be the number of
walks of length 3 from vertexvito itself.

### Figure 4

### v 1

### v 2 v^3

```
Which of the following is TRUE?
A.W3(v 1 ) = 2;W3(v 2 ) = 2;W3(v 3 ) = 2.
B.W3(v 1 ) = 4;W3(v 2 ) = 6;W3(v 3 ) = 6.
C.W3(v 1 ) = 4;W3(v 2 ) = 6;W3(v 3 ) = 8.
D.W3(v 1 ) = 4;W3(v 2 ) = 8;W3(v 3 ) = 8.
E. None of the above.
```

Q8. LetX,Y be two finite sets withmandnelements, respectively. Which of the following
statements is FALSE?
(I). Form=n, there aren! different bijective functions fromXtoY.
(II). Form= 6,n= 3, there are 120 different one-to-one functions fromXtoY.
(III). Form= 5,n= 2, there are 30 different surjective functions fromXtoY.
(IV). Form= 4,n= 5, there are 120 different injective functions fromXtoY.
A. (I) only.
B. (II) only.
C. (I) and (II) only.
D. (II), (III) and (IV) only.
E. All of (I), (II), (III) and (IV) are FALSE.

```
The next 7 questions (Q9 to Q15) refer to the following definitions.
```
```
Definition 1. AGroup, denoted(G,∗), is a setGalong with a binary operator∗
that satisfies these four axioms:
```
```
(A1) Closure: ∀a,b∈G, a∗b∈G.
(A2) Associativity: ∀a,b,c∈G,(a∗b)∗c=a∗(b∗c).
(A3) Identity: ∃e∈Gsuch that∀a∈G, a∗e=e∗a=a.
(A4) Inverse: ∀a∈G,∃b∈G(called theinverseofa) such
thata∗b=b∗a=e.
Remarks:
```
1. It is usual to writeabto meana∗b.
2. Because of Associativity, there is no ambiguity in writingabc, since the result is the
    same whichever way it is evaluated.
3. The elemente∈Gis called theidentity element, or simplyidentity.
4. The inverse ofais usually denoteda−^1.

```
Definition 2.IfGis finite withm∈Z+elements, then thegroup orderofGis
said to bem. For smallm, it is often helpful to see the group as aCayley table. Let
a 1 ,a 2 ,...,ambe the elements ofG, then each entry,cijin them×mCayley table is
defined ascij=aiaj, fori,j= 1, 2 ,...,m(see Table 1(a) on page 6.)
```
```
An example of a group is ({true,false},⊕). Its Cayley table is shown in Table 1(b). As
you may recall, ⊕ is the logicalexclusive-OR binary operator, which evaluates totrue
when both its inputs are different, andfalseotherwise.
```
```
To check whether this is a group, let’s see if it satisfies the four axioms. Closure is obvious
from the table, and Associativity is guaranteed by the⊕operator. From the table, the
identity is false, because true ⊕ false=true , and false ⊕ false=false, thus
satisfying Axiom (A3). The last equality also means thatfalseis its own inverse; while
true ⊕ true=falsemeans thattrueis its own inverse too. Thus, ({true,false},⊕) is
a group since it satisfies all 4 axioms.
```

```
∗ a 1 ... aj ... am
a 1
..
.
```
#### ..

#### .

```
ai ... cij ...
..
.
```
#### ..

#### .

```
am
```
```
⊕ true false
true false true
false true false
```
```
(a) General Cayley table (b) Cayley table for ({true,false},⊕)
```
```
Table 1: Cayley tables.
```
```
Another example of a group is the familiar (Z,+), that is, the set of integers with the
usual addition operator. Closure and Associativity are true for integers under addition,
and thus axioms (A1) and (A2) are satisfied. Theidentityis 0, sincea+ 0 = 0 +a=afor
alla∈Z. Finally, for eacha∈Z, its inverse is−a, sincea+ (−a) = (−a) +a= 0. Thus,
(Z,+) is a group. But sinceZis infinite, it is not possible to draw its Cayley table.
```
Q9. Which of the following is a group?

```
A. (R,◦), where R={R 120 ,R 240 ,R 360 }, and Rθ means “rotate an equilateral
triangle^1 θdegrees clockwise around its centerO” (see Figure 5), and◦means
function composition, ie.Rθ 2 ◦Rθ 1 means “rotate clockwise by θ 1 , followed by
θ 2 ”. Its Cayley table is shown below:
```
```
A
```
```
C B
```
```
R 120
```
```
O
```
```
C
```
```
B A
```
```
O
```
```
Figure 5: Rotation of an equilateral triangle byR 120.
```
#### ◦ R 120 R 240 R 360

#### R 120 R 240 R 360 R 120

#### R 240 R 360 R 120 R 240

#### R 360 R 120 R 240 R 360

```
B. (Z,×), that is, the set of integers with the multiplication operator.
C. ({true,false},∨), whose Cayley table is:
∨ true false
true true true
false true false
D. All of the above.
E. None of the above.
```
(^1) An equilateral triangle is a triangle in which all 3 sides have equal length, and all 3 angles are 60◦.


Q10. Define three functions as follows:

```
f:R−→R, ∀x∈R, f(x) =x+ 1.
g:R−→R, ∀x∈R, g(x) =x− 1.
h:R−→R, ∀x∈R, h(x) =x.
```
```
LetF={f,g,h}, and let◦denote function composition, ie. (f◦g)(x) =
f(g(x)).
```
```
Then, (F,◦) isnota group because:
```
```
(I) The Closure property is not satisfied. (II)◦is not associative.
(III) There is no identity element inF. (IV) Not every element inFhas an inverse.
```
```
A. (I) only.
B. (IV) only.
C. (I) and (IV) only.
D. (II), (III) and (IV) only.
E. None of A, B, C or D.
```
Q11. Given a group (G,∗), and from the 4 group axioms (A1) to (A4) alone, it is possible to
deduce that all the following statements are true, EXCEPT:
A. (Left cancellation law:)∀a,b,c∈G,(ab=ac)→(b=c).
B. (Uniqueness of inverse:) ∀a,b,b′∈G, ((ab=ba=e)∧(ab′=b′a=e))→(b=
b′).
C.∀a,b∈G, it is always possible to solve forx∈Ginax=b.
D. In each row of the Cayley table ofG, everyx∈Gappearsexactlyonce.
E. (Commutative law:)∀a,b∈G, ab=ba.

```
Definition 3.Given a group(G,∗), and anyx∈G, definepowersofxrecursively
as follows:
```
```
xn=
```
#### 

#### 

#### 

```
e(identity), ifn= 0,
x∗xn−^1 , if integern > 0 ,
x−^1 ∗xn+1, if integern < 0.
This means the usual power law holds:xm+n=xm∗xnand(xm)n=xmn,∀m,n∈Z.
```
```
Definition 4.For anyx∈G, letkbe the smallest positive integer, if such akexists,
such thatxk=e, then theelement orderofxis said to bek.
```
```
DefineG 1 ={ 1 , 2 , 3 , 4 }and define∗so thata∗b=a×b mod5, for alla,b∈G 1. In other
words, a∗b computes the remainder ofa×bwhen divided by 5. Consider the group
(G 1 ,∗), whose Cayley table is shown in Table 2.
```

#### ∗ 1 2 3 4

#### 1 1 2 3 4

#### 2 2 4 1 3

#### 3 3 1 4 2

#### 4 4 3 2 1

```
Table 2: Cayley table for (G 1 ,∗).
```
```
It is easy to verify that (G 1 ,∗) is indeed a group. Note that 4^3 = 4∗ 4 ∗4 = 1∗4 = 4.
Note also that the element order of 2 is 4, since 2^4 = 2∗ 2 ∗ 2 ∗2 = 4∗4 = 1, and 4 is the
smallest positive integer such that 2^4 = 1.
```
Q12. Using the Cayley table for (G 1 ,∗), what is 2−^1?

```
A.^12
B. 1
C. 2
D. 3
E. 4
```
Q13. Using the Cayley table for (G 1 ,∗), what is the element order of 4?

```
A. 1
B. 2
C. 3
D. 4
E. None of the above.
```
Q14. Using the Cayley table for (G 1 ,∗), solve 3x^2 = 1.

```
A. 1/
```
#### √

#### 3

#### B. 1

#### C. 2

#### D.

#### √

#### 2

```
E. There is no solution.
```
# Q15. Using the Cayley table for (G 1 ,∗), determine 3

### 45

```
67
.
```
## (Note that powers are right-associative:ab

```
c
```
## meansa(b

```
c)
.)
A. 1
B. 2
C. 3
D. 4
E. There is no solution.
```

## Part B: (40 marks) Structured questions. Write your answer in

## the Answer Sheet. Marks may be deducted for illegible hand-

## writing and unnecessary statements in proofs.

Q16. (14 marks)Counting and Probability.

```
(a) (7 marks) Answer the following parts. Working is not required.
i. (2 marks) How many integer solutions are there for the following equation, where
eachxi≥1?
x 1 +x 2 +x 3 = 10
ii. (2 marks) Assume that each cabin on a ferris wheel can carry only one person.
In how many ways can you arrange 30 people on a ferris wheel with 30 cabins?
In how many ways can you arrange 29 people on a ferris wheel with 30 cabins?
```
```
iii. (3 marks) Dueet is known to speak the truth two out of three times. He throws a
fair, six-sided die and reports that it shows a 6. What is the probability that the
number shown on the die is really 6? (Write your answer as a simple fraction.)
```
```
(b) (3 marks) Prove that two consecutive positive integers are co-prime, that is,∀x∈Z+,
xandx+ 1 are co-prime.
```
```
(c) (4 marks) Using the Pigeonhole Principle (other proofs will not be accepted), prove
that if we taken+ 1 numbers from the set{ 1 , 2 , 3 ,..., 2 n}, then some pair of numbers
will be co-prime.
```

Q17. (14 marks)Trees and Graphs.

```
(a) (3 marks) Based on the postorder traversal and inorder traversal of a binary tree
with vertices A, B, C, D, E, F, G and H as given below, draw the binary tree.
```
```
Postorder: F C E H D A B G
Inorder: C F G E D H B A
(b) (6 marks) The Dijkstra’s Shortest Path Algorithm is shown below. G, shown below,
is a connected simple graph with a positive weight for every edge,ais the starting
vertex and z the ending vertex. The function w(u,v) denotes the weight for the
edge connecting verticesu,v. The notation “x:=y” means assign the value ofyto
variablex.
```
```
Dijkstra’s Algorithm
Input:GraphG, with starting vertexa, ending vertexz.
Output:L(z), the length of the shortest path fromatoz.
```
1. InitializeT to be the graph with vertexaand no edges. LetV(T) be
    the set of vertices inT, and letE(T) be the set of edges ofT.
2. LetL(a) := 0, and for all verticesxinGexcepta, letL(x) := +∞.
    (The numberL(x) is called the label ofx.)
3. Letv:=aandF:={a}.
4. while(z /∈V(T))
    4.1.F:= (F−{v})∪ {vertices that are adjacent tovand are not in
       V(T)}
    4.2. For each vertexuthat is adjacent tovand is not inV(T)
       4.2.1. ifL(v) +w(v,u)< L(u)then
          4.2.1.1. L(u) :=L(v) +w(v,u)
          4.2.1.2. D(u) :=v
    4.3. Find a vertexxinFwith the smallest label.
    4.4. Add vertexxtoV(T), and add edge{D(x),x}toE(T).
    4.5.v:=x
    end while

# a

# b

# c

# d

# e

# f

# g

# z

## 2 18

## 8

## 3

## 42

## 5

## 48

## 62

## 10

## 6

## 36

## 30

## 40

## 10

## 12


```
Run Dijkstra’s algorithm on the graph shown above.
```
```
i. (2 marks) What is the shortest distance fromatoz?
```
```
ii. (4 marks) Write out the finalV(T), with the vertices arranged in order of their
addition intoV(T) according to the above algorithm. The first vertex and the
last vertex are of courseaandz, respectively.
```
(c) (5 marks) Suppose you are given a pile ofnstones. At each step, you are allowed to
separate a pile ofkstones into two piles ofk 1 andk 2 stones. Obviously,k 1 +k 2 =k.
On doing this, you earnk 1 ×k 2 dollars.

```
What is the maximum amount of money you can earn starting with a pile of n
stones? Explain your answer.
```

Q18. (12 marks)Group Theory. (Please refer to the Group Definitions 1 to 4 given on
pages 5 and 7.) We make one more definition.

```
Definition 5.Two groups,(G,∗) and(H, ), are said to be isomorphic, if and
only if, there exists a bijectionf:G−→Hsuch that:
```
```
(Isomorphic property:) ∀x,y∈G, f(x∗y) =f(x) f(y).
```
```
Note that in the left hand side of the above equation, the binary operator is that ofG,
while the right hand side’s binary operator is that ofH. As long as we keep this in
mind, we may re-write the property as:
```
```
(Isomorphic property:) ∀x,y∈G, f(xy) =f(x)f(y).
```
```
We writeG∼=Hto denote the fact that groups(G,∗)and(H, )are isomorphic.
```
```
Isomorphic groups are, as you may have guessed, “equal” to each other, in the sense that
one group (H, ) may be obtained from the other group (G,∗) by:
(i) renaming the elements inGto those inH, and
(ii) renaming the binary operator∗to ,
in such a way that their Cayley tables agree. The bijection f, with the isomorphic
property, captures this renaming mathematically.
```
```
Define two groups, (G 2 ,×), and (G 3 ,•) by their Cayley tables shown below:
```
```
× 1 i −i − 1
1 1 i −i − 1
i i − 1 1 −i
−i −i 1 − 1 i
− 1 − 1 −i i 1
```
- e a b c
e e a b c
a a e c b
    b b c e a
    c c b a e

```
(a) (G 2 ,×), wherei=
```
#### √

```
−1. (b) (G 3 ,•).
```
```
Table 3: Cayley tables.
```
```
(a) (2 marks) Compare groups (G 1 ,∗) (defined in Table 2, on page 8), and (G 2 ,×)
above. It should be obvious thatG 1 ∼=G 2. Find the bijectionf:G 1 −→G 2 with the
isomorphic property that establishes the isomorphism.
```
```
(b) (2 marks) Now compare (G 2 ,×) with (G 3 ,•). Explain whyG 2 G 3 , ie. they are not
isomorphic. (Do not say “because no bijection exists”; instead, explain using some
property of the elements of the groups.)
```
```
(c) (4 marks) Let’s show that∼=is an equivalence relation onS, the set of groups. It is
straightforward to prove reflexivity and transitivity:
```

```
Proof (Reflexivity).
```
1. Take any groupg∈S.
2. The identity functionIg:g−→gsuch thatIg(x) =x,∀x∈g, is a bijection, by Q3(a),
    Assignment #2.
3. Also, clearly,∀x,y∈g, Ig(xy) =xy=Ig(x)Ig(y), by definition ofIg.
4. Thus,Ighas the isomorphic property.
5. Henceg∼=g, and∼=is reflexive. 
Proof (Transitivity).
1. Take any three groupsg,h,i∈S.
2. Supposeg∼=handh∼=i:
2.1. Then∃r:g−→hwhich is a bijection with the isomorphic property, by definition of
isomorphism.
2.2. Then∃s:h−→iwhich is a bijection with the isomorphic property, by definition of
isomorphism.
2.3. Thens◦r:g−→iis also a bijection, by Theorems 7.3.3, 7.3.4 (Epp).
2.4. (To prove isomorphic property:) Take anyx,y∈g.
2.5. Then,s◦r(x)s◦r(y) =s(r(x))s(r(y)), by definition of◦.
2.6. =s(r(x)r(y)), by the isomorphic property ofs.
2.7. =s(r(xy)), by the isomorphic property ofr.
2.8. =s◦r(xy), by definition of◦.
2.9. Thuss◦rhas the isomorphic property.
2.10. Thus,g∼=i.
3. Hence∼=is transitive. 

```
Notice that in these proofs, we needed to (i) find the bijection, and (ii) prove that it
possess the isomorphic property. Complete the proof below that∼=onSis symmetric.
Fill in the missing 3 (at most 4) steps from Lines 2.5. to 2.8. If you exceed 4 steps, 0
marks will be given. Be sure to justify each step.
Proof (Symmetry).
```
1. Take any two groupsg,h∈S.
2. Supposeg∼=h:
    2.1. Then∃f:g−→hwhich is a bijection with the isomorphic property, by
       definition of isomorphism.
    2.2. Thenf−^1 :h−→gis also a bijection, by Theorem 7.2.3 (Epp).
    2.3. (To prove thatf−^1 has the isomorphic property:)
    2.4. Take anyx,y∈h.
    2.5.
    2.6.
    2.7.
    2.8. (Optional)
    2.9. Thusf−^1 has the isomorphic property.
2.10. Thush∼=g.
3. Hence∼=is symmetric. 

(d) (4 marks) Prove that for any group (G,∗), with identity elemente, ifGis finite, then
∀x∈G,∃n∈Z+ such thatxn=e.

#### END OF PAPER

![E=mc^2](https://render.githubusercontent.com/render/math?math=E%3Dmc%5E2)

Einstein's equation: `E = mc^2`

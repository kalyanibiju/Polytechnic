# **DISCRETE MATHEMATICS**

### **MODULE 1**

#### **DISCRETE VS CONTINUOUS** 



Discrete Mathematics is the branch of mathematics that studies countable, distinct, and separate objects, rather than continuous quantities. It provides the mathematical foundation for computer science, digital systems, cryptography, and data structures.



Unlike calculus, which deals with continuous change, discrete mathematics focuses on individual values such as integers, graphs, logical statements, and finite sets.

"A computer works with separate, countable pieces of information like 0 and 1, Yes or No, True or False. The mathematics used to study these separate values is called Discrete Mathematics."



Imagine a classroom.

You can count:



45 students

30 chairs

5 windows



These are discrete because they are separate objects.



But you cannot count:



Air in the room

Heat

Time passing



These are continuous.





"Every computer program makes decisions."



Example:



If password is correct,

&#x20;   Open account

Else

&#x20;   Show 'Invalid Password'



"How does the computer decide?"



Answer:



"Using Logic."



| Continuous Mathematics               | Discrete Mathematics                     |

| ------------------------------------ | ---------------------------------------- |

| Deals with continuous values         | Deals with separate and countable values |

| Example: Time, Distance, Temperature | Example: Students, Books, Cars           |

| Uses Calculus                        | Uses Logic, Sets, Graphs                 |





#### **PROPOSITIONS/STATEMENTS**



A statement is a declarative sentence that is either true or false but not both. Ans it ends with a fullstop.

if a proposition is true, its truth value is TRUE.

if a proposition is false, its truth value is FALSE.

We use lowercase letters of the alphabet to represent a statement(such as p,q,....)



###### **Example for a proposition**



| Statement            | Proposition? | Reason |

| -------------------- | ------------ | ------ |

| 2 + 3 = 5            | Yes          | True   |

| Earth is round       | Yes          | True   |

| 10 > 20              | Yes          | False  |

| Water boils at 100°C | Yes          | True   |



###### **Example for not a proposition**



| Statement       | Reason       |

| --------------- | ------------ |

| How are you?    | Question     |

| Close the door. | Command      |

| x + 5 = 10      | Depends on x |

| Wow!            | Exclamation  |





##### **Simple and Compound Propositions**



###### Simple Proposition



Contains only one statement.



Example:



p : It is raining.

###### 

###### Compound Proposition



Made by combining two or more propositions.



Example:



p : It is raining.



q : I carry an umbrella.



Compound proposition:



"It is raining AND I carry an umbrella."

#### **LOGICAL CONNECTIVES**

Logical connectives combine propositions.



There are five important connectives.

##### **1. Negation (NOT)**



Symbol:



¬p



Meaning:



Opposite of p.



Example:



p : It is raining.



¬p : It is not raining.

**TRUTH TABLE**

| p | ¬p |

| - | -- |

| T | F  |

| F | T  |

##### **2. Conjunction (AND)**



Symbol:



p ∧ q



Meaning:



Both statements must be true.



Example:



"I studied AND I passed."

**TRUTH TABLE** 

| p | q | p∧q |

| - | - | --- |

| T | T | T   |

| T | F | F   |

| F | T | F   |

| F | F | F   |

Remember:



Only TT gives True.

##### **3. Disjunction (OR)**



Symbol:



p ∨ q



Meaning:



At least one statement is true.



Example:

"I will have tea OR I will have coffee."



**TRUTH TABLE**

| p | q | p∨q |

| - | - | --- |

| T | T | T   |

| T | F | T   |

| F | T | T   |

| F | F | F   |

Remember:



Only FF gives False.

##### **4. Implication**



Symbol:



p → q



Read as:



"If p, then q"



Example:



If it rains, then roads become wet.



**TRUTH TABLE**



p	q	p→q

T	T	T

T	F	F

F	T	T

F	F	T



Important:



Implication is False only when p is True and q is False.



##### **5. Biconditional**



Symbol:



p ↔ q



Read as:



p if and only if q



Example:

You pass the exam IF AND ONLY IF you study.



**TRUTH TABLE**

**| p | q | p↔q |**

**| - | - | --- |**

**| T | T | T   |**

**| T | F | F   |**

**| F | T | F   |**

**| F | F | T   |**

##### 

##### Truth Tables

##### 

A truth table shows every possible combination of truth values.



For n propositions,



Number of rows = 2ⁿ



Examples:

| Number of variables | Rows |

| ------------------- | ---- |

| 1                   | 2    |

| 2                   | 4    |

| 3                   | 8    |

| 4                   | 16   |

#### **Tautology**



Definition:



A compound proposition that is always True.



Example:



p ∨ ¬p

TRUTH TABLE

| p | ¬p | p∨¬p |

| - | -- | ---- |

| T | F  | T    |

| F | T  | T    |

Therefore, p ∨ ¬p is a tautology.

note :

Last column = All True



↓



Tautology

#### **Contradiction**



Definition



A compound proposition which is always False.



Example



p ∧ ¬p

TRUTH TABLE

| p | ¬p | p∧¬p |

| - | -- | ---- |

| T | F  | F    |

| F | T  | F    |

Therefore, p ∧ ¬p is a contradiction.



note :

Last column = All False



↓



Contradiction

#### **Contingency**



Definition



A compound proposition which is Sometimes True and Sometimes False.



Example



p ∧ q



Truth Table

| p | q | p∧q |

| - | - | --- |

| T | T | T   |

| T | F | F   |

| F | T | F   |

| F | F | F   |

Therefore, p ∧ q is a contingency.



###### **Comparison**



| Type          | Last Column               |

| ------------- | ------------------------- |

| Tautology     | All True                  |

| Contradiction | All False                 |

| Contingency   | Mixture of True and False |



###### **Translating English sentence to Logical Expression**



If it rains, then I carry an umbrella.

Here,

p: It rains.

q: I carry an umbrella.

The connective used is : If...then

"If...then" is represented by the implication symbol →.



Therefore,



p→q

note :

Every translation starts by identifying the simple statements and the connecting words.



| English Word/Phrase | Logical Symbol | Example                |

| ------------------- | -------------- | ---------------------- |

| Not                 | ¬              | Not raining → ¬p       |

| And                 | ∧              | Study and pass → p ∧ q |

| Or                  | ∨              | Tea or coffee → p ∨ q  |

| If...then           | →              | If p then q            |

| If and only if      | ↔              | p ↔ q                  |



Example 1



Let



p: I study.



q: I pass.



Sentence:



I study and I pass.



Connecting word:



and



Expression:



p∧q

Example 2



Sentence



I study or I pass.



Expression



p∨q

Example 3



Sentence



I do not study.



Expression



¬p



"If"

If p, then q



p → q



Example



If I study,



then I pass.



"Only If"

p only if q



p → q



Example



I pass only if I study.



↓



If I pass,



then I studied.



Example



I pass if and only if I study.



This means



If I study,



I pass.



AND



If I pass,



I studied.



So



p↔q



**Example** 



###### **Let**

###### 

###### **p: I study.**

###### 

###### **q: I attend class.**

###### 

###### **r: I pass.**



Translate



I study and attend class.



Answer



p∧q



Translate



If I study and attend class, then I pass.



Students first identify



"I study and attend class"



↓



p∧q



Then



"If...then"



↓



(p∧q)→r



Explain that parentheses show which part of the sentence belongs together.



ONLY IF

I write exam

&#x20;     │

&#x20;     ▼

I paid the fee



Only one arrow.



One direction.



IF AND ONLY IF

I pass  ◄────►  I receive certificate



Two arrows.



Both directions.



ONLY IF = One-way relationship



IF AND ONLY IF = Two-way relationship



##### **Logical Equivalence**



Two propositions are logically equivalent if they have identical truth values for every possible input.



Notation:



p ≡ q

Read it as:



"is logically equivalent to."



**Example : 1**

¬(¬p)

p	¬p	¬¬p

T	F	T

F	T	F



Compare the columns of p and ¬¬p.



They are identical.



Hence,



¬(¬p)≡p



###### **Important Logical Equivalences**



| Law             | Equivalent Expression |

| --------------- | --------------------- |

| Double Negation | ¬(¬p)=p               |

| Identity        | p∧T=p, p∨F=p          |

| Domination      | p∨T=T, p∧F=F          |

| Idempotent      | p∨p=p                 |

| Complement      | p∨¬p=T                |

| De Morgan's     | ¬(p∧q)=¬p∨¬q          |

| De Morgan's     | ¬(p∨q)=¬p∧¬q          |



#### **Converse, Inverse and Contrapositive**



**Original:**



p → q



If it rains,

then roads are wet.

p : it rains

q : roads are wet



**Converse**



q → p



If roads are wet,

then it rains.



(Not always true.)



**Inverse**



¬p → ¬q



If it does not rain,

roads are not wet.



(Not always true.)



**Contrapositive**



¬q → ¬p



If roads are not wet,

then it did not rain.



(Logically equivalent to the original implication.)



Statement	Symbol	How to Form

Original	p→q	Given statement

Converse	q→p	Interchange

Inverse		¬p→¬q	Negate both

Contrapositive	¬q→¬p	Interchange and negate

#### 

#### **Duality Principle**



**Definition**



The Duality Principle states that:



The dual of a logical expression is obtained by replacing:



AND (∧) with OR (∨)

OR (∨) with AND (∧)

True (T) with False (F)

False (F) with True (T)



The variables (p, q, r, ...) and negations (¬) are not changed.



Example



Dual of p ∧ T is p ∨ F



Find the dual of



(p∧q)∨r



Replace



∧ → ∨

∨ → ∧



Answer:



(p∨q)∧r

&#x09;​

Find the dual of



(p∨q)∧(r∨T)



Replace:



First ∨ → ∧

∧ → ∨

Second ∨ → ∧

T → F



Answer:



(p∧q)∨(r∧F)

&#x09;​








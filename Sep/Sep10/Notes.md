Unit 1: Digital Logic Basics

1. What is Digital Logic?

In computers/electronics, everything is represented using 0s and 1s.

0 = OFF (low voltage, ~0V)

1 = ON (high voltage, e.g., ~5V or ~3.3V)

👉 Digital logic is about building systems that take 0/1 inputs and produce 0/1 outputs using logic rules.

(Analogy: Like traffic lights – Red = stop (0), Green = go (1). The controller decides the output based on rules.)

2. Logic Gates (the building blocks of circuits)

Think of gates as functions in Python, but they always take binary inputs and give binary outputs.

Basic Gates

AND Gate ( · )

Output = 1 only if both inputs are 1.

Truth Table:

A  B | Output
0  0 |   0
0  1 |   0
1  0 |   0
1  1 |   1


(Analogy: "I will go for a trip if AND only if I have money AND time.")

OR Gate ( + )

Output = 1 if any one input is 1.

Truth Table:

A  B | Output
0  0 |   0
0  1 |   1
1  0 |   1
1  1 |   1


(Analogy: "I will order pizza if I am hungry OR bored.")

NOT Gate ( ¬ )

Inverts the input.

Truth Table:

A | Output
0 |   1
1 |   0


(Analogy: A light switch – if input = OFF, output = ON.)

Derived Gates

NAND (Not AND)

Output = opposite of AND.
(Most chips are built using NAND because it’s cheaper and universal.)

NOR (Not OR)

Output = opposite of OR.

XOR (Exclusive OR)

Output = 1 if inputs are different.

Truth Table:

A  B | Output
0  0 |   0
0  1 |   1
1  0 |   1
1  1 |   0


(Analogy: "Exactly one of us pays the bill – not both.")

3. Combinational vs Sequential Logic

Combinational Logic: Output depends only on current inputs.
(e.g., Calculator – if you input 2+3, you immediately get 5.)

Sequential Logic: Output depends on current input and past history (memory).
(e.g., Lift system – current floor depends on past button presses.)

4. Flip-Flops (Intro only)

Flip-flop = memory cell that stores 1 bit.

Controlled by clock signal.

Example: D Flip-Flop stores the input D whenever clock pulses.

(Analogy: Taking a photo at every clock tick – you store the value of input at that moment.)
module logic_gates(
    input a,
    input b,
    output and_out,
    output or_out,
    output xor_out,
    output nand_out,
    output nor_out,
    output xnor_out
);
    assign and_out = a & b;
    assign or_out = a | b;
    assign xor_out = a ^ b;
    assign nand_out = ~(a & b);
    assign nor_out = ~(a | b);
    assign xnor_out = ~(a ^ b);
endmodule

module basic_gates(a, b, and_out, or_out, xor_out);
    input a, b;
    output and_out, or_out, xor_out;

    assign and_out = a & b;
    assign or_out = a | b;
    assign xor_out = a ^ b;
endmodule

module mux_2to1(i0, i1, sel, out);
    input i0, i1, sel;
    output out;

    assign out = sel ? i1 : i0;
endmodule

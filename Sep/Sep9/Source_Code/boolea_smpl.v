module simplified_expr1(a, b, c, y);
    input a, b, c;
    output y;

    assign y = a & (~b | c);
endmodule

module simplified_expr2(a, b, y);
    input a, b;
    output y;

    assign y = ~(~a & ~b);
endmodule

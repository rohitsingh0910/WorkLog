module sensitivity_example(clk, rst, a, b, y);
    input clk, rst, a, b;
    output reg y;

    always @(posedge clk or posedge rst) begin
        if (rst)
            y <= 0;
        else
            y <= a & b;
    end
endmodule

module combinational_example(a, b, y);
    input a, b;
    output y;

    assign y = a | b;
endmodule

module sync_reset(clk, rst, d, q);
    input clk, rst, d;
    output reg q;

    always @(posedge clk or posedge rst) begin
        if (rst)
            q <= 0;
        else
            q <= d;
    end
endmodule

module comb_logic(a, b, y);
    input a, b;
    output y;

    assign y = a ^ b;
endmodule

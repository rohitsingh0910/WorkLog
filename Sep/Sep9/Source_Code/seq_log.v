module d_flip_flop(clk, rst, d, q);
    input clk, rst, d;
    output reg q;

    always @(posedge clk or posedge rst) begin
        if (rst)
            q <= 0;
        else
            q <= d;
    end
endmodule

module t_flip_flop(clk, rst, t, q);
    input clk, rst, t;
    output reg q;

    always @(posedge clk or posedge rst) begin
        if (rst)
            q <= 0;
        else if (t)
            q <= ~q;
    end
endmodule

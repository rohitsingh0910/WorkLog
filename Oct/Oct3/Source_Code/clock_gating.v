module clk_gated (
    input wire clk,
    input wire en,
    input wire rst,
    input wire d,
    output reg q
);

    wire gclk;
    assign gclk = clk & en;

    always @(posedge gclk or posedge rst) begin
        if (rst)
            q <= 1'b0;
        else
            q <= d;
    end

endmodule

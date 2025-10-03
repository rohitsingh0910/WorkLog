module mbff_example (
    input wire clk,
    input wire rst,
    input wire [3:0] d_in,
    output reg [3:0] q_out
);

    always @(posedge clk or posedge rst) begin
        if (rst)
            q_out <= 4'b0;
        else
            q_out <= d_in;
    end

endmodule

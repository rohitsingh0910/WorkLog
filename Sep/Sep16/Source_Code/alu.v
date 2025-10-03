module alu(
    input [3:0] a,
    input [3:0] b,
    input [2:0] op,
    output reg [4:0] result
);
    always @(*) begin
        case (op)
            3'b000: result = a + b;
            3'b001: result = a - b;
            3'b010: result = a & b;
            3'b011: result = a | b;
            3'b100: result = a ^ b;
            3'b101: result = ~a;
            3'b110: result = a << 1;
            3'b111: result = a >> 1;
            default: result = 5'b00000;
        endcase
    end
endmodule

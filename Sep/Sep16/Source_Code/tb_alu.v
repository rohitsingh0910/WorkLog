module alu_tb;
    reg [3:0] a;
    reg [3:0] b;
    reg [2:0] op;
    wire [4:0] result;

    alu uut (
        .a(a),
        .b(b),
        .op(op),
        .result(result)
    );

    initial begin
        a = 4'd5; b = 4'd3;
        op = 3'b000; #10;
        op = 3'b001; #10;
        op = 3'b010; #10;
        op = 3'b011; #10;
        op = 3'b100; #10;
        op = 3'b101; #10;
        op = 3'b110; #10;
        op = 3'b111; #10;
        $stop;
    end
endmodule

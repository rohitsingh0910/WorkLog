module sync_ff (
    input wire clk_dest,
    input wire async_signal,
    output reg sync_signal
);

    reg sync_ff1;

    always @(posedge clk_dest) begin
        sync_ff1 <= async_signal;
        sync_signal <= sync_ff1;
    end

endmodule

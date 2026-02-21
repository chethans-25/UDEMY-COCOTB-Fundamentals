`timescale 1ns/1ps
 
module adder(
input rst
);
 
reg clk = 0;
 
always #10 clk = ~clk; // 0-10 : 0 10-20:1
 
 
initial begin
$dumpfile("dump.vcd");
$dumpvars(1,adder);
end
 
endmodule
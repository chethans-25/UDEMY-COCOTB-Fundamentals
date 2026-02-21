`timescale 1ns/1ps
 
module adder(
input [3:0] a,b,
output [4:0] s
);
 
assign s = a + b;
 
initial begin
$dumpfile("dump.vcd");
$dumpvars(1,adder);
end
 
endmodule
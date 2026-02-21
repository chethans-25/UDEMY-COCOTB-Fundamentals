import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge, Edge, ClockCycles
 
#fixed duration rst - 2 pos edge clk , 
@cocotb.test()
async def test(dut):
      rst = dut.rst
      rst.value = 1
      await ClockCycles(dut.clk,5,True)
      rst.value = 0
      await ClockCycles(dut.clk,5,False)
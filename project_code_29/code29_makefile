import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge, Edge
 
#fixed duration rst - 2 pos edge clk , 
@cocotb.test()
async def test(dut):
      rst = dut.rst
      rst.value = 1
      await RisingEdge(dut.clk)
      await RisingEdge(dut.clk)
      rst.value = 0
      await FallingEdge(dut.clk)
      await FallingEdge(dut.clk)
      rst.value = 1
      await Edge(dut.clk)
      await Edge(dut.clk)
      rst.value = 0
      for i in range(5):
          await FallingEdge(dut.clk)
      rst.value = 1    
      for i in range(5):
          await RisingEdge(dut.clk)
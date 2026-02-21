import cocotb
import logging
from cocotb.triggers import Timer
 
#fixed duration
@cocotb.test()
async def test(dut):
      logging.warning('Value of clk : %0d',dut.clk.value)
      await Timer(15, units = 'ns')
      logging.warning('Value of clk : %0d',dut.clk.value)

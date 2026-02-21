import cocotb
import logging
from cocotb.triggers import Timer
 
#fixed duration
@cocotb.test()
async def test(dut):
      rst = dut.rst
      rst.value = 1
      await Timer(50, units = 'ns')
      rst.value = 0
      await Timer(100, units = 'ns')
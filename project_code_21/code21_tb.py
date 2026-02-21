import cocotb
import logging
from cocotb.triggers import Timer
 
@cocotb.test()
async def test(dut):
      #dut.a.value = 12
      #dut.b.value = 15
      dut.a <= 12
      dut.b <= 15
      await Timer(10, units = 'ns')
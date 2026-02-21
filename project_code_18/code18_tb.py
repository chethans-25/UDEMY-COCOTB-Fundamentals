import cocotb
import logging
from cocotb.triggers import Timer
 
@cocotb.test()
async def test(dut):
      a_val = dut.a
      a_val.value = 12
      b_val = dut.b
      b_val.value = 15
      
      await Timer(10, units = 'ns') 
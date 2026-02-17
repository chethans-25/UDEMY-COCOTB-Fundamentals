import cocotb
import logging
 
@cocotb.test()
async def test(dut):
      print('My first cocotb TB')
      logging.getLogger().setLevel(logging.INFO)
      logging.info('My first cocotb TB')
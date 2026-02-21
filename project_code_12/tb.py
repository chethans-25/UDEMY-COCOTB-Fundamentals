import cocotb
import logging
 
@cocotb.test()
async def test(dut):
      logging.getLogger().setLevel(logging.INFO)
      a = 10
      #integer hexadecimal binary
      #logging.info('Value of a in decimal format : %0s',bin(a))
      logging.info('Value of a in decimal format:%0d',a)
      logging.info('Value of a in hexadecimal format:%0x',a)
      logging.info('Value of a in binary format : %0s',f"8'b{a:08b}")
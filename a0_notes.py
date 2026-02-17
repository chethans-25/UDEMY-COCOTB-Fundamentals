# *************** Section 1: Getting Started with IDE ***************

# Tools needed:
# Latest version Python
# Icarus simulator
# GTKwave for timing diagram analysis

# files needed
# design file .sv
# testbench file .py
# make file

# Installation Commands
'''
sudo apt update
sudo apt install python3-pip
pip3 --version
sudo pip3 install cocotb
sudo pip3 install pyuvm
sudo pip3 install pandas
sudo apt install iverilog
sudo apt install gtkwave
'''

# Compilation Commands
'''
make sim = icarus

gtkwave wave.vcd

'''

# print and logging
from cocotb.triggers import Timer

import logging
import cocotb
@cocotb.test() #to recognize testcase
async def test(dut): #asynchronous function
  print("Hello")
  logging.getLogger().setLevel(logging.INFO) #default level is warning, need to change
  logging.info("COCOTB info message")
  logging.warning("COCOTB warning message")

# Sending variable values on console in different formats

# %d decimal
# %x hex

# binary format specifier is not available
num = 10
logging.info('Value of num = %0s', bin(num))

# Formatted string for num variable
num = 10
logging.info('Value of num = %0s', f'{num:08b}')
# above line: 8 bit binary with leading zeros



# ************ Section 2: Fundamentals ************

# Executing DUT from Python TB

# inside dut
# initial $display("Executed DUT Code")

# Inside TB
async def test(dut):
  print("Executing DUT code from TB")

# Results
# Executing DUT code from TB
# Executed DUT Code

# Apply Stimuli

# different methods to do
# access DUT IO handles
# Access Value property (recommended)
# Direct Assign


# access DUT IO handles
async def test(dut):
  a_val = dut.a #accessing IO handle
  a_val.value = 12 #Value method to assign value
  await Timer(10, units="ns") #to generate 10 ns delay

# Access Value property
async def test(dut):
  dut.a.value = 12 #Directly use value method
  await Timer(10, units="ns") #to generate 10 ns delay


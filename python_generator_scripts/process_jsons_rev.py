import json
import subprocess
from utils import *
from copy import deepcopy as dcp


def main():
    

    

    
    # Sample JSON data
    config_data = json.load(open('config_example.json', 'r'))
    value_data = json.load(open('value_example.json', 'r'))

    # Generate the files
    generate_files(config_data, value_data, is_tb=False, filename = 'myfile')
    

def generate_files(config_data, value_data, is_tb=False, filename='myfile'):
    """
    Description
    -----------
    
    ```process_jsons.py``` ingests these .json files above and generates up to three files named after ```filename``` field
    1. ```<filename>.v```
        - Verilog file that assigns wires named after fields in .jsons to register space
    2. ```<filename>_set_registers.py```
        - Python file that returns the values that each register should be set, note that register 0 is the control register, and the values correspond to register 1 onward.
    3. ```<filename>_tb.v``` (Optional)
        - Test bench that runs ```<filename>_set_registers.py``` intermittently to put example values in a test bench for ```<filename>.v```
        
    Parameters
    ----------
    config_data : dict
        loaded from config json that has fields and bit amounts
    value_data : dict
        loaded from value json that has fields with values
    is_tb : bool (optional)
        bool to generate a test bench file, default False
    filename : str
        filename you specify for the outputs
        
    Returns
    -------
    None
    
    """
    register_width = config_data['parameters']['REGISTER_WIDTH']
    addr_width = config_data['parameters']['REGISTER_ADDR_WIDTH']
    
    verilog_lines = []
    always_lines = []
    set_reg_lines = [
        "import subprocess",
        "import struct",
        "import json",
        "",
        "# Function to write a value to a register at a given address",
        "def write_register(addr, value):",
        f"    subprocess.run(['devmem', addr, '{register_width}', value], check=True)",
        "",
        "value_data = json.load(open('value_example.json','r'))",
        "num_control_reg = 1 #First offset after control register",
        "reg_values = []\n",
        "def main():",
        "    return set_reg_values()\n",
        "def set_reg_values():",
        "    reg_value = 0\n",
    ]
    
    # Initialize always block for all sync and steady registers
    always_lines.append("always @(posedge M_AXIS_CLK) begin")

    # Process control fields first
    reg_index = 0
    remaining_bits_in_reg = dcp(register_width)
import json
import subprocess
from utils import *
from copy import deepcopy as dcp



def main():
    
    # Sample JSON data
    config_data = json.load(open('config_example.json', 'r'))
    value_data = json.load(open('value_example.json', 'r'))

    # Generate the files
    generate_files(config_data, value_data, is_tb=True, filename = 'myfile')
    

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
    
    max_num_waveforms = 2**config_data['global_fields']['NUM_WF']  # Number of waveforms
    
    verilog_lines = []
    always_lines = []
    array_definitions = []
    set_reg_lines = []
    
    reg_index = 0
    
    set_reg_lines.extend( 
        ["import subprocess",
        "import struct",
        "import json",
        "",
        "# Function to write a value to a register at a given address",
        "def write_register(addr, value):",
        f"    subprocess.run(['devmem', addr, '{register_width}', value], check=True)",
        "",
        "value_data = json.load(open('value_example.json','r'))",
        "num_control_reg = 1 #First offset after control register",
        "reg_values = [0] #Placehold for Control Register",
        "gf_value = value_data['global_fields']",
        "wf_value = value_data['waveform_fields']\n\n",
        "def main():",
        "    return set_reg_values()\n",
        "def set_reg_values():",
        "    reg_value = 0\n"]
    )
    
    
    # Initialize always block for all sync and steady registers
    always_lines.append("always @(posedge M_AXIS_CLK) begin")

    # Process control fields first
    #reg_index = 0
    remaining_bits_in_reg = dcp(register_width)
    verilog_lines.append("// Control Fields")
    for field,bit_length in config_data['control_fields'].items():
        verilog_lines.append(f"wire [{bit_length-1}:0] {field}; assign {field} = steady_slv_reg{reg_index}[{register_width-remaining_bits_in_reg + bit_length - 1}:{register_width-remaining_bits_in_reg}];")
        remaining_bits_in_reg -= bit_length
    verilog_lines.append("\n")
    always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
    always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
    reg_index += 1
    
    #Process Global fields
    verilog_lines.append("// Global Fields")
    remaining_bits_in_reg = dcp(register_width)
    for field,bit_length in config_data['global_fields'].items():
        if bit_length <= register_width:
            if bit_length > remaining_bits_in_reg:
                # Add sync and steady registers to the always block
                always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
                always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                set_reg_lines.append("    reg_values.append(reg_value)")
                set_reg_lines.append("    reg_value = 0\n")
                reg_index += 1
                # add_register()
                remaining_bits_in_reg = dcp(register_width)
                
            verilog_lines.append(f"assign {field} = steady_slv_reg{reg_index}[{register_width-remaining_bits_in_reg + bit_length-1}:{register_width-remaining_bits_in_reg}];")
            set_reg_lines.append(f"    #slv_reg{reg_index}")
            set_reg_lines.append(f"    reg_value |= gf_value['{field}'] << {register_width-remaining_bits_in_reg}")
            remaining_bits_in_reg -= bit_length
        else:
            # Add sync and steady registers to the always block
            always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
            always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
            set_reg_lines.append("    reg_values.append(reg_value)")
            set_reg_lines.append("    reg_value = 0\n")
            reg_index += 1
            # add_register()
            remaining_bits_in_reg = dcp(register_width)
            
            # Add sync and steady registers to the always block
            remaining_bits = bit_length
            reg_concat = []
            num_regs_for_long_data = 0
            while remaining_bits > 0:
                current_bits = min(remaining_bits, register_width)
                reg_concat.append(f"steady_slv_reg{reg_index}[{current_bits-1}:0]")
                remaining_bits -= current_bits
                # Add sync and steady registers to the always block
                always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
                always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                num_regs_for_long_data += 1
                reg_index += 1
            set_reg_lines.append(f"    multi_reg_value = gf_value['{field}']")
            for j in range(num_regs_for_long_data):
                
                set_reg_lines.append(f"    #slv_reg{reg_index-num_regs_for_long_data + j} is register {j+1} of {num_regs_for_long_data} for {field}")
                set_reg_lines.append(f"    reg_value = multi_reg_value & ((1 << {register_width}) - 1)")
                set_reg_lines.append(f"    multi_reg_value >>= {register_width}")
                set_reg_lines.append("    reg_values.append(reg_value)")
                set_reg_lines.append("    reg_value = 0\n")
            reg_concat.reverse()
            verilog_lines.append(f"assign {field} = {{{', '.join(reg_concat)}}};")
    verilog_lines.append("\n")
    
    # Define arrays for waveform fields
    for field, bit_length in config_data['global_fields'].items():
        array_definitions.append(f"wire [{bit_length-1}:0] {field};")
    for field, bit_length in config_data['waveform_fields'].items():
        array_definitions.append(f"wire [{bit_length-1}:0] {field}[{max_num_waveforms-1}:0];")
    
    
    # Process the waveform fields for each array element before moving to the next one
    verilog_lines.append("// Waveform Fields")
    
    remaining_bits_in_reg = dcp(register_width)
    for i in range(max_num_waveforms):
        for field, bit_length in config_data['waveform_fields'].items():
            if bit_length <= register_width:
                if bit_length > remaining_bits_in_reg:
                    # Add sync and steady registers to the always block
                    always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
                    always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                    set_reg_lines.append("    reg_values.append(reg_value)")
                    set_reg_lines.append("    reg_value = 0\n")
                    reg_index += 1
                    remaining_bits_in_reg = dcp(register_width)
                    
                verilog_lines.append(f"assign {field}[{i}] = steady_slv_reg{reg_index}[{register_width-remaining_bits_in_reg + bit_length-1}:{register_width-remaining_bits_in_reg}];")
                set_reg_lines.append(f"    #slv_reg{reg_index}")
                set_reg_lines.append(f"    reg_value |= wf_value[{i}]['{field}'] << {register_width-remaining_bits_in_reg}")
                remaining_bits_in_reg -= bit_length
            else:
                # Add sync and steady registers to the always block
                always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
                always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                set_reg_lines.append("    reg_values.append(reg_value)")
                set_reg_lines.append("    reg_value = 0\n")
                reg_index += 1
                remaining_bits_in_reg = dcp(register_width)
                
                # Add sync and steady registers to the always block
                remaining_bits = bit_length
                reg_concat = []
                num_regs_for_long_data = 0
                while remaining_bits > 0:
                    current_bits = min(remaining_bits, register_width)
                    reg_concat.append(f"steady_slv_reg{reg_index}[{current_bits-1}:0]")
                    remaining_bits -= current_bits
                    # Add sync and steady registers to the always block
                    always_lines.append(f"    sync_slv_reg{reg_index} <= slv_reg{reg_index};")
                    always_lines.append(f"    steady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                    num_regs_for_long_data += 1
                    reg_index += 1
                set_reg_lines.append(f"    multi_reg_value = wf_value[{i}]['{field}']")
                for j in range(num_regs_for_long_data):
                    set_reg_lines.append(f"    #slv_reg{reg_index-num_regs_for_long_data + j} is register {j+1} of {num_regs_for_long_data} for {field}")
                    set_reg_lines.append(f"    reg_value = multi_reg_value & ((1 << {register_width}) - 1)")
                    set_reg_lines.append(f"    multi_reg_value >>= {register_width}")
                    set_reg_lines.append("    reg_values.append(reg_value)")
                    set_reg_lines.append("    reg_value = 0\n")
                reg_concat.reverse()
                verilog_lines.append(f"assign {field}[{i}] = {{{', '.join(reg_concat)}}};")
        verilog_lines.append("\n")
    always_lines.append("end")  # End of always block
    
    # Combine all parts into the final Verilog file content
    final_verilog = []
    for i in range(reg_index):
        final_verilog.append(f"reg [C_S_AXI_DATA_WIDTH-1:0] sync_slv_reg{i}, steady_slv_reg{i};")
    final_verilog.append('\n')
    final_verilog += always_lines + [''] + array_definitions + [''] + verilog_lines
    
    # Write the Verilog to a file
    with open(filename + '.v', 'w') as f:
        f.write('\n'.join(final_verilog))

    #Write script to pack and map each value to the proper register
    set_reg_lines.append("\n    return reg_values")
    set_reg_lines.append("\nif __name__ == '__main__':\n    output = main()\n    print(output)")
    
    with open(filename + '_set_registers.py', 'w') as f:
        f.write('\n'.join(set_reg_lines))
    
    # Create a verilog test bench file (optional)
    if is_tb:
        tb_lines = []
        for i in range(reg_index):
            tb_lines.append(f'reg [C_S_AXI_DATA_WIDTH-1:0] slv_reg{i};')
        tb_lines.append('\n')
        result = subprocess.run(['py', './' + filename + '_set_registers.py'], capture_output=True, text=True)
        reg_values = eval(result.stdout.strip())
        tb_lines.append("initial begin")
        for i in range(0,reg_index):
            tb_lines.append(f"    slv_reg{i} <= {reg_values[i]};")
        tb_lines.append("end")
        # Write the testbench Verilog to a file
        with open(filename + '_tb.v', 'w') as f:
            f.write('\n'.join(tb_lines + [''] + final_verilog))

    

            
if __name__ == '__main__':
    main()

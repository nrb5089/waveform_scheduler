import json
from copy import deepcopy as dcp

def main():
    
    # Sample JSON data
    config_data = json.load(open('config_example.json', 'r'))
    config_data = {
        'parameters': {'REGISTER_WIDTH': 32, 'REGISTER_ADDR_WIDTH': 10},
        'global_fields': {
            'START_STOP_CTRL': 1,
            'SCHEDULER_RESET_N': 1,
            'NUM_WF': 2,  # This value will be used to determine array lengths
            'NUM_WF_SEQ': 8,
            'IS_RANDOM': 1,
            'WF_SEQ': 11,
        },
        'waveform_fields': {
            'WAVEFORM_INDEX': 8,
            'NUM_PULSE_PER_BURST': 16,
            'MOD_POLARITY': 1,
            'SINGLE_OR_BURST': 1,
            'WAVEFORM_TYPE': 2,
            'NUM_CLK_CYCLES_PRI': 32,
            'NUM_CLK_CYCLES_ON': 32,
            'PHZ_INC_START': 16,
            'PHZ_INC_START_1':16,
            'PHZ_INC_OFFSET': 16,
            'NUM_CLK_CYCLES_BW_MOD': 16,
            'PHZ_INC_INC': 16,
            'BPSK_SEQ': 256,
        }
    }
    
    value_data = {
        'global_fields': {
            'NUM_WF': 3,  # This value will be used to determine array lengths
            'NUM_WF_SEQ': 6,
            'IS_RANDOM': 0,
            'WF_SEQ': [0,1,2,2,1,0],
        },
        'waveform_fields': {
            { 
            'WAVEFORM_INDEX': 0,
            'NUM_PULSE_PER_BURST': 50,
            'MOD_POLARITY': 1,
            'SINGLE_OR_BURST': 0,
            'WAVEFORM_TYPE': 0,
            'NUM_CLK_CYCLES_PRI': 500,
            'NUM_CLK_CYCLES_ON': 250,
            'PHZ_INC_START': 1999,
            'PHZ_INC_OFFSET': 0,
            'NUM_CLK_CYCLES_BW_MOD': 0,
            'PHZ_INC_INC': 0,
            'BPSK_SEQ': []},
            { 
            'WAVEFORM_INDEX': 1,
            'NUM_PULSE_PER_BURST': 1,
            'MOD_POLARITY': 1,
            'SINGLE_OR_BURST': 1,
            'WAVEFORM_TYPE': 1,
            'NUM_CLK_CYCLES_PRI': 5000,
            'NUM_CLK_CYCLES_ON': 2500,
            'PHZ_INC_START': 1999,
            'PHZ_INC_OFFSET': 0,
            'NUM_CLK_CYCLES_BW_MOD': 1,
            'PHZ_INC_INC': 7,
            'BPSK_SEQ': []},
            { 
            'WAVEFORM_INDEX': 2,
            'NUM_PULSE_PER_BURST': 1,
            'MOD_POLARITY': 1,
            'SINGLE_OR_BURST': 1,
            'WAVEFORM_TYPE': 2,
            'NUM_CLK_CYCLES_PRI': 5000,
            'NUM_CLK_CYCLES_ON': 3250,
            'PHZ_INC_START': 1999,
            'PHZ_INC_OFFSET': 0,
            'NUM_CLK_CYCLES_BW_MOD': 250,
            'PHZ_INC_INC': 13,
            'BPSK_SEQ': [1,1,1,1,1,0,0,1,1,0,1,0,1]
            }
        }
    }
    # Generate the Verilog file
    generate_verilog(config_data, value_data, is_tb = True)
    
def generate_verilog(config_data,value_data, is_tb = False, filename = 'myfile'):
    register_width = config_data['parameters']['REGISTER_WIDTH']
    num_wf = config_data['global_fields']['NUM_WF']  # Number of waveforms
    array_length = 2**num_wf  # Array length for waveform fields
    
    verilog_lines = []
    always_lines = []
    array_definitions = []
    
    # Initialize always block for all sync and steady registers
    always_lines.append("always @(posedge DAC_CLK) begin")

    # Process global fields first
    reg_index = 0
    verilog_lines.append("// Control Fields")
    verilog_lines.append(f"wire [0:0] START_STOP_CTRL; assign START_STOP_CTRL = steady_slv_reg{reg_index}[0:0];")
    verilog_lines.append(f"wire [0:0] SCHEDULER_RESET_N; assign SCHEDULER_RESET_N = steady_slv_reg{reg_index}[1:1];\n\n// Global Scheduler Fields")
    always_lines.append(f"\tsync_slv_reg{reg_index} <= slv_reg{reg_index};")
    always_lines.append(f"\tsteady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
    
    reg_index += 1
    verilog_lines.append(f"wire [7:0] NUM_WF; assign NUM_WF = steady_slv_reg{reg_index}[7:0];")
    verilog_lines.append(f"wire [7:0] NUM_WF_SEQ; assign NUM_WF_SEQ = steady_slv_reg{reg_index}[15:8];")
    verilog_lines.append(f"wire [0:0] IS_RANDOM; assign IS_RANDOM = steady_slv_reg{reg_index}[16:16];")
    verilog_lines.append(f"wire [10:0] WF_SEQ; assign WF_SEQ = steady_slv_reg{reg_index}[27:17];\n\n// Waveform Specific Fields")
    always_lines.append(f"\tsync_slv_reg{reg_index} <= slv_reg{reg_index};")
    always_lines.append(f"\tsteady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
    
    reg_index += 1
    
    # Define arrays for waveform fields
    for field, bit_length in config_data['waveform_fields'].items():
        array_definitions.append(f"wire [{bit_length-1}:0] {field}[{array_length-1}:0];")
    
    
    # Process the waveform fields for each array element before moving to the next one
    array_length = 2**num_wf
    remaining_bits_in_reg = dcp(register_width)
    for i in range(array_length):
        for category in ['waveform_fields']:
            fields = config_data[category]
            for field, bit_length in fields.items():
                if bit_length <= register_width:
                    if bit_length > remaining_bits_in_reg:
                        # Add sync and steady registers to the always block
                        always_lines.append(f"\tsync_slv_reg{reg_index} <= slv_reg{reg_index};")
                        always_lines.append(f"\tsteady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                        reg_index += 1
                        
                        remaining_bits_in_reg = dcp(register_width)
                    verilog_lines.append(f"wire [{bit_length-1}:0] {field}[{i}]; assign {field}[{i}] = steady_slv_reg{reg_index}[{register_width-remaining_bits_in_reg + bit_length-1}:{register_width-remaining_bits_in_reg}];")
                    remaining_bits_in_reg -= bit_length
                    #verilog_lines.append(f"wire [{bit_length-1}:0] {field}[{i}]; assign {field}[{i}] = steady_slv_reg{reg_index}[{bit_length-1}:0];")
                else:
                    # Add sync and steady registers to the always block
                    always_lines.append(f"\tsync_slv_reg{reg_index} <= slv_reg{reg_index};")
                    always_lines.append(f"\tsteady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                    reg_index += 1
                    # Add sync and steady registers to the always block
                    remaining_bits = bit_length
                    reg_concat = []
                    while remaining_bits > 0:
                        current_bits = min(remaining_bits, register_width)
                        reg_concat.append(f"steady_slv_reg{reg_index}[{current_bits-1}:0]")
                        remaining_bits -= current_bits
                        # Add sync and steady registers to the always block
                        always_lines.append(f"\tsync_slv_reg{reg_index} <= slv_reg{reg_index};")
                        always_lines.append(f"\tsteady_slv_reg{reg_index} <= sync_slv_reg{reg_index};")
                        reg_index += 1
                    reg_concat.reverse()
                    verilog_lines.append(f"wire [{bit_length-1}:0] {field}[{i}]; assign {field}[{i}] = {{{', '.join(reg_concat)}}};")
                
                
                
                #reg_index += 1
    
    always_lines.append("end")  # End of always block
    
    # Combine all parts into the final Verilog file content
    final_verilog = []
    for i in range(reg_index):
        final_verilog.append(f"reg [{register_width-1}:0] sync_slv_reg{i}, steady_slv_reg{i};")
    final_verilog.append('\n')
    final_verilog += always_lines + [''] + array_definitions + [''] + verilog_lines
    
    # Write the Verilog to a file
    with open(filename +'.v', 'w') as f:
        f.write('\n'.join(final_verilog))

    if is_tb:
        tb_lines = []
        for i in range(reg_index):
            tb_lines.append(f'reg [{register_width-1}:0] slv_reg{i};')
        tb_lines.append('\n')
        # Write the testbench Verilog to a file
        with open(filename + '_tb.v', 'w') as f:
            f.write('\n'.join(tb_lines + [''] + final_verilog))
            
            
            
if __name__ == '__main__':
    main()


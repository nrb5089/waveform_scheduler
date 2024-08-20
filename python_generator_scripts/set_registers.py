import subprocess
import struct
import json

# Function to write a value to a register at a given address
def write_register(addr, value):
    subprocess.run(['devmem', addr, '32', value], check=True)

value_data = json.load(open('value_example.json','r'))
num_control_reg = 1 #First offset after control register
reg_values = []
gf_value = value_data['global_fields']
wf_value = value_data['waveform_fields']


def main():
    return set_reg_values()

def set_reg_values():
    reg_value = 0

    reg_value |= gf_value['NUM_WF'] << 0
    reg_value |= gf_value['NUM_WF_SEQ'] << 2
    reg_value |= gf_value['IS_RANDOM'] << 10
    reg_value |= gf_value['WF_SEQ'] << 11
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[0]['WAVEFORM_INDEX'] << 0
    reg_value |= wf_value[0]['NUM_PULSE_PER_BURST'] << 8
    reg_value |= wf_value[0]['MOD_POLARITY'] << 24
    reg_value |= wf_value[0]['SINGLE_OR_BURST'] << 25
    reg_value |= wf_value[0]['WAVEFORM_TYPE'] << 26
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[0]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[0]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[0]['PHZ_INC_START'] << 0
    reg_value |= wf_value[0]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[0]['NUM_CLK_CYCLES_BW_MOD'] << 0
    reg_value |= wf_value[0]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[0]['BPSK_SEQ']
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[1]['WAVEFORM_INDEX'] << 0
    reg_value |= wf_value[1]['NUM_PULSE_PER_BURST'] << 8
    reg_value |= wf_value[1]['MOD_POLARITY'] << 24
    reg_value |= wf_value[1]['SINGLE_OR_BURST'] << 25
    reg_value |= wf_value[1]['WAVEFORM_TYPE'] << 26
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[1]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[1]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[1]['PHZ_INC_START'] << 0
    reg_value |= wf_value[1]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[1]['NUM_CLK_CYCLES_BW_MOD'] << 0
    reg_value |= wf_value[1]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[1]['BPSK_SEQ']
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[2]['WAVEFORM_INDEX'] << 0
    reg_value |= wf_value[2]['NUM_PULSE_PER_BURST'] << 8
    reg_value |= wf_value[2]['MOD_POLARITY'] << 24
    reg_value |= wf_value[2]['SINGLE_OR_BURST'] << 25
    reg_value |= wf_value[2]['WAVEFORM_TYPE'] << 26
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[2]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[2]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[2]['PHZ_INC_START'] << 0
    reg_value |= wf_value[2]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[2]['NUM_CLK_CYCLES_BW_MOD'] << 0
    reg_value |= wf_value[2]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[2]['BPSK_SEQ']
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[3]['WAVEFORM_INDEX'] << 0
    reg_value |= wf_value[3]['NUM_PULSE_PER_BURST'] << 8
    reg_value |= wf_value[3]['MOD_POLARITY'] << 24
    reg_value |= wf_value[3]['SINGLE_OR_BURST'] << 25
    reg_value |= wf_value[3]['WAVEFORM_TYPE'] << 26
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[3]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[3]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[3]['PHZ_INC_START'] << 0
    reg_value |= wf_value[3]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    reg_value |= wf_value[3]['NUM_CLK_CYCLES_BW_MOD'] << 0
    reg_value |= wf_value[3]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[3]['BPSK_SEQ']
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0


    return reg_values

if __name__ == '__main__':
    output = main()
    print(output)
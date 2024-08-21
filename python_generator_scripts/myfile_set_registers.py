import subprocess
import struct
import json

# Function to write a value to a register at a given address
def write_register(addr, value):
    subprocess.run(['devmem', addr, '32', value], check=True)

value_data = json.load(open('value_example.json','r'))
num_control_reg = 1 #First offset after control register
reg_values = [0] #Placehold for Control Register
gf_value = value_data['global_fields']
wf_value = value_data['waveform_fields']


def main():
    return set_reg_values()

def set_reg_values():
    reg_value = 0

    #slv_reg1
    reg_value |= gf_value['NUM_WF'] << 0
    #slv_reg1
    reg_value |= gf_value['NUM_WF_SEQ'] << 2
    #slv_reg1
    reg_value |= gf_value['IS_RANDOM'] << 10
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = gf_value['WF_SEQ']
    #slv_reg2 is register 1 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg3 is register 2 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg4 is register 3 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg5 is register 4 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg6 is register 5 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg7 is register 6 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg8 is register 7 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg9 is register 8 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg10 is register 9 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg11 is register 10 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg12 is register 11 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg13 is register 12 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg14 is register 13 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg15 is register 14 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg16 is register 15 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg17 is register 16 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg18 is register 17 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg19 is register 18 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg20 is register 19 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg21 is register 20 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg22 is register 21 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg23 is register 22 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg24 is register 23 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg25 is register 24 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg26 is register 25 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg27 is register 26 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg28 is register 27 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg29 is register 28 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg30 is register 29 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg31 is register 30 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg32 is register 31 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg33 is register 32 of 32 for WF_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg34
    reg_value |= wf_value[0]['WAVEFORM_INDEX'] << 0
    #slv_reg34
    reg_value |= wf_value[0]['NUM_PULSE_PER_BURST'] << 4
    #slv_reg34
    reg_value |= wf_value[0]['MOD_POLARITY'] << 20
    #slv_reg34
    reg_value |= wf_value[0]['SINGLE_OR_BURST'] << 21
    #slv_reg34
    reg_value |= wf_value[0]['WAVEFORM_TYPE'] << 22
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg35
    reg_value |= wf_value[0]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg36
    reg_value |= wf_value[0]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg37
    reg_value |= wf_value[0]['PHZ_INC_START'] << 0
    #slv_reg37
    reg_value |= wf_value[0]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg38
    reg_value |= wf_value[0]['NUM_CLK_CYCLES_BW_MOD'] << 0
    #slv_reg38
    reg_value |= wf_value[0]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[0]['BPSK_SEQ']
    #slv_reg39 is register 1 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg40 is register 2 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg41 is register 3 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg42 is register 4 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg43 is register 5 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg44 is register 6 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg45 is register 7 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg46 is register 8 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg47
    reg_value |= wf_value[1]['WAVEFORM_INDEX'] << 0
    #slv_reg47
    reg_value |= wf_value[1]['NUM_PULSE_PER_BURST'] << 4
    #slv_reg47
    reg_value |= wf_value[1]['MOD_POLARITY'] << 20
    #slv_reg47
    reg_value |= wf_value[1]['SINGLE_OR_BURST'] << 21
    #slv_reg47
    reg_value |= wf_value[1]['WAVEFORM_TYPE'] << 22
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg48
    reg_value |= wf_value[1]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg49
    reg_value |= wf_value[1]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg50
    reg_value |= wf_value[1]['PHZ_INC_START'] << 0
    #slv_reg50
    reg_value |= wf_value[1]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg51
    reg_value |= wf_value[1]['NUM_CLK_CYCLES_BW_MOD'] << 0
    #slv_reg51
    reg_value |= wf_value[1]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[1]['BPSK_SEQ']
    #slv_reg52 is register 1 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg53 is register 2 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg54 is register 3 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg55 is register 4 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg56 is register 5 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg57 is register 6 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg58 is register 7 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg59 is register 8 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg60
    reg_value |= wf_value[2]['WAVEFORM_INDEX'] << 0
    #slv_reg60
    reg_value |= wf_value[2]['NUM_PULSE_PER_BURST'] << 4
    #slv_reg60
    reg_value |= wf_value[2]['MOD_POLARITY'] << 20
    #slv_reg60
    reg_value |= wf_value[2]['SINGLE_OR_BURST'] << 21
    #slv_reg60
    reg_value |= wf_value[2]['WAVEFORM_TYPE'] << 22
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg61
    reg_value |= wf_value[2]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg62
    reg_value |= wf_value[2]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg63
    reg_value |= wf_value[2]['PHZ_INC_START'] << 0
    #slv_reg63
    reg_value |= wf_value[2]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg64
    reg_value |= wf_value[2]['NUM_CLK_CYCLES_BW_MOD'] << 0
    #slv_reg64
    reg_value |= wf_value[2]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[2]['BPSK_SEQ']
    #slv_reg65 is register 1 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg66 is register 2 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg67 is register 3 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg68 is register 4 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg69 is register 5 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg70 is register 6 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg71 is register 7 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg72 is register 8 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg73
    reg_value |= wf_value[3]['WAVEFORM_INDEX'] << 0
    #slv_reg73
    reg_value |= wf_value[3]['NUM_PULSE_PER_BURST'] << 4
    #slv_reg73
    reg_value |= wf_value[3]['MOD_POLARITY'] << 20
    #slv_reg73
    reg_value |= wf_value[3]['SINGLE_OR_BURST'] << 21
    #slv_reg73
    reg_value |= wf_value[3]['WAVEFORM_TYPE'] << 22
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg74
    reg_value |= wf_value[3]['NUM_CLK_CYCLES_PRI'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg75
    reg_value |= wf_value[3]['NUM_CLK_CYCLES_ON'] << 0
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg76
    reg_value |= wf_value[3]['PHZ_INC_START'] << 0
    #slv_reg76
    reg_value |= wf_value[3]['PHZ_INC_OFFSET'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg77
    reg_value |= wf_value[3]['NUM_CLK_CYCLES_BW_MOD'] << 0
    #slv_reg77
    reg_value |= wf_value[3]['PHZ_INC_INC'] << 16
    reg_values.append(reg_value)
    reg_value = 0

    multi_reg_value = wf_value[3]['BPSK_SEQ']
    #slv_reg78 is register 1 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg79 is register 2 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg80 is register 3 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg81 is register 4 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg82 is register 5 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg83 is register 6 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg84 is register 7 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0

    #slv_reg85 is register 8 of 8 for BPSK_SEQ
    reg_value = multi_reg_value & ((1 << 32) - 1)
    multi_reg_value >>= 32
    reg_values.append(reg_value)
    reg_value = 0


    return reg_values

if __name__ == '__main__':
    output = main()
    print(output)
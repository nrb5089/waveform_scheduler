# Description

Edit the ```config_example.json``` directly as a template.  Add fields as necessary, the value corresponds to the number of bits required for that field.  This is loaded as the configuration file.

Use custom scripts to generate the values file, an example is found in ```value_example.json```.

```process_jsons.py``` ingests these .json files above and generates up to three files named after ```filename``` field
    1. ```<filename>.v```
        - Verilog file that assigns wires named after fields in .jsons to register space
    2. ```<filename>_set_registers.py```
        - Python file that returns the values that each register should be set, note that register 0 is the control register, and the values correspond to register 1 onward.
    3. ```<filename>_tb.v``` (Optional)
        - Test bench that runs ```<filename>_set_registers.py``` intermittently to put example values in a test bench for ```<filename>.v```
        
# Example
    
    Run ```process_jsons.py``` and then run the ```<filename>_set_registers.py``` which will print the values for each register required.
    
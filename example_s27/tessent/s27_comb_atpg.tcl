set_context pattern -scan

# read the verilog file and define the top-level module
read_verilog ../verilog/s27_comb.v
set_current_design s27_comb

# put Tessent into pattern generation mode
set_system_mode analysis

# add all stuck-at faults to the design
add_faults -all

# generate patterns
create_patterns

# write the patterns to a file with ASCII format
write_patterns s27_comb_tests.ascii -replace

# write the faults to a file
report_faults > s27_comb.faults

exit -d

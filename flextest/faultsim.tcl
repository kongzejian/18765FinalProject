add clocks 0 CK

set test cycle 2
setup pin strobes 1

set system mode fault

set pattern source external <YOUR_PATTERNS>.ascii

set hypertrophic limit off
load faults s9234.faults

run

report statistics
write faults s9234_faults.rpt -replace

exit
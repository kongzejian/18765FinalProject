import textwrap
import sys
import optparse

def main():
    '''calls functions, etc'''
    # optparse used to accept arguments
    prog = "etr_to_ascii.py"
    usagedef = "usage: ./%prog "
    usageord = "infile(etr) outfilename(ascii)"
    usage = usagedef + usageord
    version = "%prog 1.0"

    parser = optparse.OptionParser(usage=usage, version=version)
    (options, args) = parser.parse_args()

    infile  = args[0]
    outfile = args[1]

    vectors = 0
    input_flag = 0
    output_flag = 0
    inputs = []
    outputs = []
    clocks = []
    input_vector = []
    output_vector = []
    pattern_count = 0
    primary_ins, primary_outs = False, False
    float_ins, float_outs = False, False
    total_str = ''

    writefd = open(outfile, 'w', 16777216)
    readfd = open(infile, "r", 16777216)

    line = readfd.readline()

    #with open(infile, "r") as infd:
    while line:
        if vectors == 0:

            if "CLOCKS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                for item in line:
                    item = item.replace(' ', '')
                    inputs.append(item.replace('\n', ''))
                    clocks.append(item.replace('\n', ''))

            if "CONTROLS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                for item in line:
                    item = item.replace(' ', '')
                    inputs.append(item.replace('\n', ''))

            if "SCAN_INS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                for item in line:
                    item = item.replace(' ', '')
                    inputs.append(item.replace('\n', ''))

            if "SCAN_OUTS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                for item in line:
                    item = item.replace(' ', '')
                    outputs.append(item.replace('\n', ''))

            if "PRIMARY_INPUTS:" in line:
                if input_flag == 0:
                    index_c = line.index(":")
                    line = line[index_c + 1:]
                    line = line.split(",")
                    for item in line:
                        item = item.replace(' ', '')
                        inputs.append(item.replace('\n', ''))
                    input_flag = 1
                elif "PRIMARY_OUTPUTS:" not in line:
                    line = line.split(",")
                    for item in line:
                        item = item.replace(' ', '')
                        inputs.append(item.replace('\n', ''))
                else:
                    input_flag = 0

            if "PRIMARY_OUTPUTS:" in line:
                if output_flag == 0:
                    index_c = line.index(":")
                    line = line[index_c + 1:]
                    line = line.split(",")
                    for item in line:
                        item = item.replace(' ', '')
                        outputs.append(item.replace('\n', ''))
                    input_flag = 1
                elif "**SCAN_CHAIN scan" not in line and "," in line:
                    line = line.split(",")
                    for item in line:
                        item = item.replace(' ', '')
                        outputs.append(item.replace('\n', ''))
                else:
                    output_flag = 0

            if "FLOAT_INS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                if len(line) > 0:
                    float_ins = True
                for item in line:
                    item = item.replace(' ', '')
                    inputs.append(item.replace('\n', ''))

            if "FLOAT_OUTS:" in line:
                index_c = line.index(":")
                line = line[index_c + 1:]
                line = line.split(",")
                if len(line) > 0:
                    float_outs = True
                for item in line:
                    item = item.replace(' ', '')
                    outputs.append(item.replace('\n', ''))

            #skip the first vector
            if "1:" in line:
                vectors = 1
                #write headers and inputs to file
                writefd.write("SETUP =\n	TEST_CYCLE_WIDTH=2;\n")
                #define PIs
                write_str = '     DECLARE INPUT BUS "ibus" ='
                for pi in inputs:
                    write_str = write_str + ' "/' + pi  + '",'
                write_str = write_str[:-1] + ';\n\n'
                writefd.write(write_str)

                #define POs
                write_str = '     DECLARE OUTPUT BUS "obus" ='
                for po in outputs:
                    write_str = write_str + ' "/' + po  + '",'

                write_str = write_str[:-1] + ';\n\n'
                writefd.write(write_str)

                # for clk in clocks:
                # 	write_str = 'clock "/' + clk + '" =\n' + "      off_state   = 0;\n"+ "     pulse_width = 1;\n" + " end;\n"
                # 	writefd.write(write_str)
                writefd.write("\nEND;\nCYCLE_TEST =\n\n")

                #writefd.close()

        if vectors == 1 and ":" in line:
            line = line.split()
            #inputs = ctl + scan_in + clk + PIN
            if line[1] == "P":
                # timeframe 1
                clocks_str1 = '0'*len(clocks)
                clocks_str2 = '1'*len(clocks)
                control_str = line[2]
                scanin_str = line[3]
                scanout_str = line[4]

                i = 5
                pi_str = ''
                if primary_ins:
                    pi_str = line[i]
                    i += 1

                po_str = ''
                if primary_outs:
                    po_str = line[i]
                    i += 1

                fi_str = ''
                if float_ins:
                    fi_str = line[i]
                    i += 1

                fo_str = ''
                if float_outs:
                    fo_str = line[i]
                    i += 1

                input_str1 = clocks_str1 + control_str + scanin_str + pi_str + fi_str
                input_str2 = clocks_str2 + control_str + scanin_str + pi_str + fi_str
                input_str1 = input_str1.replace('Z', 'X')
                input_str2 = input_str2.replace('Z', 'X')

                output_str = scanout_str + po_str + fo_str
                output_str = output_str.replace('H','1')
                output_str = output_str.replace('L','0')

                input_vector.append(input_str1)
                input_vector.append(input_str2)
                #if there is an output, write inputs and outputs to ascii file
                #if (output_str.count('0') + output_str.count('1')) > 0:
                write_str ="    CYCLE = "+ str(pattern_count) + ";\n"
                sub_count = 0;

                pattern_count = pattern_count + 1
                #write input vectors
                for i in range (0, len(input_vector)):
                    #print input_vector[i]
                    in_str = textwrap.wrap(input_vector[i], 50)
                    #print in_str
                    if len(in_str) == 1:
                        write_str = write_str + '    force   "ibus" "' + in_str[0] + '" '+str(sub_count) + ';\n'
                    elif len(in_str) > 1:
                        write_str = write_str + '    force   "ibus" "' + in_str[0] + '\\'

                        for j in range(1, len(in_str)):
                            if (j !=  len(in_str) - 1):
                                write_str = write_str + '\n                  ' + in_str[j] +'\\'
                            else:
                                write_str = write_str + '\n                  ' +in_str[j]+'" ' + str(sub_count)+ ';\n'

                    sub_count = sub_count + 1


                output_pat = textwrap.wrap(output_str, 50)

                if len(output_pat) == 1:
                    write_str = write_str + '    measure "obus" "' + output_pat[0]+ '" '+ str(sub_count)+';\n\n'
                if len(output_pat) > 1:
                    write_str = write_str +'    measure "obus" "'+output_pat[0]+'\\'

                    for j in range(1, len(output_pat)):
                        if (j !=  len(output_pat) - 1):
                            write_str = write_str + '\n                  '+output_pat[j]+'\\'
                        else:
                            write_str = write_str + '\n                  '+ output_pat[j] +'" '+ str(sub_count)+ ';\n\n'
                sub_count = sub_count + 1

                writefd.write(write_str)
                #total_str = total_str + write_str
                input_vector = []
                #output_vector = []
        # elif vectors == 1 and "**" in line:
        # 	input_vector = []

        line = readfd.readline()

    #writefd.write(write_str)
    writefd.write('\nend;')
    writefd.close()


if __name__ == '__main__':
    main()

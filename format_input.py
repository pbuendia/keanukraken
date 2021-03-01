import argparse
import sys


def add_count(data_l):
    if data_l[0] in counts:
        if data_l[1] in counts[data_l[0]]:
            counts[data_l[0]][data_l[1]] += 1
        else:
            counts[data_l[0]][data_l[1]] = 1
    else:
        counts[data_l[0]] = {data_l[1]: 1}


def get_max_count():
    if len(counts.values()) > 0:
        return len(list(counts.keys())) + 1
    else:
        return 0


parser = argparse.ArgumentParser(description="A tool to format BLAST qseqid/staxid files into Keanu's input")
parser.add_argument("-in", "--input", help="BLAST query/taxon data")
parser.add_argument("-out", "--output", help="Output filename")

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

check_index = 0
type_flag = True
counts = {}

with open(args.input) as query_taxid_file:
    for line in query_taxid_file:
        data = line.strip("\n").split("\t")

        if check_index == 0:
            check_index += 1
            if int(data[0]) != 0:
                type_flag = False
        if type_flag:
            add_count(data)
        else:
            for key in range(int(data[0])):
                add_count([str(get_max_count()), str(data[1])])

with open(args.output, 'w') as output_file:
    for each in counts:
        taxid_counts = counts[each]
        line = each + "\t"
        for taxid in taxid_counts:
            line += taxid + " [" + str(taxid_counts[taxid]) + "], " + taxid + " [" + str(taxid_counts[taxid]) + "], "
        output_file.write(line.strip(" ,") + "\n")

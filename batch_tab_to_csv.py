# Copyright (C) 2014 Thomas Roberts <thomasjpr@thomasjpr.com>
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or 
# implied warranty.

# Batch covert a directory of txt files (tab-delimited) to csv. Just say no to Excel. 
# Designed to be run from the command line

import csv
import glob
import os

directory = raw_input("INPUT [directory of files for conversion:]")
output = raw_input("OUTPUT [directory to store the converted files:]")

txt_files = os.path.join(directory, '*.txt')

for txt_file in glob.glob(txt_files):
    with open(txt_file, "rb") as input_file:
        in_txt = csv.reader(input_file, delimiter='\t')
        filename = os.path.splitext(os.path.basename(txt_file))[0] + '.csv'

        with open(os.path.join(output, filename), 'wb') as output_file:
            out_csv = csv.writer(output_file)
            out_csv.writerows(in_txt)
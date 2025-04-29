#!/usr/bin/env python3
import argparse
import time
import os

# Define argument parser
parser = argparse.ArgumentParser(description="Process dataset files")

# Add arguments
parser.add_argument("--output_dir", "-o", dest="output_dir", type=str, help="output directory where files will be saved")
parser.add_argument("--name", "-n", dest="name", type=str, help="name of the dataset")
parser.add_argument("--data.counts", dest="data_counts", type=str, help="input file #1")
parser.add_argument("--data.meta", dest="data_meta", type=str, help="input file #2")
parser.add_argument("-a", dest="arg_a", help="extra argument a", default="0")
parser.add_argument("-b", dest="arg_b", help="extra argument b", default="0")
parser.add_argument("--sleep", dest="sleep", type=int, help="sleep for n seconds", default=0)

# Parse command-line arguments
opt = parser.parse_args()

# Check if mandatory arguments are provided
if not opt.output_dir or not opt.name:
    raise ValueError("Error: --output_dir or --name are required.")

time.sleep(opt.sleep)

output_dir = opt.output_dir
name = opt.name
data_counts_input = opt.data_counts
data_meta_input = opt.data_meta
input_files = [file for file in [data_counts_input, data_meta_input] if file is not None]
a = float(opt.arg_a)
b = float(opt.arg_b)

# Combine content from all input files
processed_content = []
for input_file in input_files:
    # Read content of each input file
    with open(input_file, 'r') as f:
        file_content = f.read().splitlines()
    # Append content to the combined content list
    processed_content.extend(file_content)

# Write combined content to a file in the output directory
process_filtered_file = os.path.join(output_dir, f"{name}.txt.gz")

module_message = f"\n2. Preprocessing dataset files using parameters '-a {a} -b {b}' into {process_filtered_file}"
processed_content.append(module_message)

with open(process_filtered_file, 'w') as f:
    for line in processed_content:
        f.write(line + '\n')

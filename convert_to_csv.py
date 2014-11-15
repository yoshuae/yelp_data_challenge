""" Convert the dataset into csv for ease of use.
    http://www.yelp.com/dataset_challenge 
"""

import json 
import argparse
import pandas as np

def parse_json(file_path):
    return [json.loads(line) for line in open(file_path)]

def create_CSV(records, outputfile_path):
    data_frame = np.DataFrame(records)
    data_frame.to_csv(outputfile_path, index=False)
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Script to convert yelp dataset challenge json files into csv")

    parser.add_argument("JSON_file", help="JSON file to convert into CSV")
    parser.add_argument("output_name", help="Output file name", nargs="*")

    args = parser.parse_args()

    records = parse_json(args.JSON_file)

    if not args.output_name:
        output = args.JSON_file[:args.JSON_file.find(".json")] + '.csv'
    else:
        output = args.output_name

    create_CSV(records, output)

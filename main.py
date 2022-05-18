import argparse
import os
import sys


def read_file():
    default_input_file = "popData.csv"
    global input_data

    # set the parser for parsing inputs on the command line
    parser = argparse.ArgumentParser(description="Receives File name input path from the CMD line")
    parser.add_argument("--testfile", required=False, help="Input the path to the test file")
    args = parser.parse_args()

    # handle exceptions
    # if a file path is inputted on the cli and the file exists on that path read it
    if args.testfile and os.path.isfile(args.testfile):
        with open(args.testfile, 'r') as csv_input:
            input_data = csv_input.readlines()

    # if there already exists a test file in the current directory, read it
    elif not len(sys.argv) > 1:
        with open(default_input_file, 'r') as csv_input:
            input_data = csv_input.readlines()

    else:
        print(str(format(args.testfile)) + " " + "does not exist", file=sys.stderr)
        sys.exit(-1)


read_file()


def edit_data():
    output_file = open('outputFile.csv', 'w')
    row_count = 0
    field_name_dict = {'Total': 'TPop', 'Male': 'MPop', 'Female': 'FPop'}
    for row in input_data:
        row_count += 1
        fields = row.split(',')
        data_rows = []
        if row_count == 1:
            header = []
            fields.insert(3, 'County')
            for field_name in fields:
                if 'Number; SEX AND AGE' in field_name:
                    field_name = field_name.replace(" ", "")
                    field_names = field_name.split('-')
                    if field_names[1] == 'Totalpopulation':
                        if len(field_names) <= 2:
                            field_name = field_name.replace(field_name, field_name_dict['Total'])
                        else:
                            field2 = field_names[2].strip('years and()')
                            if 'to' in field_names[2]:
                                last_section = field2.replace('to', '-')
                                field_name = field_name_dict['Total'] + last_section
                            if 'over' in field_names[2]:
                                last_section = field2.replace('and', '-')
                                field_name = field_name_dict['Total'] + last_section
                            if 'Under' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Total'] + last_section
                            if 'Median' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Total'] + last_section
                    elif field_names[1] == 'Malepopulation':
                        if len(field_names) <= 2:
                            field_name = field_name.replace(field_name, field_name_dict['Total'])
                        else:
                            field2 = field_names[2].strip('years and()')
                            if 'to' in field_names[2]:
                                last_section = field2.replace('to', '-')
                                field_name = field_name_dict['Male'] + last_section
                            if 'over' in field_names[2]:
                                last_section = field2.replace('and', '-')
                                field_name = field_name_dict['Male'] + last_section
                            if 'Under' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Male'] + last_section
                            if 'Median' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Male'] + last_section
                    elif field_names[1] == 'Femalepopulation':
                        if len(field_names) <= 2:
                            field_name = field_name.replace(field_name, field_name_dict['Total'])
                        else:
                            field2 = field_names[2].strip('years and()')
                            if 'to' in field_names[2]:
                                last_section = field2.replace('to', '-')
                                field_name = field_name_dict['Female'] + last_section
                            if 'over' in field_names[2]:
                                last_section = field2.replace('years', '')
                                last_section = last_section.replace('and', '-')
                                #last_section = last_section.strip('\n ')
                                field_name = field_name_dict['Female'] + last_section
                            if 'Under' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Female'] + last_section
                            if 'Median' in field_names[2]:
                                last_section = field2.replace('years', '')
                                field_name = field_name_dict['Female'] + last_section

                header.append(field_name)

        else:
            geography_index = header.index('Geography')
            fields.insert(3, fields[2])

            data_rows.append(fields)

        if row_count == 1:
            header[len(header)-1] = header[len(header)-1] + ' '

            header = str(header)
            header = header.replace("[", '')
            header = header.replace("]", '')
            header = header.replace("'", '')

            output_file.write(header)
        else:
            for r in data_rows:
                for i in r:
                    output_file.write(row)


edit_data()


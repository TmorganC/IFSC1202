def merge_files(input_filename, merge_filename, output_filename):
    # Open input file for reading
    with open(input_filename, 'r') as input_file:
        # Open merge file for reading
        with open(merge_filename, 'r') as merge_file:
            # Open output file for writing
            with open(output_filename, 'w') as output_file:
                # Initialize record counts
                input_records = 0
                merge_records = 0
                output_records = 0
                
                # Copy lines from input file to output file until "Insert Merge File Here" is found
                for line in input_file:
                    input_records += 1
                    if "**Insert Merge File Here**" in line:
                        # Copy lines from merge file to output file
                        for merge_line in merge_file:
                            merge_records += 1
                            output_file.write(merge_line)
                            output_records += 1
                        # Break out of the loop after merging the files
                        break
                    else:
                        output_file.write(line)
                        output_records += 1

                # Continue copying remaining lines from input file to output file
                for line in input_file:
                    input_records += 1
                    output_file.write(line)
                    output_records += 1

                  # Close all files
                input_file.close()
                merge_file.close()
                output_file.close()

                # Print record counts
                print(f"Input Records: {input_records}")
                print(f"Merge Records: {merge_records}")
                print(f"Output Records: {output_records}")


# Usage
input_filename = "Input File.txt"
merge_filename = "Merge File.txt"
output_filename = "Output File.txt"

merge_files(input_filename, merge_filename, output_filename)
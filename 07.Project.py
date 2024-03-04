input_file = ("07.Project Angles Input.txt")
output_file = ("07.Project Angles Output.txt")

def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)
    minute_symbol = "'"
    second_symbol = "\""

    degree_pos = ddmmss.find(degree_symbol)
    minute_pos = ddmmss.find(minute_symbol)
    second_pos = ddmmss.find(second_symbol)

    degrees = float(ddmmss[:degree_pos])
    minutes = float(ddmmss[degree_pos + 1:minute_pos])
    seconds = float(ddmmss[minute_pos + 1:second_pos])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    return decimal_degrees

def main(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
     
    with open(output_file, 'w') as outfile:
        for line in lines:
            degrees, minutes, seconds = ParseDegreeString(line.strip())
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
        outfile.write(f"{decimal_degrees:.6f}\n")

if __name__ == "__main__":
    input_file_path = "07.Project Angles Input.txt" 
    output_file_path = "07.Project Angles Output.txt" 

    main(input_file_path, output_file_path)        
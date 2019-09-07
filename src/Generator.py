"""
Interprets AHK script into keyboard-compliant Python
Features are limited
"""
import sys
import os
import re as regex

def main():
    SUBSTITUTION = regex.compile("^:\*?:.+::.+$")
    print(sys.argv[1:])
    if len(sys.argv) == 0 or not os.path.isfile(sys.argv[1]):
        print("Invalid program call")
        exit(1)
    
    with open(sys.argv[1], "r") as raw:
        # Each line is a string in the array
        lines = raw.read().split("\n")
    
    outString = "\"\"\"AUTO_GENERATED PYTHON SCRIPT\nMade using LION: https://github.com/AtkLordOverAll/LazinessIsOnlyNatural\"\"\"\nimport keyboard\n\n"
    for line in lines:
        
        # line is comment, preserve it
        if line.startswith(";"):
            outString += "\n#" + line[1:] + "\n"
        
        # line is a text substitution command
        if regex.match(SUBSTITUTION, line):
            if line[1] == "*":
                offset = 3
                match_suffix = "True"
            else:
                offset = 2
                match_suffix = "False"
            command = line[offset:].split("::")
            # TODO: Support for case insensitive binds
            lineCommand = "keyboard.add_abbreviation('" + command[0] + "', '" + command[1] + "', match_suffix = " + match_suffix + ")\n"
            print(lineCommand)
            outString += lineCommand
    
    print(outString)

if __name__ == '__main__':
    main()
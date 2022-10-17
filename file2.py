A function that uses command line arguments. This function will print two variables used, the script and then the script AND variables:
  
#!/usr/bin/env python3

import sys

def command_line_arguments():
        name = str()
        section = str()
      
        name = sys.argv[1]
        section = sys.argv[2]
        
        print(f"Element1 = {name}")
        print(f"Element2 = {section}")
        print(f"Script: {sys.argv[0]}")
        print("Script and variables are : ", sys.argv[0], name, section)
        
   if __name__ == "__main__":
     command_line_arguments()

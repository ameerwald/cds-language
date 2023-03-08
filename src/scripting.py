import argparse
#sys.path.append("utils")
#import classifier_utils

def input_parse(): # don't need to put in an argument because it goes in the command line
    #initialize the parser
    parser = argparse.ArgumentParser() 
    # add arguments
    parser.add_argument("--name", type=str, default="Beautiful") # if no name arg, will return default 
    parser.add_argument("--age", type=int, required=True) # not a default but is required 
    # parse the arguments from the command line 
    args = parser.parse_args()

    return args # need this, it acts similiar to print

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old.") # need to wrap age in a str(), so it will treat it like a string to concatenate it together 

# main function adds as primary logic 
def main():
    # run input parse to get name 
    args = input_parse()
    # pass name to hell0()
    hello(args.name,args.age)

# if .py script is called from command line, then do this, otherwise don't do anything 
# this way we can all on it later when we want to but won't print or do something we don't want  
if __name__=="__main__": 
    main()

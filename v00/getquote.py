import datetime
import os
import argparse
from me.stock_info import get_quote_table
from bluemesa.util import lineutil
from bluemesa.redis import util

## This is the group symbol file that will be processed
## Just enter a filename without the .txt extension
## from the directory symbol_dir

path = os.environ['BMTOP']

## This is the directory where symbol files are located
symbol_dir  = path + '/bluemesa/config/symbols/'

## This is the base directory of where files get written to
base_pathout = path + '/bluemesa/tmp/fun/in/'

def mkdir_ifnothere(parent_dir, dirname):
    # check to see that parent_dir exists
    # and if does not print problem and exit
    mybool = os.path.isdir(parent_dir)
    if (not mybool):
        print("mkdir_ifnothere: parent directory does not exist exiting process")
        exit()
    # Path
    path = os.path.join(parent_dir, dirname)
    mybool = os.path.isdir(path)
    # check to see if dirname exists
    # and if it does then do not create a new directory
    if (not mybool):
        os.mkdir(path)
    path = path + '/'
    return(path)

def get_day():
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d")
    return y

def build_file_name(symbol):
    day = get_day()
    filename = f"{symbol}-fun-{day}.csv"
    return(filename)

def process(symbols,path,key):
    for symbol in symbols:
        filename = build_file_name(symbol)
        bool = util.redis_set_read(key,symbol)
        if not bool:
            print(symbol)
            data = get_quote_table(symbol)
            out_file = path + filename
            print(data['Market Cap'])
#           data.to_csv(out_file)
#           util.redis_set_write(key,symbol)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("groupname")
    args = parser.parse_args()
    groupname = args.groupname
    filename = groupname + '.txt'

    # This is the actual symbol file name
    symbol_file = symbol_dir + filename

    symbols = lineutil.get_lines_as_set(symbol_file)
    path_out = mkdir_ifnothere(base_pathout,groupname)
    redis_check_key = "symbol-check-" + groupname
    process(symbols,path_out,redis_check_key)

# The variable symbols is always a Python set which is nice
# because then we will not get any duplication of data
# symbols = {"ui","psa","ip","t"}
# symbols.add("nly")

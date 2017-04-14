import sys
import os
import glob

def clean_files(working_dir):
    os.chdir(working_dir)
    cmd = "sudo rm -f *.exe ; sudo rm -f .*.exe ; sudo rm -f autorun.inf ; sudo rm -rf Recycled*"
    os.system(cmd)

def arrange_dirs(working_dir):
    dirs = glob.glob("{}/*/".format(working_dir))
    for mydir in dirs:
        mydir = mydir[:-1]
        new_dir = "{}_temp".format(mydir)
        cmd = "mv {} {} && mv {} {}".format(mydir, new_dir, new_dir, mydir)
        os.system(cmd)

def main(argv):
    # remove autorun generated things and reveal the hidden dirs.
    if len(argv) == 2:
        working_dir = argv[1]
        clean_files(working_dir)
        arrange_dirs(working_dir)
    else:
        print("wrong args number")
if __name__ == "__main__":
    main(sys.argv)

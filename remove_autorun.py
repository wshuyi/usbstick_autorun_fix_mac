import sys
import os
import glob

def clean_files(working_dir):
    os.chdir(working_dir)
    cmd = "rm -f *.exe ; rm -f .*.exe ; rm -f autorun.inf ; rm -rf Recycled*"
    print cmd
    os.system(cmd)

def arrange_dirs(working_dir):
    dirs = glob.glob("{}/*/".format(working_dir))
    for mydir in dirs:
        mydir = mydir[:-1]
        new_dir = "{}_temp".format(mydir)
        cmd = 'mv "{}" "{}" && mv "{}" "{}"'.format(mydir, new_dir, new_dir, mydir)
        print cmd
        os.system(cmd)

def build_empty_dirs(working_dir):
    os.chdir(working_dir)
    cmd = "mkdir autorun.inf"
    os.system(cmd)
    cmd = "mkdir autorun.exe"
    os.system(cmd)

def main(argv):
    # remove autorun generated things and reveal the hidden dirs.
    if len(argv) == 2:
        working_dir = argv[1]
        clean_files(working_dir)
        arrange_dirs(working_dir)
        build_empty_dirs(working_dir)
    else:
        print("wrong args number")
if __name__ == "__main__":
    main(sys.argv)

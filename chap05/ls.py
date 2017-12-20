import optparse
import locale
import collections
import os
import time


def main():
    usage = ("usage: %prog [options] [path1 [path2 [... pathN]]]\n"
             "The paths are optional; if not given . is used.")
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-H", "--hidden",
                      action="store_true", dest="hidden", default=False,
                      help="show hidden files [default: %default]")
    parser.add_option("-m", "--modified",
                      action="store_true", dest="modified", default=False,
                      help="show last modified date/time [default: %default]")
    parser.add_option("-o", "--order",
                      default="name", type="choice",
                      choices=['name', 'n', 'modified', 'm', 'size', 's'],
                      help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: %default]")
    parser.add_option("-r", "--recursive",
                      action="store_true", dest="recursive", default=False,
                      help="recurse into subdirectories [default: %default]")
    parser.add_option("-s", "--sizes",
                      action="store_true", dest="sizes", default=False,
                      help="show sizes [default: %default]")
    opts, args = parser.parse_args()
    print(opts, args)
    get_files_list(*args, hidden=opts.hidden, recursive=opts.recursive)
    print(os.listdir("."))
    for file in os.listdir("."):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file))))
        print()


def get_files_list(*args, hidden, recursive):
    if not args:
        args = ["."]
    file_dict = collections.defaultdict(dict)
    for dir in args:
        for root, dirs, files in os.walk(dir):
            for filename in files:
                fullname = os.path.join(root, filename)
                filesize = os.path.getsize(fullname)
                filedate = os.path.getmtime(fullname)

    print(args, hidden, recursive)


main()

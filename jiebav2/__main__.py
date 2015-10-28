"""Jieba command line interface."""
import sys
import jiebav2
from argparse import ArgumentParser
from ._compat import *

parser = ArgumentParser(usage="%s -m jieba [options] filename" % sys.executable, description="Jieba command line interface.", epilog="If no filename specified, use STDIN instead.")
parser.add_argument("-d", "--delimiter", metavar="DELIM", default=' / ',
                    nargs='?', const=' ',
                    help="use DELIM instead of ' / ' for word delimiter; or a space if it is used without DELIM")
parser.add_argument("-D", "--dict", help="use DICT as dictionary")
parser.add_argument("-u", "--user-dict",
                    help="use USER_DICT together with the default dictionary or DICT (if specified)")
parser.add_argument("-a", "--cut-all",
                    action="store_true", dest="cutall", default=False,
                    help="full pattern cutting")
parser.add_argument("-n", "--no-hmm", dest="hmm", action="store_false",
                    default=True, help="don't use the Hidden Markov Model")
parser.add_argument("-q", "--quiet", action="store_true", default=False,
                    help="don't print loading messages to stderr")
parser.add_argument("-V", '--version', action='version',
                    version="Jieba " + jiebav2.__version__)
parser.add_argument("filename", nargs='?', help="input file")

args = parser.parse_args()

if args.quiet:
    jiebav2.setLogLevel(60)
delim = text_type(args.delimiter)
cutall = args.cutall
hmm = args.hmm
fp = open(args.filename, 'r') if args.filename else sys.stdin

if args.dict:
    jiebav2.initialize(args.dict)
else:
    jiebav2.initialize()
if args.user_dict:
    jiebav2.load_userdict(args.user_dict)

ln = fp.readline()
while ln:
    l = ln.rstrip('\r\n')
    result = delim.join(jiebav2.cut(ln.rstrip('\r\n'), cutall, hmm))
    if PY2:
        result = result.encode(default_encoding)
    print(result)
    ln = fp.readline()

fp.close()

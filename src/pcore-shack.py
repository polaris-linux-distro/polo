# this is so fucking hacky

import pcore
import sys

if sys.argv[1] == "browser":
    print(pcore.browser)
elif sys.argv[1] == "editor":
    print(pcore.editor)
elif sys.argv[1] == "terminal":
    print(pcore.terminal)
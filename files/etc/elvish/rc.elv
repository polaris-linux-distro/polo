set EDITOR = (python3 /usr/share/polaris/pcore-shack.py editor)
set TERMINAL = (python3 /usr/share/polaris/pcore-shack.py terminal)
set BROWSER = (python3 /usr/share/polaris/pcore-shack.py browser)

put $EDITOR | env:put EDITOR
put $TERMINAL | env:put TERMINAL
put $BROWSER | env:put BROWSER
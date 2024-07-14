#
# /etc/bash.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

GREEN="\[\e[1;32m\]"
BLUE="\[\e[1;34m\]" 
RESET="\[\e[0m\]"

PS1="( $BLUE\u $RESET@ $BLUE\h $RESET-$BLUE \w $RESET) \n$GREEN>> $RESET"

if [[ -r /usr/share/bash-completion/bash_completion ]]; then
  . /usr/share/bash-completion/bash_completion
fi

if [ ! -f ~/.nobanner ]; then
    cat /etc/polaris/banner
fi

source /etc/polaris/lib.sh

export TERMINAL=$(get_ini_value "conf" "terminal" "$HOME/usr.conf")
export BROWSER=$(get_ini_value "conf" "browser" "$HOME/usr.conf")
export EDITOR=$(get_ini_value "conf" "editor" "$HOME/usr.conf")
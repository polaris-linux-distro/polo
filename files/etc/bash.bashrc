#
# /etc/bash.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# Function to get value from an INI file
function get_ini_value() {
  local section=$1
  local key=$2
  local file=$3

  awk -F '=' -v section="$section" -v key="$key" '
    $0 ~ "\\[" section "\\]" { in_section=1; next }
    $0 ~ "^\\[" { in_section=0 }
    in_section && $1 == key { print $2; exit }
  ' "$file"
}

export TERMINAL=$(get_ini_value "conf" "terminal" "$HOME/usr.conf")
export BROWSER=$(get_ini_value "conf" "browser" "$HOME/usr.conf")
export EDITOR=$(get_ini_value "conf" "editor" "$HOME/usr.conf")

GREEN="\[\e[1;32m\]"
BLUE="\[\e[1;34m\]" 
RESET="\[\e[0m\]"

PS1="( $BLUE\u $RESET@ $BLUE\h $RESET-$BLUE \w $RESET) \n$GREEN>> $RESET"

if [[ -r /usr/share/bash-completion/bash_completion ]]; then
  . /usr/share/bash-completion/bash_completion
fi
precmd() {
    print -rP "( %F{blue}%n%f @ %F{blue}%m%f - %F{blue}%~%f )"
}
PROMPT="%F{green}>>%f "

alias cd..="cd .."
alias cd.="cd ."

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/pieyisapie/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

export EDITOR=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py editor)
export TERMINAL=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py terminal)
export BROWSER=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py browser)


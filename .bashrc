# ~/.bashrc
neofetch
#colorscript exec ghosts
# If not running interactively, don't do anything
[[ $- != *i* ]] && return
### ARCHIVE EXTRACTION
# usage: ex <file>
ex ()
{
  if [ -f "$1" ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
# Github Alias
alias gitssh='eval $(ssh-agent -s)'
alias gitstart='ssh-add ~/GitHub/SSH/github'
alias commit='git commit -m'
# Changing "ls" to "exa"
alias ls='exa -lGh --icons --git --no-permissions --no-filesize --color=always' # my preferred listing
alias la='exa -lGh --icons --git --no-permissions -a --no-filesize --color=always'  # all files and dirs
# grep colours
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'
# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -h'                      # show sizes in MB
# the terminal rickroll
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'

# Bash Shell
PS1='[\u@\h \W]\$ '

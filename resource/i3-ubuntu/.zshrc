export ZSH="/home/vitor/.oh-my-zsh"
ZSH_THEME="agnoster"
plugins=(zsh-autosuggestions git)
source $ZSH/oh-my-zsh.sh

#custom proprieties

alias repetier-host='~/tools/repetier-host/repetierHost'

export PATH=/usr/local/cuda-11.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

export PATH=/home/vitor/.local/bin${PATH:+:${PATH}}


export PATH="$PATH:$HOME/go/bin"
export GOPATH=$HOME/go

export GOBIN="$GOPATH/bin"

alias vim="nvim"
alias vi="nvim"
alias oldvim="vim"

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

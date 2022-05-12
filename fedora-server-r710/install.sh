#instalation

sudo dnf install -y tigervnc
sudo dnf install -y openssh-server
sudo dnf install -y gcc-go golang-bin
go install github.com/cjbassi/gotop@latest


#put on .bashrc
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin

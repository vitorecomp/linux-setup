# Ubuntu setup - With I3

## Programs

>Install i3:  
    sudo apt install i3

>Install i3:
    sudo apt install git
    sudo apt-get install -y i3blocks
    sudo apt-get install zsh curl git
    sh -c "\$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    sudo apt-get install feh

>install all the fonts
mv resources/fonts ~/.fonts

>Install visual code:
snap install code --classic

>Install intellij-idea-community:
sudo snap install intellij-idea-community --classic

>Install Anaconda:
cd tools
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh

>Install docker
sudo apt install docker.io
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-\$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
#!/bin/bash
echo "installing the PIP package management system"
sudo apt install python3-pip -y
echo "installation of the seed phrase generator BIP39"
pip install mnemonic
echo "installation of software for working with a website"
pip install selenium
echo "installing the chromium automation browser"
sudo apt-get install chromium-chromedriver -y
echo "setting client url"
sudo apt  install curl
echo "opening a home directory"
cd ~
echo "copying the CHIA COIN distribution"
git clone https://github.com/Chia-Network/chia-blockchain.git -b latest --recurse-submodules
echo "opening the CHIA COIN distribution folder"
cd chia-blockchain
echo "CHIA COIN installation"
sh install.sh
. ./activate
echo "CHIA COIN initialization"
chia init

#!/bin/bash
installpkg() {
    is_installed="$(apt list 2>/dev/null | grep "^$1/")"
    if [ -z "$is_installed" ]; then
        understands=0
        while [ ! understands ]; do
            program_is_to_install="$(read -p "$1 has not been detected on this system. Would you like to install? [y/N] ")"
            if [ $program_is_to_install || $program_is_to_install == 'y|Y' ]; then
                understands=1
                echo "\n> sudo apt install $1\n"
                sudo apt install "$1"
            elif [ -z $program_is_to_install || $program_is_to_install == 'n|N' ]; then
                exit
            else
                echo "I didn't catch that."
            fi
        done
    fi
}

installpkg python3
installpkg git-all

where_to_clone="$(read -p "Choose where to install Aurora (~/.aurora/lib/) ")"
if [ -z "$where_to_clone" ]; then
    where_to_clone="~/.aurora/lib"
fi
echo "> mkdir ~/.aurora"
mkdir ~/.aurora
echo "> mkdir -p $where_to_clone"
mkdir -p "$where_to_clone"
git clone https://github.com/anowa-eng/Aurora.git "$where_to_clone"

cd "$where_to_clone/install"
pip install -r requirements.txt

echo "\nAurora has now been installed onto this computer.\nGet started by creating a new model with \`aurora new\`"
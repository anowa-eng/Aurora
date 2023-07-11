

installpkg() {
    is_installed="$(apt list | grep "^$1/")"
    if [ -z "$is_installed" ]; then
        understands=0
        while [ ! understands ]; do
            program_is_to_install="$(read -i "$1 has not been detected on this system. Would you like to install? [y/N] ")"
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

where_to_clone="$(read -i "Where would you like the Aurora repository to be cloned? (~/.aurora/lib/)")"
if [ -z "$where_to_clone" ]; then
    where_to_clone="~/aurora/lib"
mkdir "$where_to_clone"
git clone https://github.com/anowa-eng/Aurora.git "$where_to_clone"

cd "$where_to_clone/install"
pip install -r requirements.txt

echo "\n\u001b[1mAurora has now been installed onto this computer.\u001b[0m\nGet started by creating a new model with \`aurora new\`"
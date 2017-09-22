# not a normal case, python modules should not install on system
echo "Installing abcd in the system"
# install dependencies on the system
sudo -E pip install -r requirements.txt
# install the current module on the system with symbolic link
sudo pip install -e .
# installed: /usr/local/bin/start_abcd
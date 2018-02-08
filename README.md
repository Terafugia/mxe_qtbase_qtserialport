# How to build qt project for Windows on Linux
```
sudo apt-get install -y git build-essential
git clone https://github.com/ilyayunkin/mxe_qtbase_qtserialport ~/mxe
export PATH=~/mxe/usr/bin:$PATH
cd [your .pro dir]
i686-w64-mingw32.static-qmake-qt5 [your project].pro && make
```

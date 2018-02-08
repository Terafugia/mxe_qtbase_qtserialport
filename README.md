# How to build qt project for Windows on Linux

If you are using x64 machine, do:
```
dpkg --add-architecture i386
apt update
apt -y install libc6:i386 libncurses5:i386 libstdc++6:i386
```

Then do:
```
sudo apt-get install -y git build-essential
git clone https://github.com/ilyayunkin/mxe_qtbase_qtserialport ~/mxe
export PATH=~/mxe/usr/bin:$PATH
cd [your .pro dir]
i686-w64-mingw32.static-qmake-qt5 [your project].pro && make
```

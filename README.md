It is a build of [MXE](https://github.com/mxe/mxe). Please visit it to know about license and etc. Note also that this build contains static Qt - read a Qt license.

We use it to accelerate building on gitlab-ci (building of qt with mxe takes a lot of time).

If you have a time - build [MXE](https://github.com/mxe/mxe) in your machine.

If you can use arch-linux - use [mingw-w64-archlinux](https://sourceforge.net/projects/mingw-w64-archlinux/).

# How to build Qt project for Windows on Ubuntu or Debian Linux

**It is strongly recommended to use it on virtual machine**

Use username **"user"** or create /home/user directory:
```
sudo mkdir /home/user/
sudo chmod a+rw /home/user/
```

If you are using x64 machine, do:
```
sudo dpkg --add-architecture i386
sudo apt update
sudo apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

Then do:
```
sudo apt-get install -y git build-essential
git clone https://github.com/ilyayunkin/mxe_qtbase_qtserialport /home/user/mxe
export PATH=/home/user/mxe/usr/bin:$PATH
cd [your .pro dir]
i686-w64-mingw32.static-qmake-qt5 [your project].pro && make
```

Yes, I know, that this is not elegant, but it works.

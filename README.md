# djsimplifier

Gui for [youtube-dl](https://youtube-dl.org/)

## Build

### MacOS

1.  install dependencies

        pip3 -r requirements.txt

1.  build app

         pyinstaller -y djsimplifier.spec

1.  create dmg

        chmod +x builddmg.sh
        sh builddmg.sh djsimplifier

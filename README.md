# Python script to disable the language switching popup on OS X
# THE PROBLEM:
<img width="463" alt="image" src="https://user-images.githubusercontent.com/55480132/192276045-1e3c69b9-1188-408a-8e49-08fef5ea8aa6.png">

Not only its slow, but when mouse cursor happens to be in the center of the screen, it selects the wrong language for you!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# THE SOLUTION (get rid of the pop up):

1. Install ["issw"](https://github.com/vovkasm/input-source-switcher) - a small utility for macos to switch input sources from a command line.
------------

    git clone https://github.com/norflin321/input-source-switcher.git
    cd input-source-switcher
    mkdir build && cd build
    cmake ..
    make
    make install
------------
By default executable will be installed as `/usr/local/bin/issw`

You can run `issw -l` in terminal to get list of available input sources and modify script above if needed!

For simple test run: 
`issw com.apple.keylayout.ABC` | `issw com.apple.keylayout.Russian`

Watch for the changes in languages. If the languages are switched, the issw installation was successful.

2. Create fn.py file in ~/. Or clone the repository. Add the desired language switching playback sound (optional).

Set rights to file: `chmod u+x fn.py `
------------

    import os
    import pynput
    import playsound
    from pynput import keyboard
    from playsound import playsound

    def on_press(key):
        key_str = '{0}'.format(key)
        if (key_str == '<179>'):
            stream = os.popen('/usr/local/bin/issw')
            output = stream.read().strip()
            if (output == 'com.apple.keylayout.ABC'):
                os.system('/usr/local/bin/issw com.apple.keylayout.Russian')
                playsound('/Users/`$USER$`/knopka-klik-zvonkii-myagkaya.wav')
            else:
                os.system('/usr/local/bin/issw com.apple.keylayout.ABC')
                playsound('/Users/`$USER$`/knopka-klik-zvonkii-myagkaya.wav')


    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()

`<179>` is key code for `fn`.

3. Set this to "Do Nothing"
------------
![ezgif-5-aeb126ae5e](https://user-images.githubusercontent.com/33498670/167285047-18f7a509-b56d-4f1f-896a-963c034947dc.jpeg)


4. Setup auto run of the script every time you log in (python3 should be installed).
------------
    4.1. Install `pynput` and `playsound` python module:
        `/usr/bin/python3 -m pip install pynput`
            `pip install pynput`
            `pip install playsound`

    4.2. Inside `fn.plist` file, change paths to the python executable (if you are using custom python installation) and the script file.
    Mine is `/Users/benristar/fn.py`. Paths should be full.

    4.3. Copy the plist file to special directory: `cp -R fn.plist ~/Library/LaunchAgents/`.

    4.4. Then run this command: `sudo launchctl bootstrap gui/501 ~/Library/LaunchAgents/fn.plist`
    - it will tell mac to run this file every time you log in. 
    
    If you want to stop it run `sudo launchctl bootout gui/501 ~/Library/LaunchAgents/fn.plist`.
    Also remove the file `rm -rf ~/Library/LaunchAgents/fn.plist`.

    4.5. Mac might ask you to grant permission for python to monitor input from your keyboard and `Accessibility`. 
    Generally macOS asking about `Input Monitoring`, add your python3 executable to `Accessibility` if no popup with this showed.
<img width="773" alt="image" src="https://user-images.githubusercontent.com/55480132/192275874-40bf787e-1945-49fd-b947-77bd25d3948c.png">
<img width="777" alt="image" src="https://user-images.githubusercontent.com/55480132/192275926-7bebb75b-446b-44d8-a40a-62598cde8e1d.png">
------------

5. Restart. Log in. It should work.

P.S. Don't forget to reinstall `pynput` and `pynput` after upgrades.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# RESULT:
You can toggle input source with "fn" button, but without showing the pop up!


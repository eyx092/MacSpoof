# MacSpoof
A dumb repository where I tell you how to spoof your mac address.

So step one is figuring out what operating system you have, which should be pretty easy. If you're using Windows, just go down, and you should see some directions. If you're using linux, you can just go a bit further down. If you're using MacOS, scroll past the Linux section and you should see the directions for MacOS users.

Windows users:

The second step is finding the driver number of your network card. This can be done using the Registry Editor on Windows. When you get into the Registry Editor, go to this path: `HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlClass{4D36E972-E325-11CE-BFC1-08002BE10318}`. Under this path, there should be a bunch of folders with numbers on them. Click each one until you find the folder for your network card. Once you do that, change the part of the command in the powershell script that has been highlighted with stars below to match the network driver number (the number of the folder in which you found your network card): 

`_reg add HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlClass{4D36E972-E325-11CE-BFC1-08002BE10318}_**0004** /v NetworkAddress /d AABBCCDDEEFF /f`

so that it looks somewhat like this:

`_reg add HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlClass{4D36E972-E325-11CE-BFC1-08002BE10318}_0004 /v NetworkAddress /d AABBCCDDEEFF /f`

Once you've done that, open PowerShell as an administrator. If you're not an administrator, you will unfortunately be unable to run this script due to lack of permissions. If you got PowerShell open as an administrator, navigate to the script's directory using the `cd` command. Once you're in the same directory, go ahead and run the Windows script with the command `./windows_mac_spoof.ps1`. You have now successfully spoofed your mac address on Windows. 

If you're having trouble using the `cd` command, I would reccommend watching this video which helps guide you through using the `cd` command: https://www.youtube.com/watch?v=BfXh11ryBJg.

Linux users:

The second step is making sure you're in the correct directory and you have root or administrator permissions. On linux, this should be pretty easy to test. Go to the terminal, and type:

```bash
sudo pwd
```

If the terminal responds with "Permission denied" or "Operation not permitted", you may not be in the correct user account or you don't have high enough permissions. The problem with this is that you need administrator or root permissions for these scripts to work. Sooo... if you don't have the correct permissions, I'm sorry, but good luck with changing your mac address...

If you have the necessary permissions, make sure you are in the same directory as the script, and run it. I would reccommend putting the script on your desktop. If the script is on your desktop, then try typing the following:

```bash
cd Desktop
```
That should put you in the same directory as the script. If the terminal tells you that the directory does not exist run this command:

```bash
pwd
```
This command tells you the current directory you're in. It should probably say something like /home/user or something. If it doesn't, try typing:

```bash
cd ..
```
and then the "pwd" command again until you get to a point where the terminal tells you the directory you are in is somewhat like /home/user. After you get to that, just try typing "cd Desktop" again. If this is all confusing for you, try watching this video to get to the desktop directory: https://www.youtube.com/watch?v=FTTr2bjI2UM.

After you finish getting to the correct directory, the next step is choosing the correct script.

If you are on an Ethernet connection, run the script that has the name linux_mac_spoof_ethernet.sh

Or just copy and paste this command:
```bash
./linux_mac_spoof_ethernet.sh
```

If it says "No such file or directory", you may be in the incorrect directory. Try going back to the last step to find the correct directory. If the output from the terminal says "Operation successful" you have successfully spoofed your mac address on linux.

If the terminal responds with "Permission denied" or "Operation not permitted", you may not be in the correct user account or you don't have high enough permissions. The problem with this is that you need administrator or root permissions for these scripts to work. Sooo... if you don't have the correct permissions, I'm sorry, but good luck with changing your mac address...

If you are on a wireless connection, which is probably more likely, run the script that has the name linux_mac_spoof_wireless.sh

Or just copy and paste this command:
```bash
./linux_mac_spoof_wireless.sh
```

If it says "No such file or directory", you may be in the incorrect directory. Try going back to the last step to find the correct directory. If the output from the terminal says "Operation successful" you have successfully spoofed your mac address on linux.

If the terminal responds with "Permission denied" or "Operation not permitted", you may not be in the correct user account or you don't have high enough permissions. The problem with this is that you need administrator or root permissions for these scripts to work. Sooo... if you don't have the correct permissions, I'm sorry, but good luck with changing your mac address...

MacOS users:

The script provided should work on any computer which has MacOS X or a newer operating system installed on it. Read this article to figure what your Mac has isntalled: https://www.businessinsider.com/how-to-check-mac-os-version. If the Mac says it has MacOS X, MacOS High Sierra, or MacOS Catalina installed, you should be good. I haven't tried the script on Big Sur, but I might in the future. 

Now to check if you are an Administrator on a Mac, go to "System Preferences" and then click on "Users & Groups". From there, under "Current User", you should be able to see if your account is a standard, managed, or admin account. If you have a standard or managed account I'm sorry, but good luck changing your mac address...

For the directory part, you should mainly just follow the linux instructions because the MacOS terminal is largely based off of the linux "bash" terminal. If you think I'm bad at explaining things, which I am, go check out this video on how to get to the Desktop (my reccomendation for the location of the script): https://www.youtube.com/watch?v=FTTr2bjI2UM.

Ok now you're ready to run the script. Run the script that has the name macos_mac_spoof.sh

Or just copy and paste this command:
```bash
./macos_mac_spoof.sh
```

A prompt should come up for your password. Type your password, then hit enter.

If it says "No such file or directory", you may be in the incorrect directory. Try going back to the last step to find the correct directory. If the output from the terminal says "Operation successful" you have successfully spoofed your mac address on MacOS.

If the terminal says that you don't have permission to run following script, or your action was not permitted, you may not be in the correct user account or you don't have high enough permissions. The problem with this is that you need administrator or root permissions for these scripts to work. Sooo... if you don't have the correct permissions, I'm sorry, but good luck with changing your mac address...


In summary, you just have to run the right script in the right directory with the right permissions. If you don't have the right permissions, it will be a lot harder to spoof your mac address, but I think that it is still possible (don't quote me on that).

Now if you've read down to this point, you might still be asking for one thing. What if I want to change my mac address more than once?

Well, then you might want to use the python program that is named "generate_mac_address.py". This program will automatically generate a mac address for you which you can replace with the current mac address in the scripts. To run this script, type
```bash
python3 generate_mac_address.py
```
and then press enter. The program should output a string of numbers and/or letters. 

If you get an error, you probably don't have Python installed. If you're on Windows or MacOS, go to https://python.org/downloads/ and download the latest version of Python 3. If you're on linux, its much easier. Open the terminal as a root user, and type this command: `sudo apt-get install python3.8`. You shouldn't get anymore errors after that.

Copy the output, and then open the script you want to modify by double-clicking on it. This should usually bring up the contents of the script in a text editor. Then just highlight the part of the script that seems similar to the output of the program. Then hit Ctrl-V, and the old mac address should be replaced by the new one generated by the program. Follow the steps to run the script for your operating system again, and you have successfully spoofed your mac address more than once!

Thank you for reading and using my repository!

If you have any questions, feel free to ask them in the 'Issues' section.

Credits (Can also be found in credits.txt):

All of the spoofing scripts: eyx092

The mac address generator: Based off of a script from Russ on Stack Overflow (https://stackoverflow.com/questions/8484877/mac-address-generator-in-python)

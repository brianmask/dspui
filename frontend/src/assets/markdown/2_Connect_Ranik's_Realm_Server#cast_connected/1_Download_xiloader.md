## In this section we will describe how to download and install xiloader to connect to the server.

**Download xiloader.exe** from [here.](https://github.com/DarkstarProject/xiloader/releases/latest)

If you have issues: Set **pol.exe** and **xiloader.exe** to run as administrator by right-clicking on them and going **Properties**, opening the **Compatibility** tab and clicking the **Run as Administrator** checkbox at the bottom of the window.

## Prerequisites

* xiloader requires **MSVC** runtimes for **2015** from [here] 
* Regardless of your current setup, be sure to install the x86 version :-)

This version takes command-line options and was designed to work seamlessly with Windower.

Extract the xiloader.exe into a folder of your choice (it does **not** need to be any particular location, and you can specify the path to it in windower). Note: it is not recommended that you place it inside your "Program files" or Final Fantasy XI folders.

To play on the server, open up a command prompt, navigate to the folder you extracted to, and type in:

```
xiloader.exe --server ffxi.brianmask.com --user username --pass password
```

The first time you log into the server you will be asked to create a username and password.



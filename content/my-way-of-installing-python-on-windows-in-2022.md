Title: My Way of Intalling Python on Windows in 2022
Date: 2022-11-02 18:41
Modified: 2022-11-02 18:41
Tags: Python, Windows, Development, Installing
Category: Python
Slug: my-way-of-installing-python-on-windows-in-2022
Authors: Joe Stanley
Summary: Finally! Python 3.11 is out! It's new, it's fast(er than previous Python versions), and it's got some dandy new features. And if you wanted to know how I go about putting it on a Windows machine, let me show you...

Python is a bit of a tricky subject on Windows, and that's why I've developed my own "best practice" for installing it on my systems. Let me briefly walk you through the steps.

## 1) Download the latest version of Python
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-36-36.png" style="width: 100%" alt="Step 1 - Download the Latest Python">

## 2) Run the installer
> but make sure you check "Add Python to Path" and use the "Customize" option for installation
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-37-12.png" style="width: 100%" alt="Step 2 - Run the Installer">

## 3) Select Everything!
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-37-41.png" style="width: 100%" alt="Step 3 - Select Everything">

## 4) Select "Install for All Users" and Customize the Installation Path
This will make sure that Python is installed in a simple, and accessible place. I find it VERY helpful to have Python rooted at the `C:\` drive level. You can argue with me;
that's fine. This is just the way *I* do it.
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-40-03.png" style="width: 100%" alt="Step 4 - Change the Path">

## 5) Install!

## 6) Verify the Path
It's time to make sure that Python got installed and the Path variable was set correctly.

Press your Windows key and search for "path". Then open the "Edit the system environment variables" dialog.
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-37-41.png" style="width: 100%" alt="Step 6 - Verify the Path">

From the dialog, select "Environment Variables" in the bottom-right.

Then, in the bottom window, make sure that you can see "`C:\Python311\Scripts\`" and "`C:\Python311\`" listed in the "Path" variable.
If they're not there, double click on the "Path" variable, and add them!
<img src="{attach}/images/installing-python-on-windows-2022/2022-11-02_16-45-01.png" style="width: 100%" alt="Step 6 - Verify the Path">

-----

That's about it! Have fun with the faster, newer, Python, everyone!

<!---
title:Package Managers Will Change Your Life
date:Fri, 03 Dec 2021 22:00:00 EDT
description:Learn to install programs the hackerman way
--->

## Package Managers Will Change Your Life

### 2021-12-03

How do you go about installing programs normally on your computer? Do you use an app store? Do you download the installation file from a website? While both of those methods are definitely viable, I'm going to introduce you to the best way to install apps: using a terminal-based package manager.

### What is a package manager?

Package managers allow you to install packages of apps, programs, and other data, such as dependencies for programs. Their main purposes are to install, remove, and update anything on your system. The package manager system is actually exactly what is used in programs like the app/play store on smartphones. With these apps, you're able to manage most/all your apps. Traditional package managers on Linux are usually terminal-based, though.

### Examples of package managers:

If you've programmed before, you've probably used some language-based package managers, such as pip (Python) or npm (JavaScript). You can do stuff like this to install libraries for your programs.

```
pip install <package>
```

```
npm install <package>
```

What may be more helpful for the average user are the OS-level package managers. On Linux, there are many, but the three most commonly used are: APT (on Debian and Ubuntu-based systems), Pacman (on Arch-based systems), and DNF (RHEL-based systems like Fedora). You can install, update, and remove software and many other packages just with some terminal commands. What's nice about that is that you can continue using your computer as it's being updated.

Examples of installing packages:

APT:

```
sudo apt-get install <package>
```

Pacman:

```
sudo pacman -S <package>
```

DNF:

```
sudo dnf install <package>
```

Examples of updating packages/system:

APT:

```
sudo apt update
```

```
sudo apt upgrade
```

Pacman:

```
sudo pacman -Syu
```

DNF:

```
sudo dnf update
```

```
sudo dnf upgrade
```

Installing packages like this is also possible using PowerShell and winget on Windows. Winget is developed by Microsoft, so it's fairly limited. I'd highly suggest installing Chocolatey as well to be able to install more apps and programs.

```
winget install <author.package>
```

```
choco install <package>
```

\*Make sure you're running powershell as an admin when using chocolatey

### Why you should care

Using winget and Chocolatey on Windows really made my experience so much better. Instead of opening a browser and searching for Spotify, Discord, and other applications, I was able to just open the Windows terminal and install them with a simple command.

```
winget install Discord.Discord
```

and

```
winget install Spotify.Spotify
```

I didn't have to deal with the setup.exe or anything. The apps just opened a few seconds after, just like as if I installed them from the Microsoft Store (that's because I basically did). It's quick, efficient, and you look cool when you do it. All it took was a simple command in the terminal. Using the terminal in general is something that is really useful, especially when installing programs, as it will often tell you exactly what's wrong with the program if you need to troubleshoot it. It's always more useful than getting some random numbered error and a very ambiguous dialog box. Just don't be like Linus Tech Tips and read the message before nuking your desktop environment haha.

<!---
title:Making Super Mario 64 Remixes of Songs
date:Sat, 19 Nov 2022 12:00:00 EST
description:Who knew making remixes could be so easy
--->

## Making Super Mario 64 Remixes of Songs

### 2022-11-19

A while back, I discovered Super Mario 64 Super Mario remixes of Aphex Twin and Radiohead tracks and thought that they were the coolest thing ever. I tried having a go at it, only to find out that it's incredibly easy to do it. It uses a simple yet effective technology: MIDI (scroll down if you want to learn how I did it).

Here are some of my favourites that I've remixed:

**2 of Amerikaz Most Wanted** - _2Pac, Snoop Dogg_

<div style="
background: rgb(0,0,0);
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/2_Of_Bowzaz_Most_Wanted.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/snoop.gif">
</div>

**A Cruel Angel's Thesis** - _Yoko Takahashi_

<div style="
background: rgb(0,0,0);
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/cruel_goombas_thesis.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/asuka_dance.gif">
</div>

**Beat It** - _Michael Jackson_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/beat_it64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/mario_jackson.gif">
</div>

**Duvet** - _bôa_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/serial_experiments_mario.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/lain_dance.gif">
</div>

**Everytime We Touch** - _Cascada_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/EverytimeWeTouch64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/baby.gif">
</div>

**Feel Good Inc.** - _Gorillaz_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/FeelGoombaInc.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/gorillaz.gif">
</div>

**Flim** - _Aphex Twin_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/flim64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/afx_dance.gif">
</div>

**Gerudo Valley** - _Koji Kondo_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls><source src="../assets/audio/gerudo64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/lonk.gif">
</div>

**Reckoner** - _Radiohead_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px
">
<audio controls><source src="../assets/audio/reckon64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/thomdance.gif">
</div>

**Waluigi Pinball** - _Kentaro Ishizaka_

<div style="
background: rgb(0,0,0);
border-radius: 15px;
background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(68,68,68,1) 65%, rgba(255,255,255,0) 100%);
padding:15px;
max-width: 615px">
<audio controls style="vertical-align: middle;"><source src="../assets/audio/waluigi64.mp3" type="audio/mpeg"></audio>
<img class="no-border" style="max-height:100px;vertical-align: middle;" src="../assets/images/waluigi.gif">
</div>

### How It Works

MIDI (musical instrument digital interface) is essentially a universal system that allows for instruments to communicate with each other and computers. While MIDI encompasses a lot more, including programming and other musical standards, what's important for this case are the files. MIDI files (.mid) are not like typical .mp3 and .wav files as they don't actually hold any audio data. Instead, they're a lot more like sheet music in that they are instructions for an interpreter to play notes. MIDI files hold data like the notes all the instruments are playing, dynamics (volume), and tempo (speed). Along with that, they are all standardized in some ways. Drums should always be on the 10th channel for example. Note that there are different standards, which is probably why some of your MIDI files seem extremely wrong.

There's another important component to this: soundfonts. If you were to play a MIDI file on your computer (assuming you have a media player that can play them), you would just hear the song normally. To add the Mario 64 instruments and sounds, you need use a soundfont. Soundfonts contain the actual audio for instruments. As I mentioned, MIDI is a standard, so this would mean that instruments will correspond to whatever the MIDI file requests.

### How To Make Your Own Remixes

To actually render and play the MIDI files with the Mario 64 soundfont, I use [VLC media player](https://www.videolan.org/vlc/). The classic, legendary, FOSS audio program that can run anything.

![vlc<3](../assets/images/vlclessthan3.jpg)

By default I wasn't able to play MIDI files, so I had to install FluidSynth, which supports soundfonts.

On Debian/Ubuntu:

```
sudo apt-get install fluidsynth
```

Arch Linux:

```
pacman -S fluidsynth
```

Fedora:

```
sudo dnf install fluidsynth
```

[Get FluidSynth](https://www.fluidsynth.org/download/)

You will need the Mario 64 soundfont as well.
[Click here to download it](../assets/resources/Super_Mario_64_SF_v1.4.sf2)

Open VLC and go to Tools > Preferences (or Ctrl+P). Then, make sure "All" settings is enabled at the bottom left corner.
Under Input / Codecs > Audio Codecs, click FluidSynth. Press "Browse", then select the Mario 64 soundfont. Be sure to save your changes.

![vlc settings](../assets/images/vlc_settings.png)

Now, all you need to do is to play a .mid file and you're done!

### Finding MIDI Files

I found most of mine on

[https://www.hamienet.com/)](https://www.hamienet.com/) (best in general)

[https://www.vgmusic.com/](https://www.vgmusic.com/) (best for games)

[https://freemidi.org/](https://freemidi.org/) (everything)

[https://www.midishrine.com/](https://www.midishrine.com/) (games and anime)

[https://animezen.net/midis](https://animezen.net/midis) (anime)

Choosing a good MIDI file will make the song much better. Choose MIDIs with lots of instruments used for best results! Try a variety of artists and genres when looking for stuff. The best ones tend to be instrumentals and dance music (IDM, EDM, etc.), but I've listened to some amazing MIDIs in all of my favourite genres.

### Rendering Files as mp3

If you want to send your files to other people without having them to go through this process, then I would recommend rendering them as an mp3 like I did above. You can do it easily with VLC once again.

Under Media, press Convert/Save (or Ctrl+R).
Press + Add to add your file, click on Convert, and you can save your file as pretty much anything. Make sure you press the play button to actually render it.

### Adjusting Soundfonts

Sometimes the soundfonts just don't work well. I recommend using [Swami](http://www.swamiproject.org/) to edit soundfont files. You can add/remove instruments, change the channels for instruments, and a lot more to make them work better with your midi files.

### You Can Do More Than Mario 64

I've seen soundfonts for Undertale, Minecraft, DOOM, and more. The instruments for DOOM and Undertale are not nearly as unique as Minecraft or Mario so most of the MIDIs just sound normal.

### In Conclusion...

The world of MIDI is so cool. I love browsing through MIDI file websites and checking out what talented people have made. This was the way a lot of people enjoyed their music back when internet speeds were slow. MIDI files were also used in game consoles up until the early 2000s, which is one of the reasons as to why an N64 game's soundfont is used for these remixes. Unfortunately, games are allowed to be as large as they please, (side note: why are games like COD: Warzone like 200+ GB, its absurd) so we don't see MIDI used nearly as much in this recreational manner as before. I think there's a lot more potential with this technique and I'm just scratching the surface on crazy things someone can do with this knowledge. Go on and make a MIDI remix!

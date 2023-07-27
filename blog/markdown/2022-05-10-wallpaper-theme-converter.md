<!---
title:All About Wallpaper Theme Converter
date:Tues, 10 May 2022 12:00:00 EST
description:An explanation on how it works and cool things I learned while making it
--->

## All About Wallpaper Theme Converter

### 2022-05-10

Wallpaper Theme Converter (WTC) is a webpage that converts any image to any colour palette. You can adjust the colours to a wallpaper to better match your setup, terminal, and/or IDE. There are some theme presets such as [Gruvbox](https://github.com/morhetz/gruvbox), [Nord](https://github.com/arcticicestudio/nord), [Solarized](https://github.com/altercation/solarized), [Catppuccin](https://github.com/catppuccin/catppuccin), [Dracula](https://github.com/dracula/dracula-theme), and a custom theme.

It is inspired by [Gruvbox Factory](https://github.com/paulopacitti/gruvbox-factory) and [ImageGoNord](https://github.com/Schrodinger-Hat/ImageGoNord). I originally saw Gruvbox Factory a few months ago and that was the spark for me to start it. I found out later that it actually is just ImageGoNord but with the Gruvbox colour scheme.

### Examples

![example](../assets/images/this_took_way_too_long.png)

### How it works

It starts by using the html canvas element to draw the image and make the changes to it. When the user selects any of the buttons, it assigns the rgb values of the palette to a list/array. It also shows the colour palette by creating a new div element that is a square block for each colour.

Upon clicking the convert button, it does a few calculations. In simple terms, it is trying to find the closest colour in the palette for each pixel. It does this by using the formula for 3D distances. This works because you can think of the x,y, and z coordinates as r,g, and b coordinates.

![formula](../assets/images/dist_formula.png)

After calculating the distance for each of the colours in the palette, a list of all the distances is created and a simple sorting algorithm is used to find the lowest number. This value is the closest, since it's "distance" is the least compared to the original value of the pixel. The lowest number is associated with the colour in the palette that is closest to the original value.

Once all the calculations are done for each pixel, the new image data is used to reconstruct the image.

You can take a look at the source code [here](https://github.com/NotNeelPatel/WallpaperThemeConverter/blob/main/assets/convert.js) if you want to see exactly what I'm explaining.

### Custom Theme

For the custom palette, a few extra things needed to be done. The menu can add/remove swatches (the colour blocks that you can use to change the colour). I chose swatches because they were the simplest to implement, but I may add more features to make it better.

This is the part I want to work on more in the future. I don't love how adding the colours works. If you want to remove a colour that isn't at the end, you have to remove all the other colours prior to it. It's not a huge deal since you can simply change the colour to something you'd like, but I still may want to add that as a feature.

### Highlights

Considering this is one of my first Javascript projects, I'm very proud of what I was able to achieve. I had it working with Gruvbox within a day, and kept on adding features almost every day. The UI is pretty minimal, which is exactly what I like. I love how you can see the palette when you click on any of the themes, and my code is flexible so I can add themes as I please. The only difficult part of adding preset themes is looking for the hex values of the theme. I then use an excel spreadsheet to convert them to rgb values and also to format it so all I need to do is copy/paste the values into the js file.

### Downfalls

This isn't perfect, just as Gruvbox Factory and ImageGoNord aren't either. The pictures that work best are those that are fairly flat and have little to no gradients. For that reason, pixel art works very well and is why I used it as the example. Another downfall that can't really be fixed is that the output image by default is more posterized than the original image. That makes sense since the image likely has colours more than the amount of colours in the colour palettes.

### What's next?

At the moment, I'm happy with what I have now. I want to rework the custom theme menu a little so that it's easier to paste in values or remove specific swatches. I also don't like how the palette isn't shown upon pressing the custom theme button.

Maybe in the future when I really understand how image processing works, I can add some kind of algorithm that can make smoother images.

I also need to fix the download button, since it only works on desktops at the moment.

### Conclusion

Like probably 99% of other projects, a lot of my code is really just a melting pot of StackOverflow answers, especially the canvas code since that was completely foreign to me. I hope you learned something and if you have any comments, leave them below!

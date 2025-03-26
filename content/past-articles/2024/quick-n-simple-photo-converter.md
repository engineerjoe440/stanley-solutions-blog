Title: Quick-n-Simple Photo Converter (for HEIC format)
Date: 2024-01-24 20:52
Modified: 2024-01-24 20:52
Tags: blog, website, shell, script, heic, image, photo, converter, conversion, file, iphone
Category: Scripting
Slug: quick-n-simple-photo-converter
Authors: Joe Stanley
Summary: Those techy, geeks in the audience that use an iPhone probably recognize that the photos they take are in a format that's generally a little... Tricky to use with other resources. Seems I most frequently run into this issue when working on updating my blog with pictures that I took on my phone. I really would much rather use a `.png` format in place of the somewhat irksome `.heic` format that my iPhone captures. There's plenty of things online that I could upload my photos too, but who really wants to do that? I'd rather use something a little more "close to home."

I end up taking lots of pictures. Maybe not as many as some folks, but I do take a lot... Pretty much all of those pictures are taken with my iPhone. As such, they're all in
the [`.heic` (high efficiency image) format](https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format). Now, that's neat and all, but those images are harder to embed
in all the places I want to put them. Thus, I'm stuck back-converting them to [PNG format](https://en.wikipedia.org/wiki/PNG).

Like any good programmer, I went right to Google to do a little "lookin' around" to find a way to do this with locally on a Linux machine.

Didn't take long to find plenty of articles recommending `heif-convert`, which can be installed with the following command:

```shell
sudo apt install libheif-examples
```

**GREAT!**

... but ...

It's a touch too long for my impatient fingers, and I don't want to run that same command over, and over, and over, and over, and over again...

> Time for a script!

I decided to make a simple little script to find all of the `*.heic` photos in the specified directory, and run the conversion required...

```shell
#!/usr/bin/bash
# Simple HEIC Conversion Utility (so Joe doesn't need to remember)
for file in $1/*.HEIC
do
    echo "Converting: $file"
    heif-convert "$file" "${file%.*}.png"
    rm $file
done
```
> [`photo-convert` script](https://github.com/engineerjoe440/stanley-solutions-blog/tree/master/photo-convert)

This really made for a nice, handy little script for my photo conversion needs. Maybe you'll find it helpful, too!

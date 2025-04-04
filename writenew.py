#!/usr/bin/python3
"""
`writenew.py`

Simple Python script to get a user started with writing a new Pelican blog post.

"""

import os
import re
import time
import argparse
import subprocess

keymap = {}

try:
    import win32api
    def usr_callback(prompt=False):
        """Username Callback."""
        global keymap
        usr = win32api.GetUserName()
        usr_str = ' [{}]'.format(usr)
        if prompt:
            return usr_str
        elif keymap['author'] == '':
            return usr
        else:
            return keymap['author']
except ImportError:
    import pwd
    def usr_callback(prompt=False):
        """Username Callback."""
        global keymap
        usr = pwd.getpwuid(os.getuid())[4].replace(',','')
        usr_str = ' [{}]'.format(usr)
        if prompt:
            return usr_str
        elif keymap['author'] == '':
            return usr
        else:
            return keymap['author']

def tagerizer(prompt=False):
    """Automatically Render the Tags."""
    global keymap
    if prompt:
        return ''
    tags = [t.lower() for t in re.split(r', ?',keymap['tags'])]
    tags.sort()
    return ', '.join(tags)

def slugerizer(prompt=False):
    """Automatically Render the Slugs."""
    global keymap
    tag = re.sub(r'[^\w\s]', '', keymap['title'].lower())
    tag = tag.replace(' ', '-')
    if prompt:
        return " [{}]".format(tag)
    elif keymap['slug'] == '':
        return tag
    else:
        return keymap['slug'].replace(' ', '-')

prompts = [
    ['title',       "What will the new article's title be? ",                       None],
    ['tags',        "What tags should the new article include? (comma separated) ", tagerizer],
    ['category',    "What category should the article associate with? ",            None],
    ['slug',        "What should the slug be? "                     ,               slugerizer],
    ['author',      "Who is the author? ",                                          usr_callback],
    ['summary',     "Please give a brief summary: ",                                None],
]

# Define the default RST file format
RST_FORMAT = """{title}
{underline}

:date: {year}-{month}-{day} {hour}:{minute}
:modified: {year}-{month}-{day} {hour}:{minute}
:tags: {tags}
:category: {category}
:slug: {slug}
:authors: {author}
:summary: {summary}


"""

# Define the default MD file format
MD_FORMAT = """Title: {title}
Date: {year}-{month}-{day} {hour}:{minute}
Modified: {year}-{month}-{day} {hour}:{minute}
Tags: {tags}
Category: {category}
Slug: {slug}
Authors: {author}
Summary: {summary}


"""

parser = argparse.ArgumentParser(prog='writenew', description=
            'Pelican ReStructuredText blog post build assistant.')
parser.add_argument('-o','--open',action='store_true',help=
            'Open the *.rst file in default editor after creation.')
parser.add_argument('-f','--filename',help=
            'Specific filename (if it should be different than title).')

def main( parser, keymap ):
    args = parser.parse_args()
    open_after   = args.open
    filename    = args.filename
    # Welcome User
    print("Welcome! Let's start that new article you're planning!")
    print("——————————————————————————————————————————————————————")
    # Gather Information - Allow User to "Back-Track" with Carrot Operator
    index = 0
    while True:
        prompt_set = prompts[index]
        prompt_msg = prompt_set[1]
        if prompt_set[2] is not None:
            prompt_msg += prompt_set[2](prompt=True)
        response = input(prompt_msg)
        if response == '^':
            index -= 1
            continue
        else:
            keymap[prompt_set[0]] = response
            if prompt_set[2] is not None:
                keymap[prompt_set[0]] = prompt_set[2]() # Call the callback function
            print(f"   {prompt_set[0].title()}: \"{keymap[prompt_set[0]]}\"") 
            index += 1
        if index >= len(prompts):
            break
    # Capture System-Determined Information
    keymap['underline'] = '#' * len(keymap['title'])
    keymap['year']  = time.strftime('%Y')
    keymap['month'] = time.strftime('%m')
    keymap['day']   = time.strftime('%d')
    keymap['hour']  = time.strftime('%H')
    keymap['minute']= time.strftime('%M')
    # Determine File Format
    file_type = input("Should the file be formatted as Markdown or ReStructuredText? [md, rst]   ")
    if file_type == '':
        file_type = 'md'
    # Determine Filename
    if filename in ['', None]:
        filename = f"{keymap['title'].lower().replace(' ','-')}.{file_type}"
        # Clean Filename
        filename = filename.replace('?','')
        filename = filename.replace('!','')
        filename = filename.replace('/','-')
        filename = filename.replace('\\','-')
    # Clean Filename
    filename = filename.replace('\\','/')
    filename = filename.replace(',','')
    filename = re.sub(r'-{2,}', '-', filename)
    filename = re.sub(r'\.{2,}', '.', filename)
    filename = filename.replace('`','')
    print("——————————————————————————————————————————————————————")
    if 'content/' not in filename:
        filename = './content/' + os.path.basename(filename)
    # Write Contents
    print("Writing contents to:", filename)
    with open(filename, 'w', encoding='utf-8') as fObj:
        if 'm' in file_type.lower():
            fObj.write( MD_FORMAT.format(**keymap) )
        else:
            fObj.write( RST_FORMAT.format(**keymap) )
    if not open_after:
        response = ''
        while response.upper() not in ['Y','N']:
            response = input("Would you like to start writing now? [Y,n]  ")
        if response.upper() == 'Y':
            open_after = True
    if open_after:
        subprocess.run(
            ["code", "--reuse-window", filename.replace('./',os.getcwd()+'/')],
            shell=True,
            check=False,
        )


if __name__ == '__main__':
    main( parser, keymap )

# END

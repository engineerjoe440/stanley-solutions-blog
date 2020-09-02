"""
`writenew.py`

Simple Python script to get a user started with writing a new Pelican blog post.

"""

import os
import time
import argparse

try:
    import win32api
    def usr_callback(prompt=False):
        usr = win32api.GetUserName()
        usr_str = ' [{}]'.format(usr)
        return usr_str if prompt else usr
except:
    def usr_callback(prompt=False):
        return ''

keymap = {}

def slugerizer():
    global keymap
    return keymap['slug'].replace(' ','-')

prompts = [
    ['title',       "What will the new article's title be? ",                       None],
    ['tags',        "What tags should the new article include? (comma separated) ", None],
    ['category',    "What category should the article associate with? ",            None],
    ['slug',        "What should the slug be? ",                                    slugerizer],
    ['author',      "Who is the author?{} ".format(usr_callback(prompt=True)),      usr_callback],
    ['summary',     "Please give a brief summary: ",                                None],
]

# Define the default RST file format
rst_format = """{title}
{underline}

:date: {year}-{month}-{day} {hour}:{minute}
:modified: {year}-{month}-{day} {hour}:{minute}
:tags: {tags}
:category: {category}
:slug: {slug}
:authors: {author}
:summary: {summary}


"""

parser = argparse.ArgumentParser(prog='writenew', description=
            'Pelican ReStructuredText blog post build assistant.')
parser.add_argument('-o','--open',action='store_true',help=
            'Open the *.rst file in default editor after creation.')
parser.add_argument('-f','--filename',help=
            'Specific filename (if it should be different than title).')

def main( parser, keymap ):
    args = parser.parse_args()
    openafter   = args.open
    filename    = args.filename
    # Welcome User
    print("Welcome! Let's start that new article you're planning!")
    print("——————————————————————————————————————————————————————")
    # Gather Information - Allow User to "Back-Track" with Carrot Operator
    index = 0
    while True:
        prompt_set = prompts[index]
        response = input(prompt_set[1])
        if response == '^':
            index -= 1
            continue
        else:
            keymap[prompt_set[0]] = response
            if prompt_set[2] != None:
                keymap[prompt_set[0]] = prompt_set[2]() # Call the callback function
            print("   "+prompt_set[0].title()+': "'+keymap[prompt_set[0]]+'"') 
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
    # Determine Filename
    if filename in ['', None]:
        filename = keymap['title'].lower().replace(' ','-') + '.rst'
    filename = filename.replace('\\','/')
    print("——————————————————————————————————————————————————————")
    if 'content/' not in filename:
        filename = './content/' + os.path.basename(filename)
    # Write Contents
    print("Writing contents to:", filename)
    with open(filename, 'w') as fObj:
        fObj.write( rst_format.format(**keymap) )
    if openafter:
        os.startfile(filename)


if __name__ == '__main__':
    main( parser, keymap )
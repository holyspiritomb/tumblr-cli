#!/usr/bin/env python3

import pytumblr
from configuration import consumer_key, consumer_secret, oauth_token, oauth_token_secret, selected_blog

client = pytumblr.TumblrRestClient(
         consumer_key,
         consumer_secret,
         oauth_token,
         oauth_token_secret)


def tags():
    print("Enter tags separated by commas.")
    input_string = input("> ")
    tag_list = input_string.split(",")
    return tag_list


def postbody():
    print('''Enter paragraphs one at a time, pressing enter after each.
    When finished, leave blank and press enter.''')
    paragraphs = []
    while True:
        paragraph = input("new paragraph > ")
        if paragraph:
            paragraphs.append("<p>" + paragraph + "</p>")
        else:
            break
    postbody = "\n".join(paragraphs)
    return postbody


print('''What type of post would you like to make?

Allowed options: text, chat, quote, link, photo, audio, video''')
posttype = input("> ")

if posttype == "text":
    client.create_text(
        blogname=selected_blog,
        state=input("published, draft, queue or private? > "),
        title=input("title > "),
        body=postbody(),
        tags=tags()
    )
elif posttype == "quote":
    client.create_quote(
        blogname=selected_blog,
        state=input("published, draft, queue or private? > "),
        quote=input("the quote > "),
        source=input("who said it? > "),
        tags=tags()
    )
elif posttype == "link":
    client.create_link(
        blogname=selected_blog,
        state=input("published, draft, queue or private? > "),
        title=input("title > "),
        url=input("URL of link > "),
        description=postbody(),
        tags=tags()
    )
elif posttype == "chat":
    print('''Enter chat lines one at a time, pressing enter after each.
    When finished, leave blank and press enter.''')
    lines = []
    while True:
        line = input("line of chat > ")
        if line:
            lines.append(line)
        else:
            break
    chat = '\n'.join(lines)
    client.create_chat(
        blogname=selected_blog,
        state=input("published, draft, queue or private? > "),
        title=input("title > "),
        conversation=chat,
        tags=tags()
    )
else:
    print(f"Sorry, {posttype} posts are not yet supported by this script.")

# Same as convert.py but this only converts a file from markdown to html
# I use it to test my markdown and to make sure there aren't any errors before updating the rss, json, and blog html file

import markdown
import sys


def readFile(filename):
    """
    Stores a file's content into a variable
    """
    fr = open(filename, 'r')
    the_file = fr.read()
    fr.close()
    return the_file


def compile(filename, header, footer):
    """
    Makes an html file with the header and footer.
    """
    f = open(filename, 'w')
    header = readFile(header)
    footer = readFile(footer)
    content = readFile("./templates/processing.html")

    f.write(header)
    f.write(content)
    f.write(footer)
    f.close()


def convert(file):
    """
    Converts given markdown file to html using the above functions
    """
    html_file_name = file.split(".md")[0] + ".html"
    try:
        markdown.markdownFromFile(
            input=file, output="./templates/processing.html")
        compile(html_file_name, "./templates/header.html",
                "./templates/footer.html")
        print("Success!!!!! HTML file created")
    except:
        print("epic fail!")


if __name__ == "__main__":
    file = str(sys.argv[1])
    convert(file)

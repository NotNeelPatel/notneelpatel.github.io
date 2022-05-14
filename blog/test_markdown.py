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
        UpdateSiteLinks(html_file_name)
    except:
        print("epic fail!")


def UpdateSiteLinks(file):
    md_file = readFile(file.split(".html")[0] + ".md")
    xml_dataString = md_file[5:md_file.index("--->")]
    xmltitle = xml_dataString[7:xml_dataString.index("date:")-1]
    xmldate = xml_dataString[len(
        xmltitle)+13:xml_dataString.index("description:")]
    xmldescription = xml_dataString[len(xmltitle)+1+len(xmldate)+24:-1]
    addComments(xmltitle, file)
    metadata(xmltitle, xmldescription, file)


def addComments(title, file):
    htmlfile = readFile(file)
    topHalf = htmlfile[:-554]
    bottomHalf = htmlfile[-554:]
    c = open(file, 'w')
    c.write(topHalf)
    c.write('data-page-id="'+title+'"\ndata-page-title="'+title+'"')
    c.write(bottomHalf)
    c.close()


def metadata(title, description, file):
    title = title + " - Neel Patel"
    htmlfile = readFile(file)
    topHalf = htmlfile[:641]
    bottomHalf = htmlfile[641:]
    m = open(file, 'w')
    m.write(topHalf)
    m.write('<meta property="og:title" content="'+title+'"/>\n<meta property="og:description" content="' +
            description+'"/>\n<meta property="og:url" content="notneelpatel.github.io/blog/'+file+'"/>')
    m.write(bottomHalf)
    m.close()


if __name__ == "__main__":
    file = str(sys.argv[1])
    convert(file)

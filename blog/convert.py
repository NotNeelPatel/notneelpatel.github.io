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
    """
    Updates feed.xml, searchindex.json and blog.html
    """
    # Use md file, which contains RSS information
    md_file = readFile(file.split(".html")[0] + ".md")
    xml_dataString = md_file[5:md_file.index("--->")]

    xmltitle = xml_dataString[7:xml_dataString.index("date:")-1]
    xmldate = xml_dataString[len(
        xmltitle)+12:xml_dataString.index("description:")]
    xmldescription = xml_dataString[len(xmltitle)+len(xmldate)+24:-1]

    # Write into the XML file
    old_xml = readFile("../feed.xml")
    old_xml = old_xml[:-18]
    x = open("../feed.xml", 'w')
    x.write(old_xml)
    x.write("\n\t\t<item>\n\t\t\t<title>"+xmltitle+"\n\t\t\t</title>\n\t\t\t<pubDate>"+xmldate+"\n\t\t\t</pubdate>\n\t\t\t<link>https://notneelpatel.github.io/blog/"+file +
            "</link>\n\t\t\t<guid>https://notneelpatel.github.io/blog/"+file+"</guid>\n\t\t\t<description>"+xmldescription+"\n\t\t\t</description>\n\t\t</item>\n\t</channel>\n</rss>")
    x.close()

    # Use the title of the md file and RSS information to create link titles
    date = file[:10]
    entry = (date + " [" + xmltitle + "](./blog/" + file + ")")

    # Use above information to generate new entry in json file
    old_json = readFile("../assets/searchindex.json")
    old_json = old_json[:-4]
    j = open("../assets/searchindex.json", 'w')
    j.write(old_json)
    j.write('},')
    j.write('\n\t{\n\t\t"title": "'+xmltitle+'",\n\t\t"date": "'+date +
            '",\n\t\t"url": "https://notneelpatel.github.io/blog/'+file+'",\n\t\t"description": "'+xmldescription+'"\n\t}\n]')
    j.close()

    # Write into Blog.html
    previous_content = readFile("./templates/bloglist.md")
    previous_content = previous_content[31:]
    flist = open("./templates/bloglist.md", 'w')
    flist.write("## Blog\n[RSS Feed](./feed.xml)\n\n" +
                entry + "\n\n"+xmldescription+"...\n___" + previous_content)
    flist.close()
    markdown.markdownFromFile(
        input="./templates/bloglist.md", output="./templates/processing.html")
    compile("../blog.html", "./templates/blog_header.html",
            "./templates/blog_footer.html")

    print("Success!!!!! Added to Blog page")


if __name__ == "__main__":
    file = str(sys.argv[1])
    convert(file)

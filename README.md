# VA-Markup

Creating Mark up files of VistA docx files.

# Process

A given link is parsed using Snapy and all the links are followed in order to extract docx download links.

These links are then used to download the docx files then using them to create md files using Pandoc.

A complete site crawling example is not shown here, just a proof of concept (PoC) The PoC is split into 2 parts, **scrape.py** scapes https://www.va.gov/vdl/application.asp?appid=5 and extracts all docx files on the page, converting them to md files accordingly (as contained in this repo)

**scrape1.py** scrapes https://www.va.gov/vdl/section.asp?secid=2, following links and extracting all links with docx download links. These links are added to a links.txt file

# Running the demo

    git clone github.com/RamSailopal/VA-Markup.git
    
    cd VA-Markup

    docker run -v $PWD:/home/tmp --entrypoint /home/tmp/entrypoint.sh -it ubuntu /bin/bash

# References

Snapy - https://pypi.org/project/snapy/

Pandoc - https://pandoc.org/

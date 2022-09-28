# VA-Markup

Creating Mark up files of VistA docx files.

# Process

A given link is parsed using Snapy and all the links are followed in order to extract docx download links.

These links are then used to download the docx files then using them to create md files using Pandoc.

A complete site crawling example is not shown here, just a proof of concept (PoC) The PoC is split into 2 parts, **scrape.py** scapes https://www.va.gov/vdl/application.asp?appid=5 and extracts all docx files on the page, converting them to md files accordingly (as contained in this repo)

Conversions were also made from docx format to html the links to the resulting html files as below:

https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2dg.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2ig.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2p8_dac_ug.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2rn.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2tm.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2um1.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_2um2.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_krn8_file_security.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/fm22_tutorial.html
https://htmlpreview.github.io/?https://github.com/RamSailopal/VA-Markup/blob/main/scrn_tut.html

**scrape1.py** scrapes https://www.va.gov/vdl/section.asp?secid=2, following links and extracting all links with docx download links. These links are added to a links.txt file

# Running the demo

    git clone github.com/RamSailopal/VA-Markup.git
    
    cd VA-Markup

    docker run --name markup -v $PWD:/home/tmp --entrypoint /home/tmp/entrypoint.sh -d ubuntu
    
Then to run scrape.py:

    docker exec -it markup /bin/bash
    
    cd /home/tmp
    
    scrapy runspider scrape.py
    
To run scrape1.py:

    scrapy runspider scrape1.py

# References

Snapy - https://pypi.org/project/snapy/

Pandoc - https://pandoc.org/

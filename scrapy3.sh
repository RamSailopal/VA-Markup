#!/bin/bash
if [[ "$1" == "" ]]
then
    echo "Pass the address of the base address to crawl as the first parameter"
    exit
fi
echo -e "<html>\n" > table.html
echo -e "<style>\n" >> table.html
echo -e "table, th, td {\nborder: 1px solid black;\n}" >> table.html
echo -e "</style>\n" >> table.html
echo -e  "<body>\n" >> table.html
echo -e "<table>\n" >> table.html
echo -e "<tr><th>Section</th><th>Package</th><th>Title</th><th>DOCX</th><th>PDF</th></tr>\n" >> table.html
sed -i "s@start_urls = \['.*'\]@start_urls = ['"$1"']@" scrape3.py
scrapy runspider scrape3.py >> table.html
echo -e "</table>\n" >> table.html
echo -e "</body>\n" >> table.html
echo -e "</html>\n" >> table.html  
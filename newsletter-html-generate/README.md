## Background:
An e-commerce client requires a weekly newsletter index.html file to be sent to them with custom content/imagery.
The index.html file is a fixed template (built in house), loaded into their own newsletter system (for which we do not have access).
The requirement for our team is basic: we receive a PSD file from the client, and we then:
    1. Create the product/banner imagery from the PSD for the newsletter
    2. Set the HTML content (e.g. title, subheader, product titles, product image hrefs, buttons) to match the PSD
    3. Test the newsletter and send it back to the client.

This script was built to automate step 2 - as the newsletter HTML is quite long (email HTML is almost always complex and never as clean as "website" HTML), 
updating it is tedious and may result in copy/paste errors. The intention is to reduce time spent to build the newsletter, and avoid copy/paste errors within HTML tag.

## Solution:
As a learning exercise, I built this simple script that contains all the HTML,
with all dynamic variables stripped out and replaced by Python variables which are defined in a central function.
This one script contains all the code, as is a first-time attempt for automation of this process.

* Note: The code in this script has been modified and does not contain the original (client) newsletter HTML.
It is simplified and is useful for a beginner to learn functions, how to dynamically replace values in strings, loop through a list of products. write a file, open a browser (with the index.html file).

Further work to be done:
a. Use Django framework to utilize web/HTML features and MVC model so that input can be accepted and code can be optimized.
b. Change input so this script does not need to be modified, e.g. input can come from a text file or database, but take into account that simplicity is required as the purpose is to save time for the developer.

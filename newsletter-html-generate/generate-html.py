'''
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

'''

import webbrowser

def buildHTML():
    ## Change this data as required
    mmdd = "01-08"
    title = "Newletter title"
    preheader = "Free US delivery on orders over $35"

    ## HEADER
    htmlcode = buildHTMLHeader(title, preheader)

    ## PRODUCTS - dict byindex (used for image ID, e.g. p1.jpg) with values [caption, URL] per product). Displaying one brand at a time for this newsletter.
    products_set1 = {'1': ["Tshirt A", "http://www.mydomain.com/armani/a/"],
                   '2': ["Tshirt B", "http://www.mydomain.com/armani/b/"],
                   '3': ["Tshirt C", "http://www.mydomain.com/armani/c/"],
                   '4': ["Tshirt D", "http://www.mydomain.com/armani/d/"],
                   '5': ["Tshirt E", "http://www.mydomain.com/armani/e/"],
                   '6': ["Tshirt F", "http://www.mydomain.com/armani/f/"],
                   '7': ["Tshirt G", "http://www.mydomain.com/armani/g/"],
                   '8': ["Tshirt H", "http://www.mydomain.com/armani/h/"]
                   }
    htmlcode += buildProductHTML(mmdd, "http://www.mydomain.com/armani/", "Armani", products_set1, True)

    products_set2 = {'9': ["White sneakers","http://www.mydomain.com/filling-pieces/t1/"],
                     '10': ["Curve roots sneakers", "http://www.mydomain.com/filling-pieces/crs/"],
                     '11': ["Mondo sneaker", "http://www.mydomain.com/filling-pieces/mn2/"],
                     '12': ["Red hoodie", "http://www.mydomain.com/filling-pieces/redhoodie/"]
                     }
    htmlcode += buildProductHTML(mmdd, "http://www.mydomain.com/filling-pieces/", "Filling Pieces", products_set2, True, "fp")

    ## FOOTER
    htmlcode += buildFooter()

    return htmlcode

# Other HTML functions and rest of code --- do not edit ---
def buildHTMLHeader(title, preheader):
    header = """
    <!doctype html>
    <html style="opacity: 1;" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
    <head>
       <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
       <title>{0}</title>
    </head>
    """ # <title> will be dynamically updated
    body_start = """
    <body style="">
        <span class="preheader">{0}</span>
    	Body starts here
    	"""  # <span class="preheader"> will be updated
    htmlcode = header.format(title) + body_start.format(preheader)
    return htmlcode

def buildFooter():
    # returns static HTML, no variables
    return """	
        <!-- footer starts here -->
    	<div>
    	    Footer here
    	</div>
    </div>
    </body>
    </html>"""

def buildProductBanner(mmdd, mainbannerurl, imgname_aux=''):
    if not mainbannerurl:
        return ""  # no product banner to display

    # mainbannerurl is passed, so build the product banner. imgname_aux is a postfix to the banner image name.
    # note in other functions we used string.format, but here we directly use the variable name, which is purely for learning. The .format code looks more clean, but the following is easier for referencing variable names while writing the code
    return """	
        <!--main banner-->
    	<a target="_blank" href=\"""" + mainbannerurl + """\" style="text-decoration: none;"><img alt="" class="hiddenimgdesk1" height="auto" src="http://www.mydomain.com/images/email/2018/""" + mmdd + """/main_banner_desktop""" + imgname_aux + """.jpg" style="margin: auto; display: block; line-height: 100%; height: auto; max-width: 100%;" width="800" /></a>"""

def aux_get4rowsHTML():
    # Simplified product HTML for 4 product images in a row (demonstration purposes only)

    return """
        <!-- Product row -->
        <div class="products4">
            <a target="_blank" href="{3}">
                <img alt="{4} {2}" src="http://www.mydomain.com/images/email/2018/{0}/p{1}.jpg" style="display: block; margin: auto; outline: none; text-decoration: none; border: none; line-height: 1px; margin-left: auto; margin-right: auto; height: auto; width: 95%;" width="185" />
            </a>
            <a target="_blank" href="{7}">
                <img alt="{8} {6}" src="http://www.mydomain.com/images/email/2018/{0}/p{5}.jpg" style="display: block; margin: auto; outline: none; text-decoration: none; border: none; line-height: 1px; margin-left: auto; margin-right: auto; height: auto; width: 95%;" width="185" />
            </a>
            <a target="_blank" href="{11}">
                <img alt="{12} {10}" src="http://www.mydomain.com/images/email/2018/{0}/p{9}.jpg" style="display: block; margin: auto; outline: none; text-decoration: none; border: none; line-height: 1px; margin-left: auto; margin-right: auto; height: auto; width: 95%;" width="185" />
            </a>
            <a target="_blank" href="{15}">
                <img alt="{16} {14}" src="http://www.mydomain.com/images/email/2018/{0}/p{13}.jpg" style="display: block; margin: auto; outline: none; text-decoration: none; border: none; line-height: 1px; margin-left: auto; margin-right: auto; height: auto; width: 95%;" width="185" />
            </a>		
        </div>
        <!-- end Product row -->
    """

def buildProductHTML(mmdd, brandurl, brandname, products, displaybanner=True, bannerimgname_aux=''):
    # Accepts a products list, and loops through to display 4 in a row (according to the template I am using). 
    # Also generates HTML for a product banner (if displayBanner==True).
    # Of course, change this as per your own HTML requirement.
    
    # Check if a product banner is to be displayed
    if (displaybanner):
        htmlcode = buildProductBanner(mmdd, brandurl, bannerimgname_aux)
    else:
        htmlcode = ""

    # 4 products in a row, so we are only going to process blocks of 4 products at a time. If any extra are sent by mistake, we ignore the balance odd ones.
    prodcount = 0
    temp4products = {}

    for key, product in products.items():
        prodcount += 1
        try:
            overridebrand = product[2]
        except:
            overridebrand = brandname

        temp4products[prodcount] = {'key': key, 'caption': product[0], 'url': product[1],
                                    'brand': overridebrand}  # a product has a key, an alt tag/caption, URL, optional brand override for its description

        if (prodcount == 4):
            # set of 4 rows of products
            htmlcode += aux_get4rowsHTML().format(mmdd,
                                                  temp4products[1]['key'], temp4products[1]['caption'],
                                                  temp4products[1]['url'], temp4products[1]['brand'],
                                                  temp4products[2]['key'], temp4products[2]['caption'],
                                                  temp4products[2]['url'], temp4products[2]['brand'],
                                                  temp4products[3]['key'], temp4products[3]['caption'],
                                                  temp4products[3]['url'], temp4products[3]['brand'],
                                                  temp4products[4]['key'], temp4products[4]['caption'],
                                                  temp4products[4]['url'], temp4products[4]['brand']
                                                  )
            prodcount = 0  # reset as we only consider blocks of 4 products
            temp4products = {}

    return htmlcode


# Main code - write the file
f = open('index.html', 'w')
f.write(buildHTML())
f.close()

# You can also open the file directly in your default web browser:
# filename = 'file:///path/to/htdocs/' + 'index.html'
# webbrowser.open_new_tab(filename)
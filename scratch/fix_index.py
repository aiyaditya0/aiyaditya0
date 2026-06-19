with open('index.html', 'rb') as f:
    content = f.read()

target_crlf = b'\r\n    </div><!-- /products-grid -->'
replacement_crlf = b'\r\n      <!-- DYNAMIC_INDIVIDUAL_PRODUCTS_END -->\r\n    </div><!-- /products-grid -->'

target_lf = b'\n    </div><!-- /products-grid -->'
replacement_lf = b'\n      <!-- DYNAMIC_INDIVIDUAL_PRODUCTS_END -->\n    </div><!-- /products-grid -->'

if target_crlf in content:
    content = content.replace(target_crlf, replacement_crlf)
    print("CR-LF End Tag added successfully!")
elif target_lf in content:
    content = content.replace(target_lf, replacement_lf)
    print("LF End Tag added successfully!")
else:
    print("End Tag Target not found!")

with open('index.html', 'wb') as f:
    f.write(content)

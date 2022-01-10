#generation page web
page = open("index.html","w+")
title = "test2"

page.write("<html>")
page.write("<head>")
page.write('<meta charset="utf-8" />')
page.write("<title>")
page.write( title )
page.write("</title>")
page.write("</head>")
page.write("<body>")
page.write("</body>")
page.write("</html>")

page.close




    
    




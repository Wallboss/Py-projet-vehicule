#generation page web
# page = open("index.html","w+")


# page.write("<html>")
# page.write("<head>")
# page.write('<meta charset="utf-8" />')
# page.write("<title>")
# page.write( title )
# page.write("</title>")
# page.write("</head>")
# page.write("<body>")
# page.write("<h2>")
# page.write( h2 )
# page.write("</h2>")
# page.write("</body>")
# page.write("</html>")
# 
# page.close


title = "Voiture"
h2 = "titre h2"
with open("index.html","w+") as file:
    file.write("<html>")
    #head
    file.write("<head>")
    file.write('<meta charset="utf-8" />')
    file.write("<title>")
    file.write( title )
    file.write("</title>")
    file.write("</head>")
    #body
    file.write("<body>")
    file.write("<h2>")
    file.write( h2 )
    file.write("</h2>")
    file.write("</body>")
    
    file.write("</html>")
    
    file.close
    




    
    




import webbrowser
from tkinter import *

#This creates our html file using Python!
#Originally, I used x instead of w.
#Since I already created the file with x, I'm just overwriting it now with w.
f = open("VeryBasicWebPage.html", "w")
f.write("""<html>
                <body>
                    <h1>
                        Stay tuned for our amazing summer sale!
                    </h1>
                </body>
            </html>""")
f.close()

#This will open our html file in a new tab!
g = webbrowser.open_new_tab("VeryBasicWebPage.html")

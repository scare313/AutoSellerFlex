from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#Create a QApplication instance. 
#This is necessary for any PyQt5 application, and it needs to be done before any other widgets are created.

app = QApplication([])

#Create a QWebEngineView widget, which is the widget that will display the webpage.
web_view = QWebEngineView()

#Create a QLineEdit widget, which will be used as the address bar.
address_bar = QLineEdit()

#Create a QVBoxLayout to hold the address bar and the web view. 
#This layout will be used to organize the widgets on the screen.
layout = QVBoxLayout()
layout.addWidget(address_bar)
layout.addWidget(web_view)

#Create a QWidget to hold the layout. This widget will be used as the main window of the application.
main_window = QWidget()
main_window.setLayout(layout)

#Create a function to load the URL entered in the address bar into the web view. 
#Connect the function to the returnPressed signal of the address bar.
def load_url():
    
    def on_load_finished(status):
        if status:
            print("Web page loaded successfully.")
            result = web_page.runJavaScript("document.getElementById('login-button').click()")
            print(result)
        
        else:
            print("Web page failed to load.")


    
    print("ReturnButtonPressed")
    url = address_bar.text()
    web_view.loadFinished.connect(on_load_finished)
    web_view.load(QUrl(url))
    
   

    web_page = web_view.page()
    print(web_page)
    #web_page.runJavaScript("document.getElementById('ap_email').value()")

    
    
address_bar.returnPressed.connect(load_url)


#Show the main window and start the application.
main_window.show()
app.exec_()


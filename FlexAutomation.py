from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



app = QApplication([])
web_view = QWebEngineView()
layout = QVBoxLayout()
layout.addWidget(web_view)
main_window = QWidget()
main_window.resize(600,400)
main_window.setLayout(layout)

profile = QWebEngineProfile(f"cookie.txt", web_view)
webpage = QWebEnginePage(profile, web_view)


url = 'https://sellerflex.amazon.in/pack'
web_view.load(QUrl(url))



main_window.show()
app.exec_()
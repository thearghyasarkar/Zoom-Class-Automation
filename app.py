from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon
from main import join_meeting, notify, handle_input_data
import sys, os 
import webbrowser
import schedule
from config import python_bin_path, main_file_path
import playsound

class ZoomAutomation(QDialog):
    def __init__(self):
        super(ZoomAutomation, self).__init__()
        loadUi("./app_ui/landing.ui",self)
        self.start_schedule.clicked.connect(lambda: self.schedulerHandler(JSON=False))
        
    def schedulerHandler(self, JSON=True):
        if JSON==False:
            data = []
            classdata_raw = self.data_field.toPlainText()
            classdata_raw= classdata_raw.replace("\n", " ")
            classdata_raw= classdata_raw.replace("(", "\\(")
            os.system(f"{python_bin_path} main.py '{classdata_raw}'")
        
        # for meeting in data:
        #     meeting_time = meeting["time"]
        #     schedule.every().day.at(meeting_time).do(join_meeting, meeting)
        #     print(schedule.get_jobs())
                
        
app = QApplication(sys.argv)
window = ZoomAutomation()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setWindowIcon(QIcon("Zoom"))
widget.setWindowTitle("Zoom Automation")
widget.setWindowOpacity(1)
widget.setFixedHeight(598)
widget.setFixedWidth(565)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

# Coded by Yongzhi and Jun Wei

style_home = """

QPushButton {
    background-color:darkseagreen; 
    font-size: 21px;
    border-radius: 10px;
}

QPushButton:hover {
    font-size: 21.25px;
    background-color: #a1d4a1;
    color: #293829;
    font-weight: bold;
}

QLabel#Time_Date_Label {
    background-color:silver; 
    font-size: 21px;
    border-radius: 5px;
    padding-left: 70px;
}

QPushButton#button_exit{
    background-color:lightcoral;
    font:bold; 
    font-size: 21px;
    border-radius: 10px;
}

QPushButton#button_exit:hover{
    font-size: 21.5px;
    color: black;
    background-color: #ea4848;
    font-weight: bold;
}

"""

style_stalls = """

QMainWindow{
    background-color: #121212;
}

QPushButton{
    background-color: #BB86FC;
    border-radius: 3px;
}

QPushButton:hover{
    background-color: #8f38fa
}

QListWidget{
    background-color: #3700B3;
}

QListWidget::item{
    background-color: #03DAC6;
    border: 1px solid black;

}

QListWidget::item:hover{
    background-color: #03b09f;
}

QListWidget::item:selected{

}

QTextEdit#queueTextBox{
    font-size: 20px;
}

QMessageBox QPushButton{
    padding: 3px;
    background-color: transparent;
}

QMessageBox QPushButton:hover{
    background-color: #d5b4fd;
}

QMessageBox QLabel{
    color: black;
    background-color: white;
}

QLabel{
    font-size: 22px;
    color: white; 
    text-align: center;
    background-color: #15120d;
}

QScrollArea{
    background-color: #15120d;
}


QScrollBar:vertical{background-color: #15120d;}

QScrollBar::handle:vertical {background-color:#4f4430;}

QScrollBar::add-line:vertical {
    background-color: #15120d;
    subcontrol-position: bottom;
}

QScrollBar::sub-line:vertical {
    background-color: #15120d;
    subcontrol-position: top;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

"""

style_datetime = """

QLabel#calendar_label{
    background-color:lightgrey; 
    font-size: 21px;
    border-radius: 10px;
}

QTimeEdit#timeWidget{
    font-size: 20px;
}

QPushButton{
    font-size: 18px;
}


"""

style_opHours = """

QLabel{
    background-color:rgba(0,0,0,0%); 
    font-size: 30px; 
    color:white;
}

QLabel#operatingHeader{
    font-size: 50px; 
}

QLabel#stallLabel{
    font-size: 21px;
    border-radius: 5px;
}

QPushButton#backButton{
    background-color:gold; 
    font-size: 21px; 
    border-radius: 10px;
}

QPushButton#backButton:hover{
    background-color: #e3af05;
}

QComboBox{
    background-color:lightgrey; 
    font-size: 21px;
    border-radius: 5px;
}

QComboBox{
    background-color:lightgrey; 
    font-size: 21px;
    border-radius: 5px;
}




"""
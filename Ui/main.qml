import QtQuick 2.0
import QtQuick.Controls 2.13


ApplicationWindow {
    visible: true
    width: 720
    height: 530
    property alias label1Text: label1.text
    title: qsTr("Loop Translate")
    ToolBar {
        id: titleBackground
        x: 0
        y: 0
        width: 720
        height: 48

        Label {
            id: title
            x: 15
            y: 12
            color: "#ffffff"
            text: qsTr("Loop Translate")
            font.pointSize: 15
            font.family: "Arial"
        }
    }

    Button {
        id: doStart
        objectName: "doStart"
        y: 79
        width: 70
        height: 45
        text: "Start"
        anchors.horizontalCenterOffset: -222
        font.capitalization: Font.Capitalize
        font.family: "Arial"
        highlighted: true
        anchors.horizontalCenter: parent.horizontalCenter
    }


    TextField {
        id: cycles
        objectName: "cycles"
        x: 20
        y: 84
        width: 77
        height: 40
        text: qsTr("")
        font.family: "Arial"
        placeholderText: "Cycles"
    }
    
    ScrollView {
        id: scrollView
        x: 20
        y: 130
        width: 330
        height: 320
        
        TextArea {
            objectName: "translateText"
            id: inputText
            text: qsTr("")
            placeholderText: qsTr("Input text which you need translate")
            font.strikeout: false
            font.family: "Arial"
            selectByMouse: true
            textFormat: Text.AutoText
            wrapMode: Text.WrapAtWordBoundaryOrAnywhere
        }
    }
    
    ScrollView {
        id: scrollView1
        x: 370
        y: 130
        width: 330
        height: 320
        TextArea {
            id: layoutText
            objectName: "layoutText"
            text: qsTr("")
            font.strikeout: false
            placeholderText: qsTr("Translate result will export here")
            font.family: "Arial"
            wrapMode: Text.WrapAtWordBoundaryOrAnywhere
            selectByMouse: true
            textFormat: Text.AutoText
        }
    }

    Label {
        id: label1
        x: 20
        y: 450
        width: 680
        height: 70
        color: "#37474f"
        text: "This is an application based on the Google Translate website API, which can translate your sentences or articles in a loop to achieve a funny effect\n\\nOpensource URL: https://github.com/Flyfish2333/loop_translate"
        font.wordSpacing: 0
        font.pointSize: 9
        textFormat: Text.AutoText
        wrapMode: Text.WrapAtWordBoundaryOrAnywhere
        font.family: "Arial"
    }




}

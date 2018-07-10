import QtQuick 2.2
import QtQuick.Controls 2.1

Rectangle {
    width: 320;
    height: 240;
    color: "gray";
    
    Button {
        text: "Quit";
        anchors.centerIn: parent;
        onClicked: {
            Qt.quit();
        }
    }
}
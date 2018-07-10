import QtQuick 2.2
import QtQuick.Window 2.1

Window{
    visible:true;
    width:360;
    height:360;

    MouseArea {
        anchors.fill: parent;
        onClicked: {
            Qt.quit();
        }
    }

    Text{
        text: qsTr("Hello Qt Quick app");
        anchors.centerIn: parent;
    }
}

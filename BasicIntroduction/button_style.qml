import QtQuick 2.10
import QtQuick.Controls 2.1
import QtQuick.Controls 1.2 as QQC1
import QtQuick.Controls.Styles 1.4

Rectangle {
    width: 300;
    height: 200;
    QQC1.Button {
        text: "Quit";
        anchors.centerIn: parent;
        /*QtQuick.Controls 1.2 版本中 */

        style: ButtonStyle {
            background: Rectangle {
                implicitWidth: 70;
                implicitHeight: 25;
                border.width: control.pressed ? 2 : 1;
                border.color: (control.hovered || control.pressed) ? "green" : "#888888";
            }
        }

        //            contentItem: Rectangle {
        //                implicitWidth: 70;
        //                implicitHeight: 25;
        //                border.width: control.pressed ? 2 : 1;
        //                border.color: (control.hovered || control.pressed) ? "green" : "#888888";
        //            }
     }

     //onClicked: Qt.quit();
}

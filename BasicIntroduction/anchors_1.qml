import QtQuick 2.2

Rectangle{
    height: 300;
    width: 600;

    Rectangle{
        color: "blue";
        anchors.fill: parent;
        border.width: 10;
        border.color: "#888888";

        Rectangle{
            anchors.centerIn: parent
            height: 100;
            width: 100;
            color: "#00c000";
            border.width: 2;
            border.color: "black";
            antialiasing: true;
        }
    }


}

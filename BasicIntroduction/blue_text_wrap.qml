import QtQuick 2.2

Rectangle {
    width: 320;
    height: 200;
    Text {
        width: 150;
        height: 100;
        //wrapMode: Text.Wrap;    //长度不足换行
        elide: Text.ElideRight;     //长度不足省略
        font.bold: true;
        font.pixelSize: 24;
        font.underline: true;
        text: "Hello Blue Text Hello Everyone All People";
        anchors.centerIn: parent;
        color: "blue";
    }
}

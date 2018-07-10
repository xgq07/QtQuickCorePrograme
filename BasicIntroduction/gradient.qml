import QtQuick 2.2
import QtQuick.Window 2.1

Rectangle{
    width: 100;
    height: 100;
    //rotation:90;
    gradient: Gradient{
        GradientStop{
            position: 0.0; color: "#202020";
        }
        GradientStop{
            position: 0.33; color: "blue";
        }
        GradientStop{
            position: 0.66; color: "#FFFFFF";
        }
        GradientStop{
            position: 1.0; color: "red";
        }
    }
}

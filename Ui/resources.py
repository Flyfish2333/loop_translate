# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 5.14.0
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x7f\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0a\x0d\x0a[Un\
iversal]\x0d\x0aTheme=\
System\x0d\x0aAccent=R\
ed\x0d\x0a\x0d\x0a[Material]\
\x0d\x0aTheme=Light\x0d\x0aA\
ccent=Teal\x0d\x0aPrim\
ary=BlueGrey\x0d\x0a\
\x00\x00\x0a\xce\
i\
mport QtQuick 2.\
0\x0d\x0aimport QtQuic\
k.Controls 2.13\x0d\
\x0a\x0d\x0a\x0d\x0aApplication\
Window {\x0d\x0a    vi\
sible: true\x0d\x0a   \
 width: 720\x0d\x0a   \
 height: 530\x0d\x0a  \
  property alias\
 label1Text: lab\
el1.text\x0d\x0a    ti\
tle: qsTr(\x22Loop \
Translate\x22)\x0d\x0a   \
 ToolBar {\x0d\x0a    \
    id: titleBac\
kground\x0d\x0a       \
 x: 0\x0d\x0a        y\
: 0\x0d\x0a        wid\
th: 720\x0d\x0a       \
 height: 48\x0d\x0a\x0d\x0a \
       Label {\x0d\x0a\
            id: \
title\x0d\x0a         \
   x: 15\x0d\x0a      \
      y: 12\x0d\x0a   \
         color: \
\x22#ffffff\x22\x0d\x0a     \
       text: qsT\
r(\x22Loop Translat\
e\x22)\x0d\x0a           \
 font.pointSize:\
 15\x0d\x0a           \
 font.family: \x22A\
rial\x22\x0d\x0a        }\
\x0d\x0a    }\x0d\x0a\x0d\x0a    B\
utton {\x0d\x0a       \
 id: doStart\x0d\x0a  \
      objectName\
: \x22doStart\x22\x0d\x0a   \
     y: 79\x0d\x0a    \
    width: 70\x0d\x0a \
       height: 4\
5\x0d\x0a        text:\
 \x22Start\x22\x0d\x0a      \
  anchors.horizo\
ntalCenterOffset\
: -222\x0d\x0a        \
font.capitalizat\
ion: Font.Capita\
lize\x0d\x0a        fo\
nt.family: \x22Aria\
l\x22\x0d\x0a        high\
lighted: true\x0d\x0a \
       anchors.h\
orizontalCenter:\
 parent.horizont\
alCenter\x0d\x0a    }\x0d\
\x0a\x0d\x0a\x0d\x0a    TextFie\
ld {\x0d\x0a        id\
: cycles\x0d\x0a      \
  objectName: \x22c\
ycles\x22\x0d\x0a        \
x: 20\x0d\x0a        y\
: 84\x0d\x0a        wi\
dth: 77\x0d\x0a       \
 height: 40\x0d\x0a   \
     text: qsTr(\
\x22\x22)\x0d\x0a        fon\
t.family: \x22Arial\
\x22\x0d\x0a        place\
holderText: \x22Cyc\
les\x22\x0d\x0a    }\x0d\x0a   \
 \x0d\x0a    ScrollVie\
w {\x0d\x0a        id:\
 scrollView\x0d\x0a   \
     x: 20\x0d\x0a    \
    y: 130\x0d\x0a    \
    width: 330\x0d\x0a\
        height: \
320\x0d\x0a        \x0d\x0a \
       TextArea \
{\x0d\x0a            o\
bjectName: \x22tran\
slateText\x22\x0d\x0a    \
        id: inpu\
tText\x0d\x0a         \
   text: qsTr(\x22\x22\
)\x0d\x0a            p\
laceholderText: \
qsTr(\x22Input text\
 which you need \
translate\x22)\x0d\x0a   \
         font.st\
rikeout: false\x0d\x0a\
            font\
.family: \x22Arial\x22\
\x0d\x0a            se\
lectByMouse: tru\
e\x0d\x0a            t\
extFormat: Text.\
AutoText\x0d\x0a      \
      wrapMode: \
Text.WrapAtWordB\
oundaryOrAnywher\
e\x0d\x0a        }\x0d\x0a  \
  }\x0d\x0a    \x0d\x0a    S\
crollView {\x0d\x0a   \
     id: scrollV\
iew1\x0d\x0a        x:\
 370\x0d\x0a        y:\
 130\x0d\x0a        wi\
dth: 330\x0d\x0a      \
  height: 320\x0d\x0a \
       TextArea \
{\x0d\x0a            i\
d: layoutText\x0d\x0a \
           objec\
tName: \x22layoutTe\
xt\x22\x0d\x0a           \
 text: qsTr(\x22\x22)\x0d\
\x0a            fon\
t.strikeout: fal\
se\x0d\x0a            \
placeholderText:\
 qsTr(\x22Translate\
 result will exp\
ort here\x22)\x0d\x0a    \
        font.fam\
ily: \x22Arial\x22\x0d\x0a  \
          wrapMo\
de: Text.WrapAtW\
ordBoundaryOrAny\
where\x0d\x0a         \
   selectByMouse\
: true\x0d\x0a        \
    textFormat: \
Text.AutoText\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    Label {\x0d\x0a\
        id: labe\
l1\x0d\x0a        x: 2\
0\x0d\x0a        y: 45\
0\x0d\x0a        width\
: 680\x0d\x0a        h\
eight: 70\x0d\x0a     \
   color: \x22#3747\
4f\x22\x0d\x0a        tex\
t: \x22This is an a\
pplication based\
 on the Google T\
ranslate website\
 API, which can \
translate your s\
entences or arti\
cles in a loop t\
o achieve a funn\
y effect\x5cn\x5c\x5cnOpe\
nsource URL: htt\
ps://github.com/\
Flyfish2333/loop\
_translate\x22\x0d\x0a   \
     font.wordSp\
acing: 0\x0d\x0a      \
  font.pointSize\
: 9\x0d\x0a        tex\
tFormat: Text.Au\
toText\x0d\x0a        \
wrapMode: Text.W\
rapAtWordBoundar\
yOrAnywhere\x0d\x0a   \
     font.family\
: \x22Arial\x22\x0d\x0a    }\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x000\x00\x00\x00\x00\x00\x01\x00\x00\x00\x83\
\x00\x00\x01s\xd3\x1b\x08.\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01s\x83\xd8\xf8J\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

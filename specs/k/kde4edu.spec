
%def_disable avogadro
%def_disable kpercentage
%def_disable qalculate
%def_enable openbabel
%def_enable artikulate
%def_disable facile

%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_K4apps/parley/plugins/*.py

%define rname kdeedu
Name: kde4edu
%define major 15
%define minor 12
%define bugfix 3
Version: %major.%minor.%bugfix
Release: alt7%ubt

Packager: Sergey V Turchin <zerg at altlinux dot org>

Group: Graphical desktop/KDE
Summary: Free Educational Software based on the KDE technologies
License: GPL
Url: http://edu.kde.org

%if_enabled artikulate
Requires: %name-artikulate = %version-%release
%endif
Requires: %name-kqtquickcharts = %version-%release
Requires: %name-blinken = %version-%release
Requires: %name-cantor = %version-%release
Requires: %name-kalgebra = %version-%release
Requires: %name-kalzium = %version-%release
Requires: %name-kanagram = %version-%release
Requires: %name-kbruch = %version-%release
Requires: %name-kgeography = %version-%release
Requires: %name-khangman = %version-%release
Requires: %name-kig = %version-%release
Requires: %name-kiten = %version-%release
Requires: %name-klettres = %version-%release
Requires: %name-kmplot = %version-%release
%if_enabled kpercentage
Requires: %name-kpercentage = %version-%release
%endif
Requires: %name-kstars = %version-%release
Requires: %name-ktouch = %version-%release
Requires: %name-kturtle = %version-%release
Requires: %name-parley = %version-%release
Requires: %name-kwordquiz = %version-%release
Requires: %name-step = %version-%release
Requires: kde4-marble
Requires: %name-rocs = %version-%release

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Patch1: alt-kstars-fix-compile.patch
Patch2: alt-kturtle-default-language.patch
Patch3: alt-find-luajit.patch
Patch4: alt-rocs-fix-compile.patch

# Automatically added by buildreq on Thu Oct 16 2008 (-bi)
#BuildRequires: boost-python-devel eigen facile gcc-c++ getfemxx indilib-devel kde4base-runtime-devel kde4base-workspace-devel libXScrnSaver-devel libXcomposite-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libbfd-devel libcfitsio-devel libcln-devel libgmp-devel libgsl-devel libjpeg-devel libncurses-devel libnova-devel libopenbabel-devel libpth-devel libqalculate-devel libreadline-devel libusb-devel libxkbfile-devel libxslt-devel nvidia_glx_177.80 openbabel python-modules-encodings rpm-build-ruby subversion xorg-xf86vidmodeproto-devel xsltproc
BuildRequires(pre): kde4base-workspace-devel rpm-build-ubt
BuildRequires: python-modules-encodings python-devel boost-devel boost-python-devel eigen2 eigen3 gcc-c++ libindi-devel
BuildRequires: libbfd-devel libcfitsio-devel wcslib-devel libcln-devel libgmp-devel libgsl-devel libjpeg-devel libncurses-devel libnova-devel
BuildRequires: libpth-devel libreadline-devel libusb-devel
%if_enabled qalculate
BuildRequires: libqalculate-devel
%endif
BuildRequires: libluajit-devel
%if_enabled artikulate
BuildRequires: qt-gstreamer1-devel
%endif
BuildRequires: ocaml4
%if_enabled facile
BuildRequires: facile
%endif
BuildRequires: xplanet attica-devel libspectre-devel libgps-devel qt4-mobility-devel
BuildRequires: libxslt-devel xsltproc libglew-devel
%if_enabled openbabel
BuildRequires: libopenbabel-devel >= 2.2 openbabel
%if_enabled avogadro
BuildRequires: avogadro-devel
%endif
%endif
BuildRequires: libkdeedu4-devel kde4-analitza-devel pkgconfig(chemical-mime-data) shared-mime-info
BuildRequires: libshape-devel qextserialport-devel libquazip-devel grantlee-devel
BuildRequires: kde4base-runtime-devel kde4base-workspace-devel

%description
%name metapackage, which contains:
* blinken: Simon Says Game
* kalgebra: MathML-based graph calculator
* kbruch: Exercise Fractions
* kgeography: Geography Trainer
* khangman: Hangman Game
* kig: Interactive Geometry
* kiten: Japanese Reference/Study Tool
* klettres: French alphabet tutor
* kmplot: Mathematical Function Plotter
%if_enabled kpercentage
* kpercentage: Excersie Percentages
%endif
* ktouch: Touch Typing Tutor
* kturtle: Logo Programming Environment
* kvoctrain: Vocabulary Trainer
* kwordquiz: Vocabulary Trainer

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
%description common
Common package for %name

%package core
Summary: %name core files
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package artikulate
Summary: Language learning application
Url: http://edu.kde.org/artikulate
Group: Education
Requires: %name-common = %version-%release
%description artikulate
Artikulate is a language learning application that helps improving pronunciation skills for
various languages. This repository maintains the application and language specifications.

%package kqtquickcharts
Summary: QtQuick plugin for interactive charts
Url: http://edu.kde.org/artikulate
Group: System/Libraries
Requires: %name-common = %version-%release
%description kqtquickcharts
A QtQuick plugin to render beautiful and interactive charts.

%package blinken
Summary: Simon Says Game
Url: http://edu.kde.org/blinken
Group: Games/Educational
Requires: %name-common = %version-%release
%description blinken
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%package rocs
Summary: Graph - Editor and a Programming Enviroment
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: kde4-kwrite
%description rocs
rocs aims to provide a full featured Graph - Editor and a Programming
Enviroment that's connected to the Graph by doing it so, it can be
used for teachers to show the joy and mistery of Graph Theory,

%package cantor
Summary: KDE Interface for doing Mathematics and Scientific Computing
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: kde4base-runtime-core
%description cantor
Cantor is a KDE Application aimed to provide a nice Interface 
for doing Mathematics and Scientific Computing. It doesn't implement 
its own Computation Logic, but instead is built around different 
Backends. 

%package 	kalgebra
Summary: MathML-based graph calculator
Url: http://edu.kde.org/kalgebra
Group: Education
Requires: %name-common = %version-%release
Requires: kde4-calgebra
%description kalgebra
KAlgebra is a mathematical calculator based content markup MathML
language. Nowadays it is capable to make simple MathML operations
(arithmetic and logical) and representate 2D and 3D graphs. It is
actually not necessary to know MathML to use KAlgebra.

%package kalzium
Summary: Shows the periodic system of the elements
Url: http://edu.kde.org/kalzium
Group: Education
Requires: %name-common = %version-%release
%if_enabled avogadro
Requires: avogadro
%endif
Requires: chemical-mime-data
%description kalzium
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%package -n libcompoundviewer4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libcompoundviewer4
KDE 4 library

%package -n libavogadro4_kalzium
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libavogadro4_kalzium
KDE 4 library

%package 	kanagram
Summary: Word learning program
Url: http://edu.kde.org/kanagram
Group: Games/Educational
Requires: %name-common = %version-%release
%description kanagram
Kanagram is a replacement for KMessedWords. Kanagram mixes up the letters
of a word (creating an anagram), and you have to guess what the mixed up
word is. Kanagram features several built-in word lists, hints, and a cheat
feature which reveals the original word. Kanagram also has a vocabulary
editor, so you can make your own vocabularies, and distribute them through
Kanagram's KNewStuff download service.

%package kbruch
Summary: Practice calculating with fractions
Url: http://edu.kde.org/kbruch
Group: Education
Requires: %name-common = %version-%release
%description kbruch
KBruch is a small program to practice calculating with fractions.

%package kgeography
Summary: A geography learning program
Url: http://edu.kde.org/kgeography
Group: Education
Requires: %name-common = %version-%release
%description kgeography
KGeography is a geography learning program.

%package khangman
Summary: Classical hangman game
Url: http://edu.kde.org/khangman
Group: Games/Educational
Requires: %name-common = %version-%release
%description khangman
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%package kig
Summary: A program for exploring geometric constructions
Url: http://edu.kde.org/kig
Group: Education
Requires: %name-common = %version-%release
%description kig
Kig is a program for exploring geometric constructions.

%package kiten
Summary: A Japanese reference/learning tool
Url: http://edu.kde.org/kiten/
Group: Games/Educational
%description kiten
Kiten is a Japanese reference/learning tool.

Kiten features:
* Search with english keyword, Japanese reading, or a Kanji string on a
  list of EDICT files.
* Search with english keyword, Japanese reading, number of strokes, grade
  number, or a Kanji on a list of KANJIDIC files.
* Comes with all necessary files.
* Very fast.
* Limit searches to only common entries.
* Nested searches of results possible.
* Compact, small, fast interface.
* Global KDE keybindings for searching highlighted strings.
* Learning dialog. (One can even open up multiple ones and have them sync
  between each other.)
* Browse Kanji by grade.
* Add Kanji to a list for later learning.
* Browse list, and get quizzed on them.

%package -n libkiten4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkiten4
KDE 4 library

%package klettres
Summary: Language learning program
Url: http://edu.kde.org/klettres/
Group: Games/Educational
Requires: %name-common = %version-%release
%description klettres
KLettres aims to help to learn the alphabet and then to read some syllables
in different languages. It is meant to help learning the very first sounds
of a new language, for children or for adults.

%package kmplot
Summary: A mathematical function plotter
Url: http://edu.kde.org/kmplot
Group: Education
Requires: %name-common = %version-%release
%description kmplot
KmPlot is a mathematical function plotter for the KDE-Desktop.

It has built in a powerfull parser. You can plot different functions
simultaneously and combine their function terms to build new functions.
KmPlot supports functions with parameters and functions in polar
coordinates. Several grid modes are possible. Plots may be printed with
high precision in correct scale.

%package kpercentage
Summary: Percentages training program
Url: http://edu.kde.org/kpercentage/
Group: Education
Requires: %name-common = %version-%release
%description kpercentage
KPercentage is a small math application that will help pupils to improve
their skills in calculating percentages.

%package kstars
Summary: A Desktop Planetarium
Url: http://edu.kde.org/kstars
Group: Education
Requires: %name-common = %version-%release
Requires: indi
%description kstars
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%package -n libanalitza4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libanalitza4
KDE 4 library

%package -n libanalitzagui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libanalitzagui4
KDE 4 library

%package -n libsatlib4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsatlib4
KDE 4 library

%package -n libsbigudrv4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsbigudrv4
KDE 4 library

%package ktouch
Summary: A program for learning touch typing
Url: http://edu.kde.org/ktouch
Group: Education
Requires: %name-common = %version-%release
Requires: libqt4-sql-sqlite
%description ktouch
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.

%package kturtle
Summary: An educational programming environment
Url: http://edu.kde.org/kturtle
Group: Education
Requires: %name-common = %version-%release
%description kturtle
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%package parley
Summary: KDE Vocabulary training application
Url: http://edu.kde.org/parley
Group: Education
Requires: %name-common = %version-%release
Requires: python-module-kde4
%description parley
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%package kwordquiz
Summary: A general purpose flash card program
Url: http://edu.kde.org/kwordquiz
Group: Education
Requires: %name-common = %version-%release
%description kwordquiz
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%package step
Summary: Interactive physical simulator
Url: http://edu.kde.org/step
Group: Education
Requires: %name-common = %version-%release
%description step
Step is an interactive physical simulator. It works like this:
you place some bodies on the scene, add some forces such as gravity
or springs, then click "Simulate" and Step shows you how your scene
will evolve according to the laws of physics. You can change every
property of bodies/forces in your experiment (even during simulation)
and see how this will change evolution of the experiment. With Step
you can not only learn but feel how physics works !

%package -n libscience4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libscience4
KDE 4 library

%package -n libkdeeduui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdeeduui4
KDE 4 library

%package -n libkeduvocdocument4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkeduvocdocument4
KDE 4 library

%package -n libmarblewidget4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmarblewidget4
KDE 4 library

%package -n libcantorlibs4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libcantorlibs4
KDE 4 library

%package -n libcantor4_config
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libcantor4_config
KDE 4 library

%package -n librocscore4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n librocscore4
KDE 4 library

%package -n librocsvisualeditor4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n librocsvisualeditor4
KDE 4 library

%package -n libkhangmanengine4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkhangmanengine4
KDE 4 library

%package -n libkanagramengine4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkanagramengine4
KDE 4 library

%package marble
Summary: A virtual globe and world atlas
Url: http://edu.kde.org/marble
Group: Education
Requires: %name-common = %version-%release
Requires: xplanet
%description marble
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel libkdeedu4-devel
Requires: kde4-marble-devel
Requires: %name-common = %version-%release
%description devel
Files needed to build applications based on %name.

%package -n libartikulatecore4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libartikulatecore4
KDE 4 library

%package -n libartikulatelearnerprofile4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libartikulatelearnerprofile4
KDE 4 library

%package -n libartikulatesound4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libartikulatesound4
KDE 4 library

%package -n libastro4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libastro4
KDE 4 library

%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

pushd cantor/src/backends/lua
LUA_BASE_VER=`echo "%{get_version libluajit-devel}" | sed -E 's|^([[:digit:]]+\.[[:digit:]]).*|\1|'`
for f in *.{h,cpp} ; do
    sed -i "s|luajit-2.0/lua.hpp|luajit-${LUA_BASE_VER}/lua.hpp|" $f
done
popd

%if_disabled artikulate
rm -rf artikulate
%endif


%build
export CFLAGS="${optflags} -DOCAMLIB=%_libdir/ocaml"
export CPPFLAGS="${optflags} -DOCAMLIB=%_libdir/ocaml "
ls -d1 * | \
while read d
do
    [ -d "$d" ] || continue
    pushd $d
    %K4build \
	-DBoostPython_FOUND=ON \
	-DKDE4_BUILD_TESTS:BOOL=OFF \
	-DNOVA_INCLUDE_DIR=%_includedir/libnova \
	-DNOVA_LIBRARIES="-lnova" \
	-DINDI_INCLUDE_DIR=%_includedir/libindi \
	-DNOVA_FUNCTION_COMPILE:BOOL=true \
	-DQALCULATE_CFLAGS:STRING="`pkg-config libqalculate --cflags| sed 's|@CLN_CPPFLAGS@||g'`" \
	-DQALCULATE_LIBRARIES:STRING="`pkg-config libqalculate --libs`"
    popd
done


%install
ls -d1 * | \
while read d
do
    [ -d "$d" ] || continue
    pushd $d
    %K4install
    popd
done
mkdir -p %buildroot/%_K4apps/step/objinfo/l10n


%files
%files common
#%doc README
%_K4iconsdir/hicolor/*/mimetypes/application-x-k*.*

%if_enabled openbabel
%if_enabled avogadro
%files -n libcompoundviewer4
%_K4libdir/libcompoundviewer.so.*
%endif
%endif

%if_enabled artikulate
%files artikulate
%_K4bindir/artikulate
%_K4xdg_apps/artikulate.desktop
%_K4apps/artikulate/
%_K4apps/artikulateui.rc
%_K4conf/artikulate.knsrc
%_K4cfg/artikulate.kcfg
%_K4iconsdir/hicolor/*/apps/artikulate.*
%_K4doc/en/artikulate/
%files -n libartikulatecore4
%_K4libdir/libartikulatecore.so.*
%files -n libartikulatelearnerprofile4
%_K4libdir/libartikulatelearnerprofile.so.*
%files -n libartikulatesound4
%_K4libdir/libartikulatesound.so.*
%endif

%files kqtquickcharts
%_K4lib/imports/org/kde/charts/

%files blinken
%_K4bindir/blinken
%_K4xdg_apps/blinken.desktop
%_K4iconsdir/hicolor/*/apps/blinken.*
%_K4apps/blinken
%_K4cfg/blinken.kcfg
%_K4doc/*/blinken

%files -n libcantor4_config
%_K4libdir/libcantor_config.so

%files -n libcantorlibs4
%_K4libdir/libcantorlibs.so.*

%files cantor
%_K4bindir/cantor
%_K4xdg_apps/cantor.desktop
%_K4iconsdir/hicolor/*/apps/cantor.*
%_K4iconsdir/hicolor/*/apps/maximabackend.*
%_K4iconsdir/hicolor/*/apps/octavebackend.*
%_K4iconsdir/hicolor/*/apps/pythonbackend.*
%_K4iconsdir/hicolor/*/apps/rbackend.*
%_K4iconsdir/hicolor/*/apps/sagebackend.*
%_K4iconsdir/hicolor/*/apps/qalculatebackend.*
%_K4iconsdir/hicolor/*/apps/scilabbackend.*
%_K4iconsdir/hicolor/*/apps/luabackend.*
%_K4lib/cantor_*.so
%_K4lib/concentrationCalculator.so
%_K4lib/gasCalculator.so
%_K4lib/libcantorpart.so
%_K4lib/nuclearCalculator.so
%_K4apps/cantor
%_K4cfg/cantor.kcfg
%_K4cfg/cantor_libs.kcfg
%_K4cfg/maximabackend.kcfg
%_K4cfg/sagebackend.kcfg
%_K4cfg/octavebackend.kcfg
%_K4cfg/luabackend.kcfg
%_K4cfg/python2backend.kcfg
%if_enabled qalculate
%_K4cfg/qalculatebackend.kcfg
%endif
%_K4cfg/scilabbackend.kcfg
%_K4conf/cantor.knsrc
%_K4conf/cantor_*.knsrc
%_K4srv/concentrationCalculator.desktop
%_K4srv/gasCalculator.desktop
%_K4srv/nuclearCalculator.desktop
%_K4srv/cantor
%_K4srvtyp/cantor_*.desktop
%_K4doc/*/cantor

%files kalgebra
%_K4bindir/kalgebra
%_K4bindir/kalgebramobile
%_K4xdg_apps/kalgebra.desktop
%_K4xdg_apps/kalgebramobile.desktop
%_K4lib/imports/org/kde/analitza/
%_K4apps/plasma/plasmoids/org.kde.graphsplasmoid/
%_K4iconsdir/hicolor/*/apps/kalgebra.*
#%_K4apps/kalgebra
%_K4apps/kalgebramobile/
%_K4apps/katepart/syntax/kalgebra.xml
%_K4cfg/kalgebrabackend.kcfg
#%_K4srv/kalgebraplasmoid.desktop
%_K4srv/kalgebra*.desktop
%_K4srv/graphsplasmoid.desktop
#%_K4srvtyp/kalgebra*.desktop
%_K4lib/plasma_applet_kalgebra.so
%_K4doc/*/kalgebra

%files kalzium
%_K4bindir/kalzium
%_K4xdg_apps/kalzium*.desktop
%_K4iconsdir/hicolor/*/apps/kalzium.*
%_K4lib/plasma_engine_kalzium.so
%_K4lib/plasma_applet_didyouknow.so
%_K4lib/plasma_applet_molmassCalculator.so
%_K4apps/desktoptheme/default/widgets/chalkboard.svg
%_K4apps/kalzium
%_K4srv/plasma-dataengine-kalzium.desktop
%_K4srv/plasma_didyouknow.desktop
%_K4srv/plasma-applet-Molmasscalculator.desktop
%_K4cfg/kalzium.kcfg
%_K4conf/kalzium.knsrc
%_K4doc/*/kalzium
%_man1dir/kalzium.*

%files kanagram
%_K4bindir/kanagram
%_K4xdg_apps/kanagram.desktop
%_K4iconsdir/hicolor/*/apps/kanagram*.*
%_K4apps/kanagram
%_K4cfg/kanagram.kcfg
%_K4conf/kanagram.knsrc
%_K4doc/*/kanagram

%files kbruch
%_K4bindir/kbruch
%_K4xdg_apps/kbruch.desktop
%_K4iconsdir/hicolor/*/apps/kbruch.*
%_K4apps/kbruch
%_K4cfg/kbruch.kcfg
%_K4doc/*/kbruch
%_man1dir/kbruch.*

%files kgeography
%_K4bindir/kgeography
%_K4xdg_apps/kgeography.desktop
%_K4iconsdir/hicolor/*/apps/kgeography.*
%_K4apps/kgeography
%_K4cfg/kgeography.kcfg
%_K4doc/*/kgeography

%files khangman
%_K4bindir/khangman
%_K4xdg_apps/khangman.desktop
%_K4iconsdir/hicolor/*/apps/khangman*.*
%_K4apps/khangman
%_K4apps/plasma/packages/org.kde.kanagram/
%_K4cfg/khangman.kcfg
%_K4conf/khangman.knsrc
%_K4doc/*/khangman
%_man6dir/khangman.*

%files kig
%_K4bindir/kig
%_K4bindir/pykig.py
%_K4xdg_apps/kig.desktop
%_K4iconsdir/hicolor/*/apps/kig.*
%_K4lib/kigpart.so
%_K4apps/kig
%_K4srv/kig_part.desktop
%_K4apps/katepart/syntax/python-kig.xml
%_K4doc/*/kig
%_man1dir/kig.*

%files kiten
%_K4bindir/kiten*
%_K4xdg_apps/kiten.desktop
%_K4xdg_apps/kitenkanjibrowser.desktop
%_K4xdg_apps/kitenradselect.desktop
%_K4iconsdir/hicolor/*/apps/kiten.*
%_K4apps/kiten
%_K4apps/kitenradselect
%_K4apps/kitenkanjibrowser
%_K4cfg/kiten.kcfg
%_K4doc/*/kiten

%files -n libkiten4
%_K4libdir/libkiten.so.*

%files klettres
%_K4bindir/klettres
%_K4xdg_apps/klettres.desktop
%_K4iconsdir/hicolor/*/apps/klettres.*
%_K4apps/klettres
%_K4cfg/klettres.kcfg
%_K4conf/klettres.knsrc
%_K4doc/*/klettres

%files kmplot
%_K4bindir/kmplot
%_K4xdg_apps/kmplot.desktop
%_K4iconsdir/hicolor/*/apps/kmplot.*
%_K4apps/kmplot
%_K4lib/libkmplotpart.so
%_K4cfg/kmplot.kcfg
%_K4srv/kmplot_part.desktop
%_K4doc/*/kmplot
%_man1dir/kmplot.*

%if_enabled kpercentage
%files kpercentage
%_K4bindir/kpercentage
%_K4xdg_apps/kpercentage.desktop
%_K4apps/kpercentage
%_K4doc/*/kpercentage
%endif

%files kstars
%_K4bindir/kstars
%_K4xdg_apps/kstars.desktop
%_K4iconsdir/hicolor/*/apps/kstars.*
%_K4apps/kstars
%_K4libdir/libhtmesh.a
%_K4cfg/kstars.kcfg
%_K4conf/kstars.knsrc
%_K4doc/*/kstars

%files ktouch
%_K4bindir/ktouch
#%_K4lib/imports/org/kde/ktouch/
%_K4xdg_apps/ktouch.desktop
%_K4iconsdir/hicolor/*/apps/ktouch.*
%_K4apps/ktouch
%_K4cfg/ktouch.kcfg
%_K4doc/*/ktouch
%_man1dir/ktouch.*

%files kturtle
%_K4bindir/kturtle
%_K4xdg_apps/kturtle.desktop
%_K4iconsdir/hicolor/*/apps/kturtle.*
%_K4apps/kturtle
%_K4conf/kturtle.knsrc
%_K4doc/*/kturtle

%files parley
%_K4bindir/parley
%_K4xdg_apps/parley.desktop
%_K4iconsdir/hicolor/*/apps/parley*.*
%_K4apps/parley
%_K4srv/plasma-dataengine-parley.desktop
%_K4srv/plasma_parley.desktop
%_K4cfg/parley.kcfg
%_K4cfg/languagesettings.kcfg
%_K4cfg/documentsettings.kcfg
%_K4conf/parley-themes.knsrc
%_K4conf/parley.knsrc
%_K4lib/plasma_applet_parley.so
%_K4lib/plasma_engine_parley.so
%_K4apps/desktoptheme/default/widgets/parley_plasma_card.svg
%_K4doc/*/parley

%files kwordquiz
%_K4bindir/kwordquiz
%_K4xdg_apps/kwordquiz.desktop
%_K4iconsdir/hicolor/*/apps/kwordquiz.*
%_K4apps/kwordquiz
%_K4cfg/kwordquiz.kcfg
%_K4conf/kwordquiz.knsrc
%_K4doc/*/kwordquiz

%files step
%_K4bindir/step
%_K4xdg_apps/step.desktop
%_K4iconsdir/hicolor/*/apps/step.*
%_K4apps/step
%_K4cfg/step.kcfg
%_K4conf/step.knsrc
%_K4doc/*/step

%files -n libscience4
%_K4apps/libkdeedu/
%_K4libdir/libscience.so.*

%files rocs
%_K4bindir/rocs
%_K4xdg_apps/rocs.desktop
%_K4lib/rocs_*.so
%_K4apps/rocs/
%_K4apps/rocs_rootedtree/
%_K4conf/rocs.knsrc
%_K4cfg/rocs.kcfg
%_K4iconsdir/hicolor/*/apps/rocs.*
%_K4srv/rocs_*.desktop
%_K4srvtyp/Rocs*Plugin.desktop
%_K4doc/*/rocs

%files -n librocscore4
%_K4libdir/librocscore.so.*
%files -n librocsvisualeditor4
%_K4libdir/librocsvisualeditor.so.*
%files -n libkhangmanengine4
%_K4libdir/libkhangmanengine.so.*

%files devel
%_includedir/khangman/
%_K4link/*.so
%_K4includedir/*
%_K4dbus_interfaces/*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 15.12.3-alt7%ubt
- NMU: rebuilt with boost-1.67.0

* Wed Aug 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.12.3-alt6%ubt
- Rebuilt with new libgsl.
- Built without facile.

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt5%ubt
- build without avogadro

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt4
- rebuild with new openbabel

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt3
- fix to build with new luajit

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt2
- rebuild with new wcslib

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Tue Feb 02 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Thu Jul 02 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt2
- rebuild with new libindi

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 4.14.3-alt1.1
- rebuild with boost 1.57.0

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Thu Sep 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- split marble to separate package

* Thu Aug 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt3
- rebuilt with new cfitsio

* Fri Mar 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1.M70P.1
- built for M70P

* Fri Mar 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt2
- rebuilt with new avogadro

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Tue Nov 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt2.M70P.1
- built for M70P

* Tue Nov 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt3
- add fix for KDEBUG#327474 (ALT#29575)

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1.M70P.1
- new version

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt2
- build kstars with wcslib

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Mon Oct 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Wed Jan 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.3-alt1.1
- Rebuilt with Boost 1.52.0

* Tue Nov 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 29 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt2
- don't obsolete KDE3 kdeedu (ALT#27900)

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- built for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- rebuild with new boost

* Mon Mar 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Fri Dec 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- rebuilt with new openbabel

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt1.1
- Rebuild with Python-2.7

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- rebuilt

* Tue Jul 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Fri Jun 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Fri Apr 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- rebuilt with new boost

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Feb 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- built with avogadro

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2
- obsolete kdeedu

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Fri Aug 06 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Tue May 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Fri Jan 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Sep 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- set kturtle default language to current locale language

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Wed Jan 21 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Thu Dec 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- rebuilt with new libcln

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Fri Oct 24 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt0.M41.1
- built for M41

* Fri Oct 17 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile


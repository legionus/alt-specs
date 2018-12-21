
Name: telepathy-logger-qt4
Version: 0.8.0
Release: alt3%ubt
%define sover 1
%define libname lib%name%sover

Group: Networking/Instant messaging
Summary: Qt Wrapper around TpLogger client library
Url: https://projects.kde.org/telepathy-logger-qt
License: LGPLv2.1+

Source: %name-%version.tar
Patch1: 0.1.0-alt-shared.patch
Patch2: 0.1.0-alt-install.patch
Patch3: 0.1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Wed May 30 2012 (-bi)
# optimized out: boost-devel-headers cmake-modules elfutils glib2-devel libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel libtelepathy-glib libtelepathy-glib-devel libtelepathy-logger libtelepathy-qt4 libxml2-devel pkg-config python-base python-devel python-modules python-modules-encodings python-modules-xml qt-gstreamer qt4-designer xml-utils
#BuildRequires: cmake doxygen flex gcc-c++ graphviz libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libtelepathy-logger-devel libtelepathy-qt4-devel phonon-devel python-module-distribute qt-gstreamer-devel
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake doxygen flex gcc-c++ graphviz libtelepathy-logger-devel libtelepathy-qt4-devel libqt4-devel phonon-devel kde-common-devel
BuildRequires: pkgconfig(QtGLib-2.0) python-modules-distutils

%description
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package devel
Group: Development/KDE and QT
Summary: Qt Wrapper around TpLogger client library
Requires: %libname
Requires: pkgconfig(QtGLib-2.0) libtelepathy-qt4-devel
%description devel
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package -n %libname
Group: System/Libraries
Summary: Qt Wrapper around TpLogger client library

%description -n %libname
Telepathy-logger-qt4 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%prep
%setup
#%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export QTDIR=%_qt4dir
%Kbuild

%install
%Kinstall

%files -n %libname
%doc AUTHORS ChangeLog HACKING TODO
%_libdir/libtelepathy-logger-qt4.so.%sover
%_libdir/libtelepathy-logger-qt4.so.%sover.*

%files devel
%_libdir/cmake/TelepathyLoggerQt4/
%_includedir/telepathy-logger-*/TelepathyLoggerQt*/
%_libdir/lib*.so
%_libdir/pkgconfig/TelepathyLoggerQt4.pc

%changelog
* Thu Sep 13 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt3%ubt
- fix build requires

* Fri Sep 05 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- fix requires

* Thu Jun 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt2
- fix requires

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt2
- rebuilt with new libtelepathy-logger

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build

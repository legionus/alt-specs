%define _kde_alternate_placement 1

%add_findpackage_path %_kde4_bindir

%def_disable kross_falcon
%def_disable kross_java
%def_disable kross_ruby

%define rname kross-interpreters
Name: kde4-kross-interpreters
Version: 4.12.2
Release: alt1.qa1

Group: Development/KDE and QT
Summary: Kross interpreters
Url: http://developer.kde.org/language-bindings/
License: LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Sep 16 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python-modules ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel python-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel zlib-devel
BuildRequires: kde4libs-devel >= %version kde-common-devel
%if_enabled kross_falcon
BuildRequires: Falcon-devel
%endif
%if_enabled kross_java
BuildRequires: java-devel
%endif
%if_enabled kross_ruby
BuildRequires: libruby-devel ruby rpm-build-ruby
%endif
BuildRequires: python-devel rpm-build-python

%description
Kross interpreters

%package -n kde4-kross-python
Group: Development/KDE and QT
Summary: Kross plugin for python
Requires: kde4libs >= %version
Provides: kross(python) = %version-%release
%description -n kde4-kross-python
Python plugin for the Kross archtecture in KDE.

%package -n kde4-kross-falcon
Group: Development/KDE and QT
Summary: Kross plugin for falcon
Requires: Falcon
Requires: kde4libs >= %version
Provides: kross(falcon) = %version-%release
%description -n kde4-kross-falcon
Falcon plugin for the Kross archtecture in KDE.

%package -n kde4-kross-java
Group: Development/KDE and QT
Summary: Kross plugin for java
Requires: kde4libs >= %version
Provides: kross(java) = %version-%release
%description -n kde4-kross-java
Java plugin for the Kross archtecture in KDE.

%package -n kde4-kross-ruby
Group: Development/KDE and QT
Summary: Kross plugin for ruby
Requires: ruby
Requires: kde4libs >= %version
Provides: kross(ruby) = %version-%release
%description -n kde4-kross-ruby
Ruby plugin for the Kross architecture in KDE.


%prep
%setup -qn %rname-%version

%{!?_enable_kross-falcon:rm -rf falcon}
%{!?_enable_kross-ruby:rm -rf ruby}
%{!?_enable_kross-java:rm -rf java}


%build
%K4cmake
%K4make


%install
%K4install


%files -n kde4-kross-python
%_K4lib/krosspython.so

%if_enabled kross_falcon
%files -n kde4-kross-falcon
%_K4lib/krossfalcon.so
%endif

%if_enabled kross_java
%files -n kde4-kross-java
%endif

%if_enabled kross_ruby
%files -n kde4-kross-ruby
%_K4lib/krossruby.so
%endif


%changelog
* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 4.12.2-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build

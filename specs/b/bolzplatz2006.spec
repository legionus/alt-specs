# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           bolzplatz2006
Version:        1.0.3
Release:        alt1_38jpp8
Summary:        Slam Soccer 2006 is a funny football game in 3D-comic-style
Summary(fr):    Coup de Foot 2006 est un jeu comique en 3D
Summary(de):    Bolzplatz 2006 ist ein spaßiges Fußballspiel im 3D-Comic-Stil
License:        GPLv2+
Group:          Games/Other
URL:            http://www.bolzplatz2006.de
Source0:        http://downloads.sourceforge.net/bp2k6/%{name}-%{version}-src.zip
Source1:        %{name}.png
Source2:        %{name}.sh
Source3:        %{name}-settings.sh
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml
Source6:        %{name}-jirr-no-crash.patch
Source7:        %{name}-functions.sh
Source8:        %{name}.autodlrc
Source9:        input.xml
Patch0:         %{name}-irrlicht.i.patch
Patch1:         %{name}-irrlicht-extra-qualification-error.patch
Patch2:         %{name}-irrlicht-use-systemlibs.patch
Patch3:         %{name}-irrlicht-png-64bit.patch
Patch4:         %{name}-lwjgl-nofmod.patch
Patch5:         %{name}-lwjgl-openal11.patch
Patch6:         %{name}-lwjgl-Makefile.patch
Patch7:         %{name}-no-xrandr.patch
Patch8:         %{name}-versioned-openal.patch
Patch9:         %{name}-1.0.3-libpng15.patch
Patch10:        %{name}-class-version15.patch
Patch11:        %{name}-use-system-extgl.patch
Patch12:        %{name}-gcc6.patch
BuildRequires:  ant sdljava dom4j vecmath1.2 swig xml-commons-apis
BuildRequires:  libGLU-devel libdevil-devel libXxf86vm-devel libjpeg-devel
BuildRequires:  libpng-devel libXext-devel libXrandr-devel libXcursor-devel
BuildRequires:  libXt-devel libXrender-devel libvorbis-devel desktop-file-utils
# Make sure we get the normal openjdk and not the incomplete aarch32 version
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  libappstream-glib
Requires:       sdljava dom4j vecmath1.2 java >= 1.6.0 jpackage-utils
Requires:       icon-theme-hicolor autodownloader
# These are dynamically opened by lwjgl:
Requires:       libopenal1
Source44: import.info

%description
Slam Soccer 2006 is a funny football game in
3D-comic-style - and it's for free!

* Freeware and open source
* Funny 3d-comic-style
* Enthralling stadium atmosphere
* Keyboard and gamepad control
* 2-player mode
* Career and world cup
* Register in the online hall of fame
* Build your own stadium

* 80 teams
* 20 stadiums
* 10 weather conditions
* 50 adboards
* 10 referees
* 9 commentators (5 German, 2 English, 2 French)

* 3 languages: German, English, French

%description -l de
Bolzplatz 2006 ist ein spaßiges Fußballspiel
im 3D-Comic-Stil für lau.

* Kostenlos und Open-Source
* Witzige 3D-Comic-Grafik
* Packende Stadionatmosphäre
* Steuerung mit Tastatur oder Gamepad
* 2-Spieler-Modus
* Karriere und Weltmeisterschaft
* Eintrag in die Hall of Fame
* Baue Dein eigenes Stadion

* 80 Teams
* 20 Stadien
* 10 Wetterverhältnisse
* 50 Werbebanden
* 10 Schiedsrichter
* 9 Kommentatoren (5xDeutsch, 2xEnglisch, 2xFranzösisch)

* 3 Sprachen: Deutsch, Englisch und Französisch

%description -l fr
Coup de Foot 2006 est un jeu comique en 3D.
Gratuit et open-source.

* Graphiques 3D en style cartoon
* Ambiance de stade presqu'originale
* A commander par clavier ou gamepad
* Mode 2 joueurs
* Mode Carrière et Coupe du Monde
* Inscription au Hall of Fame
* Construis tes propres stades

* 80 équipes
* 20 stades
* 10 conditions atmosphériques différentes
* 50 panneaux publicitaires
* 10 arbitres
* 9 commentateurs

* 3 langues: allemand, anglais et français


%prep
%setup -q -c
pushd libsrc/jirr-dev
%patch0 -p0
cp %{SOURCE6} diff.txt
popd
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
cp %{SOURCE7} .
sed -i 's/\r//' license.txt
# we use the system versions of these
rm -r libsrc/irrlicht-0.14-patched/libpng libsrc/irrlicht-0.14-patched/zlib \
  libsrc/irrlicht-0.14-patched/jpeglib libsrc/irrlicht-0.14-patched/glext.h


%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
export JAVA_HOME=/usr/lib/jvm/java-openjdk

# special case ix86 as all of ix86 should look in the i386 jre lib subdir
%ifarch %{ix86}
export JAVA_ARCH=i386
%endif
# special case x86_64 as it should be mapped to amd64
%ifarch x86_64
export JAVA_ARCH=amd64
%endif
# All other archs
if [ -z "$JAVA_ARCH" ]; then
  export JAVA_ARCH=%{_arch}
fi

echo "export LD_LIBRARY_PATH=/usr/lib/jvm/jre-openjdk/lib/$JAVA_ARCH" >> \
  %{name}-functions.sh

# jbolzplatz ships with copies of several libraries, as these are heavily
# patched we use the bolzplatz versions and not the system ones

# build irrlicht-0.14
pushd libsrc/irrlicht-0.14-patched
%make_build CPP="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd

# build jirr-0.6
pushd libsrc/jirr-dev
make CXX="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -fpermissive" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd

# build lwjgl
pushd libsrc/lwjgl
ant jars
ant compile_native
popd

# build bolzplatz itself
mkdir classes
javac -d classes -encoding iso-8859-1 \
  -cp `build-classpath dom4j sdljava vecmath1.2`:./libsrc/jirr-dev/lib/irrlicht.jar:./libsrc/lwjgl/libs/lwjgl.jar \
  `find ./src -name '*.java'`
jar cf %{name}.jar -C classes .


%install
# dirs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

# jars
install -m 644 %{name}.jar libsrc/jirr-dev/lib/irrlicht.jar \
  libsrc/lwjgl/libs/lwjgl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}

# native libraries
install -m 755 libsrc/jirr-dev/libirrlicht_wrap.so \
  libsrc/lwjgl/libs/linux/liblwjgl.so $RPM_BUILD_ROOT%{_libdir}/%{name}

# startscripts
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-settings

# icon and menu-entry
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

# needed "data" files
install -p -m 644 %{name}-functions.sh %{SOURCE8} %{SOURCE9} \
  $RPM_BUILD_ROOT%{_datadir}/%{name}


%files
%doc --no-dereference license.txt
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_javadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_38jpp8
- java update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_34jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_32jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_30jpp8
- new version

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_30jpp7
- update to new release by jppimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_26jpp7
- update to new release by jppimport

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_25jpp7
- update to new release by jppimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_24jpp7
- update to new release by jppimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_22jpp7
- update to new release by jppimport

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1_20jpp7.1
- Rebuilt with libpng15

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_20jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_18jpp7
- update to new release by jppimport

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_15jpp6
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_13jpp6
- update to new release by jppimport


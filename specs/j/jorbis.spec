# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jorbis
Version:        0.0.17
Release:        alt1_17jpp8
Summary:        Pure Java Ogg Vorbis Decoder
URL:            http://www.jcraft.com/jorbis/
License:        LGPLv2+
Group:          System/Libraries
Source0:        http://www.jcraft.com/jorbis/%{name}-%{version}.zip
# Some fixes from the jorbis copy embedded in cortada. I've mailed upstream
# asking them to integrate these, for more info also see:
# https://trac.xiph.org/ticket/1565
# Note that although the original git headers were left in place for reference
# the actual patches have been rebased to 0.0.17 !
Patch0:         jorbis-0.0.17-cortado-fixes.patch
BuildArch:      noarch
BuildRequires:  java-devel
# We used to also package the comment editor example, but that is not so
# useful to end users (esp. the passing of cmdline args as java defines)
Obsoletes:      %{name}-comment <= 0.0.17-3
Source44: import.info

%description
JOrbis is a pure Java Ogg Vorbis decoder.


%package javadoc
Summary:        Java docs for jorbis
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for jorbis.


%package player
Summary:        Java applet for playing ogg-vorbis files from a browser
License:        GPLv2+
Group:          Sound
Requires:       java
Requires:       %{name} = %{version}-%{release}

%description player
This package contains JOrbisPlayer a simple java applet for playing
ogg-vorbis files from a browser.
See %{_docdir}/%{name}-player/JOrbisPlayer.html for
an example how to embed and use the applet.


%prep
%setup -q
%patch0 -p1


%build
javac com/jcraft/jogg/*.java com/jcraft/jorbis/*.java player/*.java
jar cf jogg.jar com/jcraft/jogg/*.class
jar cf jorbis.jar com/jcraft/jorbis/*.class
jar cf JOrbisPlayer.jar player/*.class
javadoc -d doc -public com/jcraft/*/*.java


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a *.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog COPYING.LIB README
%{_javadir}/jogg.jar
%{_javadir}/jorbis.jar

%files javadoc
%doc COPYING.LIB
%{_javadocdir}/%{name}

%files player
%doc player/JOrbisPlayer.html
%{_javadir}/JOrbisPlayer.jar


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_16jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_8jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_7jpp7
- update to new release by jppimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1_6jpp7
- new version


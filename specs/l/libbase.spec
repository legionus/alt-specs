# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libbase
Version: 1.1.3
Release: alt1_18jpp8
Summary: JFree Base Services
License: LGPLv2
Group: System/Libraries
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant ant-contrib java-devel jpackage-utils apache-commons-logging
Requires: jpackage-utils apache-commons-logging
BuildArch: noarch

Patch0: libbase-1.1.2.build.patch
Source44: import.info

%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib 

%build
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_17jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_6jpp7
- new version


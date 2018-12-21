Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          simple-xml
Summary:       An XML serialization framework for Java
Version:       2.7.1
Release:       alt1_12jpp8
License:       ASL 2.0
Url:           http://simple.sourceforge.net/
Source0:       http://downloads.sourceforge.net/simple/%{name}-%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/simpleframework/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: javapackages-tools
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bea-stax
BuildRequires: bea-stax-api
BuildRequires: junit
BuildRequires: xpp3

Requires:      bea-stax
Requires:      xpp3

Requires:      javapackages-tools
BuildArch:     noarch
Source44: import.info

%description
Simple is a high performance XML serialization and
configuration framework for Java. Its goal is to
provide an XML framework that enables rapid development
of XML configuration and communication systems.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# clean up
rm -r javadoc/* test/report/*
find . -name "*.jar" -delete
find . -name "*.class" -delete

sed -i 's/\r//' LICENSE.txt
# test @ random fails
sed -i 's|haltonfailure="yes"|haltonfailure="no"|' test/build.xml

%build

%ant -Dlib.path=%{_javadir} all

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 jar/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc --no-dereference LICENSE.txt

%changelog
* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_12jpp8
- java update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_9jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_8jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_6jpp8
- java 8 mass update


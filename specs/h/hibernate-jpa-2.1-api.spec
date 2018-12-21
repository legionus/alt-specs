Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag .Final
%global oname hibernate-jpa-api
%global apiversion 2.1
%global minversion 0
%global pkgversion %{?apiversion}%{?minversion}%{?namedreltag}
%global namedversion %{version}%{?namedreltag}

Name:          hibernate-jpa-2.1-api
Version:       1.0.0
Release:       alt1_4jpp8
Summary:       Java Persistence 2.1 (JSR 338) API
License:       EPL and BSD
URL:           http://www.hibernate.org/
Source0:       https://github.com/hibernate/hibernate-jpa-api/archive/%{pkgversion}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/hibernate/javax/persistence/%{name}/%{namedversion}/%{name}-%{namedversion}.pom
# fix mvn build, this project uses the default Gradle to build
# sets various mvn plugins properties
Patch0:        hibernate-jpa-api-2.10.Final-pom.patch

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
Source44: import.info

%description
Hibernate definition of the Java Persistence 2.1 (JSR 338) API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{pkgversion}
find . -name "*.jar" -delete

cp -p %{SOURCE1} pom.xml
%patch0 -p1

# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' src/main/javadoc/jdstyle.css

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.9.Draft.16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.Draft.16jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.Draft.16jpp7
- new release


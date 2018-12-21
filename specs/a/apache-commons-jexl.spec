Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global jarname commons-jexl
%global compatver 2.1.0

Name:           apache-%{jarname}
Version:        2.1.1
Release:        alt2_20jpp8
Summary:        Java Expression Language (JEXL)
License:        ASL 2.0
URL:            http://commons.apache.org/jexl
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/jexl/source/%{jarname}-%{version}-src.tar.gz

# Patch to fix test failure with junit 4.11
Patch0:         001-Fix-tests.patch
# Fix javadoc build
Patch1:         apache-commons-jexl-javadoc.patch
Patch2:         0001-Port-to-current-javacc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)

Provides:       %{jarname} = %{version}-%{release}
Source44: import.info

%description
Java Expression Language (JEXL) is an expression language engine which can be
embedded in applications and frameworks.  JEXL is inspired by Jakarta Velocity
and the Expression Language defined in the JavaServer Pages Standard Tag
Library version 1.1 (JSTL) and JavaServer Pages version 2.0 (JSP).  While
inspired by JSTL EL, it must be noted that JEXL is not a compatible
implementation of EL as defined in JSTL 1.1 (JSR-052) or JSP 2.0 (JSR-152).
For a compatible implementation of these specifications, see the Commons EL
project.

JEXL attempts to bring some of the lessons learned by the Velocity community
about expression languages in templating to a wider audience.  Commons Jelly
needed Velocity-ish method access, it just had to have it.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
Provides:       %{jarname}-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{jarname}-%{version}-src
%patch0 -p1 -b .test
%patch1 -p1 -b .javadoc
%patch2 -p1

# Java 1.6 contains bsf 3.0, so we don't need the dependency in the pom.xml file
%pom_remove_dep org.apache.bsf:bsf-api
find \( -name '*.jar' -o -name '*.class' \) -delete
# Fix line endings
find -name '*.txt' -exec sed -i 's/\r//' '{}' +

# Drop "-SNAPSHOT" from version
%pom_xpath_set "pom:project/pom:version" %{compatver} jexl2-compat
%pom_xpath_set "pom:dependency[pom:artifactId='commons-jexl']/pom:version" %{version} jexl2-compat

echo "
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.fedoraproject</groupId>
  <artifactId>commons-jexl-aggegator</artifactId>
  <version>%{version}</version>
  <packaging>pom</packaging>
  <modules>
    <module>.</module>
    <module>jexl2-compat</module>
  </modules>
</project>" >>aggregator-pom.xml
%mvn_package :commons-jexl-aggegator __noinstall

%build
%mvn_build -- -f aggregator-pom.xml

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_14jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp7
- new version

* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_5jpp6
- fixed obsoletes (closes: #25046)

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp6
- new version


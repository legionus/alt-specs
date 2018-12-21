Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             cookcc
Version:          0.3.3
Release:          alt3_16jpp8
Summary:          Lexer and Parser Generator
License:          BSD
URL:              https://github.com/coconut2015/cookcc

# svn export -r 678 http://cookcc.googlecode.com/svn/trunk/ cookcc-0.3.3
# tar -J -cf cookcc-0.3.3.tar.xz cookcc-0.3.3
Source0:          %{name}-%{version}.tar.xz
Source1:          %{name}-%{version}-pom.xml

Patch0:           %{name}-%{version}-xerces.patch
Patch1:           %{name}-%{version}-buildxml.patch
Patch2:           %{name}-%{version}-port-to-jsr-269.patch
Patch3:           %{name}-0.3.3-freemarker2.3.2+.patch

BuildArch:        noarch

BuildRequires:    ant
BuildRequires:    cookxml
BuildRequires:    freemarker2.3.23
BuildRequires:    javapackages-local
BuildRequires:    xerces-j2

Requires:         freemarker2.3.23
Requires:         cookxml
Requires:         xerces-j2
Source44: import.info

%description
CookCC is a lexer and parser (LALR (1)) generator project, combined.
It is written in Java, but the target languages can vary. 

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

find . -name '*.jar' -delete

%build
CLASSPATH=$(build-classpath xerces-j2 freemarker2.3.23-2.3.23 cookxml) ant cookcc_jar javadocs

%install
%mvn_artifact %{SOURCE1} dist/%{name}-%{version}.jar
%mvn_install -J javadocs

%files -f .mfiles
%doc LICENSE_cookcc.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE_cookcc.txt

%changelog
* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_16jpp8
- build with compat fremarker2.3.23

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_16jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_15jpp8
- new jpp release

* Sun Nov 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_6jpp7
- update to new release by jppimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_5jpp7
- new version


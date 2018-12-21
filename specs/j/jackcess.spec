Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackcess
Version:       2.2.0
Release:       alt1_1jpp8
Summary:       Java library for reading from and writing to MS Access databases
License:       ASL 2.0
URL:           http://jackcess.sourceforge.net/
# svn checkout http://svn.code.sf.net/p/jackcess/code/jackcess/tags/jackcess-2.1.3
# tar cJf jackcess-2.1.3.tar.xz jackcess-2.1.3
Source0:       %{name}-%{version}.tar.xz

Patch0:        jackcess-2.1.3-Remove-unreliable-test-for-ancient-dates.patch

BuildRequires: maven-local
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(org.apache.poi:poi)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
Jackcess is a pure Java library for reading from and
writing to MS Access databases (currently supporting
versions 2000-2013).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1

# com.healthmarketscience:openhms-parent:1.1.1
%pom_remove_parent
#%%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin

%pom_change_dep :log4j ::12

%mvn_file :%{name} %{name}
%mvn_file :%{name}-tests::tests: %{name}-tests
%mvn_package :::tests:

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc TODO.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1_1jpp8
- New version (ALT #35509).

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_1jpp8
- new version


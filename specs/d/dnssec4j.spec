Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          dnssec4j
Version:       0.1.6
Release:       alt1_5jpp8
Summary:       Java Wrapper around DNSSEC primitives in dnsjava
License:       Apache-2.0 and GPL-3.0-or-later
URL:           https://github.com/adamfisk/DNSSEC4J
Source0:       https://github.com/adamfisk/DNSSEC4J/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(dnsjava:dnsjava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
DNSSEC4J is a higher level wrapper around the
DNSSEC primitives in dnsjava allowing applications to
more easily integrate DNSSEC into their applications.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n DNSSEC4J-%{name}-%{version}

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-site-plugin

%pom_change_dep :dnsjava dnsjava:

%mvn_file :%{name} %{name}

%build
# Tests use web access, and @ random fails
# DnsSecTest.testGetByName:55  Results not equal for www.beck.com expected:<[54.243.91.158]> but was:<[107.21.220.33]>
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference COPYRIGHT.txt LICENSE_APACHE_2.txt LICENSE_GPL.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYRIGHT.txt LICENSE_APACHE_2.txt LICENSE_GPL.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_1jpp8
- new version


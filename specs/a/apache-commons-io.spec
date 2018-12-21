Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-commons-io
Epoch:          1
Version:        2.6
Release:        alt1_3jpp8
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            http://commons.apache.org/io
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
Source44: import.info

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%{?javadoc_package}

%prep
%setup -q -n commons-io-%{version}-src
sed -i 's/\r//' *.txt

%build
%mvn_file  : commons-io %{name}
%mvn_alias : org.apache.commons:

# NOTE: tests *may* fail because commons-io is on surefire's classpath and causes
# tests to be run against the system version and not the one we just built
%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_1jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_3jpp8
- fc27 update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_2jpp8
- fixed build with new testng

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt1_2jpp8
- new version

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt6_15jpp8
- fixed build

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_15jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_14jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt1_2jpp7
- new release

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp6
- added osgi manifest

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp6
- added compat mapping

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp6
- renamed


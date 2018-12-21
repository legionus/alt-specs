Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# should be consistent across one release
%global build_date 20130405

Name:           sat4j
Version:        2.3.5
Release:        alt1_12jpp8
Summary:        A library of SAT solvers written in Java

License:        EPL or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh sat4j-fetch.sh
Source0:        sat4j-%{version}.tar.xz
Source1:        sat4j-fetch.sh
Patch0:         sat4j-classpath.patch

BuildRequires:  ant
BuildRequires:  javapackages-local

BuildArch:      noarch
Source44: import.info

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q -n sat4j-%{version}
%patch0

%build
ant -Dbuild.compiler=modern -Drelease=%{version} \
 -Dtarget=1.5 -DBUILD_DATE=%{build_date} p2 

%mvn_artifact "org.ow2.sat4j:org.ow2.sat4j.core::%{version}" dist/%{version}/org.sat4j.core.jar
%mvn_artifact "org.ow2.sat4j:org.ow2.sat4j.pb::%{version}" dist/%{version}/org.sat4j.pb.jar
%mvn_file ":org.ow2.sat4j.core" org.sat4j.core
%mvn_file ":org.ow2.sat4j.pb" org.sat4j.pb

%install
%mvn_install

%files -f .mfiles
# No %%doc files as the about.html is in the jar

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_11jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4jpp7
- update to new release by jppimport

* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_2jpp6
- update to new release by jppimport

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp6
- new version

* Mon Oct 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_2jpp6
- new version; for eclipse 2.5.2

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_7jpp6
- rebuild with eclipse 3.4.1

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_7jpp5
- new version


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global spec_name geronimo-jms_1.1_spec

Name:           geronimo-jms
Version:        1.1.1
Release:        alt3_25jpp8
Summary:        J2EE JMS v1.1 API
License:        Apache-2.0
URL:            http://geronimo.apache.org/
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/%{spec_name}-%{version}/
Source0:        %{spec_name}-%{version}.tar.bz

# Remove unavailable dependencies
Patch0:         geronimo-jms-1.1-api-remove-mockobjects.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.geronimo.specs:specs:pom:)
Source44: import.info

%description
The Java Message Service (JMS) API is a messaging standard that allows
application components based on the Java 2 Platform, Enterprise Edition
(J2EE) to create, send, receive, and read messages. It enables distributed
communication that is loosely coupled, reliable, and asynchronous.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{spec_name}-%{version}
%patch0 -p1

%mvn_file  : %{name} %{spec_name} jms
%mvn_alias : javax.jms:jms

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_25jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_24jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_23jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_22jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_20jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_17jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_16jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_13jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_13jpp7
- new version


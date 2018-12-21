Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-j2eemgmt-api_1.1_spec
Name:          jboss-j2eemgmt-1.1-api
Version:       1.0.1
Release:       alt2_13jpp8
Summary:       Java EE Management 1.1 API
License:       LGPLv2+
URL:           http://www.jboss.org/
# git clone git://github.com/jboss/jboss-j2eemgmt-api_spec.git jboss-j2eemgmt-1.1-api
# cd jboss-j2eemgmt-1.1-api/ && git archive --format=tar --prefix=jboss-j2eemgmt-1.1-api/ jboss-j2eemgmt-api_1.1_spec-1.0.1.Final | xz > jboss-j2eemgmt-1.1-api-1.0.1.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: java-devel
BuildRequires: jboss-specs-parent

BuildRequires: jboss-ejb-3.1-api

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
JSR-77: Java EE Management 1.1 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}

%build

%mvn_file :%{oname} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_10jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_9jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version


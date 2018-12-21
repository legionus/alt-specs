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
%global namedversion %{version}%{?namedreltag}

Name:             jboss-iiop-client
Version:          1.0.0
Release:          alt2_16jpp8
Summary:          JBoss IIOP Client
License:          LGPLv2+
URL:              http://www.jboss.org/jbossiiop
Source0:          https://github.com/jbossas/jboss-iiop-client/archive/1.0.0.Final.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
Source44: import.info


%description
Client library for EJB applications working against JBoss AS using
the IIOP protocol

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-iiop-client-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_14jpp8
- new jpp release

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- updated gradle support

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_10jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new version


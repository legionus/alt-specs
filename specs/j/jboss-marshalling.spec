Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.4.11
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-marshalling
Version:          1.4.11
Release:          alt1_4jpp8
Summary:          JBoss Marshalling
# LGPLv2 ./serial/src/main/java/org/jboss/marshalling/serial/UnknownDescriptor.java
License:          ASL 2.0 and LGPLv2+
URL:              http://jbossmarshalling.jboss.org/
BuildArch:        noarch

Source0:          https://github.com/jboss-remoting/jboss-marshalling/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)
BuildRequires:    mvn(org.testng:testng)
%if 0%{?fedora}
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
%endif
Source44: import.info

%description
JBoss Marshalling is an alternative serialization API that fixes many
of the problems found in the JDK serialization API while remaining
fully compatible with java.io.Serializable and its relatives, and adds
several new tunable parameters and additional features, all of which
are pluggable via factory configuration (externalizers, class/instance
lookup tables, class resolution, and object replacement, to name a
few).

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%package osgi
Group: Development/Java
Summary:          JBoss Marshalling OSGi Bundle

%description osgi
JBoss Marshalling OSGi Bundle.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin -r :maven-shade-plugin
%pom_disable_module tests

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

%mvn_package :jboss-marshalling-osgi osgi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%files osgi -f .mfiles-osgi

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt1_3jpp7
- new version


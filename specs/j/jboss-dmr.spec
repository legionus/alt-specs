Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-dmr
Version:          1.3.0
Release:          alt1_3jpp8
Summary:          JBoss DMR
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-dmr
Source0:          https://github.com/jbossas/jboss-dmr/archive/%{namedversion}.tar.gz
# pre-generated with JDK7:
# JAVA_HOME=/path/to/jdk7/ mvn clean generate-resources
# cp target/generated-sources/apt/org/jboss/dmr/* src/main/java/org/jboss/dmr/
# git add src/main/java/org/jboss/dmr/*.java
# git commit -m 'Add pre-generated Java classes' && git format-patch -1
Patch0:           0001-Add-pre-generated-Java-classes.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.google.code.cookcc:cookcc)
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss.apiviz:apiviz:pom:)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
Source44: import.info

%description
This package contains the Dynamic Model Representation.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

%pom_remove_plugin :apt-maven-plugin
%pom_remove_plugin :maven-antrun-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_6jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp8
- java8 update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.1.Beta2jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version


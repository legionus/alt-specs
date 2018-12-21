# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.1
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jaxws-jboss-httpserver-httpspi
Version:          1.0.1
Release:          alt1_13jpp8
Summary:          JBoss httpserver to JAXWS 2.2 HTTP SPI bridge
Group:            Development/Other
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/projects/jaxws-jboss-httpserver-httpspi/tags/jaxws-jboss-httpserver-httpspi-1.0.1.GA/
# tar cafJ jaxws-jboss-httpserver-httpspi-1.0.1.GA.tar.xz jaxws-jboss-httpserver-httpspi-1.0.1.GA
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-dependency-plugin
BuildRequires:    cxf-rt
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-httpserver
BuildRequires:    junit
Source44: import.info

%description
This package contains the JBoss httpserver to JAXWS 2.2 HTTP SPI bridge.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Remove the parent as it is not packaged
%pom_xpath_remove "pom:parent"

%build
# Some Apache CXF modules are still not avialable
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_10jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_9jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- new release

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp7
- new version


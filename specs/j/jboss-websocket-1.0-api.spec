Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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

Name:             jboss-websocket-1.0-api
Version:          1.0.0
Release:          alt1_8jpp8
Summary:          JSR-356: Java WebSocket 1.0 API
License:          CDDL or GPLv2 with exceptions
Url:              https://github.com/jboss/jboss-websocket-api_spec
Source0:          https://github.com/jboss/jboss-websocket-api_spec/archive/jboss-websocket-api_1.0_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    maven-plugin-bundle
BuildRequires:    felix-osgi-foundation
BuildRequires:    felix-parent

BuildArch:        noarch
Source44: import.info

%description
The JSR-356: Java WebSocket 1.0 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-websocket-api_spec-jboss-websocket-api_1.0_spec-%{namedversion}

%build
%mvn_alias "org.jboss.spec.javax.websocket:jboss-websocket-api_1.0_spec" "javax.websocket:javax.websocket-api" "javax.websocket:javax.websocket-client-api"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


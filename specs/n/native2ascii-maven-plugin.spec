Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0
%global namedreltag -beta-1
%global namedversion %{version}%{?namedreltag}
Name:          native2ascii-maven-plugin
Version:       1.0
Release:       alt3_0.15.beta1jpp8
Summary:       Native2Ascii Maven Plugin
License:       MIT
URL:           http://mojo.codehaus.org/%{name}/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip

BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)

BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-plugin

# requires by javadoc-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-invoker)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch
Source44: import.info

%description
Converts files with characters in any
supported character encoding to
one with ASCII and/or Unicode escapes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.15.beta1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.14.beta1jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.13.beta1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.12.beta1jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.11.beta1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.7.beta1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.5.beta1jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.beta1jpp7
- fixed build

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.beta1jpp7
- fixed build

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.beta1jpp7
- new version


Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-injection-plugin
Version:        1.0.2
Release:        alt3_18jpp8
Summary:        Bytecode injection at Maven build time
License:        LGPLv2+
URL:            http://www.jboss.org
BuildArch:      noarch

# svn export http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/maven-plugins/tags/maven-injection-plugin-1.0.2/
# tar cafJ maven-injection-plugin-1.0.2.tar.xz maven-injection-plugin-1.0.2
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  maven-local
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
This package provides capability to perform bytecode injection as part of build.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_16jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_14jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_5jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_5jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp6
- new version


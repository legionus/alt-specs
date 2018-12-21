Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             jboss-specs-parent
Version:          1.0.0
Release:          alt3_0.18.Beta2jpp8
Summary:          JBoss Specification API Parent POM
# The license is not included because it's not a part of this tag. License file
# was pushed to trunk and no new tag will be created for this change.
# http://anonsvn.jboss.org/repos/jbossas/projects/specs/trunk/jboss-specs-parent/LICENSE-2.0.txt
License:          ASL 2.0
Url:              http://www.jboss.org/

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/specs/tags/jboss-specs-parent-1.0.0.Beta2/
# tar czf jboss-specs-parent-1.0.0.Beta2-src-svn.tar.gz jboss-specs-parent-1.0.0.Beta2
Source0:          %{name}-%{namedversion}-src-svn.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Parent POM that allows building all specification projects at once.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_xpath_remove //pom:modules
%pom_remove_plugin :maven-release-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_0.18.Beta2jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_0.17.Beta2jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_0.14.Beta2jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.14.Beta2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.13.Beta2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.12.Beta2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.7.Beta2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.6.Beta2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.5.Beta2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Beta2jpp7
- new release


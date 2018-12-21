Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global spec_ver 1.1
%global spec_name geronimo-commonj_%{spec_ver}_spec
Name:    geronimo-commonj
Version: 1.1.0
Release: alt2_16jpp8
Summary: CommonJ Specification
License: ASL 2.0
URL:     http://geronimo.apache.org/
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/specs-1.4/geronimo-commonj_1.1_spec geronimo-commonj-1.1.0
# tar cvfJ geronimo-commonj-1.1.0.tar.xz geronimo-commonj-1.1.0
Source:  %{name}-%{version}.tar.xz

# Remove the SNAPSHOT tag from the version in the POM file:
Patch0:  %{name}-version-fix.patch

BuildArch: noarch
BuildRequires: geronimo-parent-poms
BuildRequires: maven-local
Source44: import.info

%description
Geronimo CommonJ Specification.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0

%mvn_file :%{spec_name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3jpp7
- new version


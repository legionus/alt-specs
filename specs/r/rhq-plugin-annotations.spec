Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             rhq-plugin-annotations
Version:          3.0.4
Release:          alt2_14jpp8
Summary:          RHQ plugin annotations
License:          GPL-1.0-only and LGPLv2+
URL:              http://rhq-project.org

# git clone git://git.fedorahosted.org/rhq/rhq.git
# git checkout rhq-pluginGen-3.0.4
# cd rhq/modules/helpers/
# tar cafJ rhq-plugin-annotations-3.0.4.tar.xz pluginAnnotations
Source0:          rhq-plugin-annotations-%{version}.tar.xz
Patch0:           rhq-plugin-annotations-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    maven-local
Source44: import.info

%description
Annotations to help generate RHQ plugin descriptors.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n pluginAnnotations
%patch0 -p1

%mvn_file : %{name}/%{name} %{name}

%build
%mvn_build -- -Dproject.build.sourceEncoding=iso8859-1

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_3jpp7
- new version


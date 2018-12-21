Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.osgi.core

Name:           felix-osgi-core
Version:        1.4.0
Release:        alt5_23jpp8
Summary:        Felix OSGi R4 Core Bundle
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-osgi-core.html
BuildArch:      noarch

Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
export LC_ALL=en_US.UTF-8
%mvn_build -- -Drat.numUnapprovedLicenses=50

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_23jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_22jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_21jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_20jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_19jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_18jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_10jpp7
- new release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_6jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_6jpp6
- new version


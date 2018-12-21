Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-toolchain
Version:        1.4
Release:        alt3_16jpp8
Summary:        Jetty Toolchain main POM file

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
Source44: import.info

%description
Jetty Toolchain main POM file

%prep
%setup -q
cp -p jetty-distribution-remote-resources/src/main/resources/* .

pushd %{name}
%pom_remove_plugin :maven-release-plugin

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_12jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version


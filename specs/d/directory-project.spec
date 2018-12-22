Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          directory-project
Version:       35
Release:       alt1_5jpp8
Summary:       Apache Directory Project Root pom
License:       Apache-2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/project/tags/35 directory-project-35
# tar cJf directory-project-35.tar.xz directory-project-35
Source0:       directory-project-35.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
The Apache Directory Project provides directory solutions
entirely written in Java. These include a directory server,
which has been certified as LDAP v3 compliant by the
Open Group (Apache Directory Server), and Eclipse-based
directory tools (Apache Directory Studio).

%prep
%setup -q
%pom_remove_plugin :tools-maven-plugin
%pom_remove_plugin :maven-xbean-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :javancss-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :l10n-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :versions-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin

%pom_remove_plugin :maven-site-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 35-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 35-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 35-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 35-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 27-alt1_1jpp7
- new version


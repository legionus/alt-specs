Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name       configuration
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.10
Release:        alt1_11jpp8
Summary:        Commons Configuration Package

License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-digester:commons-digester)
BuildRequires:  mvn(commons-jxpath:commons-jxpath)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.commons:commons-jexl)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-resolver:xml-resolver)
Source44: import.info


%description
Configuration is a project to provide a generic Configuration
interface and allow the source of the values to vary. It
provides easy typed access to single, as well as lists of
configuration values based on a 'key'.
Right now you can load properties from a simple properties
file, a properties file in a jar, an XML file, JNDI settings,
as well as use a mix of different sources using a
ConfigurationFactory and CompositeConfiguration.
Custom configuration objects are very easy to create now
by just subclassing AbstractConfiguration. This works
similar to how AbstractList works.

%if 0
%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.
%endif


%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt NOTICE.txt

%pom_change_dep :log4j ::1.2.17

%build
%mvn_file   : %{short_name} %{name}
%mvn_alias  : org.apache.commons:%{short_name}
# We skip tests because we don't have test deps (dbunit in particular).
# FIXME Javadocs are temporarly disabled due to JDK bug, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1423421
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%if 0
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt
%endif


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_6jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_5jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt3_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt3_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt3_1jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new version

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp6
- new version


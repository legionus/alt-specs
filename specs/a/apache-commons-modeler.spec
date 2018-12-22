Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name       modeler
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.0.1
Release:          alt1_21jpp8
Summary:          Model MBeans utility classes
License:          Apache-2.0
URL:              http://commons.apache.org/%{base_name}/
BuildArch:        noarch

Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# POM file based on the one from an unreleased upstream snapstream
Source1:          pom.xml

BuildRequires:  maven-local
BuildRequires:  mvn(commons-digester:commons-digester)
BuildRequires:  mvn(commons-logging:commons-logging-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(xml-apis:xml-apis)
Source44: import.info


%description
Commons Modeler makes the process of setting up JMX (Java Management
Extensions) MBeans easier by configuring the required meta data using an XML
descriptor. In addition, Modeler provides a factory mechanism to create the
actual Model MBean instances.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Copy pom file into place
cp -p %{SOURCE1} .

# Remove redundant dep on mx4j
%pom_remove_dep mx4j:mx4j-jmx

# Fix ant dependency
%pom_remove_dep ant:ant
%pom_add_dep org.apache.ant:ant:1.8

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{name} %{short_name}

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_21jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_20jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_19jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_18jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_17jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_11jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_9jpp7
- fc update

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_0.r832084.4jpp6
- set target 5

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_0.r832084.4jpp6
- new version


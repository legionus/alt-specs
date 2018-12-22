Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           XmlSchema
Version:        2.2.3
Release:        alt1_1jpp8
Summary:        Lightweight schema object model
License:        Apache-2.0
URL:            http://ws.apache.org/xmlschema/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/ws/xmlschema/%{version}/xmlschema-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xmlunit:xmlunit)
Source44: import.info

Provides: ws-commons-%name = 0:%version-%release
Conflicts:  ws-commons-%name <= 0:1.4.7-alt3_7jpp7
Obsoletes:  ws-commons-%name <= 0:1.4.7-alt3_7jpp7


%description
Commons XMLSchema is a lightweight schema object model that can be 
used to manipulate or generate a schema.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n xmlschema-%{version}

# Fix line endings
sed -i -e 's/\r//g' RELEASE-NOTE.txt

# Missing deps on org.ops4j for this module
%pom_disable_module xmlschema-bundle-test

# This module contains only testdata and according to upstream, should not be deployed
%pom_disable_module w3c-testcases

# Compatibility alias
%mvn_alias :xmlschema-core org.apache.ws.commons.schema:XmlSchema

%build
%mvn_build -- -P!sourcecheck

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.3-alt1_1jpp8
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_14jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_12jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_11jpp8
- java 8 mass update


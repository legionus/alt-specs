Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           args4j
Version:        2.33
Release:        alt1_4jpp8
Summary:        Java command line arguments parser
License:        MIT
URL:            http://args4j.kohsuke.org
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-site-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.kohsuke:pom:pom:)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info

%description
args4j is a small Java class library that makes it easy
to parse command line options/arguments in your CUI application.
- It makes the command line parsing very easy by using annotations
- You can generate the usage screen very easily
- You can generate HTML/XML that lists all options for your documentation
- Fully supports localization
- It is designed to parse javac like options (as opposed to GNU-style
  where ls -lR is considered to have two options l and R)

%package tools
Group: Development/Java
Summary:        Development-time tool for generating additional artifacits

%description tools
This package contains args4j development-time tool for generating
additional artifacits.

%package parent
Group: Development/Java
Summary:        args4j parent POM

%description parent
This package contains parent POM for args4j project.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-site-%{version}

# removing classpath addition
sed -i 's/<addClasspath>true/<addClasspath>false/g' %{name}-tools/pom.xml

# fix ant group id
sed -i 's/<groupId>ant/<groupId>org.apache.ant/g' %{name}-tools/pom.xml

# removing bundled stuff
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%pom_remove_plugin :maven-shade-plugin %{name}-tools
%pom_remove_plugin -r :maven-site-plugin

# XMvn cannot generate requires on dependecies with scope "system"
%pom_xpath_remove "pom:profile[pom:id[text()='jdk-tools-jar']]" %{name}-tools
%pom_add_dep com.sun:tools %{name}-tools

# we don't need these now
%pom_disable_module args4j-maven-plugin
%pom_disable_module args4j-maven-plugin-example

# put args4j-tools and parent POM to separate subpackages
%mvn_package :args4j-tools::{}: %{name}-tools
%mvn_package :args4j-site::{}: %{name}-parent

# install also compat symlinks
%mvn_file ":{*}" %{name}/@1 @1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference %{name}/LICENSE.txt

%files tools -f .mfiles-%{name}-tools

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference %{name}/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference %{name}/LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1_2jpp8
- java8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.25-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt1_8jpp7
- new version


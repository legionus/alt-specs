Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          evo-inflector
Version:       1.2.1
Release:       alt1_7jpp8
Summary:       Implements English pluralization algorithm
License:       Apache-2.0
URL:           https://github.com/atteo/evo-inflector
Source0:       https://github.com/atteo/evo-inflector/archive/%{version}.tar.gz
# Test deps
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
Evo Inflector implements English pluralization algorithm
based on Damian Conway's paper "An Algorithmic Approach to
English Pluralization".

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# org.atteo:parent:pom:1.11
%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.atteo</groupId>"

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp8
- new version


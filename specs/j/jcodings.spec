# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit_hash d50ee0e
%global tag_hash d50ee0e

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.9
Release:        alt2_13jpp8
Summary:        Java-based codings helper classes for Joni and JRuby

Group:          Development/Other
License:        MIT
URL:            http://github.com/jruby/%{name}
Source0:        https://github.com/jruby/jcodings/tarball/%{version}/jruby-%{name}-%{version}-0-g%{commit_hash}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-source-plugin
Source44: import.info

%description
Java-based codings helper classes for Joni and JRuby.


%prep
%setup -q -n jruby-%{name}-%{tag_hash}

find -name '*.class' -delete
find -name '*.jar' -delete

%mvn_file : %{name}

%build
echo "See %{url} for more info about the %{name} project." > README.txt

%pom_xpath_remove "pom:build/pom:extensions"
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_5jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_1jpp7
- rebuild with maven-local

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp5
- new version


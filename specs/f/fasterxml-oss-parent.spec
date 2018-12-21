Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname oss-parent
Name:          fasterxml-oss-parent
Version:       26
Release:       alt1_6jpp8
Summary:       FasterXML parent pom
License:       ASL 2.0
URL:           http://fasterxml.com/
Source0:       https://github.com/FasterXML/oss-parent/archive/oss-parent-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{oname}-%{oname}-%{version}

%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
# org.kathrynhuxtable.maven.wagon:wagon-gitsite:0.3.1
%pom_xpath_remove "pom:build/pom:extensions"
# remove unavailable com.google.doclava doclava 1.0.3
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']" '
<configuration>
  <encoding>UTF-8</encoding>
  <quiet>true</quiet>
  <source>${javac.src.version}</source>
</configuration>'

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.creole
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 26-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 24-alt1_3jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 18e-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 18e-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt2_3jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt2_1jpp7
- fixed maven1 dependency

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- use /var/lock/serial


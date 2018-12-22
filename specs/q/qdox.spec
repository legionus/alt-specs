Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global vertag M7

Summary:        Extract class/interface/method definitions from sources
Name:           qdox
Version:        2.0
Release:        alt1_0.12.M7jpp8
Epoch:          1
License:        Apache-2.0
URL:            https://github.com/paul-hammant/qdox
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/com/thoughtworks/qdox/qdox/%{version}-%{vertag}/%{name}-%{version}-%{vertag}-project.tar.gz
Source1:        qdox-MANIFEST.MF

BuildRequires:  byaccj
BuildRequires:  jflex
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info
Obsoletes: qdox16-poms < 1.1


%description
QDox is a high speed, small footprint parser
for extracting class/interface/method definitions
from source files complete with JavaDoc @tags.
It is designed to be used by active code
generators or documentation tools.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API docs for %{name}.


%prep
%setup -q -n %{name}-%{version}-%{vertag}
find -name *.jar -delete
rm -rf bootstrap

# We don't need these plugins
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-jflex-plugin

%mvn_file : %{name}
%mvn_alias : qdox:qdox

%pom_xpath_set pom:workingDirectory '${basedir}/src/main/java/com/thoughtworks/qdox/parser/impl'

%build
# Generate scanners (upstream does this with maven-jflex-plugin)
jflex --inputstreamctor -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/lexer.flex
jflex --inputstreamctor -d src/main/java/com/thoughtworks/qdox/parser/impl src/grammar/commentlexer.flex

# Build artifact
%mvn_build -f -- -Dqdox.byaccj.executable=byaccj

# Inject OSGi manifests
jar ufm target/%{name}-%{version}*.jar %{SOURCE1}

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.12.M7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.11.M7jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.8.M5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.5.M3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt1_0.4.M3jpp8
- unbootstrap build

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt2_5jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_5jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_2jpp7
- fc update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt3_2jpp6
- fixed build

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt2_2jpp6
- fixed build with java 7

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt1_2jpp6
- new version

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt2_5jpp6
- rebuild with target=5

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp6
- new version

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp5
- reverted to version 1.6.1

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp5
- fixed build with jpackage 5

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- rebuilt with maven1

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp1.7
- converted from JPackage by jppimport script


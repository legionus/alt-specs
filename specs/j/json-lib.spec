Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           json-lib
Version:        2.4
Release:        alt1_14jpp8
Summary:        JSON library for Java
License:        ASL 2.0
URL:            http://json-lib.sourceforge.net/
# NOTE: newer release (> 2.4) is available here https://github.com/aalmiray/Json-lib/
# A plain jarball with the source is provided by upstream.  We could use
# it, but we choose to build with maven for the sake of consistency.
# Therefore we pull the tree with maven metadata from git.
# sh create-tarball.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        create-tarball.sh
Patch0:         %{name}-%{version}-antrun-plugin.patch

# Jenkins sources/patches
# tarball comming from not yet released upstream git repo
# it contains changes from Jenkins upstream
Source100:      jenkins-%{name}-%{version}.tar.xz
Source101:      http://repo.jenkins-ci.org/releases/org/kohsuke/stapler/json-lib/%{version}-jenkins-3/json-lib-%{version}-jenkins-3.pom
Patch100:       %{name}-%{version}-Use-Jenkins-default-values.patch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(net.sf.ezmorph:ezmorph)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy18:1.8)
BuildRequires:  mvn(org.codehaus.groovy:groovy18-all:1.8)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(xom:xom)
BuildRequires:  mvn(xmlunit:xmlunit)

# antrun-plugin deps for groovy ant task
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(asm:asm-all)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(org.slf4j:slf4j-nop)

BuildArch:      noarch
Source44: import.info

%description
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

%package -n jenkins-json-lib
Group: Development/Java
Summary:        Jenkins JSON library

%description -n jenkins-json-lib
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

This package contains JSON library used in Jenkins.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

tar xf %{SOURCE100}

# compile: src/main/groovy/net/sf/json/groovy/GJson.groovy
#          src/main/jdk15/net/sf/json/util/EnumMorpher.java
%patch0 -p1

# Not strictly needed, but it makes no harm to be on the safe side
find -name '*.jar' -delete 
find -name '*.class' -delete

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy

%pom_remove_plugin :maven-compiler-plugin
%pom_remove_plugin :gmaven-plugin

%pom_xpath_remove "pom:project/pom:prerequisites"
%pom_xpath_remove "pom:project/pom:reporting"

# error: duplicate class
rm -r src/main/jdk15/net/sf/json/JSON*.java
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . '
<configuration>
  <charset>UTF-8</charset>
  <docencoding>UTF-8</docencoding>
  <sourcepath>${basedir}/src/main</sourcepath>
</configuration>'

# should be removed from distribution
%pom_remove_dep :commons-httpclient

%pom_change_dep org.codehaus.groovy:groovy org.codehaus.groovy:groovy18:1.8

cp %{SOURCE101} jenkins-%{name}-%{version}/pom.xml

pushd jenkins-%{name}-%{version}
%patch100 -p1

%pom_change_dep org.codehaus.groovy:groovy-all org.codehaus.groovy:groovy18-all:1.8

%mvn_file org.kohsuke.stapler:json-lib jenkins-%{name}
%mvn_package org.kohsuke.stapler:json-lib jenkins-json-lib

popd

%build
%mvn_file : %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

# build Jenkins JSON lib
pushd jenkins-%{name}-%{version}
%mvn_build -f
popd

%install
%mvn_install

# install Jenkins JSON lib
pushd jenkins-%{name}-%{version}
%mvn_install
popd

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%files -n jenkins-json-lib -f jenkins-%{name}-%{version}/.mfiles-jenkins-json-lib
%doc --no-dereference LICENSE.txt
%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_12jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_10jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_9jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_10jpp7
- new release

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_8jpp7
- fc update

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_5jpp7
- fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_5jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp6
- new version


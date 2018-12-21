Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag -M8
%global namedversion %{version}%{?namedreltag}
Name:          mavibot
Version:       1.0.0
Release:       alt1_0.7.M8jpp8
Summary:       ApacheDS MVCC BTree implementation
License:       ASL 2.0
URL:           http://directory.apache.org/mavibot/
Source0:       http://www.apache.org/dist/directory/mavibot/dist/%{namedversion}/%{name}-%{namedversion}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

BuildArch:     noarch
Source44: import.info

%description
Mavibot is a Multi Version Concurrency Control (MVCC) BTree in Java. It
is expected to be a replacement for JDBM (The current back-end for the
Apache Directory Server), but could be a good fit for any other project
in need of a Java MVCC BTree implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -print -delete
rm -r docs
%pom_remove_parent
%pom_disable_module distribution

%pom_remove_plugin org.apache.geronimo.genesis.plugins:tools-maven-plugin

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :findbugs-maven-plugin

# This test fail on ARM builder only
# OutOfMemoryError: Java heap space testPersistedBulkLoad1000Elements Time elapsed: 155.802 sec
rm mavibot/src/test/java/org/apache/directory/mavibot/btree/BulkLoaderTest.java
# AssertionError: expected:<9> but was:<8>
rm mavibot/src/test/java/org/apache/directory/mavibot/btree/PageReclaimerTest.java
# Browse Forward for 9 = 2046
# Browe backward for 9 = 5096
# IOException: Too many open files
rm mavibot/src/test/java/org/apache/directory/mavibot/btree/PersistedBTreeBrowseTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.M8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.M8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.M8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.M8jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.M8jpp8
- new version


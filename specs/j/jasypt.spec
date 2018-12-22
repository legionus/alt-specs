Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jasypt
Version:       1.9.2
Release:       alt1_8jpp8
Summary:       Java Simplified Encryption
License:       Apache-2.0
Url:           http://www.jasypt.org/
# svn export https://jasypt.svn.sourceforge.net/svnroot/jasypt/tags/jasypt/jasypt-1.9.2 jasypt-1.9.2
# tar cJf jasypt-1.9.2.tar.xz jasypt-1.9.2
Source0:       %{name}-%{version}.tar.xz
# remove internal commons-codec 1.3
Patch0:        %{name}-1.9.0-use-system-commons-codec.patch
# tks to jhernand
# system commons-codec 1.4 support
Patch1:        %{name}-1.9.0-StandardStringDigester.patch
Patch2:        %{name}-1.9.0-StandardPBEStringEncryptor.patch

BuildRequires: maven-local
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk16)

BuildArch:     noarch
Source44: import.info

%description
Java library which enables encryption
in java apps with minimum effort.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-assembly-plugin

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-resources-plugin']/pom:configuration"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-resources-plugin']" "
<configuration>
  <encoding>UTF-8</encoding>
</configuration>"

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']" "
<configuration>
  <source>1.6</source>
  <target>1.6</target>
  <encoding>UTF-8</encoding>
</configuration>"

%pom_change_dep bouncycastle:bcprov-jdk12 org.bouncycastle:bcprov-jdk16:1.46:test

%pom_add_dep commons-logging:commons-logging::test

# force servlet-3.1 api
%pom_change_dep javax.servlet: :javax.servlet-api:3.1.0


%mvn_file :%{name} %{name}

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt README.txt RELEASING.txt USAGE.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_6jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_2jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_4jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2_2jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_4jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_2jpp7
- new version


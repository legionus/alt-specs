Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          mybatis-parent
Version:       21
Release:       alt1_8jpp8
Summary:       The MyBatis parent POM
License:       Apache-2.0
URL:           http://www.mybatis.org/
Source0:       https://github.com/mybatis/parent/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:     noarch
Source44: import.info

%description
The MyBatis parent POM which has to be inherited by all MyBatis modules.

%prep
%setup -q -n parent-%{name}-%{version}
# require com.github.stephenc.wagon:wagon-gitsite:0.4.1
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# unavailable plugins
%pom_remove_plugin org.apache.maven.plugins:maven-pdf-plugin
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

# animal-sniffer is currently broken. it uses asm4, but asm3 is loaded
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-scm-plugin

# remove com.google.doclava:doclava:1.0.3
# javac.target.version is set 1.5
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" '
 <configuration>
  <minmemory>128m</minmemory>
  <maxmemory>1024m</maxmemory>
  <breakiterator>true</breakiterator>
  <quiet>true</quiet>
  <verbose>false</verbose>
  <source>${javac.target.version}</source>
  <linksource>true</linksource>
</configuration>'

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-enforcer-plugin']/pom:executions/pom:execution/pom:configuration/pom:rules/pom:requirePluginVersions"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 21-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 21-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 21-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 21-alt1_3jpp8
- java 8 mass update


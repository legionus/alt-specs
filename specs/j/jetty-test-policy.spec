Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-test-policy
Version:        1.2
Release:        alt3_19jpp8
Summary:        Jetty test policy files
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
Source2:        http://www.eclipse.org/legal/epl-v10.html
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         0001-Sign-JAR-with-maven-jarsigner-plugin.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-jarsigner-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
Source44: import.info

%description
Jetty test policy files

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE2} %{SOURCE3} .

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
    <execution>
      <id>default-jar</id>
      <phase>skip</phase>
    </execution>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference epl-v10.html LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_17jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new version


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-version-maven-plugin
Version:        1.0.7
Release:        alt4_18jpp8
Summary:        Jetty version management Maven plugin

License:        Apache-2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
Source44: import.info


%description
Jetty version management Maven plugin

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q
# copy license files
cp -p jetty-distribution-remote-resources/src/main/resources/* .

# we have java.util stuff in JVM directly now
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=401163
sed -i 's|edu.emory.mathcs.backport.||' \
    jetty-version-maven-plugin/src/main/java/org/eclipse/jetty/toolchain/version/Release.java

%build
pushd %{name}
# skip tests because we don't have jetty-test-helper (yet)
%mvn_build -f

%install
pushd %{name}
%mvn_install


%files -f %{name}/.mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html

%files javadoc -f %{name}/.mfiles-javadoc
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_16jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_14jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt4_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_4jpp7
- new version


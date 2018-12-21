Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          spec-version-maven-plugin
Version:       1.2
Release:       alt1_11jpp8
Summary:       Spec Version Maven Plugin
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/spec-version-maven-plugin-1.2
# tar czf spec-version-maven-plugin-1.2-src-svn.tar.gz spec-version-maven-plugin-1.2
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# spec-version-maven-plugin package don't include the license file
Source1:       glassfish-LICENSE.txt


BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-resources)

# test dep
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-plugin

BuildArch:     noarch
Source44: import.info

%description
Maven Plugin to configure APIs version and
specs in a MANIFEST.MF file.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp7
- new release


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-master-pom
Version:       8
Release:       alt1_11jpp8
Summary:       Master POM for Glassfish Maven projects
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/master-pom-8/ glassfish-master-pom-8
# tar czf glassfish-master-pom-8-src-svn.tar.gz glassfish-master-pom-8
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-master-pom package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
This is a shared POM parent for Glassfish Maven projects.

%prep
%setup -q
# remove wagon-webdav
%pom_xpath_remove pom:build/pom:extensions
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-compiler-plugin']" "<groupId>org.apache.maven.plugins</groupId><version>2.5.1</version>"
cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 8-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 8-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 8-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_8jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_7jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt1_4jpp7
- new release


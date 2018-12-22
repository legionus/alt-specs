Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname annotations
Name:          jetbrains-annotations
Version:       15.0
Release:       alt1_6jpp8
Summary:       IntelliJ IDEA Annotations
License:       Apache-2.0
URL:           http://www.jetbrains.org
Source0:       http://central.maven.org/maven2/org/jetbrains/annotations/%{version}/annotations-%{version}-sources.jar
Source1:       http://central.maven.org/maven2/org/jetbrains/annotations/%{version}/annotations-%{version}.pom
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local

BuildArch:     noarch
Source44: import.info

%description
A set of annotations used for code inspection support and code documentation.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -T -q -c

mkdir -p src/main/{java,resources}

(
  cd src/main/java
  %jar -xf %{SOURCE0}
  rm -rf META-INF
)

cp -p %{SOURCE1} pom.xml

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_inject pom:properties "<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

cp -p %{SOURCE2} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file org.jetbrains:%{oname} %{name}
%mvn_alias org.jetbrains:%{oname} com.intellij:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_4jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_3jpp8
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt2_2jpp5
- fixes for java6 support

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt1_2jpp5
- new jpp release

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt1_1jpp5
- jpp5 build


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
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global apiversion 3.2
%global oname jboss-ejb-api_%{apiversion}_spec
%global pname jboss-ejb-api_spec
Name:          jboss-ejb-3.2-api
Version:       1.0.0
Release:       alt1_4jpp8
Summary:       Enterprise JavaBeans 3.2 API
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-ejb-api_spec
Source0:       https://github.com/jboss/jboss-ejb-api_spec/archive/%{oname}-%{namedversion}.tar.gz
Source1:       http://jcp.org/aboutJava/communityprocess/cddl.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.xml.rpc:jboss-jaxrpc-api_1.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)

BuildArch:     noarch
Source44: import.info

%description
JSR 345: Enterprise JavaBeans 3.2 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pname}-%{oname}-%{namedversion}
# Unwanted build source jar
%pom_remove_plugin :maven-source-plugin

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE
cp -p %{SOURCE1} .

%mvn_file :%{oname} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference cddl.txt LICENSE

%files javadoc -f .mfiles-javadoc
%doc README
%doc --no-dereference cddl.txt LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Alpha2jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha2jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.Alpha2jpp7
- new version


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.2.13
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jsf-2.2-api
Version:       2.2.13
Release:       alt1_4jpp8
Summary:       JavaServer Faces 2.2 API
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://www.jboss.org
Source0:       https://github.com/jboss/jboss-jsf-api_spec/archive/jboss-jsf-api_2.2_spec-%{namedversion}.tar.gz
Source1:       cddl.txt
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(com.sun.faces:jsf-impl)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.3_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec)

BuildArch:     noarch
Source44: import.info

%description
This package contains JSR-344: JavaServer Faces 2.2 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jsf-api_spec-jboss-jsf-api_2.2_spec-%{namedversion}

# We don't have this
%pom_remove_dep "org.jboss.spec:jboss-javaee-all-7.0"
# But we have this
%pom_add_dep "javax.inject:javax.inject"
%pom_add_dep "javax.enterprise:cdi-api"

cp %{SOURCE1} .
cp %{SOURCE2} .

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference cddl.txt LICENSE LICENSE-2.0.txt
%doc README

%files javadoc -f .mfiles-javadoc
%doc --no-dereference cddl.txt LICENSE LICENSE-2.0.txt
%doc README


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


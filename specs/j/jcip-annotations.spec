Epoch: 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jcip-annotations
Version:        1
Release:        alt3_23.20060626jpp8
Summary:        Java annotations for multithreaded software

License:        CC-BY
URL:            http://www.jcip.net/
Source0:        http://jcip.net.s3-website-us-east-1.amazonaws.com/%{name}-src.jar
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/net/jcip/%{name}/1.0/%{name}-1.0.pom

# Add temporary dependency on javapackages-local, for %%add_maven_depmap macro
# See https://lists.fedoraproject.org/archives/list/java-devel@lists.fedoraproject.org/thread/R3KZ7VI5DPCMCELFIVJQ4AXB2WQED35C/
BuildRequires:  javapackages-local

# There is no point in building native libraries, as the sources contain only
# annotation definitions, so no code would be generated.
BuildArch:      noarch
BuildRequires:  java-devel >= 1.5.0 jpackage-utils

Requires:       jpackage-utils
Source44: import.info


%description
This package provides class, field, and method level annotations for
describing thread-safety policies.  These annotations are relatively
unintrusive and are beneficial to both users and maintainers.  Users can see
immediately whether a class is thread-safe, and maintainers can see
immediately whether thread-safety guarantees must be preserved.  Annotations
are also useful to a third constituency: tools.  Static code-analysis tools
may be able to verify that the code complies with the contract indicated by
the annotation, such as verifying that a class annotated with @Immutable
actually is immutable.

%package javadoc
Group: Development/Java
Summary:        Javadoc for jcip-annotations
BuildArch: noarch

%description javadoc
Javadoc documentation for the jcip-annotations package.
On systems where javadoc is sinjdoc, this package contains nothing useful
since sinjdoc does not understand annotations.

%prep
%setup -q -c

# Get rid of the manifest created upstream with ant
rm -fr META-INF

# Fix DOS line endings
sed -i 's/\r//' net/jcip/annotations/package.html

%build
mkdir classes
find . -name '*.java' | xargs %javac -g -source 1.5 -target 1.5 -d classes
cd classes
%jar cf ../%{name}.jar net
cd ..
%javadoc -Xdoclint:none -d docs -source 1.5 net.jcip.annotations

%install
mkdir -p %{buildroot}%{_javadir}
mv %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# install maven metadata
mkdir -p %{buildroot}/%{_mavenpomdir}
cp %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a com.github.stephenc.jcip:jcip-annotations

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:1-alt3_23.20060626jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1-alt3_22.20060626jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:1-alt3_19.20060626jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1-alt3_18.20060626jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1-alt3_17.20060626jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_8.20060626jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_7.20060626jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_5.20060626jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- added repolib

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script


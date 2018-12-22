Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    jackson
Version: 1.9.11
Release: alt1_13jpp8
Summary: Jackson Java JSON-processor
License: Apache-2.0 or LGPLv2
URL:     http://jackson.codehaus.org
Source0: http://jackson.codehaus.org/1.9.11/jackson-src-1.9.11.tar.gz
# Build plain jar files instead of OSGi bundles in order to avoid depending on
# BND:
Patch0:  %{name}-build-plain-jars-instead-of-osgi-bundles.patch
# Don't require a repackaged version of ASM:
Patch1:  %{name}-dont-require-repackaged-asm.patch
# Don't bundle the ASM classes:
Patch2:  %{name}-dont-bundle-asm.patch
# fix for JACKSON-875
Patch3:  %{name}-1.9.11-to-1.9.13.patch
# Fix javadoc build
Patch4:  %{name}-1.9.11-javadoc.patch

BuildArch: noarch

Requires: joda-time >= 1.6.2
Requires: stax2-api >= 3.1.1
Requires: jsr-311 >= 1.1.1
Requires: objectweb-asm3 >= 3.3

BuildRequires: javapackages-local
BuildRequires: ant >= 1.8.2
BuildRequires: joda-time >= 1.6.2
BuildRequires: stax2-api >= 3.1.1
BuildRequires: jsr-311 >= 1.1.1
BuildRequires: objectweb-asm3 >= 3.3
BuildRequires: cglib >= 2.2
BuildRequires: groovy18 >= 1.8.5
Source44: import.info

%description
JSON processor (JSON parser + JSON generator) written in Java. Beyond basic
JSON reading/writing (parsing, generating), it also offers full node-based Tree
Model, as well as full OJM (Object/Json Mapper) data binding functionality.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

# Remove all the binary jar files, as the packaging policies
# forbids using them:
find . -type f -name '*.jar' -exec rm {} \;

# Remove some tests to avoid additional dependencies:
rm src/test/org/codehaus/jackson/map/interop/TestHibernate.java
rm src/perf/perf/TestJsonPerf.java
rm src/test/org/codehaus/jackson/map/interop/TestGoogleCollections.java

# Make symbolic links to the jar files expected by the ant build
# scripts:
ln -s $(build-classpath joda-time) lib/ext/joda-time.jar
ln -s $(build-classpath stax2-api) lib/xml/sta2-api.jar
ln -s $(build-classpath jsr-311) lib/jaxrs/jsr-311.jar
ln -s $(build-classpath objectweb-asm3/asm) lib/ext/asm/asm.jar
ln -s $(build-classpath objectweb-asm3/asm) lib/repackaged/jackson-asm.jar
ln -s $(build-classpath cglib/cglib) lib/ext/cglib/cglib-nodep.jar
ln -s $(build-classpath groovy18-1.8) lib/ext/groovy/groovy.jar
ln -s $(build-classpath junit) lib/junit/junit.jar

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," \
 release-notes/lgpl/LGPL2.1

native2ascii -encoding UTF8 src/test/org/codehaus/jackson/jaxrs/TestUntouchables.java \
 src/test/org/codehaus/jackson/jaxrs/TestUntouchables.java

%build

ant dist

%install

# For each jar file install it and its pom:
jars='
jackson-core-asl
jackson-mapper-asl
jackson-xc
jackson-smile
jackson-mrbean
jackson-jaxrs
'
for jar in ${jars}
do
  %mvn_artifact dist/${jar}-%{version}.pom dist/${jar}-%{version}.jar
done

%mvn_install -J dist/javadoc/

%files -f .mfiles
%doc README.txt
%doc release-notes

%files javadoc -f .mfiles-javadoc
%doc README.txt
%doc release-notes

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_12jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_8jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt1_6jpp8
- java 8 mass update

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt1_5jpp7
- new version


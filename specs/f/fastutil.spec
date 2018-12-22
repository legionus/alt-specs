Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          fastutil
Version:       7.0.7
Release:       alt1_5jpp8
Summary:       Fast & compact type-specific collections for Java
# LGPL (v2.1 or later):
# src/it/unimi/dsi/fastutil/io/InspectableFileCachedInputStream.java
# test/it/unimi/dsi/fastutil/io/InspectableFileCachedInputStreamTest.java
License:       Apache-2.0 and LGPLv2+
# altenative url
#URL:           https://github.com/vigna/fastutil
# often is offline
URL:           http://fastutil.di.unimi.it/
Source0:       https://github.com/vigna/fastutil/archive/%{version}.tar.gz
# Disable ivy and maven-ant-tasks support
# Fix aqute-bnd classpath
# Fix pom task
Patch0:        fastutil-7.0.7-build.patch

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: emma
BuildRequires: java-javadoc
BuildRequires: javapackages-local
# Required for generate source code
BuildRequires: gcc

BuildArch:     noarch
Source44: import.info

%description
Fastutil extends the Java Collections Framework by providing type-specific
maps, sets, lists and priority queues with a small memory footprint and
fast access and insertion; it also includes a fast I/O API for binary and
text files. The classes implement their standard counterpart interface
(e.g., Map for maps) and can be plugged into existing code. Moreover, they
provide additional features (such as bidirectional iterators) that are not
available in the standard classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%patch0 -p1

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," \
 src/it/unimi/dsi/fastutil/io/InspectableFileCachedInputStream.java \
 test/it/unimi/dsi/fastutil/io/InspectableFileCachedInputStreamTest.java
 
# Remove empty dependencies list
%pom_xpath_remove "pom:dependencies" pom-model.xml

%build

# Generate source code
mkdir -p build
make -s clean sources
# Build
ant -Djar.base=%{_javadir}/emma -Dj2se.apiurl=%{_javadocdir}/java pom

%install
%mvn_file it.unimi.dsi:%{name} %{name}
%mvn_artifact dist/lib/pom.xml dist/lib/%{name}-%{version}.jar
%mvn_install -J docs

%check
mkdir -p reports
ant -Djar.base=%{_javadir}/emma junit

%files -f .mfiles
%doc CHANGES README.md
%doc --no-dereference LICENSE-2.0

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 7.0.7-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 7.0.7-alt1_4jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 7.0.7-alt1_3jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 7.0.7-alt1_2jpp8
- new version


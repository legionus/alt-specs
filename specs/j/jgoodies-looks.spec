# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global shortname looks

Name:           jgoodies-looks
Version:        2.6.0
Release:        alt1_7jpp8
Summary:        Free high-fidelity Windows and multi-platform appearance

Group:          Development/Other
License:        BSD
URL:            http://www.jgoodies.com/freeware/looks/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# Fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu
BuildRequires:  fontconfig
BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common) >= 1.8.0
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
# JGoodies Looks >= 2.4.2 doesn't provide demo jars anymore
Provides:       %{name}-demo = %{version}-%{release}
Obsoletes:      %{name}-demo < 2.4.2
BuildArch:      noarch
Source44: import.info

%description
The JGoodies look&feels make your Swing applications and applets look better.
They have been optimized for readability, precise micro-design and usability.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Move the resources into a "resources" directory so they end up packaged
# properly
mkdir -p src/main/resources/com/jgoodies/looks/plastic/
mv src/main/java/com/jgoodies/looks/plastic/icons/ src/main/resources/com/jgoodies/looks/plastic/
mkdir -p src/main/resources/com/jgoodies/looks/common
mv src/main/java/com/jgoodies/looks/common/*.png src/main/resources/com/jgoodies/looks/common/

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Fix wrong end-of-line encoding
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed -i.orig "s/\r//" $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%mvn_file :%{name} %{name} %{name}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.html RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt


%files javadoc -f .mfiles-javadoc


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_5jpp8
- new jpp release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_3jpp8
- new version

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt2
- NMU: BR: maven-local

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1
- update to 2.5.2

* Wed Sep 23 2009 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21517)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt2
- Added java-devel-default

* Wed Apr 30 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt1
- Initial RPM.


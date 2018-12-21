Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /bin/ping
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name exec
%global short_name commons-%{base_name}

Name:           apache-commons-exec
Version:        1.3
Release:        alt1_8jpp8
Summary:        Java library to reliably execute external processes from within the JVM
License:        ASL 2.0
URL:            http://commons.apache.org/exec/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)

# Tests execute /usr/bin/ping
BuildRequires:  iputils
Source44: import.info

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Fix wrong end-of-line encoding
for file in LICENSE.txt NOTICE.txt RELEASE-NOTES.txt STATUS; do
  sed -i.orig "s/\r//" $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

# Shell scripts used for unit tests must be executable (see
# http://commons.apache.org/exec/faq.html#environment-testing)
chmod a+x src/test/scripts/*.sh

# Skip Exec57Test (it is unstable), see rhbz#1202260
find -name Exec57Test.java -delete

%mvn_file :%{short_name} %{short_name} %{name}


%build
%mvn_build -- -Dmaven.test.failure.ignore=true 


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt STATUS RELEASE-NOTES.txt


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_8jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_7jpp8
- fixed build

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp8
- new fc release; disabled tests due to network dependency

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp8
- java8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp7
- new version

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp7
- new version

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_6jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_6jpp6
- renamed; new jpp version


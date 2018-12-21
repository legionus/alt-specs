Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          mongo-java-driver2
Version:       2.14.3
Release:       alt1_4jpp8
Summary:       MongoDB Java Driver
# BSD-3-clause: src/main/org/bson/io/UTF8Encoding.java
# CC-BY-SA-3.0: src/main/org/bson/util/annotations/*
License:       ASL 2.0 and BSD and CC-BY-SA
URL:           http://docs.mongodb.org/ecosystem/drivers/java/
Source0:       https://github.com/mongodb/mongo-java-driver/archive/r%{version}/mongo-java-driver-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)
# Those files are modifications of code included in:
# src/main/com/mongodb/util/Base64Codec.java
Provides:      bundled(apache-commons-codec)
# src/main/org/bson/util/annotations/*
Provides:      bundled(jcip-annotations)
# src/main/org/bson/io/UTF8Encoding.java
Provides:      bundled(postgresql-jdbc) = 9.0-801

BuildArch:     noarch
Source44: import.info

%description
Java library to connect to the MongoDB document database.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n mongo-java-driver-r%{version}
# Cleanup
find -name '*.class' -delete
find -name '*.jar' -print -delete

# Unwanted task
%pom_remove_plugin :maven-source-plugin

# Fix osgi manifest
%pom_xpath_remove pom:Export-Package
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
                 <Export-Package>com.mongodb.*,org.bson.*</Export-Package>'

%mvn_compat_version org.mongodb:mongo-java-driver %{version} 2
%mvn_file org.mongodb:mongo-java-driver mongo-java-driver %{name}

%build

# Test suite disabled; require web connection
# java.net.ConnectException: Connection refused
# com.mongodb.MongoTimeoutException: Timed out after 10000 ms while waiting to connect.
# Client view of cluster state is {type=Unknown, servers=[{address=127.0.0.1:27017,
# type=Unknown, state=Connecting, exception={com.mongodb.MongoException$Network:
# Exception opening the socket}, caused by {java.net.ConnectException: Connection refused}}]
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc History.md README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.14.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.14.3-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.14.3-alt1_2jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.14.1-alt1_3jpp8
- new version


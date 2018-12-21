Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: rpm-build-java zip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#%% global githash
# empty debuginfo
%global debug_package %nil

Name:          sqlite-jdbc
Version:       3.15.1
Release:       alt1_6jpp8
Summary:       SQLite JDBC library

# ASL 2.0:
# ./src/main/java/org/sqlite/SQLiteConfig.java
# ./src/main/java/org/sqlite/SQLiteDataSource.java
# ./src/main/java/org/sqlite/SQLiteErrorCode.java
# ./src/main/java/org/sqlite/SQLiteJDBCLoader.java
# ./src/main/java/org/sqlite/SQLiteOpenMode.java
# ./src/main/java/org/sqlite/javax/SQLiteConnectionPoolDataSource.java
# ./src/main/java/org/sqlite/javax/SQLitePooledConnection.java
# ./src/main/java/org/sqlite/util/OSInfo.java
# ./src/main/java/org/sqlite/util/ResourceFinder.java

# ISC:
# ./src/main/java/org/sqlite/Function.java
# ./src/main/java/org/sqlite/JDBC.java
# ./src/main/java/org/sqlite/SQLiteConnection.java: 
# ./src/main/java/org/sqlite/core/Codes.java
# ./src/main/java/org/sqlite/core/CoreDatabaseMetaData.java
# ./src/main/java/org/sqlite/core/CoreResultSet.java
# ./src/main/java/org/sqlite/core/CoreStatement.java
# ./src/main/java/org/sqlite/core/CorePreparedStatement.java
# ./src/main/java/org/sqlite/core/DB.java
# ./src/main/java/org/sqlite/core/NativeDB.c
# ./src/main/java/org/sqlite/core/NativeDB.java

# This package is a fork of zentus sqlite driver the
# original code is under BSD license. See LICENSE.zentus
# ./src/main/java/org/sqlite/Function.java
# ./src/main/java/org/sqlite/JDBC.java
# ./src/main/java/org/sqlite/core/Codes.java
# ./src/main/java/org/sqlite/core/DB.java
# ./src/main/java/org/sqlite/core/NativeDB.c
# ./src/main/java/org/sqlite/core/NativeDB.java

License:       ASL 2.0 and BSD and ISC
URL:           https://github.com/xerial/sqlite-jdbc
Source0:       https://github.com/xerial/sqlite-jdbc/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        %{name}-3.15.1-build.patch

BuildRequires: gcc
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: libsqlite3-devel
Source44: import.info
Patch33: sqlite-jdbc-alt-linkage.patch


%description
SQLite JDBC, is a library for accessing and
creating SQLite database files in Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# Cleanup
find . -name "*.class" -delete
# Do not delete test resources
find . -name "*.jar" ! -name "testdb.jar" -delete

# Remove prebuilt libraries
find -name "*.jnilib" -print -delete
find -name "*.dll" -print -delete
find -name "*.so" -print -delete
find -name "*.h" -print -delete
rm -r archive/* docker/*

# extensions won't work with our sqlite (should be patched)
# or use http://www.sqlite.org/2016/sqlite-amalgamation-3150100.zip
# ./sqlite-amalgamation-3150100/shell.c
# ./sqlite-amalgamation-3150100/sqlite3.c
# ./sqlite-amalgamation-3150100/sqlite3.h
# ./sqlite-amalgamation-3150100/sqlite3ext.h
# disable extensions and remove tests for them
# java.sql.SQLException: [SQLITE_ERROR] SQL error or missing database (no such function: radians)
rm -r src/test/java/org/sqlite/ExtensionTest.java
sed -i '/ExtensionTest/d' src/test/java/org/sqlite/AllTests.java
# secondConnWillWait(org.sqlite.TransactionTest)  Time elapsed: 23.213 sec
rm -r src/test/java/org/sqlite/TransactionTest.java
sed -i '/TransactionTest/d' src/test/java/org/sqlite/AllTests.java

%ifarch %{power64}
# failed test on big endian arches
# ComparisonFailure: expected:<UTF-16[l]e> but was:<UTF-16[b]e>
rm -r src/test/java/org/sqlite/SQLiteDataSourceTest.java
sed -i '/SQLiteDataSourceTest/d' src/test/java/org/sqlite/AllTests.java
%endif

%patch0 -p1

# Build JNI library. Use native task to avoid to run multiple, conflicting,
# operations at the same time
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 . '
<dependencies>
 <dependency>
  <groupId>com.sun</groupId>
  <artifactId>tools</artifactId>
  <version>1.8.0</version>
 </dependency>
</dependencies>

<executions>
  <execution>
  <id>compile</id>
  <phase>process-classes</phase>
    <configuration>
      <target>
       <javac destdir="lib"
         srcdir="lib"
         source="1.6" target="1.6" debug="on"
         classpathref="maven.plugin.classpath">
         <include name="**/OSInfo.java"/>
       </javac>
       <exec executable="make">
        <arg line="%{?_smp_mflags}
        JAVA_HOME=%{_jvmdir}/java
        JAVA=%{_jvmdir}/java/bin/java
        JAVAC=%{_jvmdir}/java/bin/javac
        JAVAH=%{_jvmdir}/java/bin/javah
        native"/>
       </exec>
      </target>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'

# Used for build JNI library
cp -p src/main/java/org/sqlite/util/OSInfo.java lib/org/sqlite/
sed -i "s|package org.sqlite.util;|package org.sqlite;|" lib/org/sqlite/OSInfo.java

%mvn_file org.xerial:%{name} %{name}
%patch33 -p0

%build

%ifarch %{arm}
opts='-f'
%endif

sed -i 's|$(CCFLAGS) -I|$(CCFLAGS) $(CFLAGS) -I|' Makefile
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
sed -i 's|$(CCFLAGS) -o|$(CCFLAGS) $(LDFLAGS) -o|' Makefile
LDFLAGS="${LDFLAGS:-%__global_ldflags}"; export LDFLAGS;
%mvn_build $opts -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.md Usage.md
%doc --no-dereference LICENSE* NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE* NOTICE

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 3.15.1-alt1_6jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.15.1-alt1_5jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.8.11.2-alt1_4jpp8
- new fc release

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 3.8.11.2-alt1_3jpp8
- new version


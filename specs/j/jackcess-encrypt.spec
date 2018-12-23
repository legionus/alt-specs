Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackcess-encrypt
Version:       2.1.1
Release:       alt1_5jpp8
Summary:       Java implementation of the encryption service for MS Access
License:       Apache-2.0
URL:           http://jackcessencrypt.sourceforge.net/
# svn checkout http://svn.code.sf.net/p/jackcessencrypt/code/tags/jackcess-encrypt-2.1.1
# tar cJf jackcess-encrypt-2.1.1.tar.xz jackcess-encrypt-2.1.1
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess)
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess::tests:)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(com.sun.xml.bind:jaxb-xjc)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.codehaus.mojo:jaxb2-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
Jackcess Encrypt is an extension library for the Jackcess project
which implements support for some forms of Microsoft Access and
Microsoft Money encryption.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# com.healthmarketscience:openhms-parent:1.1.1
%pom_remove_parent
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin

# Switch to jaxb2-maven-plugin
# com.sun.tools.xjc.maven2:maven-jaxb-plugin:1.0
%pom_remove_plugin com.sun.tools.xjc.maven2:maven-jaxb-plugin
%pom_add_plugin org.codehaus.mojo:jaxb2-maven-plugin:1.6 . '
<executions>
    <execution>
        <id>jaxb1</id>
        <goals>
            <goal>xjc</goal>
        </goals>
        <configuration>
            <schemaDirectory>${project.basedir}/src/main/resources/com/healthmarketscience/jackcess/cryptmodel</schemaDirectory>
            <packageName>com.healthmarketscience.jackcess.cryptmodel</packageName>
            <schemaFiles>encryptionInfo.xsd</schemaFiles>
            <strict>false</strict>
        </configuration>  
    </execution>
    <execution>
        <id>jaxb2</id>
        <goals>
            <goal>xjc</goal>
        </goals>
        <configuration>
            <schemaDirectory>${project.basedir}/src/main/resources/com/healthmarketscience/jackcess/cryptmodel</schemaDirectory>
            <packageName>com.healthmarketscience.jackcess.cryptmodel.password</packageName>
            <schemaFiles>encryptionInfo.xsd,passwordEncryptor.xsd</schemaFiles>
            <clearOutputDir>false</clearOutputDir>
            <strict>false</strict>
        </configuration>  
    </execution>
    <execution>
        <id>jaxb3</id>
        <goals>
            <goal>xjc</goal>
        </goals>
        <configuration>
            <schemaDirectory>${project.basedir}/src/main/resources/com/healthmarketscience/jackcess/cryptmodel</schemaDirectory>
            <packageName>com.healthmarketscience.jackcess.cryptmodel.cert</packageName>
            <schemaFiles>certificateEncryptor.xsd</schemaFiles>
            <clearOutputDir>false</clearOutputDir>
            <strict>false</strict>
        </configuration>  
    </execution>
</executions>
<dependencies>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-xjc</artifactId>
        <version>2.1.9</version>
    </dependency>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-impl</artifactId>
        <version>2.1.9</version>
    </dependency>          
</dependencies>'

# Use old com.healthmarketscience.jackcess:jackcess
rm -r src/test/java/com/healthmarketscience/jackcess/CryptCodecProviderTest.java

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1jpp8
- new version


Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.aries.blueprint.annotation.api
Name:          aries-blueprint-annotation-api
Version:       1.0.1
Release:       alt1_4jpp8
Summary:       Apache Aries Blueprint Annotation API
License:       ASL 2.0
URL:           http://aries.apache.org/
#Source0:       http://www.apache.org/dist/aries/%%{bundle}-%%{version}-source-release.zip
Source0:       http://central.maven.org/maven2/org/apache/aries/blueprint/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)

BuildArch:     noarch
Source44: import.info

%description
This bundle contains the blueprint annotation api and
the corresponding XML schema.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_parent
%pom_remove_plugin org.apache.aries.versioning:org.apache.aries.versioning.plugin

%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi:3.10.102.v20160416-2200

%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Export-Package>${aries.osgi.export.pkg}</Export-Package>
    <Import-Package>${aries.osgi.import.pkg}</Import-Package>
    <Implementation-Title>Apache Aries</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp8
- new version


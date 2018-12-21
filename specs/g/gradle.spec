Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install gcc-c++ rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 28
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Gradle depends on itself for building.  This can be problematic, for
# example when some library it uses changes API, Gradle may stop
# working and it may be impossible to rebuild it in normal way.
#
# For cases like that bootstrap mode can be used.  In this mode a
# minimal working version of Gradle is built with plain groovyc.  The
# only purpose of bootstrapped Gradle is to rebuild itself.  Gradle
# built using bootstrap mode doesn't have all features, for example it
# doesn't provide Maven metadata, and it may have some functionality
# missing.  For this reason a normal non-bootstrap build should be
# done immediately after Gradle is bootstrapped.
%bcond_with bootstrap

Name:           gradle
Version:        4.3.1
Release:        alt3_7jpp8
Summary:        Build automation tool
# Some examples and integration tests are under GNU LGPL and Boost
# Software License, but are not used to create binary package.
License:        ASL 2.0
URL:            http://www.gradle.org/
BuildArch:      noarch

Source0:        http://services.gradle.org/distributions/gradle-%{version}-src.zip
Source1:        http://services.gradle.org/versions/all#/all-released-versions.json
Source2:        gradle-font-metadata.xml
Source3:        gradle-jquery-metadata.xml
Source4:        gradle-launcher.sh
Source5:        gradle.desktop
Source6:        gradle-man.txt

# Sources 99xx are used only for bootstrapping.
# Main script used to build gradle with plain groovyc
Source9900:     gradle-bootstrap.sh
# Script used to generate Source991x from upstream binaries
Source9901:     gradle-bootstrap-generate-resources.py
# Files containing information about Gradle module structure
Source9910:     gradle-bootstrap-module-list
Source9911:     gradle-bootstrap-module-dependencies
# List of API mappings, extracted from gradle-docs.jar
Source9920:     gradle-bootstrap-api-mapping.txt
# List of default imorts, extracted from gradle-docs.jar
Source9921:     gradle-bootstrap-default-imports.txt
# List of Gradle plugins, extracted from gradle-core.jar
Source9922:     gradle-bootstrap-plugin.properties
Source9923:     gradle-bootstrap-implementation-plugin.properties
Source9924:     gradle-bootstrap-api-relocated.txt
Source9925:     gradle-bootstrap-test-kit-relocated.txt

Patch0001:      0001-Gradle-local-mode.patch
Patch0002:      0002-Remove-Class-Path-from-manifest.patch
Patch0003:      0003-Implement-XMvn-repository-factory-method.patch
Patch0004:      0004-Use-unversioned-dependency-JAR-names.patch
Patch0005:      0005-Port-to-Maven-3.3.9-and-Eclipse-Aether.patch
Patch0006:      0006-Disable-code-quality-checks.patch
Patch0007:      0007-Port-to-Kryo-3.0.patch
Patch0008:      0008-Port-to-Ivy-2.4.0.patch
Patch0009:      0009-Port-to-Polyglot-0.1.8.patch
Patch0010:      0010-Port-from-Simple-4-to-Jetty-9.patch
Patch0011:      0011-Disable-benchmarks.patch
Patch0012:      0012-Disable-patching-of-external-modules.patch
Patch0013:      0013-Add-missing-transitive-dependencies.patch
Patch0014:      0014-Disable-ideNative-module.patch
Patch0015:      0015-Disable-docs-build.patch
Patch0016:      0016-Port-to-guava-20.0.patch
# it depends on ant which is Java 8+
Patch0017:      0017-Set-core-api-source-level-to-8.patch

# For autosetup
BuildRequires:  git

# Dependencies on build system used.  In bootstrap mode we use plain
# groovyc to compile Gradle, otherwise Gradle is built with itself.
%if %{with bootstrap}
BuildRequires:  groovy >= 2.3
BuildRequires:  javapackages-local
%else
BuildRequires:  gradle-local
%endif

# Generic build dependencies
BuildRequires:  desktop-file-utils
BuildRequires:  coreutils
BuildRequires:  procps

# manpage build dependencies
BuildRequires:  asciidoc asciidoc-a2x
BuildRequires:  xmlto

# Artifacts required for Gradle build
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(biz.aQute.bnd:bndlib)
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-kms)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-s3)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.esotericsoftware:minlog)
BuildRequires:  mvn(com.esotericsoftware:reflectasm)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.findbugs:findbugs)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.google.guava:guava-jdk5:20.0)
BuildRequires:  mvn(com.google.http-client:google-http-client)
BuildRequires:  mvn(com.google.oauth-client:google-oauth-client)
BuildRequires:  mvn(com.googlecode.jarjar:jarjar)
BuildRequires:  mvn(com.googlecode.jatl:jatl)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.puppycrawl.tools:checkstyle)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.typesafe.zinc:zinc)
BuildRequires:  mvn(com.uwyn:jhighlight)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.rubygrapefruit:native-platform)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-builder-support)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.groovy.modules.http-builder:http-builder)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codenarc:CodeNarc)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.eclipse.jetty:jetty-annotations)
BuildRequires:  mvn(org.eclipse.jetty:jetty-jsp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.eclipse.jetty:jetty-security)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)
BuildRequires:  mvn(org.gmetrics:GMetrics)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.mozilla:rhino)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildRequires:  mvn(org.parboiled:parboiled-core)
BuildRequires:  mvn(org.parboiled:parboiled-java)
BuildRequires:  mvn(org.pegdown:pegdown)
BuildRequires:  mvn(org.samba.jcifs:jcifs)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:jul-to-slf4j)
BuildRequires:  mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-common)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-groovy)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)

# Artifacts required for Gradle build which don't have Maven metadata
# and thus no mvn provides.
BuildRequires:  fonts-ttf-google-lato
BuildRequires:  fonts-ttf-liberation
#BuildRequires:  js-jquery

# Generic runtime dependencies.
Requires:       javapackages-tools
Requires:       bash sh
Requires:       icon-theme-hicolor

# Theoretically Gradle might be usable with just JRE, but typical Gradle
# workflow requires full JDK, so we recommend it here.

# Providers of symlinks in Gradle lib/ directory. Generated with:
# for l in $(find /usr/share/gradle -type l); do rpm -qf --qf 'Requires:       %{name}\n' $(readlink $l); done | sort -u | grep -v gradle
Requires:       ant-lib
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-lang3
Requires:       apache-ivy
Requires:       aqute-bndlib
Requires:       atinject
Requires:       aws-sdk-java-core
Requires:       aws-sdk-java-kms
Requires:       aws-sdk-java-s3
Requires:       base64coder
Requires:       beust-jcommander
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       ecj
Requires:       glassfish-servlet-api
Requires:       google-gson
Requires:       google-guice
Requires:       groovy-lib
Requires:       guava20
Requires:       hawtjni-runtime
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jackson-annotations
Requires:       jackson-core
Requires:       jackson-databind
Requires:       jansi
Requires:       jansi-native
Requires:       jatl
Requires:       jcifs
Requires:       jcip-annotations
Requires:       jcl-over-slf4j
Requires:       jetty-server
Requires:       jetty-util
Requires:       joda-time
Requires:       jsch
Requires:       jsr-305
Requires:       jul-to-slf4j
Requires:       junit
Requires:       kryo
Requires:       log4j-over-slf4j
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       minlog
Requires:       native-platform
Requires:       nekohtml
Requires:       objectweb-asm
Requires:       objenesis
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       reflectasm
Requires:       rhino
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       tesla-polyglot-common
Requires:       tesla-polyglot-groovy
Requires:       testng
Requires:       xbean
Requires:       xerces-j2
Requires:       xml-commons-apis
Source44: import.info

%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

# Remove bundled wrapper JAR
rm -rf gradle/wrapper/
# Remove bundled JavaScript
>subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js

# This file is normally downloaded from Internet during package build
mkdir -p build
cp %{SOURCE1} build/all-released-versions.json

# quality checks for which we don't have deps
rm -r buildSrc/src/main/groovy/org/gradle/binarycompatibility
rm buildSrc/src/main/groovy/org/gradle/build/docs/CacheableAsciidoctorTask.groovy

# jquery and fonts don't have Maven metadata
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}

# Tests for bulid script currently fail, but the bulid works.
# TODO: enble tests
rm -rf buildSrc/src/test

# Compilation with Fedora versions of some libraries produces
# warnings. Lets not treat them as errors to make the build work.
sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle

removeProject() {
sed -i "/'$1'/d" settings.gradle
sed -i "s/'$1',\?//" build.gradle
}
removeProject resourcesGcs
rm -r subprojects/resources-gcs
rm -r subprojects/ide-native
# alt linux
sed -i -e 's,/usr/share/fonts/lato,/usr/share/fonts/ttf/lato,;s,/usr/share/fonts/liberation,/usr/share/fonts/ttf/liberation,' ../../SOURCES/gradle-font-metadata.xml

%build
%if %{with bootstrap}
mkdir -p subprojects/docs/src/main/resources
mkdir -p subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded
cp %{SOURCE9920} subprojects/docs/src/main/resources/api-mapping.txt
cp %{SOURCE9921} subprojects/docs/src/main/resources/default-imports.txt
cp %{SOURCE9922} subprojects/core/src/main/resources/gradle-plugins.properties
cp %{SOURCE9923} subprojects/core/src/main/resources/gradle-implementation-plugins.properties
cp %{SOURCE9924} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/api-relocated.txt
cp %{SOURCE9925} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/test-kit-relocated.txt
%{SOURCE9900} %{SOURCE9910} %{SOURCE9911}
%else
# Disables parallel build and daemon mode
rm gradle.properties
gradle-local --offline --no-daemon install xmvnInstall \
    -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="ALTLinux %{version}-%{release}"
%endif

# manpage build
mkdir man
asciidoc -b docbook -d manpage -o man/gradle.xml %{SOURCE6}
xmlto man man/gradle.xml -o man

%install
cp subprojects/distributions/src/toplevel/NOTICE .
cp subprojects/docs/src/samples/application/src/dist/LICENSE .

install -d -m 755 %{buildroot}%{_javadir}/%{name}/

%if %{with bootstrap}
cp -r bootstrap-home %{buildroot}%{_datadir}/%{name}
# Launcher with dependencies needs to be in _javadir
# Dependencies of xmvn-connector-gradle need to have Maven metadata
for mod in launcher base-services core core-api dependency-management resources \
        logging base-services-groovy model-core; do
    %mvn_file ":{gradle-$mod}" %{name}/@1 %{_datadir}/lib/@1
    %mvn_artifact org.gradle:gradle-$mod:%{version} bootstrap-home/lib/gradle-$mod.jar
done

%else # non-bootstrap

rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/%{name} inst/bin/gradle
find inst/lib -type f -name 'gradle*' | sed 's:.*/\(gradle-.*\)-%{version}.*:ln -sf %{_javadir}/%{name}/\1.jar &:' | bash -x
ln -sf $(build-classpath ecj) inst/lib/plugins/ecj.jar
xmvn-subst -s $(find inst/lib -type f)
# TODO figure out why this one is missing
ln -s `find-jar commons-lang` inst/lib/
cp -a inst %{buildroot}%{_datadir}/%{name}

%endif

%mvn_install

install -d -m 755 %{buildroot}%{_bindir}/
install -p -m 755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}

for r in 16 24 32 48 64 128 256; do
    install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/
    install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-${r}x${r}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{name}.png
done

install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/gradle.1 %{buildroot}%{_mandir}/man1/gradle.1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf
sed -i -e s,/usr/bin/bash,/bin/sh, %buildroot%_bindir/*

%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/gradle.1*
%doc --no-dereference LICENSE NOTICE
%config(noreplace,missingok) /etc/java/%name.conf

%changelog
* Mon Jun 04 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt3_7jpp8
- unbootstrap rebuild with new guava and objectweb-asm

* Mon Jun 04 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt2_7jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_7jpp8
- java fc28+ update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_5jpp8
- unbootstrap build

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_10jpp8
- fixed build with new checkstyle

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_7jpp8
- rebuild with new xpp3

* Wed Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_1jpp8
- unbootstrap build

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3jpp8
- unbootstrap build

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13jpp7
- rebuild with maven-local

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


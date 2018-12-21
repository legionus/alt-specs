%define _unpackaged_files_terminate_build 0
%define javapackagestoolsver 0.15.0
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define distver 5.0
%def_enable gcj_filesystem
%def_disable gcj_support
%def_without lua_scripts

Name:           rpm-build-java-osgi
Version:        5.0.0
Release:        alt45
Epoch:          0
URL:            http://www.jpackage.org/
License:        BSD

Source0:        jpackage-utils-%{version}.tar

Source1: rpm-build-java.tar
Source2: jpackage-utils-safe.tar
Source3: javapackages.tar
# fedora utils - let us install them for compatibility
Source22:        abs2rel.sh
Source23:        abs2rel.lua
# not used: duplicate Patch21: jpackage-utils-own-mavendirs.patch
Patch0:  jpackage-utils-maven-macros.patch
Patch1: jpackage-utils-openjdk-1.7.0-alt-version.patch
Patch2: jpackage-utils-1.7.4-alt-fix-typo-in-comments.patch    
Patch3: jpackage-utils-1.7.5-alt-rpmscript-safe-mode.patch
Patch4: jpackage-utils-1.7.5-alt-hasher-support-hack.patch
Patch5: jpackage-utils-1.7.5-alt-undefined-alternatives-during-transaction-hack.patch
Patch6: javapackages-0.12.3-macros.fjava-alt-nopython.patch
Patch7: javapackages-0.15.0-alt-macros-rpm404.patch
Patch8: javapackages-0.15.0-alt-fix-install.patch

# macros.jpacage patches
Patch10: jpackage-utils-enable-gcj-support.patch
Patch11: jpackage-utils-1.7.5-alt-remove-duplication-of-sys-macros.patch
Patch12: jpackage-utils-1.7.5-alt-update_maven_depmap-is-obsolete.patch
Patch13: jpackage-utils-1.7.5-alt-add_add_to_maven_depmap_in_macros.patch
Patch14: jpackage-utils-1.7.5-alt-jpackage-script-no-dep.patch

# fedora modified to be old jpackage dirs
Patch21: jpackage-utils-own-mavendirs.patch
# fedora
Patch22: jpackage-utils-prefer-jre.patch
Patch23: jpackage-utils-set-classpath.patch
Patch24: jpackage-utils-jnidir.patch
Patch25: jpackage-utils-build-classpath-symlink-fix.patch

BuildRequires:  awk, grep

#package -n rpm-build-java-osgi
Summary: RPM build helpers for Java packages with OSGi dependencies
Group: Development/Java
BuildArch:      noarch

%description -n rpm-build-java-osgi
RPM build helpers for Java packages with OSGi dependencies

%package -n rpm-macros-java
Summary: RPM helper macros to build Java packages
Group: Development/Java
Conflicts: rpm-build-java < 0:5.0.0-alt34

# can't due to the jni path
#BuildArch:      noarch

%description -n rpm-macros-java
These helper macros facilitate creation of RPM packages containing Java
bytecode archives and Javadoc documentation.

%package -n jpackage-utils
Summary:        JPackage utilities
#Requires:       rpm-build-java = %{epoch}:%{version}-%{release}
Group:          Development/Java

# can't due to the jni path
#BuildArch:      noarch

%description -n jpackage-utils
Utilities for the JPackage Project <http://www.jpackage.org/>:

* %{_bindir}/build-classpath
                                build the Java classpath in a portable manner
* %{_bindir}/build-jar-repository
                                build a jar repository in a portable manner
* %{_bindir}/rebuild-jar-repository
                                rebuild a jar repository in a portable manner
                                (after a jvm change...)
* %{_bindir}/build-classpath-directory
                                build the Java classpath from a directory
* %{_bindir}/diff-jars
                                show jar content differences
* %{_bindir}/jvmjar
                                install jvm extensions
* %{_bindir}/create-jar-links
                                create custom jar links
* %{_bindir}/clean-binary-files
                                remove binary files from sources
* %{_bindir}/check-binary-files
                                check for presence of unexpected binary files
* %{_datadir}/java-utils/java-functions
                                shell script functions library for Java
                                applications
* %{_sysconfdir}/java/jpackage-release
                                string identifying the currently installed
                                JPackage release
* %{_sysconfdir}/java/java.conf
                                system-wide Java configuration file
* %{_sysconfdir}/rpm/macros.d/jpackage
                                RPM macros for Java packagers and developers
* %{_docdir}/jpackage-utils-%{version}/jpackage-policy
                                Java packaging policy for packagers and
                                developers

It contains also the License, man pages, documentation, XSL files of general
use with maven2, a header file for spec files etc.

%package -n rpm-build-java-maven-fragments
Summary: RPM build helpers for Java packages
Group: Development/Java
BuildArch:      noarch
#Requires:       jpackage-utils = %{epoch}:%{version}-%{release}
Requires: 	rpm-macros-java >= %{epoch}:%{version}-%{release}
#Requires: rpm-build-java-osgi = %{epoch}:%{version}-%{release}
# for maven_depmap.pl
BuildRequires:  perl-XML-Simple
#Provides: javapackages-tools = %javapackagestoolsver
#Provides: rpm-build-java = %version

%description -n rpm-build-java-maven-fragments
RPM build helpers for Java packages.

%package -n maven-local
Summary:        Macros and scripts for Maven packaging support
Group: Development/Java
#Version:	%javapackagestoolsver
BuildArch:	noarch

Conflicts:	maven < 3.0.5
Conflicts:	rpm-build-maven-local < 5.0.0-alt38
Obsoletes:	rpm-build-maven-local < 5.0.0-alt38
Requires:       rpm-build-java = %{?epoch:%{epoch}}%{version}-%{release}
Requires:       maven
Requires:       xmvn
# POM files needed by maven itself
Requires:       apache-commons-parent
Requires:       apache-parent
Requires:       geronimo-parent-poms
Requires:       httpcomponents-project
Requires:       jboss-parent
Requires:       maven-parent
Requires:       maven-plugins-pom
Requires:       mojo-parent
Requires:       plexus-components-pom
Requires:       plexus-pom
Requires:       plexus-tools-pom
Requires:       sonatype-oss-parent
Requires:       weld-parent
# added by viy@ for initial bootstrapping transaction TODO drop
Requires:       sonatype-forge-parent
# Common Maven plugins required by almost every build. It wouldn't make
# sense to explicitly require them in every package built with Maven.
Requires:       maven-assembly-plugin
Requires:       maven-compiler-plugin
Requires:       maven-enforcer-plugin
Requires:       maven-jar-plugin
Requires:       maven-javadoc-plugin
Requires:       maven-surefire-plugin
# Tests based on JUnit are very common and JUnit itself is small.
# Include JUnit provider for Surefire just for convenience.
Requires:       maven-surefire-provider-junit
# testng is quite common as well
Requires:       maven-surefire-provider-testng

# for safe migration -- comment later
Requires: maven-plugin-testing-tools maven-invoker-plugin easymock3

%description -n maven-local
This package provides macros and scripts to support packaging Maven artifacts.

%prep
%setup -q -n jpackage-utils-%version -a1 -a2 -a3

#patch0 -p0 -b .sav0
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6
%patch7 -p1
%patch8 -p1
%if_enabled gcj_support
%patch10 -p0
%endif
%patch11 -p0
%patch12 -p2
%patch13 -p0
%patch14 -p2

%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1


cp -p %{SOURCE22} %{SOURCE23} .

%build
echo "JPackage release %{distver} (%distribution) for %buildarch" \
 > etc/jpackage-release

%install
# Pull macros out of macros.jpackage and emulate them during install for
# smooth bootstrapping experience.
for dir in \
    jvmdir jvmjardir jvmprivdir \
    jvmlibdir jvmdatadir jvmsysconfdir \
    jvmcommonlibdir jvmcommondatadir jvmcommonsysconfdir \
    javadir jnidir javajnidir javadocdir mavenpomdir \
    mavendepmapdir mavendepmapfragdir; do
  export _${dir}=$(rpm --eval $(grep -E "^%%_${dir}\b" \
    misc/macros.jpackage | awk '{ print $2 }'))
done

install -dm 755 ${RPM_BUILD_ROOT}%{_bindir}
install -dm 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/java
%if_enabled gcj_filesystem
install -dm 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/java/security
install -dm 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/java/security/security.d
%endif
install -dm 755 ${RPM_BUILD_ROOT}${_jvmdir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmjardir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmprivdir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmlibdir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmdatadir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmsysconfdir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmcommonlibdir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmcommondatadir}
install -dm 755 ${RPM_BUILD_ROOT}${_jvmcommonsysconfdir}
install -dm 755 ${RPM_BUILD_ROOT}${_javadir}
install -dm 755 ${RPM_BUILD_ROOT}${_javadir}-utils
install -dm 755 ${RPM_BUILD_ROOT}${_javadir}-ext
install -dm 755 ${RPM_BUILD_ROOT}${_javadir}-{1.4.2,1.5.0,1.6.0,1.7.0,1.8.0}
install -dm 755 ${RPM_BUILD_ROOT}${_jnidir}
install -dm 755 ${RPM_BUILD_ROOT}${_jnidir}-ext
install -dm 755 ${RPM_BUILD_ROOT}${_jnidir}-{1.4.2,1.5.0,1.6.0,1.7.0,1.8.0}
install -dm 755 ${RPM_BUILD_ROOT}${_javajnidir}
install -dm 755 ${RPM_BUILD_ROOT}${_javadocdir}
install -dm 755 ${RPM_BUILD_ROOT}${_mavenpomdir}
install -dm 755 ${RPM_BUILD_ROOT}${_mavendepmapdir}
install -dm 755 ${RPM_BUILD_ROOT}${_mavendepmapfragdir}

%if_enabled gcj_filesystem
cat > bin/rebuild-security-providers << EOF
#!/bin/bash
# Rebuild the list of security providers in classpath.security

secfiles="/usr/lib/security/classpath.security /usr/lib64/security/classpath.security"

for secfile in \$secfiles; do
  # check if this classpath.security file exists
  [ -f "\$secfile" ] || continue

  sed -i '/^security\.provider\./d' "\$secfile"

  count=0
  for provider in \$(ls /etc/java/security/security.d)
  do
    count=\$((count + 1))
    echo "security.provider.\${count}=\${provider#*-}" >> "\$secfile"
  done
done
EOF
%endif

install -pm 755 bin/* ${RPM_BUILD_ROOT}%_bindir
install -pm 644 etc/font.properties ${RPM_BUILD_ROOT}%_sysconfdir/java

# Install abs2rel scripts
install -pm 755 abs2rel.sh  ${RPM_BUILD_ROOT}${_javadir}-utils/
%if_with lua_scripts
install -pm 644 abs2rel.lua ${RPM_BUILD_ROOT}${_javadir}-utils/
%endif

# Create an initial (empty) depmap
echo -e "<dependencies>\\n" > ${RPM_BUILD_ROOT}${_mavendepmapdir}/maven2-depmap.xml
echo -e "</dependencies>\\n" >> ${RPM_BUILD_ROOT}${_mavendepmapdir}/maven2-depmap.xml

cat > etc/java.conf << EOF
# System-wide Java configuration file                                -*- sh -*-
#
# JPackage Project <http://www.jpackage.org/>

# Location of jar files on the system
JAVA_LIBDIR=${_javadir}

# Location of arch-specific jar files on the system
JNI_LIBDIR=${_jnidir}

# Location for noarch jar files using arch-specifics jar files
JAVAJNI_LIBDIR=${_javajnidir}

# Root of all JVM installations
JVM_ROOT=${_jvmdir}

# You can define a system-wide JVM root here if you're not using the
# default one.
#
# If you have the a base JRE package installed
# (e.g. java-1.6.0-openjdk):
#JAVA_HOME=\$JVM_ROOT/jre
#
# If you have the a devel JDK package installed
# (e.g. java-1.6.0-openjdk-devel):
#JAVA_HOME=\$JVM_ROOT/java

# Options to pass to the java interpreter
JAVACMD_OPTS=
EOF

install -pm 644 etc/java.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/java
install -pm 644 etc/jpackage-release ${RPM_BUILD_ROOT}%{_sysconfdir}/java
install -pm 644 java-utils/* ${RPM_BUILD_ROOT}${_javadir}-utils

mkdir -p ${RPM_BUILD_ROOT}%_rpmmacrosdir
install -pm 644 misc/macros.jpackage ${RPM_BUILD_ROOT}%_rpmmacrosdir/jpackage
mkdir -p ${RPM_BUILD_ROOT}%_man1dir/
mkdir -p ${RPM_BUILD_ROOT}%_man5dir/
mkdir -p ${RPM_BUILD_ROOT}%_man7dir/
install -pm 644 man/*.1 ${RPM_BUILD_ROOT}%_man1dir/
install -pm 644 man/*.5 ${RPM_BUILD_ROOT}%_man5dir/
install -pm 644 man/*.7 ${RPM_BUILD_ROOT}%_man7dir/
mkdir -p ${RPM_BUILD_ROOT}${_javadir}-utils/xml
install -pm 644 xml/* ${RPM_BUILD_ROOT}${_javadir}-utils/xml

cat <<EOF > jpackage-utils-%{version}.files
%%dir %_sysconfdir/java
%%dir $_jvmdir
%%dir $_jvmjardir
%%dir $_jvmprivdir
%%dir $_jvmdatadir
%%dir $_jvmsysconfdir
%%dir $_jvmcommonlibdir
%%dir $_jvmcommondatadir
%%dir $_jvmcommonsysconfdir
%%dir $_javadir
%%dir $_javadir-*
%%dir $_jnidir
%%dir $_jnidir-*
%%dir $_javadocdir
%%dir ${_mavenpomdir}
%%dir $_mavendepmapdir
%%dir ${_mavendepmapfragdir}
$_javadir-utils/*
%%config %_sysconfdir/java/jpackage-release
%%config(noreplace) %_sysconfdir/java/java.conf
%%config(noreplace) %_sysconfdir/java/font.properties
%%config(noreplace) $_mavendepmapdir/maven2-depmap.xml
EOF


%define jit_arches %{ix86} x86_64 sparcv9 sparc64
%ifarch %{ix86}
%define archinstall i386
%endif
%ifarch x86_64
%define archinstall amd64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%define archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%define archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%define archinstall %{_arch}
%endif
mkdir -p ${RPM_BUILD_ROOT}%_rpmmacrosdir
cat > ${RPM_BUILD_ROOT}%_rpmmacrosdir/libjvm << EOF
%ifarch %ix86
%%_libjvmclient_sun_private_default $_jvmdir/java/jre/lib/%archinstall/client/libjvm.so
%%_libjvmserver_sun_private_default $_jvmdir/java/jre/lib/%archinstall/server/libjvm.so
%else
%%_libjvmclient_sun_private_default $_jvmdir/java/jre/lib/%archinstall/server/libjvm.so
%%_libjvmserver_sun_private_default $_jvmdir/java/jre/lib/%archinstall/server/libjvm.so
%endif
EOF

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/rpm/
install -pm 755 rpm-build-java/maven-fragments.prov* ${RPM_BUILD_ROOT}/usr/lib/rpm/
install -pm 755 rpm-build-java/maven-fragments.prov.files ${RPM_BUILD_ROOT}/usr/lib/rpm/maven-fragments.req.files
install -pm 755 rpm-build-java/maven-fragments.req ${RPM_BUILD_ROOT}/usr/lib/rpm/
install -pm 755 rpm-build-java/osgi.prov* ${RPM_BUILD_ROOT}/usr/lib/rpm/
pushd ${RPM_BUILD_ROOT}/usr/lib/rpm/
# un/comment ln's below to enable/disable osgi.req
      ln -s osgi.prov osgi.req
      ln -s osgi.prov.files osgi.req.files
popd

install -D -m755 rpm-build-java/maven_depmap.pl %buildroot%{_datadir}/java-utils/maven_depmap
echo '%%attr(755,root,root) %{_datadir}/java-utils/maven_depmap' >> jpackage-utils-%{version}.files
install -D -m755 javapackages/scripts/pom_editor.sh %buildroot%{_datadir}/java-utils/pom_editor.sh
echo '%%attr(755,root,root) %{_datadir}/java-utils/pom_editor.sh' >> jpackage-utils-%{version}.files


# ------------- safe jpackage utils --------------------
install -pm 644 jpackage-utils-safe/java-functions-safe ${RPM_BUILD_ROOT}${_javadir}-utils
#install -pm 755 jpackage-utils-safe/safe-*build-jar-repository ${RPM_BUILD_ROOT}%_bindir/
# ------------- end safe jpackage utils ----------------

install -pm 644 rpm-build-java/macros.eclipse ${RPM_BUILD_ROOT}%_rpmmacrosdir/jpackage-eclipse
## TMP hack for maven1 dep on /usr/lib/java - remove
##if ! %_libdir = /usr/lib
#mkdir -p %buildroot/usr/lib/java
#echo '%%dir /usr/lib/java' >> jpackage-utils-%{version}.files
##endif

pushd javapackages
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven-effective-poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/xmvn
install -pm 644 macros.fjava ${RPM_BUILD_ROOT}%_rpmmacrosdir/javapackages-fjava
install -pm 644 macros.xmvn ${RPM_BUILD_ROOT}%_rpmmacrosdir/javapackages-xmvn
install -p -m 644 metadata/*.xml $RPM_BUILD_ROOT%{_sysconfdir}/maven
install -p -m 755 scripts/xmvn_config_editor.sh $RPM_BUILD_ROOT${_javadir}-utils
install -p -m 755 scripts/mvn-* $RPM_BUILD_ROOT%{_bindir}

install -p -m 644 configs/configuration*.xml $RPM_BUILD_ROOT%{_datadir}/xmvn
ln -sf %{_datadir}/xmvn/configuration-19.xml $RPM_BUILD_ROOT%{_datadir}/xmvn/configuration.xml
popd

%define fedora 19
# On Fedora 18 we don't want to install mvn-local and mvn-rpmbuild
# scripts as they are already provided by maven package.
%if 0%{?fedora} == 18
rm -f $RPM_BUILD_ROOT%{_bindir}/mvn-{local,rpmbuild}
%endif

### TODO drop maven remnants
mkdir -p $RPM_BUILD_ROOT%{_datadir}/maven-{poms,fragments} $RPM_BUILD_ROOT%{_datadir}/java/maven
install -pm 644 rpm-build-java/maven-remnants/JPP.maven-empty-dep.pom ${RPM_BUILD_ROOT}%{_datadir}/maven-poms/
install -pm 644 rpm-build-java/maven-remnants/empty-dep ${RPM_BUILD_ROOT}%{_datadir}/maven-fragments/empty-dep-hacks
install -pm 644 rpm-build-java/maven-remnants/empty-dep.jar ${RPM_BUILD_ROOT}%{_datadir}/java/maven/
### END TODO drop maven remnants


%post -n jpackage-utils
rm -f /etc/maven/maven2-depmap.xml

%if 0
%files -n jpackage-utils -f jpackage-utils-%{version}.files
%_bindir/build-classpath
%_bindir/build-classpath-directory
%_bindir/build-jar-repository
%_bindir/check-binary-files
%_bindir/clean-binary-files
%_bindir/create-jar-links
%_bindir/diff-jars
%_bindir/find-jar
%_bindir/jvmjar
%_bindir/rebuild-jar-repository
%_bindir/rebuild-security-providers
%_mandir/man?/*
%doc LICENSE.txt HEADER.JPP doc/* etc/httpd-javadoc.conf
%doc jpackage-utils-safe/README.ALT
%if_enabled gcj_filesystem
%_sysconfdir/java/security
%_sysconfdir/java/security/security.d
%endif
%exclude %{_datadir}/java-utils/xmvn_config_editor.sh

%files -n rpm-macros-java
%_rpmmacrosdir/jpackage
%_rpmmacrosdir/jpackage-eclipse
%_rpmmacrosdir/libjvm
%_rpmmacrosdir/javapackages-fjava
%_rpmmacrosdir/javapackages-xmvn
%endif

%files -n rpm-build-java-osgi
/usr/lib/rpm/osgi.*

%if 0
%files -n rpm-build-java-maven-fragments
/usr/lib/rpm/maven-fragments.*
%endif

%if 0
%files -n maven-local
%{_sysconfdir}/maven/metadata-*.xml
#%{_bindir}/mvn-*
%_bindir/mvn-alias
%_bindir/mvn-build
%_bindir/mvn-config
%_bindir/mvn-file
%_bindir/mvn-local
%_bindir/mvn-package
%_bindir/mvn-rpmbuild
%dir %{_datadir}/maven-effective-poms
%{_datadir}/java-utils/xmvn_config_editor.sh
%{_datadir}/xmvn/configuration*.xml
### TODO drop maven remnants
%{_datadir}/maven-poms/JPP.maven-empty-dep.pom
%{_datadir}/maven-fragments/empty-dep-hacks
%{_datadir}/java/maven/empty-dep.jar
### END TODO drop maven remnants
%endif

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt45
- bugfix release

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt44
- dropped rpm-build-java-maven-fragments
- renamed to rpm-build-java-osgi

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt43
- migration on javapackages-tools

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt42
- java 8 support

* Fri Jan 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt41
- preparations for migration on javapackages-tools and maven-metadata

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt40
- dropped filetrigger for jpackage maven
- backported some xpath macros for rpm 4.0.4

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt39
- maven.req

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt38
- migration to xmvn

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt37
- javapackages tools 0.15.0

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt36
- maven.prov and xmvn fixes

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt35
- support for versioned mvn(g:a:v) triplet provides

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt34
- added rpm-macros-java due to excessive dependencies

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt33
- bugfix release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt32
- moved %%_mavendepmapfragdir to %%{_datadir}/maven-fragments
  and %%_mavenpomdir to %%{_datadir}/maven-poms

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt31
- sync with javapackages-tools = 0.14.1

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt30
- proper man page locations (closes: 28885)

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt29
- fixes in osgi.prov

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt28
- added maven-local
- sync with javapackages-tools = 0.12.6

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt27
- sync with javapackages-tools = 0.7.5

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt26
- disabled lua scripts

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt25
- store poms in /usr/share/maven-poms

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt24
- sync with eclipse 4.2.0-13 macros

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt23
- packaged eclipse macros

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt22
- fjava macros fixes

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt21
- bugfix release

* Fri Aug 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt20
- maven.prov fixes (provide valid versions only)

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt19
- added macros.eclipse

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt18
- added maven.prov

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt17
- sync with javapackges-utils 0.6.0

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt16
- sync with fc jpackage-utils 1.7.5-18

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt15
- bugfix in maven_depmap script

* Mon Mar 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt14
- maven-fragments moved to %%_datadir

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt13
- added /etc/java/security for gcj
- sync with fedora - packaged _javajnidir, _mavendepmapfragdir.

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt12
- bugfix in filetrigger

* Tue Mar 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt11
- bugfix release

* Mon Mar 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt10
- support for mavendepmapfragdir at %{_datadir}/maven-fragments

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt9
- support for FC macro add_maven_depmap
- merged fedora patches
- maven_depmap ported to perl

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt8
- added add_add_to_maven_depmap_at macros

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt7
- added support for Specification-Version in osgi manifest

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt6
- removed dependecy of rpm-build-java on rpm-build-java-osgi

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt5
- added separate rpm-build-java-osgi
- bugfixes in osgi.req/prov

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt4
- bugfixes in osgi.req/prov

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt3
- sync with fedora (patches 21/23)

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt2
- added mavenpomdir macros
- man pages synced with jpackage-utils 5.0-2

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.0-alt1
- bumped version to match jpackage

* Fri Oct 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt13
- removed requires: on rpm-build-java (repo seems ready now)

* Thu Oct 08 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt12
- rpm-build-java now is arch-dependent: added arch-dependent macro
  _libjvmclient_sun_private_default/_libjvmserver_sun_private_default
  (thanks to Sergey V. Turchin)

* Sun Oct 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt10
- returned requires: on rpm-build-java
  those packages are not ready yet:
    389-ds-console-1.2.0-alt3
    freemind-0_9_0-alt3.rc1
    vuze-4.2.0.2-alt1

* Fri Oct 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt9
- removed requires: on rpm-build-java

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt8
- added safe mode to find-jar

* Fri May 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt7
- fix for safe mode for %post w/o jvm

* Fri May 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt6
- fix for safe mode for %post w/o jvm

* Fri May 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt5
- safe mode for %post w/o jvm

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt4
- removed useless warning in safe mode support patch

* Wed Feb 18 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt3
- safe mode for *build-jar-repository inside rpm scripts

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt2
- fix in osgi.req (optional dependencies are now skipped)

* Sun Dec 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt1
- update_maven_depmap made as a filetrigger
- future support of $RPM_FORCE_UPDATE_ALTERNATIVES
- fix in osgi.prov (empty line as separator support)

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt11
- support for M4x backports

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt10
- dirty hack until migration to new alternatives will be finished
  (jpackage-utils-1.7.5-alt-undefined-alternatives-during-transaction-hack)

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt9
- added jpackage-utils-1.7.5-alt-hasher-support-hack.patch

* Thu Oct 30 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt8
- removed ant.deprecated macros 
- range support in osgi.req

* Sat Jul 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt6
- enabled osgi.req*

* Thu Jul 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt5
- renamed ant.deprecated to ant-deprecated (not to be ignored)

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt4
- enabled osgi.prov* (osgi.req* symlinks are still disabled)

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt3
- added osgi.prov* (osgi.req* symlinks are still disabled)

* Wed May 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt2
- rpm-build-java is now built from jpackage-utils

* Wed May 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1
- sync'ed with jpackage 1.7.5 1jpp.
- removed BuildRequires rpm-build-java

* Wed Feb 13 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt2
- Do not override system macros (#12223) - made as external patch
- removed Requires rpm-build-java. (buildrequires is still left).
  The right way should be that rpm-build-java will Requires 
  and buildrequires jpackage-utils, or even will provide them.

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1
- new version

* Tue Nov 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.7.3-alt6
- fixed openjdk misdetection

* Sun Jul 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 0:1.7.3-alt5
- Added directory for Java 1.7.0 (openjdk) #12409

* Sun Jul 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0:1.7.3-alt4
- Do not override system macros (#12223)
- Requires and buildrequires rpm-build-java

* Fri Apr 06 2007 Damir Shayhutdinov <damir@altlinux.ru> 0:1.7.3-alt3
- Disabled gcj support 

* Mon Feb 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 0:1.7.3-alt2
- Some spec cleanup 

* Wed Feb 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 0:1.7.3-alt1
- Initial build for ALT Linux (based on Fedora 6 spec)


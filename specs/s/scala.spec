Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /osgi(org.apache.ant*/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.10.6
%global fullversion %{version}
%global release_repository http://nexus.scala-tools.org/content/repositories/releases
%global snapshot_repository http://nexus.scala-tools.org/content/repositories/snapshots
%global jansi_jar %{_javadir}/jansi/jansi.jar
%global jline2_jar %{_javadir}/jline/jline.jar
%global scaladir %{_datadir}/scala

%global want_jdk8 1
%global bootstrap_build 0

Name:           scala
Version:        2.10.6
Release:        alt2_8jpp8
Summary:        A hybrid functional/object-oriented language for the JVM
BuildArch:      noarch
# License was confirmed to be standard BSD by fedora-legal
# https://www.redhat.com/archives/fedora-legal-list/2007-December/msg00012.html
License:        BSD
URL:            http://www.scala-lang.org/

Source0:        https://github.com/scala/scala/archive/v%{version}.tar.gz
Source1:        scala-library-2.10.0-bnd.properties
# Bootstrap file generated by ./get-sources.sh
Source2:        scala-2.10.3-bootstrap.tgz
# git information generated by ./get-sources.sh
Source3:        scala.gitinfo


# we need this binary copy of the scala 2.10.4 compiler
# for bootstrapping under Java 8; this can be removed if
# necessary after Scala 2.10.5 is released if it uses 2.10.4
# for bootstrapping.
%if 0%{?bootstrap_build}
Source4:        http://www.scala-lang.org/files/archive/scala-2.10.4.tgz
%endif

# Source0:        http://www.scala-lang.org/downloads/distrib/files/scala-sources-%%{fullversion}.tgz
# Change the default classpath (SCALA_HOME)
Patch1:         scala-2.10.0-tooltemplate.patch
# Use system jline2 instead of bundled jline2
Patch2:         scala-2.10.3-use_system_jline.patch
# change org.scala-lang jline in org.sonatype.jline jline
Patch3:         scala-2.10.3-compiler-pom.patch
# Patch Swing module for JDK 1.7
Patch4:         scala-2.10.2-java7.patch
# fix incompatibilities with JLine 2.7
Patch6:         scala-2.10-jline.patch
# work around a known bug when running binary-compatibility tests against
# non-optimized builds (we can't do optimized builds due to another bug):
# http://grokbase.com/t/gg/scala-internals/1347g1jahq/2-10-x-bc-test-fails
# Patch7:         scala-2.10.1-bc.patch
Patch8:         scala-2.10.4-build_xml.patch

Source21:       scala.keys
Source22:       scala.mime
Source23:       scala-mime-info.xml
Source24:       scala.ant.d

Source31:       scala-bootstript.xml

BuildRequires:  java-devel >= 1.7.0
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  ant-contrib
BuildRequires:  jline >= 2.10
BuildRequires:  aqute-bnd
BuildRequires:  junit
BuildRequires:  javapackages-local

%if !(0%{?bootstrap_build})
BuildRequires:  scala
%endif

Requires:       jpackage-utils
Requires:       jansi

Requires:       jline >= 2.10

%{echo 
%filter_from_requires /ant/d;

}
Source44: import.info

%description
Scala is a general purpose programming language designed to express common
programming patterns in a concise, elegant, and type-safe way. It smoothly
integrates features of object-oriented and functional languages. It is also
fully interoperable with Java.

%package apidoc
Group: Development/Java
Summary:        Documentation for the Scala programming language

%description apidoc
Scala is a general purpose programming language for the JVM that blends
object-oriented and functional programming. This package provides
reference and API documentation for the Scala programming language.

%package swing
Group: Development/Other
Summary:        The swing library for the scala programming languages
Requires:       scala = %{version}-%{release}
Requires:       java >= 1.7.0

%description swing
This package contains the swing library for the scala programming languages. This library is required to develope GUI-releate applications in scala. The release provided by this package
is not the original version from upstream because this version is not compatible with JDK-1.7.

%package -n ant-scala
Group: Development/Other
Summary:        Development files for Scala
Requires:       scala = %{version}-%{release} ant

%description -n ant-scala
Scala is a general purpose programming language for the JVM that blends
object-oriented and functional programming. This package enables support for
the scala ant tasks.

%if 0
%package examples
Group: Development/Other
Summary:        Examples for the Scala programming language
# Otherwise it will pick up some perl module
Autoprov:       0
Requires:       scala = %{version}-%{release}
Requires:       ant

%description examples
Scala is a general purpose programming language for the JVM that blends
object-oriented and functional programming. This package contains examples for
the Scala programming language

%package swing-examples
Group: Development/Other
Summary:        Examples for the Scala Swing library
Requires:       scala = %{version}-%{release}
Requires:       ant

%description swing-examples
This package contains examples for the Swing library of the Scala language which is required
to create GUI applications in the Scala programming language. 
%endif

%prep

%global _default_patch_fuzz 2

%setup -q 
%patch1 -p1 -b .tool
%patch2 -p1 -b .sysjline
%patch3 -p1 -b .compiler-pom
%patch4 -p1 -b .jdk7
%patch6 -p1 -b .rvk
# %patch7 -p1 -b .bc
%patch8 -p1 -b .bld

echo "starr.version=2.10.4\nstarr.use.released=0" > starr.number

pushd src
rm -rf jline
popd

sed -i '/is not supported by/d' build.xml
sed -i '/exec.*pull-binary-libs.sh/d' build.xml

%if 0%{?bootstrap_build}
%global do_bootstrap -DdoBootstrapBuild=yes
tar -xzvf %{SOURCE2}
%if %{want_jdk8}
tar -xzvf %{SOURCE4} --strip-components=1 scala-2.10.4/lib
%endif
%else
%global do_bootstrap %{nil}
%endif

pushd lib
#  fjbg.jar ch.epfl.lamp
#  forkjoin.jar scala.concurrent.forkjoin available @ https://bugzilla.redhat.com/show_bug.cgi?id=854234 as jsr166y
#  find -not \( -name 'scala-compiler.jar' -or -name 'scala-library.jar' -or -name 'midpapi10.jar' -or \
#       -name 'msil.jar' -or -name 'fjbg.jar' -or -name 'forkjoin.jar' \) -and -name '*.jar' -delete


#  midpapi10.jar https://bugzilla.redhat.com/show_bug.cgi?id=807242 ?
#  msil.jar ch.epfl.lamp.compiler
#  scala-compiler.jar
#  scala-library-src.jar
#  scala-library.jar
%if !(0%{?bootstrap_build})
    rm -rf scala-compiler.jar
    ln -s $(build-classpath scala/scala-compiler.jar) scala-compiler.jar
    rm -rf scala-library.jar
    ln -s $(build-classpath scala/scala-library.jar) scala-library.jar
    rm -rf scala-reflect.jar
    ln -s $(build-classpath scala/scala-reflect.jar) scala-reflect.jar
%endif
  pushd ant
    rm -rf ant.jar
    rm -rf ant-contrib.jar
    ln -s $(build-classpath ant.jar) ant.jar
    ln -s $(build-classpath ant/ant-contrib) ant-contrib.jar
#    rm -rf ant-dotnet-1.0.jar
#    rm -rf maven-ant-tasks-2.1.1.jar
#    rm -rf vizant.jar
  popd
popd

cp -rf %{SOURCE31} .


sed -i -e 's!@JLINE@!%{jline2_jar}!g' build.xml

echo echo $(head -n 1 %{SOURCE3}) > tools/get-scala-commit-sha
echo echo $(tail -n 1 %{SOURCE3}) > tools/get-scala-commit-date
chmod 755 tools/get-scala-*

%build

export ANT_OPTS="-Xms2048m -Xmx2048m %{do_bootstrap}"

# NB:  the "build" task is (unfortunately) necessary
#  build-opt will fail due to a scala optimizer bug
#  and its interaction with the system jline
# ant -f scala-bootstript.xml build
ant build docs || exit 1
pushd build/pack/lib
mv scala-library.jar scala-library.jar.no
bnd wrap --properties %{SOURCE1} --output scala-library.jar \
    --version "%{version}" scala-library.jar.no
popd

%check

# these tests fail, but their failures appear spurious
rm -f test/files/run/parserJavaIdent.scala
rm -rf test/files/presentation/implicit-member
rm -rf test/files/presentation/t5708
rm -rf test/files/presentation/ide-bug-1000349
rm -rf test/files/presentation/ide-bug-1000475
rm -rf test/files/presentation/callcc-interpreter
rm -rf test/files/presentation/ide-bug-1000531
rm -rf test/files/presentation/visibility
rm -rf test/files/presentation/ping-pong

rm -f test/osgi/src/ReflectionToolboxTest.scala

# fails under mock but not under rpmbuild
rm -f test/files/run/t6223.scala

## Most test dependencies still aren't available in Fedora
# ant test

%install

install -d $RPM_BUILD_ROOT%{_bindir}
for prog in scaladoc fsc scala scalac scalap; do
        install -p -m 755 build/pack/bin/$prog $RPM_BUILD_ROOT%{_bindir}
done

install -p -m 755 -d $RPM_BUILD_ROOT%{scaladir}/lib

# Add symlinks in lib directory
%mvn_file ':{*}:jar:' %{name}/@1 %{scaladir}/lib/@1
# Add compat symlinks to POMs because climbing-nemesis uses the old JPP naming convention
%mvn_file ':{*}:pom:' %{name}/@1 JPP.%{name}-@1

%mvn_package :scala-swing swing

# XXX: add scala-partest when it works again
for libname in scala-compiler \
    scala-library \
    scala-reflect \
    scalap \
    scala-swing ; do
        sed -i "s|@VERSION@|%{fullversion}|" src/build/maven/$libname-pom.xml
        sed -i "s|@RELEASE_REPOSITORY@|%{release_repository}|" src/build/maven/$libname-pom.xml
        sed -i "s|@SNAPSHOT_REPOSITORY@|%{snapshot_repository}|" src/build/maven/$libname-pom.xml
        %mvn_artifact src/build/maven/$libname-pom.xml build/pack/lib/$libname.jar
done
ln -s $(abs2rel %{jline2_jar} %{scaladir}/lib) $RPM_BUILD_ROOT%{scaladir}/lib
ln -s $(abs2rel %{jansi_jar} %{scaladir}/lib) $RPM_BUILD_ROOT%{scaladir}/lib

%mvn_install

install -d $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
install -p -m 644 %{SOURCE24} $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/scala

%if 0
cp -pr docs/examples $RPM_BUILD_ROOT%{_datadir}/scala/
%endif 

install -d $RPM_BUILD_ROOT%{_datadir}/mime-info
install -p -m 644 %{SOURCE21} %{SOURCE22} $RPM_BUILD_ROOT%{_datadir}/mime-info/

install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages/
install -p -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_datadir}/mime/packages/

sed -i -e 's,@JAVADIR@,%{_javadir},g' -e 's,@DATADIR@,%{_datadir},g' $RPM_BUILD_ROOT%{_bindir}/*

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 build/scaladoc/manual/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%files -f .mfiles
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/j*.jar
%{_datadir}/mime-info/*
%{_datadir}/mime/packages/*
%{_mandir}/man1/*
%doc docs/LICENSE
%dir %_datadir/scala/lib

%files swing -f .mfiles-swing
%doc docs/LICENSE

%files -n ant-scala
# Following is plain config because the ant task classpath could change from
# release to release
%config %{_sysconfdir}/ant.d/*
%doc docs/LICENSE

%files apidoc
%doc build/scaladoc/library/*
%doc docs/LICENSE

%if 0
%files examples
%{_datadir}/scala/examples
%exclude %{_datadir}/scala/examples/swing 
%doc docs/LICENSE

%files swing-examples
%{_datadir}/scala/examples/swing 
%doc docs/LICENSE
%endif

%changelog
* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_8jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_3jpp8
- added BR: javapackages-local for javapackages 5

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt1_3jpp8
- new version

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt2_9jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_8jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies


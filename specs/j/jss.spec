%define _unpackaged_files_terminate_build 1

Name: jss
Version: 4.5.0
Release: alt1

Summary: Java Security Services (JSS)
License: MPL-1.1 or GPL-2.0-or-later or LGPLv2+
Group: System/Libraries
# Source-git: https://github.com/dogtagpki/jss.git
Url: http://www.dogtagpki.org/wiki/JSS

Source0: %name-%version.tar
Source1: jss.watch
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-codec
BuildRequires: slf4j
BuildRequires: slf4j-jdk14

Requires: apache-commons-lang
Requires: apache-commons-codec
Requires: slf4j
Requires: java-headless

%description
Network Security Services for Java (JSS) is a Java interface to NSS. JSS
supports most of the security standards and encryption technologies supported by
NSS. JSS also provides a pure Java interface for ASN.1 types and BER/DER
encoding.

JSS offers a implementation of Java SSL sockets that uses NSS's SSL/TLS
implementation rather than Sun's JSSE implementation. You might want to use
JSS's own SSL classes if you want to use some of the capabilities found in NSS's
SSL/TLS library but not found in JSSE.

NSS is the cryptographic module where all cryptographic operations are
performed. JSS essentially provides a Java JNI bridge to NSS C shared libraries.
When NSS is put in FIPS mode, JSS ensures FIPS compliance by ensuring that all
cryptographic operations are performed by the NSS cryptographic module.

%package javadoc
Summary: Java Security Services (JSS) Javadocs
Group: Development/Java
Requires: %name = %EVR
BuildArch: noarch

%description javadoc
This package contains the API documentation for JSS.

%prep
%setup
%patch0 -p1

%build
export JAVA_HOME=%_jvmdir/java
export USE_INSTALLED_NSPR=1
export USE_INSTALLED_NSS=1

# Enable compiler optimizations and disable debugging code
# NOTE: If you ever need to create a debug build with optimizations disabled
# just comment out this line and change in the %%install section below the
# line that copies jars xpclass.jar to be xpclass_dbg.jar
export BUILD_OPT=1

# Generate symbolic info for debuggers
export XCFLAGS="-g $RPM_OPT_FLAGS"

export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

NSPR_INCLUDE_DIR=`/usr/bin/pkg-config --cflags-only-I nspr | sed 's/-I//'`
NSPR_LIB_DIR=`/usr/bin/pkg-config --libs-only-L nspr | sed 's/-L//'`
[ -z $NSPR_LIB_DIR ] && NSPR_LIB_DIR="%_libdir"

NSS_INCLUDE_DIR=`/usr/bin/pkg-config --cflags-only-I nss | sed 's/-I//'`
NSS_LIB_DIR=`/usr/bin/pkg-config --libs-only-L nss | sed 's/-L//'`
[ -z $NSS_LIB_DIR ] && NSS_LIB_DIR="%_libdir"

export NSPR_INCLUDE_DIR
export NSPR_LIB_DIR
export NSS_INCLUDE_DIR
export NSS_LIB_DIR

%ifarch aarch64 x86_64 ppc64 ia64 s390x sparc64
export USE_64=1
%endif

# The Makefile is not thread-safe
rm -rf ../dist
mkdir ../dist
%make -C coreconf
%make
%make javadoc
# actually must be at 'check' section, but requires all exports as 'build'
%make test_jss

%install
install -d -m 0755 %buildroot%_jnidir
install -m 644 ../dist/xpclass.jar %buildroot%_jnidir/jss4.jar

# We have to use the name libjss4.so because this is dynamically
# loaded by the jar file.
install -d -m 0755 %buildroot%_libdir/jss
install -m 0755 ../dist/Linux*.OBJ/lib/libjss4.so %buildroot%_libdir/jss/
pushd  %buildroot%_libdir/jss
    ln -fs %_jnidir/jss4.jar jss4.jar
popd

# javadoc
install -d -m 0755 %buildroot%_javadocdir/%name-%version
cp -rp ../dist/jssdoc/* %buildroot%_javadocdir/%name-%version
cp -p jss.html %buildroot%_javadocdir/%name-%version
cp -p *.txt %buildroot%_javadocdir/%name-%version

%check

%files
%dir %_libdir/jss
%_libdir/jss/jss4.jar
%_libdir/jss/libjss4.so
%_jnidir/jss4.jar

%files javadoc
%_javadocdir/%name-%version

%changelog
* Mon Aug 13 2018 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 4.4.5 -> 4.5.0.

* Tue Jul 10 2018 Stanislav Levin <slev@altlinux.org> 4.4.5-alt1
- 4.4.4 -> 4.4.5

* Fri Jun 01 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.4-alt2
- fixed packaging on aarch64

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 4.4.4-alt1
- 4.4.3 -> 4.4.4

* Wed May 23 2018 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1
- 4.4.2 -> 4.4.3

* Wed Sep 20 2017 Levin Stanislav <slev@altlinux.org> 4.4.2-alt1
- Update to upstream 4.4.2 version

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 4.2.6-alt6_41jpp8.M80P.1
- Build for p8.

* Mon Nov 21 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt6_42jpp8
- update (closes: #32779)

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt6_37jpp8
- new version

* Wed Nov 18 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.6-alt6_31jpp7
- Provide Tomcat support for TLS v1.1 and TLS v1.2 via NSS through JSS

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt5_31jpp7
- any-kernel patch thanks to gleb

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_31jpp7
- new version (closes: 29317)

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_29jpp7
- new release

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_28jpp7
- fixed build

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_25jpp7
- added jss4 compat symlink

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt3_25jpp7
- added jss4 compat symlink

* Tue Oct 30 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt2_25jpp7
- new release; fixed build, updated fedora patches

* Wed Dec 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.6-alt2
- Fix build on 3.x kernels

* Sat Dec 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.6-alt1
- 4.2.6 with Fedora patches

* Tue Oct 23 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.5-alt1
- 4.2.5, spec cleanup

* Thu May 31 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.4-alt0
- Initial for Sisyphus

* Wed May 16 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-5
- Include the 3 license files
- Remove Requires for nss and nspr. These libraries have versioned symbols
  so BuildRequires is enough to set the minimum.
- Add sparc64 for the 64-bit list

* Mon May 14 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-4
- Included additional comments on jar signing and why ldconfig is not
  required.

* Thu May 10 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-3
- Added information on how to pull the source into a tar.gz

* Thu Mar 15 2007  Rob Crittenden <rcritten@redhat.com> 4.2.4-2
- Added RPM_OPT_FLAGS to XCFLAGS

- Added link to Sun JCE information
* Mon Feb 27 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-1
- Initial build

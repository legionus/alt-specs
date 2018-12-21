Name: node-gyp
Version: 3.8.0
Release: alt1

Summary: Node.js native addon build tool
License: MIT
Group: Development/Tools

Url: https://github.com/TooTallNate/node-gyp

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: http://registry.npmjs.org/node-gyp/-/node-gyp-%version.tgz
# Note: see .gear/gear-sources created with rpmgs -f from etersoft-build-utils
# Source-url: https://github.com/nodejs/node-gyp/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-sources-%version.tar
Source2: %name-production-%version.tar

Source10: addon-rpm.gypi

BuildArch: noarch

# we do not need any module provides here
AutoProv: yes,nonodejs
AutoReq: yes,nonodejs

Provides: npm(node-gyp) = %version

# These patches are Fedora-specific for the moment, although I'd like to find
# a way to support this kind of stuff upstream.

# use RPM installed headers by default instead of downloading a source tree
# for the currently running node version
Patch1: node-gyp-addon-gypi.patch

# use the system gyp
Patch2: node-gyp-system-gyp.patch

BuildRequires: node-devel rpm-build-nodejs

BuildRequires(pre): rpm-macros-nodejs

BuildRequires: gcc-c++ python-devel

#gyp is the actual build framework node-gyp uses
Requires: gyp

#this is the standard set of headers expected to build any node native module
Requires: rpm-build-nodejs
#we also need a C++ compiler to actually build stuff ;-)
# TODO: what about toolchain?
Requires: gcc-c++ make
#Patch33: addon-rpm.gypi.patch

%description
node-gyp is a cross-platform command-line tool written in Node.js for compiling
native addon modules for Node.js, which takes away the pain of dealing with the
various differences in build platforms.

%prep
%setup -a 2
#patch1 -p1
#patch2 -p1

# use system gyp
#__subst "s|\(var gyp_script =\).*|\1 '/usr/bin/gyp'|g" lib/configure.js

#nodejs_fixdep request 2.x
#nodejs_fixdep npmlog 3
#nodejs_fixdep nopt 3
#nodejs_fixdep semver 2.1
#patch33 -p0

rm -rf gyp/
mkdir gyp/
# compat hack
ln -s %_bindir/gyp gyp/gyp_main.py

%build
#nothing to do

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%nodejs_sitelib/node-gyp/
cp -pr addon*.gypi bin lib gyp node_modules package.json %buildroot%nodejs_sitelib/node-gyp/
cp -p %SOURCE10 %buildroot%nodejs_sitelib/node-gyp/addon-rpm.gypi

mkdir -p %buildroot%_bindir
ln -sf ../lib/node_modules/node-gyp/bin/node-gyp.js %buildroot%_bindir/node-gyp

# we will do bundle
#nodejs_symlink_deps

%files
%_bindir/node-gyp
%nodejs_sitelib/node-gyp/
%doc README.md LICENSE

%changelog
* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version (3.8.0) with rpmgs script

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version (3.6.2) with rpmgs script

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt2
- build fixes

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt1
- new version 3.4.0 (with rpmrb script)

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt4_2
- fc import

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt4_1
- addon.gypi patched also

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt3_1
- link with libv8

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt2_1
- use -fPIC on ix86

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt1_1
- fc import

* Tue Jun 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- initial import


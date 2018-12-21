%define _unpackaged_files_terminate_build 1

Name: os-autoinst
Version: 4.5.1527308405.8b586d5
Release: alt1
Summary: OS-level test automation
License: GPLv2+
Group: Development/Tools
Url: https://github.com/os-autoinst/os-autoinst/
Source: %name-%version.tar
Patch0: fixdependencies.patch

BuildRequires: perlcritic
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: libopencv-devel
BuildRequires: perl-devel
BuildRequires: perl-Test-Warnings
BuildRequires: perl-Package-Generator
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(ExtUtils/Embed.pm)
BuildRequires: perl(Module/CPANfile.pm)
BuildRequires: perl(Perl/Critic.pm)
BuildRequires: perl(Perl/Tidy.pm)
BuildRequires: perl(Pod/Html.pm)
BuildRequires: perl(Term/ReadLine.pm)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(theoraenc)
BuildRequires: systemd
BuildRequires: perl(Devel/Cover.pm)
BuildRequires: perl(Pod/Coverage.pm)
BuildRequires: perl(Test/Compile.pm)
BuildRequires: perl(Socket/MsgHdr.pm)
BuildRequires: perl(Test/Fatal.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/MockTime.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Output.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Warnings.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: /usr/bin/qemu-system-i386
BuildRequires: /usr/bin/qemu-img
BuildRequires: perl(Mojo/File.pm)
BuildRequires: perl(Carp/Always.pm) perl(Data/Dump.pm) perl(Crypt/DES.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(autodie.pm) perl(Class/Accessor/Fast.pm) perl(Exception/Class.pm) perl(File/Which.pm) perl(IPC/Run/Debug.pm) perl(Net/DBus.pm) perl(Net/SNMP.pm) perl(Net/IP.pm) perl(IPC/System/Simple.pm) perl(Net/SSH2.pm) perl(XML/LibXML.pm)
BuildRequires: perl(Mojolicious.pm)
Requires: qemu-kvm
Requires: tesseract
Requires: withlock
Requires: perl(Carp/Always.pm) perl(Data/Dump.pm) perl(Net/SNMP.pm) perl(Net/IP.pm)
Requires: /usr/bin/qemu-img
Requires: optipng
Requires: qemu >= 2.0.0

%add_perl_lib_path %buildroot%_libexecdir/os-autoinst

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer and
upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used to
test applications on top of a newly installed OS.

%package openvswitch
Summary: Open vSwitch support for os-autoinst
Group: System/Servers
BuildArch: noarch

Requires: %name = %EVR
Requires: openvswitch

%description openvswitch
This package contains Open vSwitch support for os-autoinst.

%prep
%setup
%patch0 -p1
rm -f t/99-full-stack.t
sed -i -e 's, 99-full-stack.t,,g' t/Makefile.am
sed -i -e 's|/usr/lib/systemd/|/lib/systemd/|' Makefile.am

%build
mkdir -p m4
%autoreconf
%configure --docdir=%_defaultdocdir/%name-%version
%make_build INSTALLDIRS=vendor

%install
%makeinstall_std INSTALLDIRS=vendor
rm %buildroot%_libexecdir/os-autoinst/tools/tidy
rm -r %buildroot%_libexecdir/os-autoinst/tools/lib/perlcritic
rm %buildroot%_libexecdir/os-autoinst/tools/check_coverage
rm %buildroot%_libexecdir/os-autoinst/crop.py*

%check
sed -i -e '/tidy --check/d' Makefile
%make check VERBOSE=1

%files
%_docdir/*
%perl_vendorarch/tinycv.pm
%perl_vendorarch/auto/tinycv
%_libexecdir/os-autoinst
%exclude %_libexecdir/os-autoinst/os-autoinst-openvswitch
%_bindir/*

%files openvswitch
%_libexecdir/os-autoinst/os-autoinst-openvswitch
%_unitdir/os-autoinst-openvswitch.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.5.1527308405.8b586d5-alt1
- initial build for ALT

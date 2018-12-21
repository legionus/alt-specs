#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: freehdl
Summary: VHDL simulator
Version: 0.0.8
Release: alt4
License: GPL
Group: Development/Other
BuildRequires: flex gcc-c++
%define _keep_libtool_files 1
%set_verify_elf_method unresolved=relaxed
Url: http://www.freehdl.seul.org/
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires: lib%name-devel = %version-%release
Requires: lib%name = %version-%release
Source: %name-%version.tar
Patch1: %name-%version-alt-gcc6.patch

%package -n libfreehdl
Summary: VHDL simulator
Group: Development/Other

%description -n libfreehdl
VHDL simulator

%package -n libfreehdl-devel
Summary: VHDL simulator
Group: Development/Other
Requires: lib%name = %version-%release

%description -n libfreehdl-devel
VHDL simulator

%package -n libfreehdl-devel-static
Summary: VHDL simulator
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n libfreehdl-devel-static
VHDL simulator

%description
VHDL simulator


%prep
%setup
%patch1 -p2

%build
sed -i 's!FREEHDL/lib!%_libdir!g' v2cc/gvhdl.in
%autoreconf -fisv
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/freehdl-config
%_bindir/freehdl-gennodes
%_bindir/freehdl-v2cc
%_bindir/gvhdl
%_datadir/freehdl
%_datadir/freehdl/lib
%_datadir/freehdl/lib/ieee
%_datadir/freehdl/lib/std
%_datadir/freehdl/lib/ieee/math_real.vhdl
%_datadir/freehdl/lib/ieee/numeric_bit.vhdl
%_datadir/freehdl/lib/ieee/numeric_std.vhdl
%_datadir/freehdl/lib/ieee/std_logic_1164.vhdl
%_datadir/freehdl/lib/ieee/std_logic_arith.vhdl
%_datadir/freehdl/lib/ieee/std_logic_signed.vhdl
%_datadir/freehdl/lib/ieee/std_logic_unsigned.vhdl
%_datadir/freehdl/lib/ieee/vital_timing.vhdl
%_datadir/freehdl/lib/std/standard.vhdl
%_datadir/freehdl/lib/std/textio.vhdl
%_datadir/info/fire.info*
%_man1dir/freehdl-config.1*
%_man1dir/freehdl-gennodes.1*
%_man1dir/freehdl-v2cc.1*
%_man1dir/gvhdl.1*
%_man5dir/v2cc.libs.5*

%files -n libfreehdl
%_libdir/freehdl
%_libdir/freehdl/libieee.so.0
%_libdir/freehdl/libieee.so.0.0.0
%_libdir/libfreehdl-cdfggen.so.0
%_libdir/libfreehdl-cdfggen.so.0.0.0
%_libdir/libfreehdl-fire.so.0
%_libdir/libfreehdl-fire.so.0.0.0
%_libdir/libfreehdl-kernel.so.0
%_libdir/libfreehdl-kernel.so.0.0.0
%_libdir/libfreehdl-std.so.0
%_libdir/libfreehdl-std.so.0.0.0
%_libdir/libfreehdl-vaul.so.0
%_libdir/libfreehdl-vaul.so.0.0.0

%files -n libfreehdl-devel
%_libdir/freehdl/libieee.la
%_libdir/freehdl/libieee.so
%_libdir/libfreehdl-cdfggen.so
%_libdir/libfreehdl-fire.so
%_libdir/libfreehdl-kernel.so
%_libdir/libfreehdl-std.so
%_libdir/libfreehdl-vaul.so
%_libdir/*.la
%_pkgconfigdir/freehdl.pc
%_includedir/freehdl

%files -n libfreehdl-devel-static
%_libdir/freehdl/libieee.a
%_libdir/libfreehdl-cdfggen.a
%_libdir/libfreehdl-fire.a
%_libdir/libfreehdl-kernel.a
%_libdir/libfreehdl-std.a
%_libdir/libfreehdl-vaul.a

%changelog
* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.8-alt4
- Fixed build with gcc-6

* Tue Jan 26 2016 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt3
- fix build

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt2
- fix subpackage requires

* Mon Oct 15 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt1
- 0.0.8

* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt5
- fix build

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt4
- auto rebuild

* Thu Dec 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt3
- small cleanups

* Thu Dec 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt2
- split to subpackages

* Sun Dec 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt1
- first build for Sisyphus


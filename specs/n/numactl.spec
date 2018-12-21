%def_disable static

Name: numactl
Version: 2.0.11
Release: alt1

Summary: Simple NUMA policy support
License: GPL
Group: System/Libraries

Url: http://oss.sgi.com/projects/libnuma/
Source: %name-%version.tar.gz
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

%description
NUMA stands for Non-Uniform Memory Access, in other words a system whose
memory is not all in one place. The system consists of multiple "nodes"
of CPUs (processors) and/or memory which are linked together by a special
high-speed network. All CPUs have access to all of memory, but a CPU's
access to memory on the local or a nearby node is faster than to distant
nodes.

%package -n libnuma
Group: System/Libraries
Summary: Shared libraries for %name

%description -n libnuma
%summary

%package -n libnuma-devel
Summary: Development files for %name
Group: Development/C
Requires: libnuma = %version-%release

%description -n libnuma-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%if_enabled static
%package -n libnuma-devel-static
Summary: Development files for %name
Group: Development/C
Requires: libnuma = %version-%release

%description -n libnuma-devel-static
The %name-devel package contains libraries and header files for
developing applications that use %name.
%endif

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%doc README CHANGES DESIGN TODO
%_bindir/*
#_man2dir/* -- see man-pages package
%_man3dir/*
%_man8dir/*

%files -n libnuma
%_libdir/*.so.*

%files -n libnuma-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n libnuma-devel-static
%_libdir/*.a
%endif

%changelog
* Sun Dec 13 2015 Michael Shigorin <mike@altlinux.org> 2.0.11-alt1
- new version (watch file uupdate)

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 2.0.10-alt2
- dropped numactl(2) page conflicting with man-pages package

* Sat Oct 04 2014 Michael Shigorin <mike@altlinux.org> 2.0.10-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 2.0.9-alt1
- new version (watch file uupdate)

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0.7-alt1
- 2.0.7
- build for debuginfo

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1.1
- rebuild for set:provides by request of mithraen

* Sun Jul 11 2010 Michael Shigorin <mike@altlinux.org> 2.0.3-alt1
- TMC package built for Sisyphus
- static library build disabled by default
- minor spec cleanup



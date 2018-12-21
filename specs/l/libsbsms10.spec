%define major 10

Summary: C++ library for subband sinusoidal modeling time stretching and pitch scaling
Name: libsbsms%major
Version: 2.0.2
Release: alt2
License: GPLv2
Group: System/Libraries
URL: http://sbsms.sourceforge.net/
Source0: %name-%version.tar

Patch0: DEBIAN-set-library-version.patch
Patch1: ALT-e2k-fft.patch
Patch3: GENTOO-cflags.patch
Patch4: ALT-audacity-bug-955.patch

BuildRequires: gcc-c++ pkgconfig(sndfile)

%description
C++ library for subband sinusoidal modeling time stretching and pitch scaling

%package -n libsbsms-devel
Summary: Development files of C++ library for subband sinusoidal modeling time stretching and pitch scaling
Group: Development/C++
Requires: %name = %EVR

%description -n libsbsms-devel
Development files of the C++ library for subband sinusoidal modeling time stretching and pitch scaling
#--------------------------------------

%prep
%setup

%patch0 -p1
%patch3 -p1
%patch4 -p3

%ifarch %e2k
%patch1 -p1
%endif

%build
%autoreconf

%configure \
	--enable-shared \
	--disable-static \
%ifarch %ix86 x86_64 %e2k
	--enable-sse \
%else
	--disable-sse \
%endif
	--disable-multithreaded
# --enable-multithreaded causes building error: "verify-elf: ERROR: ./usr/lib64/libsbsms.so.10.0.1: undefined symbol: pthread_create".
# According to Gentoo's ebuild (https://gitweb.gentoo.org/repo/gentoo.git/tree/media-libs/libsbsms), multithreaded build segfaults.
# Multithereding is also disabled by default in both sbsms's upstream and Audacity's built-in sbsms.
	
%make_build

%install
%makeinstall_std
#--------------------------------------

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_libdir/libsbsms.so.%{major}
%_libdir/libsbsms.so.%{major}.*

%files -n libsbsms-devel
%_pkgconfigdir/*.pc
%_includedir/*
%_libdir/libsbsms.so

#--------------------------------------
%changelog
* Sun Dec 02 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt2
- Port from Audacity commit 954bb0f: ALT-audacity-bug-955.patch

* Wed Nov 07 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt1
- Initial build for ALT Linux (version 2.0.2)

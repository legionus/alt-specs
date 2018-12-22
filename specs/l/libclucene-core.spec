%define rname clucene-core
Name: libclucene-core
Version: 2.3.3.4
Release: alt4

Summary: CLucene is a C++ port of Lucene.
License: LGPL-1.0-only or Apache-2.0
Group: System/Libraries

Url: http://clucene.sf.net
Source: %rname-%version.tar.gz
# FC
Patch1: clucene-core-2.3.3.4-install_contribs_lib.patch
Patch2: clucene-core-2.3.3.4-pkgconfig.patch
# SuSE
Patch11: clucene-kill-ext-includes.diff
# ALT
Patch21: %rname-%version-alt-build.patch

BuildRequires: boost-devel-headers cmake gcc-c++ zlib-devel kde-common-devel

%description
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.

%package -n libclucene-shared
Group: System/Libraries
Summary: CLucene shared library
%description -n libclucene-shared
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.

%package -n libclucene-contribs-lib
Group: System/Libraries
Summary: CLucene contribs library
%description -n libclucene-contribs-lib
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.

%package -n %name-devel
Summary: Development library and headers files fo CLucene
Group: Development/C++
#Requires: libclucene-core libclucene-shared
Conflicts: libclucene-devel
%description -n %name-devel
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.


%package -n %name-devel-static
Summary: Static library for CLucene
Group: Development/C++
Requires: %name-devel
%description -n %name-devel-static
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.


%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1
%patch11 -p1
%patch21 -p2

%build
%Kbuild \
    -DBUILD_CONTRIBS_LIB:BOOL=ON \
    -DLUCENE_SYS_INCLUDES:PATH=%_libdir

%install
%Kinstall

%files
%_libdir/libclucene-core.so.*

%files -n libclucene-shared
%_libdir/libclucene-shared.so.*

%files -n libclucene-contribs-lib
%_libdir/libclucene-contribs-lib.so.*

%files -n %name-devel
%_pkgconfigdir/libclucene-core.pc
%_libdir/CLucene/
%_libdir/CLuceneConfig.cmake
%_includedir/CLucene
%_includedir/CLucene.h
%_libdir/lib*.so

#%files -n %name-devel-static
#%_libdir/lib*.a

%changelog
* Wed Nov 28 2018 Sergey V Turchin <zerg@altlinux.org> 2.3.3.4-alt4
- fix check gcc version

* Mon Jul 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.3.4-alt3
- Fixed build with gcc-6

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2.3.3.4-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.3.4-alt2
- don't export include directory with private boost headers

* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.3.4-alt0.M60P.1
- build for M60P

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.3.4-alt1
- initial build

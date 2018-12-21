Name: ferrisloki
Version: 3.0.13
Release: alt1%ubt
Summary: Loki C++ library from Modern C++ Design
License: GPL
Group: System/Libraries
Url: http://www.libferris.com/

# https://sourceforge.net/projects/witme/files/ferrisloki/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libsigc++2-devel

%description
Loki library adapted for Linux and containing extensions
in Extensions.hh that have not been feed back into the
main Loki tree yet. Note that the main library has been
renamed to libferrisloki and headers installed into
FerrisLoki/ in include so as to highlight that this is
not the standard version.

%package -n lib%name
Group: System/Libraries
Summary: Loki C++ library from Modern C++ Design

%description -n lib%name
Loki library adapted for Linux and containing extensions
in Extensions.hh that have not been feed back into the
main Loki tree yet. Note that the main library has been
renamed to libferrisloki and headers installed into
FerrisLoki/ in include so as to highlight that this is
not the standard version.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for Loki C++ library

%description -n lib%name-devel
Loki library adapted for Linux and containing extensions
in Extensions.hh that have not been feed back into the
main Loki tree yet. Note that the main library has been
renamed to libferrisloki and headers installed into
FerrisLoki/ in include so as to highlight that this is
not the standard version.

This package includes development files.

%prep
%setup

find -name '*.h' -exec sed -i '/sigc++\/object.h/d' {} + || die
find -name '*.hh' -exec sed -i '/sigc++\/object.h/d' {} + || die

%build
%configure
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a

%files -n lib%name
%doc README* COPYING AUTHORS ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%changelog
* Wed Oct 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.13-alt1%ubt
- Initial build for ALT.

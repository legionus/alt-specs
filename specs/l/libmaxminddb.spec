Name:    libmaxminddb
Version: 1.3.2
Release: alt1

Summary: C library for the MaxMind DB file format

# original libmaxminddb code is Apache Licence 2.0
# src/maxminddb-compat-util.h is BSD
License: Apache-2.0 and BSD
Url:     https://maxmind.github.io/libmaxminddb
Group:   Other

Source: %name-%version.tar

BuildRequires: gcc

%description
The package contains libmaxminddb library.

%package devel
Requires: %name = %EVR
Requires: pkgconfig
Summary: Development header files for libmaxminddb
Group:   Other

%description devel
The package contains development header files for the libmaxminddb library
and the mmdblookup utility which allows IP address lookup in a MaxMind DB file.

%prep
%setup

%build
%configure --disable-static
# remove embeded RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# link only requried libraries
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%makeinstall_std

%files
%_libdir/libmaxminddb.so.*

%files devel
%doc Changes.md
%_bindir/mmdblookup
%_includedir/maxminddb.h
%_includedir/maxminddb_config.h
%_libdir/libmaxminddb.so
%_libdir/pkgconfig/libmaxminddb.pc
%_man1dir/*
%_man3dir/*

%changelog
* Thu Dec 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus.

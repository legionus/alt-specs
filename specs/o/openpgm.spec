# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/patch gcc-c++ perl(JSON.pm) perl(Net/SSH.pm) python-devel rpm-build-perl rpm-build-python
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api 5.2
%define major  0
%define libname libpgm%{api}%{major}
%define devname libpgm-devel

Name:          openpgm
Version:       5.2.122
Release:       alt1_3
Summary:       An implementation of the PGM reliable multicast protocol
Group:         System/Libraries
# The license is LGPLv2.1
License:       LGPLv2
# New URL is https://github.com/steve-o/openpgm
URL:           http://openpgm.googlecode.com/
Source0:       http://openpgm.googlecode.com/files/libpgm-%{version}~dfsg.tar.gz
BuildRequires: python-base python-tools-2to3
BuildRequires: perl
Source44: import.info

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n %{libname}
Summary:       Library files for %{name}
Group:         System/Libraries
Obsoletes:     %{_lib}openpgm0 < 5.2.122-3

%description -n %{libname}
This package contains OpenPGM libraries.

%package -n %{devname}
Summary:       Development files for %{name}
Group:         System/Libraries
Requires:      %{libname} = %{version}-%{release}
Provides:      %{name}%{api}-devel = %{version}-%{release}
Provides:      %{name}-devel = %{version}-%{release}
Obsoletes:     %{_lib}openpgm-devel < 5.2.122-3

%description -n %{devname}
This package contains OpenPGM related development libraries and header files.

%prep
%setup -q -n libpgm-%{version}~dfsg/%{name}/pgm

%build
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc COPYING LICENSE
%{_libdir}/libpgm-%{api}.so.%{major}
%{_libdir}/libpgm-%{api}.so.%{major}.*

%files -n %{devname}
%doc examples/
%{_includedir}/*
%{_libdir}/libpgm.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 5.2.122-alt1_3
- new version


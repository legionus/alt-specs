# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 7
%define libname libmonetra%{major}
%define develname libmonetra-devel

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	7.14.0
Release:	alt1_1.1
Group:		System/Libraries
License:	GPLv2+
URL:		https://www.monetra.com/
Source0:	https://www.monetra.com/downloads/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(krb5)
Source44: import.info

%description
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{libname}
Summary:	Library to allow credit card processing through MCVE
Group:          System/Libraries

%description -n	%{libname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

This package contains the static %{name} library and its header
files.

%prep
%setup -q


%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy

%configure --enable-deprecated
%make_build

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a




%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 7.14.0-alt1_1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun May 06 2018 Igor Vlasenko <viy@altlinux.ru> 7.14.0-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 7.7.0-alt1_8
- new version


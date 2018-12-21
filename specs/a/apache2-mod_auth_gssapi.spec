%define _unpackaged_files_terminate_build 1

%define modname mod_auth_gssapi
%def_with check

Name: apache2-%modname
Version: 1.6.1
Release: alt2

Summary: A GSSAPI Authentication module for Apache2
Group: System/Servers
License: %mit
Url: https://github.com/modauthgssapi/mod_auth_gssapi

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): apache2-devel

BuildRequires: libssl-devel
BuildRequires: libkrb5-devel >= 1.15
BuildRequires: libaprutil1-devel
BuildRequires: gssntlmssp-devel
BuildRequires: flex

%if_with check
BuildRequires: words
BuildRequires: krb5-kdc
BuildRequires: socket_wrapper
BuildRequires: nss_wrapper
BuildRequires: openssl
BuildRequires: apache2-httpd-prefork
BuildRequires: apache2-mod_cache_disk
BuildRequires: apache2-suexec
BuildRequires: python-module-requests-gssapi
%endif

Provides: %modname = %EVR

Requires: apache2 >= %apache2_version
Requires: libkrb5 >= 1.15

%description
The mod_auth_gssapi module is an authentication service that implements
the SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%apache2_libexecdir
install src/.libs/%modname.so %buildroot%apache2_libexecdir
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > %buildroot%apache2_mods_available/auth_gssapi.load

%check
%make test

%files
%doc COPYING README
%apache2_libexecdir/%modname.so
%config(noreplace) %apache2_mods_available/auth_gssapi.load

%changelog
* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt2
- Build with new openssl1.1.

* Fri May 04 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.6.0 -> 1.6.1

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.4.1 -> 1.6.0

* Wed Nov 30 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1
- 1.4.1.

* Fri Jul 29 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Initial build.


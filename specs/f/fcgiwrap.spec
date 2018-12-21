Summary: Simple FastCGI wrapper for CGI scripts
Name: fcgiwrap
Version: 1.1.0
Release: alt4
License: BSD-style
Group: System/Servers
URL: http://nginx.localdomain.pl/wiki/FcgiWrap
Source: %name-%version.tar
# git://github.com/gnosek/fcgiwrap.git
Patch0: %name-%version-alt.patch

# Automatically added by buildreq on Tue Oct 19 2010
BuildRequires: libfcgi-devel
BuildRequires(pre):rpm-build-ubt
BuildRequires: libsystemd-devel

%description
fcgiwrap  is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other  web  servers
that may need it).


%prep
%setup -q
%patch0 -p1


%build
autoreconf -fisv
%configure --with-systemd --with-systemdsystemunitdir=%_unitdir 
%make

%install
%makeinstall_std

%pre
%_sbindir/groupadd -r -f _webserver ||:
%_sbindir/useradd -r -g _webserver -G _webserver -d /dev/null -s /dev/null -n _fcgiwrap \
        2> /dev/null > /dev/null ||:

%files
%_sbindir/fcgiwrap
%_unitdir/*
%_man8dir/*

%changelog
* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt4
- fixed build with recent gcc

* Sat Aug 05 2017 Anton Farygin <rider@altlinux.ru> 1.1.0-alt3
- add systemd support

* Fri Apr 18 2014 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- updated from upstream git

* Tue Sep 17 2013 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Oct 19 2010 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- first build for Sisyphus

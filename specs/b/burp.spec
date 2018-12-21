Name:		burp
Version:	2.2.4
Release:	alt1.1

Summary:	Burp is a network-based backup and restore program
License:	GPL
Group:		Archiving/Backup
Url:		https://burp.grke.org/

# https://github.com/grke/burp.git master
Source:		%{name}-%{version}.tar

BuildRequires:  libtool
BuildRequires:  librsync-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  libncurses-devel
BuildRequires:  libacl-devel
BuildRequires:  libuthash-devel
BuildRequires:  libyajl-devel

BuildRequires: rpm-macros-intro-conflicts
%filter_from_requires /^\/usr\/local\/bin\/mail\.php$/d

%description
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.

%prep
%setup

%build
%autoreconf
%configure \
    --sysconfdir="%_sysconfdir/burp" \
    --disable-static \
    --with-tcp-wrappers

%make_build

%install
%makeinstall_std install-all
install -D -p -m 0755 .gear/burp.init %{buildroot}%{_initrddir}/burp-server
install -D -p -m 0644 .gear/burp.service %{buildroot}%{_unitdir}/burp-server.service
%__subst "s,password,#password,g" %{buildroot}%_sysconfdir/burp/clientconfdir/testclient
chmod go-rwx %{buildroot}%_sysconfdir/burp
chmod go-rwx %{buildroot}%_sysconfdir/burp/clientconfdir
chmod go-rwx %{buildroot}%_sysconfdir/burp/*.conf

%files
%doc %_docdir/%name/
%dir %_sysconfdir/burp
%config(noreplace) %_sysconfdir/burp/*.c*nf
%dir %_sysconfdir/burp/CA-client
%dir %_sysconfdir/burp/clientconfdir/
%config(noreplace) %_sysconfdir/burp/clientconfdir/testclient
%dir %_sysconfdir/burp/clientconfdir/incexc
%config(noreplace) %_sysconfdir/burp/clientconfdir/incexc/example
%{_initrddir}/burp-server
%{_unitdir}/burp-*.*
%dir %_datadir/%name/
%_datadir/%name/scripts/
%_bindir/vss_strip
%_sbindir/*
%_man8dir/*

%post
%post_service burp-server

%preun
%preun_service burp-server

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Vitaly Chikunov <vt@altlinux.org> 2.2.4-alt1
- Update to version 2.2.4

* Thu Apr 19 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt2
- Fix init script
- Secure permissions for configs that supposed to contain passwords

* Sun Apr 15 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt1
- Respec for 2.1.32
- Install init scripts

* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.24-alt1
- new version 2.1.24 (with rpmrb script)

* Wed Aug 10 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.44-alt1
- initial build for ALT Linux Sisyphus


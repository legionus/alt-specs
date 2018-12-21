Name: neomutt
Version: 20180716
Release: alt2

%define docdir %_docdir/%name-%version
%undefine _configure_gettext

Summary: A version of Mutt with added features

License: GPLv2+ and Public Domain
Group: Networking/Mail
Url: https://www.neomutt.org/

# https://github.com/neomutt/neomutt.git
Source: %name-%version.tar

BuildRequires: docbook-style-xsl xsltproc tcl elinks
BuildRequires: liblua5-devel libnotmuch-devel libdb4.8-devel
BuildRequires: libgpgme-devel libncursesw-devel libssl-devel libsasl2-devel libidn2-devel

Requires: mailcap

%description
Neomutt is a small but very powerful text based program for reading
and sending electronic mail under unix operating systems, including
support for color terminals, MIME, OpenPGP, and a threaded sorting
mode.

%prep
%setup -q -n %name-%version

%build
%configure \
                --disable-nls \
		--docdir=%docdir \
                --with-ui=ncurses  \
		--gpgme \
		--notmuch \
		--lua \
		--bdb \
		--ssl \
		--sasl \
		--disable-idn --idn2

%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/neomuttrc
%_bindir/neomutt
%_mandir/man?/*
%_libexecdir/neomutt*
%docdir

%changelog
* Mon Nov 26 2018 Vitaly Chikunov <vt@altlinux.ru> 20180716-alt2
- Switch from libidn to libidn2

* Wed Aug 29 2018 Vitaly Chikunov <vt@altlinux.org> 20180716-alt1
- NeoMutt release 20180716

* Wed Feb 21 2018 Vitaly Chikunov <vt at altlinux.org> 20180221-alt1
- initial build for ALT Linux Sisyphus

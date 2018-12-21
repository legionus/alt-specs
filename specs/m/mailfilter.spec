# unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: mailfilter
Version: 0.8.6
Release: alt1.1

Summary: A program that filters your incoming e-mail to help remove spam
License: GPLv2+
Group: Networking/Mail
Url: http://mailfilter.sourceforge.net/

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: flex gcc-c++ libssl-devel

%description
Mailfilter is very flexible utility for UNIX (-like) operating systems
to get rid of unwanted e-mail messages, before having to go through
the trouble of downloading them to the local computer. It offers
support for one or many POP accounts and is especially useful for
dialup connections via modem, ISDN, etc. Install Mailfilter if you'd
like to remove spam from your POP mail accounts.

%prep
%setup
%patch1 -p1
sed -n '/^3\./,/^4\./p' INSTALL | grep -v '^[34]\.' > doc/rcfile.example

%build
%add_optflags
%configure
%make_build

%install
%makeinstall_std
# COPYING as symlink
ln -sf %_licensedir/GPL-2 COPYING

%files
# docs
%doc contrib
%doc -d AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS
%doc doc/FAQ doc/rcfile.example doc/supported_servers

%_bindir/*
%_mandir/*/*

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.8.6-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.6-alt1
- Updated to upstream version 0.8.6.

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Fixed build

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2 with upstream fix for gcc-4.5.

* Sun Oct 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.8.1-alt2
- fixed FTBFS with GCC 4.3:
  + added patch from Debian (Debian BTS #455619)

* Sat Nov 03 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.8.1-alt1
- new version 0.8.1
- use macro for License tag (rpm-build-licenses package)

* Wed Mar 28 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.8-alt1
- new version 0.8
- added full url to Source tag
- formatted description
- updated BuildRequires
- running make with --no-print-directory and --silent options
- enabled _unpackaged_files_terminate_build

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Nov 08 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.7.2-alt1
- initial build for Sisyphus


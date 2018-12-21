Name: polipo
Version: 1.1.1
Release: alt2.1
Summary: Single-threaded non blocking HTTP proxy
License: %mit
Group: System/Servers
URL: http://www.pps.jussieu.fr/~jch/software/%name/
Source0: http://www.pps.jussieu.fr/~jch/software/files/%name/%name-%version.tar.bz2
Source1: %name.init
Source2: %name.service

# Automatically added by buildreq on Sat Sep 01 2007 (-bi)
BuildRequires: symlinks

BuildRequires: rpm-build-licenses
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Polipo is single-threaded, non blocking HTTP proxy. It listens to
requests for web pages from your browser and forwards them to web
servers, and forwards the servers' replies to your browser. In the
process, it optimises and cleans up the network traffic.


%prep
%setup


%build
%define _optlevel s
%add_optflags -fno-strict-aliasing
%make_build CDEBUGFLAGS="%optflags"


%install
%make_install TARGET=%buildroot PREFIX=%_prefix MANDIR=%_mandir INFODIR=%_infodir install
install -d -m 0755 %buildroot{{%_sysconfdir,%_cachedir}/%name,%_docdir/%name-%version}
touch %buildroot%_sysconfdir/%name/{config,forbidden}
bzip2 --best --stdout CHANGES > %buildroot%_docdir/%name-%version/CHANGES.bz2
install -m 0644 README %buildroot%_docdir/%name-%version/
ln -sf %buildroot{%_datadir/%name/www/doc,%_docdir/%name-%version/html}
symlinks -c %buildroot%_docdir/%name-%version
symlinks -cs %buildroot%_docdir/%name-%version
install -pD -m 0755 %SOURCE1 %buildroot%_initdir/%name

install -d %buildroot%_unitdir
install -p -m644 %SOURCE2 %buildroot%_unitdir/

%post
%post_service %name ||:


%preun
%preun_service %name ||:


%files
%_docdir/%name-%version/*
%_bindir/*
%_man1dir/*
%_infodir/*
%_datadir/%name
%dir %_cachedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/polipo-%version 
%_unitdir/*


%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2.1
- NMU: added BR: texinfo

* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added .service file (ALT #30188)

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for polipo
  * docdir-is-not-owned for polipo

* Thu Jan 10 2008 Led <led@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Oct 07 2007 Led <led@altlinux.ru> 1.0.3-alt1
- 1.0.3
- updated init script

* Sat Sep 01 2007 Led <led@altlinux.ru> 1.0.2-alt1
- added init script

* Sat Sep 01 2007 Led <led@altlinux.ru> 1.0.2-alt0.1
- initial build

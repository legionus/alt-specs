%def_enable guile

Name: xbindkeys
Version: 1.8.6
Release: alt2

Summary: Binds keys or mouse buttons to shell commands under X
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.nongnu.org/xbindkeys/xbindkeys.html
Source0: %name-%version.tar.gz

BuildPreReq: libX11-devel
%if_enabled guile
BuildPreReq: guile-devel
%endif

%description
xbindkeys is a program that allows you to launch shell commands with your
keyboard or mouse under X. It links commands to keys or mouse buttons using
a simple configuration file, and is independant of the window manager.

%prep
%setup

%build
# --enable-tk == install xbindkeys_show to %_bindir
# but we install it to %_docdir manually, so we need --disable-tk
%configure %{subst_enable guile} --disable-tk
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS BUGS ChangeLog README TODO xbindkeys_show*

%changelog
* Fri Nov 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.6-alt2
- rebuilt with guile22 (closes: 35682)

* Thu Feb 19 2015 Fr. Br. George <george@altlinux.ru> 1.8.6-alt1
- Autobuild version bump to 1.8.6

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.8.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec  7 2010 Terechkov Evgenii <evg@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Feb 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Fri Apr 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Thu Apr 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Feb 06 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.0-alt1.1
- rebuild

* Sun Jan 21 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.8.0-alt1
- 1.8.0
- enabled guile support

* Fri Jan 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Sun May 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Sun May 08 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.2-alt1
- 1.7.2
- %%ifdef'ed guile support, still disabled by default
- packaged xbindkeys_show and its manpage as %%doc

* Wed Dec 22 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.1-alt1
- built for Sisyphus

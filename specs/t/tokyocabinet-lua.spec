%def_disable check

%define bname tokyocabinet
Name: %bname-lua
Version: 1.8
Release: alt2.qa3
Summary: Lua binding to the Tokyo Cabinet
License: %lgpl2plus
Group: Development/Other
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Requires: libtokyocabinet >= 1.4.21
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: bzlib-devel lua-devel lua zlib-devel
BuildRequires: libtokyocabinet-devel >= 1.4.21

%description
Lua binding to the Tokyo Cabinet.


%package doc
Summary: Documentation for Lua binding to the Tokyo Cabinet
Group: Documentation
BuildArch: noarch

%description doc
Documentation for Lua binding to the Tokyo Cabinet.


%prep
%setup
%patch -p1


%build
%configure
%make_build
%{?_enable_check:%make check}


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot%_docdir/%name-%version/{html/modules,example}
install -m 0644 example/* %buildroot%_docdir/%name-%version/example/
install -m 0644 overview.html %buildroot%_docdir/%name-%version/
install -m 0644 doc/modules/* %buildroot%_docdir/%name-%version/html/modules/
install -m 0644 doc/*.{css,html} %buildroot%_docdir/%name-%version/html/

rm -f %buildroot%_bindir/*test.lua

%files
%_libdir/*/*/*.so

%files doc
%_docdir/%name-%version


%changelog
* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2.qa3
- NMU: fixed unpackaged files

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2.qa2
- rebuild with new lua

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.8-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 11 2009 Led <led@altlinux.ru> 1.8-alt2
- rebuild with libtokyocabinet.so.9

* Mon Jul 20 2009 Led <led@altlinux.ru> 1.8-alt1
- 1.8

* Sun May 31 2009 Led <led@altlinux.ru> 1.7-alt1
- 1.7

* Sun May 24 2009 Led <led@altlinux.ru> 1.6-alt1
- 1.6

* Sun Apr 26 2009 Led <led@altlinux.ru> 1.5-alt1
- 1.5

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.4-alt2
- rebuild with libtokyocabinet.so.8

* Mon Dec 22 2008 Led <led@altlinux.ru> 1.4-alt1
- initial build

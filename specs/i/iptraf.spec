Name: iptraf
Version: 3.0.0
Release: alt4.2

License: GPL
Url: http://iptraf.seul.org/
Summary: IPTraf - console-based network statistics utility for Linux
Summary(ru_RU.CP1251): IPTraf - ���������� ����������� ��������� ��� ����� ������� ���������� � Linux.
Group: Monitoring

Source: %name-%version.tar.gz
Patch1: %name-3.0.0-alt-makefile.patch
Patch2: iptraf-3.0.0-interface.patch
Patch3: iptraf-3.0.0-alt-glibc-2.16.patch

Provides: %name %name-doc

# Automatically added by buildreq on Fri Dec 26 2008 (-bi)
BuildRequires: docbook-utils libncurses-devel

%description
IPTraf is a console-based network statistics utility for Linux.
It gathers a variety of figures such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic breakdowns,
and LAN station packet and byte counts.

%description -l ru_RU.CP1251
IPTraf ��� ���������� ����������� ��������� ��� ����� ������� ���������� � Linux.
��� ���������� ������ ������������� ����������, ����� ��� ������ TCP-����������,
��������� ����, ������������ ������� ����������� � ���������� ����������,
����������� TCP/UDP-�������, ��������� ������� � ���� � LAN.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p2

%__subst -p "s/asm\/types.h/sys\/types.h/" src/*
%build
#make_build -C src DEBUG= CFLAGS="$RPM_OPT_FLAGS"
%make -C src
%make -C Documentation
%make -C support

%install
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__mkdir_p $RPM_BUILD_ROOT%_docdir/%name/manual/stylesheet-images
%__mkdir_p $RPM_BUILD_ROOT%_man8dir
%__mkdir_p $RPM_BUILD_ROOT%_localstatedir/%name
%__mkdir_p $RPM_BUILD_ROOT%_logdir/%name
%__mkdir_p $RPM_BUILD_ROOT/var/run/%name
%__install -p src/{%name,rawtime,rvnamed} $RPM_BUILD_ROOT%_bindir
%__install -p -m644 Documentation/*.8 $RPM_BUILD_ROOT%_man8dir
%__install -p -m644 CHANGES FAQ LICENSE README* RELEASE-NOTES $RPM_BUILD_ROOT%_docdir/%name
%__install -p -m644 Documentation/manual/manual.html $RPM_BUILD_ROOT%_docdir/%name/manual
%__install -p -m644 Documentation/manual/stylesheet-images/*.gif $RPM_BUILD_ROOT%_docdir/%name/manual/stylesheet-images

%files
%attr(750,root,root) %dir %_localstatedir/%name
%attr(750,root,root) %dir %_logdir/%name
%attr(750,root,root) %dir /var/run/%name
%dir %_docdir/%name
%_bindir/*
%_man8dir/*
%_docdir/%name/*

%changelog
* Fri Apr 27 2018 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt4.2
- Fix typo in changelog (Closes: #18924).

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt4.1
- Fixed build with glibc 2.16

* Sun Aug 02 2009 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt4
- fix spec

* Wed Feb 18 2009 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt3
- Fix type interfaces

* Fri Dec 26 2008 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt2
- Picked up from orphaned

* Thu Sep 22 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.0.0-alt1
- 3.0.0
- %name-doc and %name splitted back into one package

* Fri Apr 08 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.7.0-alt4
- Updated BuildRequires

* Thu Feb 26 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 2.7.0-alt3
- Updated spec - added build optimisation.

* Mon Jan 27 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 2.7.0-alt2
- Changed package name from %name-manuals to %name-doc
- Updated BuildRequires

* Tue Sep 17 2002 Aleksandr Blokhin <sass@altlinux.ru> 2.7.0-alt1
- Initial release.

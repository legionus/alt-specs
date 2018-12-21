Name: pwsafe
Version: 0.2.0
Release: alt2.1
Summary: A unix commandline program that manages encrypted password databases
Summary(ru_RU.KOI8-R): ���������� �� ��������� ������ ������������� ������ � ��������

Group: Databases
License: GPLv2+
Url: http://nsd.dyndns.org/pwsafe/
Source0: http://nsd.dyndns.org/pwsafe/releases/pwsafe-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Oct 07 2008
BuildRequires: gcc-c++ libXmu-devel libncurses-devel libreadline-devel libssl-devel

%description
pwsafe is a unix commandline program that manages encrypted password databases.
Compatible with CounterPane's PasswordSafe Win32 program versions 2.x and 1.x.

%description -l ru_RU.KOI8-R
pwafe -- �������, ����������� ��������� �� ��������� ������ ������������� ����� ������ � �ޣ����� ��������. ���������� � CounterPane PasswordSafe Win32 (������ 1.x � 2.x), PasswordGorilla � �. �. ��������� ���������� ������ � ����� ������ X11, �� ��������� ���.

%prep
%setup -q

%build
%configure \
    --disable-dependency-tracking
make %{?_smp_mflags}

%install
# Convert man page to UTF-8
iconv -f iso-8859-1 -t utf8 pwsafe.1 -o pwsafe.1.utf8
mv pwsafe.1.utf8 pwsafe.1
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README TODO
%_bindir/pwsafe
%_mandir/man1/pwsafe.*

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 0.2.0-alt2
- Fix build

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.0-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Oct 07 2008 Fr. Br. George <george@altlinux.ru> 0.2.0-alt1
- Initial build from FC

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.0-5
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.0-4
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Ralf Ertzinger <ralf@skytale.net> 0.2.0-3
- Rebuild against new openssl

* Tue Jul 31 2007 Ralf Ertzinger <ralf@skytale.net> 0.2.0-2
- Enable X11 functionality

* Sun Jul 08 2007 Ralf Ertzinger <ralf@skytale.net> 0.2.0-1
- Initial build for Fedora

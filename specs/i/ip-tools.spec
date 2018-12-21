Summary: Various ip-tools
Summary(ru_RU.CP1251): ��������� IP-�������
Name: ip-tools
Version: 0.1
Release: alt1.qa1
License: GPLv2
Group: Networking/Other
Source: %name-%version.tar.gz
Packager: Motsyo Gennadi <drool@altlinux.ru>

%description
This is a small collection of tools for converting
ip-addresses to host names and vice versa, especially
useful in ip-up and ip-down scripts.

%description -l ru_RU.CP1251
��������� ������� ��� ����������� ip-������ �
host-��� � ��������, �������� �������� � ip-up
� ip-down ��������

%prep
%setup -q -n %name

%build
%make_build CFLAGS="%optflags"

%install
%__install -Dp -m 0755 hn2ip %buildroot%_bindir/hn2ip
%__install -Dp -m 0755 ip2hn %buildroot%_bindir/ip2hn

%files
%doc README COPYING
%_bindir/*

%changelog
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Dec 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- build for Sisyphus
- cleanup spec

* Fri Apr 22 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.1.-alt1.drool
- build for ALT Linux 2.4 Master

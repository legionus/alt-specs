Name: mdmpd
Version: 0.4
Release: alt1.qa1

Summary: A daemon for monitor MD multipath devices
License: GPL
Group: System/Configuration/Hardware

Source0: %name-%version.tgz
Source1: %name.init
Patch: %name-0.4-alt-gcc4warnings.patch

Summary(ru_RU.KOI8-R): ������� �������������� RAID-���������

%description
The Linux kernel portion of the md (Multiple Devices) multipath driver
used for software RAID does not try and find out if a path that has previously
failed might be working again. That's what this daemon does. 
Then it reads the current state of the md raid arrays, saves that state,
and then waits for the kernel to tell it something interesting has happened. 
It then wakes up, checks to see if any paths on a multipath device have failed,
and if they have then it starts to poll the failed path once every 15 seconds
until it starts working again. Once it starts working again, the daemon
will then add the path back into the multipath md device it was originally
part of as a new spare path.

%description -l ru_RU.KOI8-R
������� md-���������, ������������ � ������� ��� ������ � ��������� ���������
(software RAID), � ������ ������ ������ �� ������ �� �������� ����������,
��� ���� ����� ��������������. ������� ������� %name ����������� ����� ����
� ���������� ���������� ���� �� ��� ������, ���� ��������� ����� ����������.
��������� ���, %name ��������� ���� ����� �������� ���� � ������ �������.

%prep
%setup -q -n %name
%patch -p1

%build
%make_build CCFLAGS="%optflags -I."

%install
%make_install install DESTDIR=%buildroot MANDIR=%_mandir BINDIR=%_sbindir
install -pD -m744 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%{name}*
%_mandir/man?/%{name}*
%_initdir/%name

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri May 19 2006 Ilya Evseev <evseev@altlinux.ru> 0.4-alt1
- updated to version 0.4, fixed gcc4.1 warnings

* Sun Mar 13 2005 Ilya Evseev <evseev@altlinux.ru> 0.3-alt2
- specfile: fixed russian encoding (declared KOI8-R, actually was CP1251)

* Mon Mar  7 2005 Ilya Evseev <evseev@altlinux.ru> 0.3-alt1
- Initial build for ALTLinux, sources are taken from mdadm-1.9.0-1mdk.src.rpm

## EOF ##

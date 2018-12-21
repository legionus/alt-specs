Name: ipfm
Version: 0.11.5
Release: alt1.qa1

Summary: IP Flow Meter - bandwidth analysis tool
License: GPL
Group: Monitoring
Url: http://robert.cheramy.net/%name
Source0: %url/archive/%name-%version.tgz
Source1: %name.service
Source2: %name.cron
Source3: %name.conf

%define crondir %_sysconfdir/cron.weekly

BuildPreReq: libpcap-devel, flex, byacc
#uildPreReq: %crondir

Summary(ru_RU.KOI8-R): IP Flow Meter - ���������� �������� ������� �����������

%description
ipfm is a bandwidth analysis tool that starts as system service and counts
how much data was send and received by specified hosts through an Internet link.
ipfm uses PCAP library in normal or promiscuous mode.

%description -l ru_RU.KOI8-R
IP Flow Meter ����������� � �������� ���������� ������� � ������������
���������� ����, �������� � ���������� �� ����. ����������� ������
��������������� �� IP-������� ����������� � � �������� ��������������
������������ � ��������� ����� � �������� %_logdir/%name.

IPFM �������� ������������ �������� ����� ��������� ��ޣ���
� ������� ��������� ������ � �������,������������� ��� ������������� �ޣ�������,
����������� ������������� IP-������� � ������������ ������, � �.�.
� ������������ IPFM ��������� ������������� ���������
��������� ������� ����������� ������������.

��� ��������� �������� �� ���� ������������ ������� IPFM ����������
���������� PCAP � ���������� ��� �.�. promiscuous ("��������������") ������,
� ������� ������������� ������, ���������� �� ������ ����� ��������� ���������,
�� � ����� ��� ��������� ���������� � ��� �� ���������� �������� ����.

%prep
%setup -q
%__subst s,@localstatedir@/log,%_logdir,g  Makefile.common.in
%__subst s,@localstatedir@/run,%_var/run,g Makefile.common.in
%configure

%build
%make_build

%install
%make ROOT=%buildroot install
install -pD       %SOURCE1 %buildroot%_initdir/%name
#nstall -pD       %SOURCE2 %buildroot%crondir/%name
install -pD -m600 %SOURCE3 %buildroot%_sysconfdir/%name.conf

%files
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_mandir/*/%name.*
%_logdir/%name
%exclude %_var/run
%_initdir/%name
#crondir/%name

%post                                                                                                                         
%post_service %name

%preun
%preun_service %name

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.11.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 16 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.11.5-alt1
- Initial build

## EOF ##

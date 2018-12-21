Name: ipband
Version: 0.8.1
Release: alt1

Summary: PCAP-based traffic monitor
License: GPL
Group: Monitoring
Url: http://%name.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %url/%name-%version.tgz
Source1: %name.service
Source2: %name.conf

BuildPreReq: libpcap-devel

Summary(ru_RU.KOI8-R): ������� �������� ������� �� ���� ���������� PCAP

%description
ipband is a pcap based IP traffic monitor. It listens to a network interface
in promiscuous mode, tallies per-subnet traffic and bandwidth usage and starts
detailed logging if specified threshold for the specific subnet is exceeded.

The utility could be handy in a limited bandwidth WAN environment (frame relay,
ISDN etc. circuits) to pinpoint offending traffic source if certain links
become saturated to the point where legitimate packets start getting dropped.

It also can be used to monitor internet connection when specifying the range
of local ip addresses (to avoid firing reports about non-local networks).

%description -l ru_RU.KOI8-R
IP Bandwidth Monitor ������� �������� ������� ���������� ����� ���������� PCAP,
������������ ��������� � �������� ����������� ������� ��� ��������� ��������,
� �������� ����� ��������� ��������, ���� ����������� ������� ��������
��������� ������̣���� ������.

� ���������� � �������� ����������� ������� ����������� IPBand ����� ��������
� �.�. promiscuous-������, ��� ������� ������������ ���� ������
� ������ ���������� �������� ��������� ����, � �� ������ ����������
��������������� ����� ������ ���������.

��������� IPBand ����� ����� ���������: �� ������� � ��� ��������� ������.
�� ������ ������ ������� ������� ���� �������� /etc/%name.conf
�� ���� ����ݣ����� ����� �������.

����������� �������� �������� � ���� IP-������, ����� � ����������
���������� ���� ��� ������� ���������� �� ������ ���������� �����������.
�������� ������������ � ���� �/��� ���������� �� ����� �� ��������� �����.

%prep
%setup -q

%build
%make_build

%install
%__install -pD -m700 %name             %buildroot%_prefix/sbin/%name
%__install -pD -m444 %name.8           %buildroot%_man8dir/%name.8
%__install -pD -m644 %name.sample.conf %buildroot%_sysconfdir/%name.sample.conf
%__install -pD -m700 %SOURCE1          %buildroot%_initdir/%name
%__install -pD -m600 %SOURCE2          %buildroot%_sysconfdir/%name.conf
%__install -pD -m644 /dev/null         %buildroot%_logdir/%name.log

%files
%_prefix/sbin/%name
%_man8dir/%name.8*
%_sysconfdir/%name.sample.conf
%_initdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%ghost %_logdir/%name.log

%post
%post_service %name
if [ ! -f %_sysconfdir/%name.conf ]; then
    echo "NOTE: Rename %_sysconfdir/%name.sample.conf to %_sysconfdir/%name.conf"
    echo "      and put here your own settings."
fi

%preun
%preun_service %name

%changelog
* Thu Sep 30 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon Jan 22 2007 Ilya G. Evseev <evseev@altlinux.ru> 0.8-alt1
- Updated to new version 0.8

* Sat Jul 16 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.7.2-alt1
- Initial build


Name:     snort-rules
Version:  2.9.6.1
Release:  alt1

Summary:  Rules for Snort, popular network intrusion detection system
License:  GPLv2
Group:    Security/Networking
Url:      http://www.snort.org

Source0:  community-rules.tar
Source2:  snort-mergesidmaps

BuildArch: noarch
Requires: snort-base

Summary(ru_RU.KOI8-R): ����������� ��������� ��� ������� ����������� ������� ��������� Snort

%define   myconfdir   %_sysconfdir/snort
%define   myrulesdir  %myconfdir/rules

%description
Rules for Snort, popular network intrusion detection system.
Standard pack distributed under GNU GPL license.

%description -l ru_RU.KOI8-R
����������� ����� ������, �������� ���������������� ��������������
������������ ������� ��������� Snort. ������� �������� � ���� �.�. ���������,
�.�. ������ �������, ������� ������ ��������������� ��������� � ����������
������� �������, ��������������� Snort'��, � ����� ������� �� ���������
������������ - �������� ������, ����������� �������������� � �.�.

%package -n snort-base
Summary: Create base directory structure for Snort NIDS configuration
Summary(ru_RU.KOI8-R): ����� ���������, ������������ ������� �������� IDS Snort
Group: Security/Networking
Conflicts: snort < 2.4
%description -n snort-base
Create base directory structure for Snort NIDS configuration files.
%description -n snort-base -l ru_RU.KOI8-R
������ �����, ��������� ��������, ��������� ������������ ���������� ��������,
�� ������� ������ ������������ ������� ���� (IDS) Snort.

#%package doc
#Summary: Detailed descriptions for standard rules used by Snort NIDS.
#Summary(ru_RU.KOI8-R): �������� ����������� �������� ��� ����������� �������� ������� Snort
#Group: Security/Networking
#%description doc
#Tons of detailed textual listings describing all network intrusions known by Snort.
#%description doc -l ru_RU.KOI8-R
#��������� ������������ �� ���������� ������� ����, �������� � ������� ��������
#�������� ��������� ������ Snort - ������� ����������� ������� ���������.

%prep
%setup -q

%build  #..nothing to do

%install
mkdir -p %buildroot{%myconfdir,%myrulesdir,%_bindir}
install -pm 644 *.rules %buildroot%myrulesdir
install -p %SOURCE2 %buildroot%_bindir
install -pm 644 *sid-msg.map %buildroot%myconfdir

#echo "Generate maps..."
#d=$PWD
#cd %buildroot%myconfdir
#%SOURCE2 $d/etc/*sid-msg.map
#cd -
#echo "...done!"

%files -n snort-base
%dir %myconfdir

%files
%_bindir/snort-*
%config(noreplace) %myrulesdir
%config(noreplace) %myconfdir/sid-msg.map

#%files doc
#%doc doc/signatures/* docs/*

%changelog
* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 2.9.6.1-alt1
- use only community rules

* Mon Jan 14 2013 Timur Aitov <timonbl4@altlinux.org> 2.9.3.1-alt1
- new version

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5-alt2
- use config(noreplace) for rules.

* Fri Oct 23 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5-alt1
- spec cleanup.
- rules from Debian package.

* Fri Jun 16 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt1
- updated to latest state (community rules are grown from 11k to 55k)

* Thu Nov 10 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.3-alt1
- update standard rules, added community rules
- added snort-mergesidmaps helper

* Fri Aug 12 2005 Ilya Evseev <evseev@altlinux.ru> 2.4-alt1
- initial tarball from upstream (previously rules were distributed
  in single tarball with Snort binaries) and initial package for ALTLinux
- snort-base package owns /etc/snort directory used by multiple packages

## EOF ##

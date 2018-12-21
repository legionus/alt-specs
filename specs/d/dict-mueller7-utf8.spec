%define dict_name	mueller7
%define dict_file       Mueller7GPL

Name: dict-%dict_name-utf8
Version: 1.2
Release: alt5

Summary: V.K. Mueller English-Russian Dictionary, 7 Edition: dict format
Summary(ru_RU.KOI8-R): �����-������� ������� �������, �������� 7: ������ dict
License: GPL
Group: Text tools
Url: http://www.chat.ru/~muller_dic/
BuildArchitectures: noarch

Source: %dict_file.tgz
Source1: to-dict.sh
Source2: mueller2utf8

PreReq: dictd >= 1.7.1
Obsoletes: %dict_name-dict
Obsoletes: dictd-%dict_name-utf8

BuildRequires: libltdl perl-Unicode-Map8 perl-Unicode-String dict-tools >= 1.9.1-alt2

%description 
Electronic version of V.K. Mueller English-Russian Dictionary, 7 Edition
in dict format and utf8 encoding. You can use it with your favourite dict client.

%description -l ru_RU.KOI8-R
����������� ������ �����-�������� ������� ������� 7-�� ��������
� ������� dict � ��������� utf8. �� ������ ������������ ��� �� ����� �������
dict ��������.

%prep
%setup -q -c

%build
cd usr/local/share/dict

export LANG=ru_RU.KOI8-R

cat %dict_file.koi | sed 's/�  ��. et cetera � ������/� ��.  et cetera � ������/' | 
perl -e "use locale;" -pne 's/\b����\./_����./g; s/\b��\./_��./g; 
s/\b��\./_��./g; s/\b� ��\./_�_��./g; s/\b�����\./_�����./g; 
s/\b��\./_��./g; s/\b����\./_����./g; s/\b�����\./_�����./g;
s/\b�����\./_�����./g; s/\b�����\./_�����./g; s/\b���\./_.���/g;
s/\b��\./_��./g; s/\b�����\./_�����./g; s/\b����\./_����./g; ' > %dict_file.fixed

export DICTFMT_OPT="--locale ru_RU.UTF-8"
export LANG=C
/bin/sh %SOURCE1 --src-data %dict_file.fixed %dict_name.koi # && rm -f %dict_file.koi %dict_file.fixed
%SOURCE2 %dict_name.koi > %dict_name.data

/bin/sh %SOURCE1 --data-dict %dict_name.data %dict_name && rm -f %dict_name.data
/bin/sh %SOURCE1 --expand-index %dict_name.index %dict_name.index.exp
cd ../../../..

%install
install -p -m644 -D usr/local/share/dict/%dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.dict.dz
install -p -m644 -D usr/local/share/dict/%dict_name.index.exp $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.index


%files 
%_datadir/dictd/*

%changelog
* Wed Feb 04 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt5
- removed post/un in favor of filetrigger

* Thu Jan 29 2004 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt4
- fix error in spec file
- syntax fixes in dict file
- update build requires
- copyright info in mueller2utf8 script added

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt3
- fix bug #0001703: preuninstall script turns dictd off
- build with standard dictfmt and locale ru_RU.UTF-8

* Mon Oct 14 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt2
- rename to dict-mueller7-utf8
- add missing PreReq: dictd

* Fri Sep 20 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt1
- Translation to UTF-8 encoding.
- initial revision
- spec based on mueller7-mova package

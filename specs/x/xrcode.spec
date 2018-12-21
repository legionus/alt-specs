%define _unpackaged_files_terminate_build 1

Name: xrcode
Version: 1.0
Release: alt4

Url: ftp://oskin.macomnet.ru/pub/linux/misc
License: GPL
Group: Text tools

# xcode.c and rcode.tar.gz; patched here
Source: %name-%version.tar
Patch: xcode-gcc41.patch

Summary: Xcode and recode for recoding files between cyrillic codepages
Summary(ru_RU.KOI8-R): Xcode � recode ��� ��������������� ������� � ������������� ����������
Summary(uk_UA.KOI8-U): Xcode �� recode ��� ������������� ����Ԧ� � ���������� ����������

%description
rcode - Text recoder (Koi8<->Alternative<->Windows<->ISO).
        And from HEX-style ("=EF=F0") to normal,
        and from HTML-style ("&...;") to normal.
        Made by Serge Bajin (bsv/cntc.dubna.su).

xcode - This program tries to determine input document encoding
        and to convert it to koi8, CP-1251 or cp866.
        Written  by Andrey V. Lukyanov on May 14, 1997
        Last modified on May 18, 1997

These tools modified by Serhii Hlodin (hlodin/lutsk.bank.gov.ua) for
CP1125 codepage support (also known as modified CP866 for Ukraine)

%description -l ru_RU.KOI8-R
rcode - ��������� ������ (Koi8<->Alternative<->Windows<->ISO).
        ����� �� HEX ("=EF=F0") � HTML entities ("&...;").
	�����: Serge Bajin (bsv/cntc.dubna.su).

xcode - ��������� � ���������������� ��������� ������ � �����������
        ��������������� � koi8, CP-1251 ��� cp866.
	�����: Andrey V. Lukyanov 14 ��� 1997 �.
	��������� ���������: 18 ��� 1997 �.

%description -l uk_UA.KOI8-U
rcode - ��������� ������ (Koi8<->Alternative<->Windows<->ISO).
        ����� � HEX ("=EF=F0") � HTML entities ("&...;").
	�����: Serge Bajin (bsv/cntc.dubna.su).

xcode - ��������� � ��������������� ��������� ������ � ���������
	������������� � koi8, CP-1251 ��� cp866.
	�����: Andrey V. Lukyanov 14 ������ 1997 �.
	�����Φ �ͦ��: 18 ������ 1997 �. 

%prep
%setup
%patch

%build
%add_optflags -fgnu89-inline
%make CFLAGS="%optflags"

%install
install -pD -m755 xcode %buildroot%_bindir/xcode
install -m755 recode %buildroot%_bindir/rcode

%files
%_bindir/*

# TODO: In function `main': the use of `tmpnam' is dangerous, better use `mkstemp'

%changelog
* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt4
- NMU: fixed build with new toolchain.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt3.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixed build with gcc4 (thanks vsu@, gns@ and morozov@ for advice)
- minor spec cleanup

* Wed Aug 04 2004 Michael Shigorin <mike@altlinux.ru> 1.0-alt2
- added Url:
- minor spec cleanup

* Mon May 26 2003 Michael Shigorin <mike@altlinux.ru> 1.0-alt1
- built for ALT Linux

* Fri Jul 12 2002 Serhii Hlodin <hlodin@hlodin.lutsk.bank.gov.ua>
- Renamed recode to rcode

* Tue Apr 23 2002 Serhii Hlodin <hlodin@lutsk.bank.gov.ua>
- Initial build.


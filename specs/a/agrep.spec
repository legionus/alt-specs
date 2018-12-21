Name: agrep
Version: 2.04
Release: alt1.qa2

Summary: Approximate grep
License: distributable not for profit, free use
Group: Text tools
URL: http://webglimpse.net

# NB: we have permission to redistribute agrep package
# with boxed distributions -- mike

Source0: ftp://ftp.cs.arizona.edu/agrep/%name-%version.tar.Z
Source1: %name-README.ALT

Summary(ru_RU.KOI8-R): "��������" grep
Summary(uk_UA.KOI8-U): "��ަ����" grep
Summary(pl): Wersja grep dopuszczaj�ca b��dy

%description
Tool for fast text searching allowing errors. It's similar to egrep
(or grep or fgrep), but it is much more general and usually faster.

%description -l ru_RU.KOI8-R
������� ��������� grep, ����������� ��������� ����� �� ������� ���������
�������, ����������� ������������� ������� ���������.

%description -l uk_UA.KOI8-U
���̦�� �� ������ grep, �� ������Ѥ ���������� ����� �� ��ަ��� �������
��������, �� ���� �����դ ���������, ���� ���Ҧ���.

%description -l pl
agrep jest narz�dziem podobnym do grep, ale umo�liwia przeszukiwanie
przybli�one.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
install -pD -m755 agrep %buildroot%_bindir/agrep
install -pD -m644 agrep.1 %buildroot%_man1dir/agrep.1
install -pD -m644 %SOURCE1 $RPM_BUILD_DIR/%name-%version/README.ALT

%files
%doc COPYRIGHT README agrep.algorithms agrep.chronicle contribution.list
%doc README.ALT
%_bindir/*
%_mandir/man1/*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* Sun Feb 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1.qa2
- added URL: http://webglimpse.net (for distromap)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.04-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jun 08 2003 Michael Shigorin <mike@altlinux.ru> 2.04-alt1
- built for ALT Linux
- based on PLD spec; 
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  qboosh
  - which was in turn taken from some -contrib
  - based on spec by W.L.Estes <wlestes@hamlet.uncg.edu>
    and Peter Soos <sp@osb.hu>


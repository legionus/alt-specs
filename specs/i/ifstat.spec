Name: ifstat
Version: 1.1
Release: alt1.qa1

Summary: InterFace STATistics
License: GPL
Group: Monitoring

Url: http://gael.roualland.free.fr/ifstat
Source: %url/%name-%version.tar.gz
Patch0: ifstat-DESTDIR.patch
Patch1: ifstat-1.1-alt-proctest.patch

Summary(ru_RU.KOI8-R): ���������� ������� �����������
Summary(uk_UA.KOI8-U): ���������� ��������� ��������Ӧ�
Summary(pl): Program do zbierania statystyk ruchu na interfejsach sieciowych

%description
ifstat(1) is a little tool to report interface activity like
vmstat/iostat do.

%description -l ru_RU.KOI8-R
ifstat(1) -- ��������� ������� ��� ���������� �� ����������� ��
������� ����������� �� ����� vmstat/iostat.

%description -l uk_UA.KOI8-U
ifstat(1) -- ��������� ���̦�� ��� ������Ҧ����� �� �����Φ��� ��
��������� ����������� �� ������ vmstat/iostat.

%description -l pl
ifstat(1) jest ma�ym narz�dziem, kt�re s�u�y do pobierania informacji
o ruchu na interfejsach sieciowych podobnie do narz�dzi vmstat/iostat.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
unset CC CXX
%configure --with-proc=/proc/net/dev
%make_build

%install
%makeinstall

%files
%doc README TODO HISTORY
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Jan 03 2004 Michael Shigorin <mike@altlinux.ru> 1.1-alt1
- built for ALT Linux
- based on PLD spec 1.0-2 by <kloczek at pld.org.pl> (which is based on spec
  by Werner Bosse <wbosse at berlin.snafu.de>)
- dropped SNMP support (until someone needs and requests that)
- patched around /proc check that fails within hasher

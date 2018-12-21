Name: frox
Version: 0.7.18
Release: alt1

Summary: This is frox, a transparent ftp proxy
Summary(ru_RU.KOI8-R): Frox - ���������� ftp-������ ������.
Summary(ru_RU.CP1251): Frox - ���������� ftp-������ ������.

License: GPL
Group: System/Servers
Url: http://frox.sourceforge.net

Packager: Anton Korbin <ahtoh@altlinux.ru>

BuildArchitectures:i586

Source: %name-%version.tar.bz2
Source1: frox.initd

Patch1: frox.conf.patch

%description
Frox  is a transparent ftp proxy. It also has support for non-transpar-
ent connections, caching of anonymous ftp, and active --> passive  con-
version of data connections.
%description -l ru_RU.KOI8-R
Frox - ��� ���������� ftp-������ ������. �� ����� ������������ �� ����������
�������������, ��������� ���������� ������, ��� � ������� ������ ����, ��� � �����
������ ������ �������, �������� ����� squid. ����� ��������, ��� � ��������,
��� � ��������� ������ ����������. ��������� ��������� ������ �� ������� �������,
����� ������� ������������ ���������.
%description -l ru_RU.CP1251
Frox - ��� ���������� ftp-������ ������. �� ����� ������������ �� ����������
�������������, ��������� ���������� ������, ��� � ������� ������ ����, ��� � �����
������ ������ �������, �������� ����� squid. ����� ��������, ��� � ��������,
��� � ��������� ������ ����������. ��������� ��������� ������ �� ������� �������,
����� ������� ������������ ���������.

%prep
%setup -q
%patch1

%build
%configure --enable-http-cache --enable-local-cache --enable-virus-scan \
--enable-configfile=/etc/frox.conf --enable-run-as-root --enable-debug
%make_build

%install
%makeinstall
%__mkdir_p %buildroot%_man5dir
%__mkdir_p %buildroot%_man8dir
%__mkdir_p %buildroot%_docdir/%name-%version/
%__mkdir_p %buildroot%_initdir
%__mkdir_p %buildroot/var/lib/%name
%__mkdir_p %buildroot/var/log/%name
%__cp doc/* %buildroot%_docdir/%name-%version/
%__rm %buildroot%_docdir/%name-%version/{Makefile*,*.sgml,*.man}
%__cp {README,COPYING,BUGS} %buildroot%_docdir/%name-%version/
%__install doc/frox.conf.man %buildroot%_man5dir/frox.conf.5
%__install doc/frox.man %buildroot%_man8dir/frox.8
%__install -m755 %{SOURCE1} %buildroot%_initdir/frox
%__cp src/frox.conf %buildroot%_sysconfdir/frox.conf

%files
%_sbindir/*
%_initdir/*
%_man5dir/*
%_man8dir/*
%_docdir/%name-%version/
/var/lib/%name
/var/log/%name
%config(noreplace)%attr(0600,root,root)%_sysconfdir/frox.conf

%post
%post_service frox

%changelog
* Sun Apr 10 2005 Anton Korbin <ahtoh@altlinux.ru> 0.7.18-alt1
- Fix for incorrect parsing of Deny ACLs and more...
* Sun Dec 12 2004 Anton Korbin <ahtoh@altlinux.ru> 0.7.17-alt1
- Fix for initialisation error when called with no arguments and more...
* Sat Sep 04 2004 Anton Korbin <ahtoh@altlinux.ru> 0.7.15-alt1
- Allow ACLs and config file subsections to be matched on username, add SSL/TLS AUTH support and more
* Fri May 07 2004 Anton Korbin <ahtoh@altlinux.ru> 0.7.14-alt1
- First build for ALTLinux Sisyphus

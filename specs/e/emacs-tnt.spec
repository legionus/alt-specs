Version: 2.5
Release: alt1
Name: emacs-tnt
License: GPL
Group: Editors
Summary: Emacs client for AIM
Summary(ru_RU.KOI8-R): ������ AIM ��� Emacs
Requires: emacs-common emacsen-startscripts gnus
Url: http://tnt.sourceforge.net

Source: tnt-%version.tar.gz
Source1: emacs-tnt-site-start.el

# Automatically added by buildreq on Tue Jun 17 2003
BuildRequires: emacs-common

%description
TNT is an Emacs client for AIM, AOL's free instant messaging service.
Using TNT, you can, from the comfort of your Emacs window, check
whether friends and coworkers are online, send them "instant
messages", and join them in multi-party private chat sessions.

%description -l ru_RU.KOI8-R
TNT -- ������ AIM (��������� ������ ��������� AOL) ��� Emacs. ��������� TNT
�� ������ �� ���� Emacs, ��������� �� ����� �� ���� ������ � �������,
�������� �� ��������� � �������������� � ��� � ���������������������
���������.

%prep
%setup -n tnt-%version

%build
make clean
make

%install
mkdir -p %buildroot/%_emacslispdir/tnt/
install -m 644 *.el* %buildroot/%_emacslispdir/tnt/
mkdir -p %buildroot/%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot/%_sysconfdir/emacs/site-start.d/tnt.el

%files
%doc README PROTOCOL INSTALL
%_emacslispdir/*
%_sysconfdir/emacs/site-start.d/*

%changelog
* Wed May 12 2004 Ott Alex <ott@altlinux.ru> 2.5-alt1
- New version

* Tue Jun 17 2003 Ott Alex <ott@altlinux.ru> 2.4-alt2
- Initial release

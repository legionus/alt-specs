%define Name DeskMenu
Name: deskmenu
Version: 1.4.5
Release: alt1
Summary: Root menu program for Window Manager
Summary(uk_UA.CP1251): ������� ���� ��� �������� ���������
Summary(ru_RU.CP1251): ������� ���� ��� �������� ���������
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source0: %{name}_%version.tar.bz2
Source1: %name.menu-method.gz

# Automatically added by buildreq on Fri Jun 16 2006
BuildRequires: fontconfig libgtk+2-devel
BuildRequires: libXext-devel libXt-devel xorg-cf-files

%description
%Name is a root menu program for Window Manager which is activated
by clicking the root window.

%description -l uk_UA.CP1251
%Name - ������� ���� ��� �������� ���������, ����������� �����
������� �����.

%description -l ru_RU.CP1251
%Name - ������� ���� ��� �������� ���������, ���������������� ������
������� �����.


%prep
%setup -n %name-%version
subst 's/\r//g' README


%build
%autoreconf
%configure \
	--with-x
%make_build


%install
%makeinstall_std
install -d -m 0755 %buildroot%_sysconfdir/menu-methods
gzip -dc -- %SOURCE1 > %buildroot%_sysconfdir/menu-methods/%name
chmod 755 %buildroot%_sysconfdir/menu-methods/%name
gzip --best --stdout > changelog.gz


%files
%doc AUTHORS README example_rc changelog.* debian/README.Debian
%doc ChangeLog NEWS TODO
%_bindir/%name
%_man1dir/*
%_sysconfdir/menu-methods/*


%changelog
* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1
- Version 1.4.5

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.2-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for deskmenu

* Fri Jun 16 2006 Led <led@altlinux.ru> 1.4.2-alt1
- initial build

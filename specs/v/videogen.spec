Name: videogen
Version: 0.33
Release: alt1.qa1

# 0.16-ipl4 somehow got its serial, so we have to bear with that
Serial: 2

Summary: Modelines Generator
License: GPL
Group: System/Configuration/Other

Url: http://www.dynaweb.hu/opensource/videogen
Source: %name-%version.tar.gz

Summary(ru_RU.KOI8-R): ��������� ������������
Summary(uk_UA.KOI8-U): ��������� צ�������ͦ�

%description
Generates Modelines for the user specified hardware optimized
to the highest possible screen update frequency at a given
resolution.  Can be utilized via both interactive interface
and command line.  Using videogen together with XF86Setup and
xvidtune you can get out all performance your display card
and monitor provides. Now with kernel framebuffer support.

%description -l ru_RU.KOI8-R
���������� modelines ��� ���������� ������������� �����������
����������� ��� ���������� ���������� ��������� �������
���������� ������ ��� ��������� ����������.  ����� ��������������
��� � ������������� �����������, ��� � �� ��������� ������.
������ � XF86Setup � xvidtune ������ ��� �� ������ "������" :-)
����� ������������ framebuffer.

%description -l uk_UA.KOI8-U
�����դ modelines ��� ��������� ������������ ����������
������������ ��� ���������� ���¦���ϧ ������ϧ �������
���������� ������ ��� �����Φ� ���Ħ��Φ� �������Ԧ.
���� ����������������� �� � ������������� �����������,
��� � � ���������� �����.
�� XF86Setup �� xvidtune ������� ��� � ������ "��̦��" :-)
����� Ц�����դ framebuffer.

%prep
%setup

%build
%make_build CC="gcc %optflags"

%install
install -pD %name %buildroot%_x11bindir/%name
install -pD %name.1x %buildroot%_x11mandir/man1/%name.1x

%files
%_x11bindir/*
%_x11mandir/man1/*
%doc README CHANGES BUGS THANKS videogen.conf.sample

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2:0.33-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Sep 10 2010 Michael Shigorin <mike@altlinux.org> 2:0.33-alt1
- 0.33

* Mon Dec 02 2002 Michael Shigorin <mike@altlinux.ru> 2:0.32-alt1
- 0.32 (NVidia support)
- patch1 not applicable
- spec cleanup

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.16-ipl4
- Rebuilt in new environment.

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1:0.16-ipl3
- rebuild

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 0.16-ipl2
- Fixed group tag.

* Mon Oct 30 2000 Dmitry V. Levin <ldv@fandra.org> 0.16-ipl1
- RE adaptions.

* Thu Oct 28 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Tue Sep 14 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.

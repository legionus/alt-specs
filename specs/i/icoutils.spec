Name: icoutils
Version: 0.29.1
Release: alt1.1

Summary: Utility for extracting and converting Microsoft icon and cursor files
Summary(ru_RU.KOI8-R): ������� ��� ���������� � �������������� ������ Microsoft ���������� � ��������
License: GPL
Group: Graphics

Url: http://www.nongnu.org/icoutils/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://savannah.nongnu.org/download/icoutils/%name-%version.tar.bz2

# Automatically added by buildreq on Tue Jul 12 2005 (-bi)
BuildRequires: gcc-c++ libpng-devel libstdc++-devel perl-Term-ReadLine-Gnu perl-libwww zlib-devel

%package extra
Summary: Additional tools designed to work with icoutils
Summary(ru_RU.KOI8-R): �������������� ����������� ��� ������ � icoutils
Group: Graphics

Requires: %name = %version-%release

%description
The icoutils are a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the extension
.ico or .cur, but they can also be embedded in executables or libraries
(.dll-files).

%description -l ru_RU.KOI8-R
icoutils - ����� �������� ��� ���������� � �������������� ����������� ��/�
����� Microsoft Windows ���������� � ��������. ��� ����� ������ �����
���������� .ico ��� .cur, � ����� ����� ���� �������� � ����������� �����
��� ���������� (.dll-�����).

%description extra
The icoutils are a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the extension
.ico or .cur, but they can also be embedded in executables or libraries
(.dll-files).

This package contains extresso(1) and genresscript(1) with some examples of
their usage.

%description -l ru_RU.KOI8-R extra
icoutils - ����� �������� ��� ���������� � �������������� ����������� ��/�
����� Microsoft Windows ���������� � ��������. ��� ����� ������ �����
���������� .ico ��� .cur, � ����� ����� ���� �������� � ����������� �����
��� ���������� (.dll-�����).

���� ����� �������� extresso(1) � genresscript(1) � ����������� ��������� ��
�������������.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc README AUTHORS COPYING ChangeLog NEWS TODO
%_bindir/icotool
%_bindir/wrestool

%_man1dir/icotool.1*
%_man1dir/wrestool.1*

%files extra
%doc data/resscripts/*
%_bindir/extresso
%_bindir/genresscript

%_man1dir/extresso.1.*
%_man1dir/genresscript.1.*

%changelog
* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29.1-alt1.1
- Rebuilt with libpng15

* Mon Sep 27 2010 Ilya Mashkin <oddity@altlinux.ru> 0.29.1-alt1
- 0.29.1

* Wed Jul 13 2005 Andrei Bulava <abulava@altlinux.ru> 0.26.0-alt1
- 0.26.0
- fixed URLs in spec
- removed alt-extresso_makefile.patch (fixed in upstream),
  alt-extresso_am_makefile.patch for developers is no longer needed too

* Thu Aug 19 2004 Andrei Bulava <abulava@altlinux.ru> 0.23.0-alt1
- 0.23.0
- regenerated patch0
- added patch100 to regenerate patch0 on demand (it's for developers only
  to avoid dependency on autotools)
- added Russian summary and description

* Mon Mar 15 2004 Andrei Bulava <abulava@altlinux.ru> 0.22.0-alt1
- initial build for ALT Linux


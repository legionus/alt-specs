Name: cuneiform
Version: 1.1.0
Release: alt4

Summary: Cuneiform is an OCR system originally developed and open sourced by Cognitive technologies.
Summary(ru_RU.KOI8-R): ��������� ������������� �������� (OCR) Cuneiform, Linux-������

License: BSD-style
Group: Graphics
Url: https://launchpad.net/cuneiform-linux

Source: http://launchpad.net/%name-linux/%version/%version/+download/%name-linux-%version.tar.bz2
Patch: cuneiform-1.1.0-minmax.patch
Patch1: cuneiform-1.1.0-types.patch

Requires: %name-data
BuildRequires: gcc-c++ libImageMagick-devel cmake

%description
Cuneiform is an OCR system originally developed and open sourced by
Cognitive technologies. This project aims to create a fully portable
version of Cuneiform.

%description -l ru_RU.KOI8-R
��������� ������������� �������� (OCR) Cuneiform, ������� �����
���������� � ����� ������, ���� �������� ��������� Cognitive
Technologies � ��������� ������ � 2008 ����. ������ cuneiform-linux
������ ����� ����� ������ ������������ � ���������� �������� Cuneiform
��� Linux � ������ ������������ �������.

%package data
Summary: Language support and other data files required for Cuneiform OCR
Summary(ru_RU.KOI8-R): ��������� ��������� ������ � ������ ����� � ������� ��� OCR Cuneiform
Group: Graphics
BuildArch: noarch

%description data
Language support and other data files required for Cuneiform OCR

%description -l ru_RU.KOI8-R data
��������� ��������� ������ � ������ ����� � ������� ��� OCR Cuneiform

%prep
%setup -n %name-linux-%version
%patch -p1
%patch1 -p1

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%_prefix
%make_build

%install
cd build
%make preinstall
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix -P cmake_install.cmake

%files
%_bindir/%name
%_libdir/*.so*
%_includedir/%name.h

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Tue Oct 02 2018 Fr. Br. George <george@altlinux.ru> 1.1.0-alt4
- Version up

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt4
- Rebuilt for ImageMagick

* Thu Jan 19 2017 Fr. Br. George <george@altlinux.ru> 1.0-alt3.qa2
- Rebuilt for gcc6

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0-alt3.qa1
- Rebuilt for gcc5 C++11 ABI.

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 1.0-alt3
- Rebuild with new libImageMagick

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.0-alt2.1
- Rebuild with new libImageMagick

* Mon Feb 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2
- Closes bug: #21335
- fix debuginfo.req errors
- remove circular dependencies on cuneiform-data 

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.0-alt1.1
- Rebuild with new libImageMagick

* Fri Jul 16 2010 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- upstream version 1.0
- remove broken libidl patch

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1.1
- Rebuilt with libMagick++.so.2.

* Tue Mar 03 2009 Sergey Alembekov <rt@altlinux.ru> 0.6-alt1
- new upstream version

* Tue Dec 16 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1.1
- add forgotten libidl patch
- add cuneiform-data to requires

* Mon Dec 15 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1
- New 0.5 version build

* Sat Aug 16 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from scratch
- Thanks thresh@ for libdl hint


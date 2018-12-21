#
# spec file for package SASM
#
# Copyright (c)   2013 Dmitriy Manushin
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the GPL Licens v3e). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/Dman95/SASM
#

Name: sasm
Url: http://dman95.github.io/SASM/
Version: 3.7.0
Release: alt1
Summary: Simple crossplatform IDE for NASM, MASM, GAS, FASM assembly languages
License: GPL-3.0+
Group: Development/Other
source: v%version.tar.gz

Summary: Simple IDE for NASM, MASM, GAS, FASM assembly languages
Obsoletes: SASM < %version
Provides: SASM = %version-%release

# Automatically added by buildreq on Wed Feb 08 2017
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libstdc++-devel phonon-devel python-base
BuildRequires: gcc-c++ libqt4-webkit-devel

%description
Simple crossplatform IDE for NASM, MASM, GAS, FASM assembly languages

%prep
%setup -n SASM-%version
rm -f Linux/bin/*

%build
qmake-qt4 SASM.pro PREFIX=%buildroot/usr

%make_build

%install
%makeinstall

%files
%doc README* *html
%_bindir/*
%_datadir/%name
%_desktopdir/*

%changelog
* Wed Feb 08 2017 Fr. Br. George <george@altlinux.ru> 3.7.0-alt1
- Initial build for ALT

* Sun Oct 30 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.7.0
- Update - Chinese and German languages have been added, bugs with single application crashes and unprintable characters in output have been fixed.
* Sun Sep 25 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.6.0
- Update - Turkish language has been added, tab key action has been improved.
* Fri Aug 26 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.5.1
- Update - drag & drop bug, debugging bug and some small bugs have been fixed.
* Sat Mar 19 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.5.0
- Update - GoLink linker support, bug with wrong file names when saving and opening has been fixed.
* Thu Feb 11 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.4.0
- Update - ability to change line number font color, ability to switch off debug string insertion.
* Wed Jan 27 2016 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.3.0
- Update - single window, drag and drop for opening files, improved help, some bugs fixes.
* Sun Jun 14 2015 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.2.0
- Update - ability to build programs without running linker, new FASM 1.71.39, fix of some debug problems.
* Wed May 27 2015 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.1.4
- Update - fix of localized systems debug problem.
* Mon Mar 30 2015 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.1.3
- Update - showing description of received signal has been added.
* Fri Mar 27 2015 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.1.2
- Update - debugging files with include has been improved.
* Tue Mar 24 2015 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.1.1
- Update - bugs with hilighter have been fixed.
* Fri Aug 29 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.1.0
- Update - changes from pull requsts and issues - movable tabs, warning message for wrong assembler or linker executable, improve indent operation, noexecstack option for binaries.
* Thu Jul 24 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.0.1
- Update - additional registers view in debugger has been added.
* Sun Jul 13 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 3.0.0
- Update - new assemblers have been added: now NASM, GAS, MASM, FASM are supported, including syntax highlighting, debugging, and x86/x64 modes. Added ability to choose your own assembler or linker filling path to them. Many debugging improvements. Folder for include files. Many bugs have been fixed.
* Wed Apr 24 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 2.3.1
- Update - bug with spaces in path fixed
* Thu Apr 3 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 2.3.0
- Update - x64 feature added, many bugs fixed
* Thu Feb 13 2014 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 2.2.0
- Update - many functions added and bugs fixed
* Wed Nov 13 2013 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 2.1.0
- Update - many functions added and bugs fixed
* Tue Sep 3 2013 Dmitriy "Dman95" Manushin <Dman1095@gmail.com> 2.0.0
- Initial Release

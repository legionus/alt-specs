Name: jam
Version: 2.6
Release: alt1

Summary: Jam is a powerful and highly customizable utility to build programs.
License: GPL
Group: Development/C
Url: http://www.perforce.com

Source: %name-%version.tar.bz2

BuildRequires(pre): rpm-macros-make

Conflicts: boost-jam

%description
Jam is a make(1) replacement that makes building simple things
simple and building complicated things manageable.

%prep 
%setup -n %name

%build
%make_ext

%install
mkdir -p %buildroot%_bindir

./jam0 -sBINDIR=%buildroot%_bindir -sCCFLAGS=-g -sOPTIM=-O2 install

%files
%doc README RELNOTES Porting *.html
%_bindir/jam

%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.5-alt1
- Initial build for Sisyphus.


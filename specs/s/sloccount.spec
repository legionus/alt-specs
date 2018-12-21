Name: sloccount
Version: 2.26
Release: alt2

Summary: Measures source lines of code (SLOC) in programs
License: GPL
Group: Development/Other

URL: http://www.dwheeler.com/sloccount
Source: %url/sloccount-%version.tar.gz
Patch: %name-fix_brackets_for_perl5.26.patch

# Automatically added by buildreq on Thu Jun 07 2007
BuildRequires: flex

%description
SLOCCount is a suite of programs for counting physical source lines of
code (SLOC) in possibly large software systems. It can count physical
SLOC for a wide number of languages. It can take a large set of files
and automatically categorize their types using a number of different
heuristics, and also comes with analysis tools.

%prep
%setup
%patch -p2

%build
make CC="gcc %optflags"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
make install_programs PREFIX=%buildroot%_prefix
make install_man PREFIX=%buildroot%_prefix

%files
%_bindir/*
%_man1dir/*
%doc sloccount.html ChangeLog

%changelog
* Tue Apr 03 2018 Grigory Ustinov <grenka@altlinux.org> 2.26-alt2
- Add patch for building with perl 5.26.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.26-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jun 07 2007 Victor Forsyuk <force@altlinux.org> 2.26-alt1
- 2.26

* Fri Jan 31 2003 Dmitry Malenko <maldim@altlinux.ru> 2.17-alt2
- Spec cleanup

* Mon Dec 02 2002 Dmitry Malenko <maldim@altlinux.ru> 2.17-alt1
- New version

* Wed Aug 14 2002 Dmitry Malenko <maldim@altlinux.ru> 2.13-alt2
- Fixed group

* Fri Aug 09 2002 Dmitry Malenko <maldim@altlinux.ru> 2.13-alt1
- Packaged for ALT

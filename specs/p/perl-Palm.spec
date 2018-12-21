%define _unpackaged_files_terminate_build 1
Name: perl-Palm
Version: 1.400
Release: alt1

Summary: A set of modules for manupulating PalmOS databases
Summary(ru_RU.UTF-8): Набор модулей для работы с базами данных PalmOS
Group: Development/Perl
License: Artistic

URL: http://search.cpan.org/dist/Palm/
Source: http://www.cpan.org/authors/id/C/CJ/CJM/Palm-%{version}.tar.gz

BuildArch: noarch

Provides: perl-p5-Palm = %version
Obsoletes: perl-p5-Palm < 1.013

# Automatically added by buildreq on Wed May 14 2003
BuildRequires: perl-devel perl(Palm/PDB.pm) perl(Palm/Raw.pm)

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This is a set of Perl 5 modules for reading, manipulating, and writing
the .pdb and .prc database files used by PalmOS devices such as
the PalmPilot and its successors.

%description -l ru_RU.UTF-8
Набор модулей для Perl 5 для чтения, изменения и записи .pdb и .prc баз,
используемых устройствами на основе PalmOS - Palm Pilot и ему подобных.

%prep
%setup -q -n Palm-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
#perl_fix_local util/*
#rm -f util/*.bak

%files
%doc Changes FAQ README TODO examples
%perl_vendor_privlib/Palm*
#%_man1dir/*
#%_bindir/*

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.400-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.013-alt1
- renamed to perl-Palm: following upstream
- new version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1
- automated CPAN update

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.3.0-alt2
- Added forgotten files to package.
- Minor specfile fixes.
- BuildArch was changed to `noarch'.

* Wed May 14 2003 Andrey Brindeew <abr@altlinux.ru> 1.3.0-alt1
- Initial release

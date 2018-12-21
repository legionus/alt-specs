## SPEC file for Perl module Test::Spelling

Name: perl-Test-Spelling
Version: 0.20
Release: alt1

Summary: check for spelling errors in POD files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Test-Spelling/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Test-Spelling
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Feb 03 2013
# optimized out: perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-threads
BuildRequires: perl-IPC-Run3 perl-Pod-Spell perl-Test-Pod perl-Test-Tester

# Without dictionaries this module is useless
Requires: aspell aspell-en

%description
Perl module Test::Spelling lets you check the spelling of a POD file,
and report its results in standard Test::Simple fashion.

This module requires the spell program.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%exclude /.perl.req

%perl_vendor_privlib/Test/Spelling*

%changelog
* Thu Oct 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.17-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt1
- New version

* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed May 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- Initial build

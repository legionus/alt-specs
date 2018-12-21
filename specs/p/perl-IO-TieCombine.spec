## SPEC file for Perl module IO::TieCombine

Name: perl-IO-TieCombine
Version: 1.005
Release: alt1

Summary: Perl module to produce tied separate but combined variables

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/IO-TieCombine/
#URL: https://github.com/rjbs/io-tiecombine

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name IO-TieCombine
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
BuildRequires: perl-devel

%description
Perl module IO::TieCombine produced tied (and other) separate
but combined variables.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/IO/TieCombine*

%changelog
* Wed Nov 04 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.005-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.004-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.003-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.002-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.001-alt1
- Initial build for ALT Linux Sisyphus


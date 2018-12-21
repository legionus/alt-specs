## SPEC file for Perl module Ref::Util

%define real_name Ref-Util

Name: perl-Ref-Util
Version: 0.204
Release: alt1

Summary: Perl utility functions for checking references

License: %mit
Group: Development/Perl

URL: http://search.cpan.org/dist/Ref-Util/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jun 10 2017
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-Parse-CPAN-Meta perl-parent python-base python-modules python3 python3-base
BuildRequires: perl-CPAN-Meta perl-Readonly perl-Encode perl-Ref-Util-XS perl-devel

%description
Perl module Ref::Util provides several functions to help identify
references in a faster and smarter way.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Ref*

%changelog
* Sat Apr 21 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.204-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.203-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.113-alt1
- New version

* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.101-alt2
- Initial build for ALT Linux Sisyphus

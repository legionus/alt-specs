## SPEC file for Perl module String-Errf

Name: perl-String-Errf
Version: 0.008
Release: alt1

Summary: Perl module to provide a simple sprintf-like dialect

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/String-Errf/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name String-Errf
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Thu Jul 21 2016
# optimized out: perl perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Exporter perl-Sub-Install perl-Tie-RefHash perl-Time-Piece perl-Types-Serialiser perl-common-sense perl-parent python-base python-modules python3
BuildRequires: perl-CPAN-Meta perl-JSON-MaybeXS perl-JSON-XS perl-String-Formatter perl-TimeDate perl-autodie perl-devel

%description
Perl module String-Errf provides provides errf, a simple string
formatter that works something like sprintf. It is implemented
using String::Formatter and Sub::Exporter. Their documentation
may be useful in understanding or extending String::Errf.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/String/Errf*

%changelog
* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.008-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.007-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.006-alt1
- Initial build for ALT Linux Sisyphus


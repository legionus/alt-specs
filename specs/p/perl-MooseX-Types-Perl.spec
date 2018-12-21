## SPEC file for Perl module MooseX::Types::Perl

%define real_name MooseX-Types-Perl

Name: perl-MooseX-Types-Perl
Version: 0.101343
Release: alt1

Summary: Moose types that check against Perl syntax

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/MooseX-Types-Perl/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Mar 02 2014
# optimized out: perl-B-Hooks-EndOfScope perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-MooseX-Types perl-Variable-Magic perl-devel perl-unicore

%description
Perl module MooseX::Types::Perl provides Moose types for checking
things (mostly strings) against syntax that is, or is a reasonable
subset of, Perl syntax.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/Types/Perl*

%changelog
* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.101343-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.101342-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.101341-alt1
- Initial build for ALT Linux Sisyphus

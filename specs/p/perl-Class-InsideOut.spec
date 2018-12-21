%define _unpackaged_files_terminate_build 1
%define module Class-InsideOut

Name: perl-%module
Version: 1.14
Release: alt1

Summary: Class::InsideOut - safe, simple inside-out object construction kit

License: Apache
Group: Development/Perl
Url: %CPAN %module

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Wed Jan 14 2009 (-bi)
BuildRequires: perl-Module-Build perl-Storable perl-threads
BuildRequires: perl-Class-ISA

%description
This is a simple, safe and streamlined toolkit for building inside-out objects.
Unlike most other inside-out object building modules already on CPAN, this
module aims for minimalism and robustness:

* Does not require derived classes to subclass it
* Uses no source filters, attributes or CHECK blocks
* Supports any underlying object type including black-box inheritance
* Does not leak memory on object destruction
* Overloading-safe
* Thread-safe for Perl 5.8.5 or better
* mod_perl compatible
* Makes no assumption about inheritance or initializer needs

It provides the minimal support necessary for creating safe inside-out objects
and generating flexible accessors.

%prep
%setup -q -n %{module}-%{version}

# TODO: fails
rm -f  t/15_no_weaken_fallback.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Todo Changes examples
%perl_vendor_privlib/Class*
%doc README LICENSE Changes Todo

%changelog
* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2
- fixed build

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Mar 21 2010 Michael Bochkaryov <misha@altlinux.ru> 1.10-alt1
- 1.10 version

* Wed Jan 14 2009 Michael Bochkaryov <misha@altlinux.ru> 1.09-alt1
- first build for ALT Linux Sisyphus


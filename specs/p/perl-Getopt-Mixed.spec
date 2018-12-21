#
#   - Getopt::Mixed -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Getopt-Mixed-1.10.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Getopt-Mixed
%define m_distro Getopt-Mixed
%define m_name Getopt::Mixed
%define m_author_id unknown
%define _enable_test 1

Name: perl-Getopt-Mixed
Version: 1.12
Release: alt1

Summary: getopt processing with both long and short options

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Slava Dubrovskiy <dubrsl@altlinux.org>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/C/CJ/CJM/Getopt-Mixed-%{version}.tar.gz

# Automatically added by buildreq on Sun Apr 29 2007
BuildRequires: perl-devel perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is obsolete.

This package was my response to the standard modules Getopt::Std and
Getopt::Long.  "Std" doesn't support long options, and "Long"
didn't support short options.  I wanted both, since long options are
easier to remember and short options are faster to type.

However, some time ago Getopt::Long was changed to support short
options as well, and it has the huge advantage of being part of the
standard Perl distribution.  So, Getopt::Mixed is now effectively
obsolete.  I don't intend to make any more changes, but I'm leaving it
available for people who have code that already uses it.  For new
modules, I recommend using Getopt::Long like this:

    use Getopt::Long;
    Getopt::Long::Configure(qw(bundling no_getopt_compat));
    GetOptions(...option-descriptions...);

This package was intended to be the "Getopt-to-end-all-Getop's".  It
combines (I hope) flexibility and simplicity.  It supports both short
options (introduced by "-") and long options (introduced by "--").
Short options which do not take an argument can be grouped together.
Short options which do take an argument must be the last option in
their group, because everything following the option will be
considered to be its argument.

There are two methods for using Getopt::Mixed:  the simple method and
the flexible method.  Both methods use the same format for option
descriptions.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Getopt

%changelog
* Mon Feb 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.10-alt2
- Fix build

* Sun Apr 29 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.10-alt1
- first build for ALT Linux Sisyphus


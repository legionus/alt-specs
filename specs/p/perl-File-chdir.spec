BuildRequires: perl(Module/Build.pm)
#
#   - File::chdir -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       File::chdir
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module File-chdir
%define m_distro File-chdir
%define m_name File::chdir
%define m_author_id unknown
%define _enable_test 1

Name: perl-File-chdir
Version: 0.1010
Release: alt1

Summary: a more sensible way to change directories

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-%{version}.tar.gz

# Automatically added by buildreq on Sun Apr 09 2006
BuildRequires: perl-devel

%description
Perl's chdir() has the unfortunate problem of being very, very, very
global.  If any part of your program calls chdir() or if any library
you use calls chdir(), it changes the current working directory for
the whole program.

This sucks.

File::chdir gives you an alternative, $CWD and @CWD.  These two
variables combine all the power of "chdir()", File::Spec and Cwd.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File*

%changelog
* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.1010-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1009-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.1008-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.1007-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.1004-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.06-alt2
- fix building

* Sun Apr 09 2006 Denis Smirnov <mithraen@altlinux.ru> 0.06-alt1
- first build for ALT Linux Sisyphus

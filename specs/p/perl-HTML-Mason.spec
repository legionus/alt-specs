%define _unpackaged_files_terminate_build 1
# TODO: build with perl-CHI
#
#   - HTML::Mason -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only HTML::Mason --version 1.3101
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module HTML-Mason
%define m_distro HTML-Mason
%define m_name HTML::Mason
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-Mason
Version: 1.58
Release: alt1

Summary: HTML-Mason - Perl module

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Thu Nov 19 2009
BuildRequires: perl-Cache-Cache perl-HTML-Mason perl-Log-Agent perl-Module-Build perl-Switch perl-Test-Pod perl-libwww perl(Log/Any/Test.pm) perl(Test/Deep.pm)
#Requires: perl(Class/Container.pm)
#Requires: perl(Cwd.pm)
#Requires: perl(Data/Dumper.pm)
#Requires: perl(Exception/Class.pm)
#Requires: perl(File/Basename.pm)
#Requires: perl(File/Glob.pm)
#Requires: perl(File/Path.pm)
#Requires: perl(File/Spec.pm)
#Requires: perl(File/Temp.pm)
#Requires: perl(Getopt/Long.pm)
#Requires: perl(Params/Validate.pm)
#Requires: perl(Scalar/Util.pm)
#Requires: perl(Test/Builder.pm)
#Requires: perl(base.pm)
#Requires: perl(constant.pm)
#Requires: perl(mod_perl.pm)
#Requires: perl(warnings.pm)
#Requires: perl-base >= 1:5.6.0

# it is created on fly using internal voodoo masonry
Provides: perl(HTML/Mason/Request/CGI.pm)

%description
Mason is a tool for building, serving and managing large web sites. Its
features make it an ideal backend for high load sites serving dynamic
content, such as online newspapers or database driven e-commerce sites.
Actually, Mason can be used to generate any sort of text, whether for
a web site or not. But it was originally built for web sites and since
that's why most people are interested in it, that is the focus of this
documentation.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install
# due Apache1 deps
rm -f %buildroot%perl_vendor_privlib/HTML/Mason/Apache/Request.pm

rm -f %buildroot%_bindir/*

%files
%doc README.md Changes CONTRIBUTING.md CREDITS
%perl_vendor_privlib/HTML/
#perl_vendorlib/Bundle/

%changelog
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2
- added provides perl(HTML/Mason/Request/CGI.pm)

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.42-alt1
- new version 1.42 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.36-alt2
- fix directory ownership violation

* Wed Jul 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.36-alt1
- new version 1.36 (with rpmrb script)

* Wed Nov 22 2006 Vitaly Lipatov <lav@altlinux.ru> 1.35-alt0.1
- new version 1.35 (with rpmrb script)

* Wed Jun 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.33-alt0.1
- new version 1.33 (with rpmrb script)

* Sat Sep 24 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3101-alt2
- disable autoreq

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3101-alt1
- first build for ALT Linux Sisyphus
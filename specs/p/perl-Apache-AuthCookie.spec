%def_without apache1
%define _unpackaged_files_terminate_build 1
#
#   - Apache::AuthCookie -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Apache-AuthCookie
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Apache-AuthCookie
%define m_distro Apache-AuthCookie
%define m_name Apache::AuthCookie
%define m_author_id unknown
%define _enable_test 1

Name: perl-Apache-AuthCookie
Version: 3.27
Release: alt2

Summary: Perl Authentication and Authorization via cookies

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Slava Dubrovskiy <dubrsl@altlinux.org>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/M/MS/MSCHOUT/%{module}-%{version}.tar.gz

%if_with apache1
BuildRequires: apache-mod_perl
%endif

# Automatically added by buildreq on Tue Apr 06 2010
BuildRequires: apache2-mod_perl perl-CGI perl-libwww perl(Class/Load.pm) perl(autobox.pm) perl(Apache/TestMM.pm) perl(WWW/Form/UrlEncoded.pm) perl(Hash/MultiValue.pm) perl(HTTP/Body.pm) perl-devel

%package -n perl-Apache2-AuthCookie
Summary: Perl Authentication and Authorization via cookies
Group: Development/Perl

%package -n perl-Apache-AuthCookie-Util
Summary: Perl Authentication and Authorization via cookies
Group: Development/Perl

%description
Apache::AuthCookie allows you to intercept a user's first
unauthenticated access to a protected document. The user will be
presented with a custom form where they can enter authentication
credentials. The credentials are posted to the server where AuthCookie
verifies them and returns a session key.

%description -n perl-Apache-AuthCookie-Util
Apache::AuthCookie allows you to intercept a user's first
unauthenticated access to a protected document. The user will be
presented with a custom form where they can enter authentication
credentials. The credentials are posted to the server where AuthCookie
verifies them and returns a session key.

%description -n perl-Apache2-AuthCookie
Apache::AuthCookie allows you to intercept a user's first
unauthenticated access to a protected document. The user will be
presented with a custom form where they can enter authentication
credentials. The credentials are posted to the server where AuthCookie
verifies them and returns a session key.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files -n perl-Apache2-AuthCookie
%doc README.apache-2.4.pod LICENSE README.modperl2 README Changes
%perl_vendor_privlib/Apache2/AuthCookie*
%perl_vendor_privlib/Apache/README.apache-2.4.pod                               
%perl_vendor_privlib/Apache2_4/AuthCookie.pm                                    

%if_with apache1
%files
%perl_vendor_privlib/Apache/AuthCookie.pm
%else
%exclude %perl_vendor_privlib/Apache/AuthCookie.pm
%endif

%files -n perl-Apache-AuthCookie-Util
%perl_vendor_privlib/Apache/AuthCookie

%changelog
* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.27-alt2
- build w/o apache1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.26-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1
- automated CPAN update

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.24-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 3.22-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 3.20-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 3.19-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 3.18-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.12-alt1
- initial build for ALT Linux Sisyphus


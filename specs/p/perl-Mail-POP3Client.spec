%define module_name Mail-POP3Client

Name: perl-%module_name
Version: 2.19
Release: alt1

Summary: %module_name module for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-%{version}.tar.gz

# Automatically added by buildreq on Tue Mar 04 2008
BuildRequires: perl-devel
BuildArch: noarch

%description
This is a POP3 client module for perl5. It provides an object-oriented
interface to a POP3 server. It can be used to write perl-based biff clients,
mail readers, or whatever.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mail/

%changelog
* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 2.18-alt1
- 2.18

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 2.17-alt1
- 2.17
- Spec cleanups.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.16-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Maxim Tkachenko <tma@altlinux.ru> 2.16-alt1
        + Correct documentation errors for Connect().
        + Fix problem with servers not returning an empty line after
          headers when message body is blank.
	+ Create a method to set AuthMode (Jamie Le Tual)
	+ Force Mime::Base64::encode base64 result into a single line
	  (Jamie Le Tual)
	+ Documenation updates
				    
* Wed Jul 28 2004 Maxim Tkachenko <tma@altlinux.ru> 2.14-alt1
- build for AltLinux

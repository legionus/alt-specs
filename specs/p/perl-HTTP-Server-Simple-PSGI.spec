%define _unpackaged_files_terminate_build 1
%define m_distro HTTP-Server-Simple-PSGI
Name: perl-HTTP-Server-Simple-PSGI
Version: 0.16
Release: alt2
Summary: HTTP::Server::Simple::PSGI - PSGI handler for HTTP::Server::Simple

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Networking/WWW
License: Perl
Url: http://search.cpan.org/~miyagawa/HTTP-Server-Simple-PSGI/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-HTTP-Server-Simple

%description
HTTP::Server::Simple::PSGI is a HTTP::Server::Simple based HTTP server
that can run PSGI applications. This module only depends on
HTTP::Server::Simple, which itself doesn't depend on any non-core
modules so it's best to be used as an embedded web server.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTTP/Server/Simple/PSGI*
%perl_vendor_privlib/Plack/Handler/HTTP/Server/Simple.pm
%doc Changes README 

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- fixed unpackaged files

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Sun Aug 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build

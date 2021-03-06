#
#   - Net::INET6Glue -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::INET6Glue
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-INET6Glue
%define m_distro Net-INET6Glue
%define m_name Net::INET6Glue
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-INET6Glue
Version: 0.603
Release: alt1

Summary: Make common modules IPv6 ready by hotpatching

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/S/SU/SULLR/Net-INET6Glue-%{version}.tar.gz

# Automatically added by buildreq on Fri Jun 01 2012
# optimized out: perl-Socket6
BuildRequires: libnss-role perl-IO-Socket-INET6 perl-devel perl-libnet

%description
the Net::INET6Glue manpage is a collection of modules to make common modules IPv6 ready
by hotpatching them.

Unfortunatly the current state of IPv6 support in perl is that no IPv6 support
is in the core and that a lot of important modules (like the Net::FTP manpage,
the Net::SMTP manpage, the LWP manpage,...) do not support IPv6 even if the modules for IPv6
sockets the Socket6 manpage, the IO::Socket::INET6 manpage are available.

This module tries to mitigate this by hotpatching.
Currently the following submodules are available:

=over 4

=item the Net::INET6Glue::INET_is_INET6 manpage

Makes the IO::Socket::INET manpage behave like the IO::Socket::INET6 manpage, especially make it
capable to create IPv6 sockets. This makes the LWP manpage, the Net::SMTP manpage and others
IPv6 capable.

=item the Net::INET6Glue::FTP manpage

Hotpatches the Net::FTP manpage to support EPRT and EPSV commands which are needed to
deal with FTP over IPv6. Also loads the Net::INET6Glue::INET_is_INET6 manpage.

=back

%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.603-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.602-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.601-alt1
- automated CPAN update

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- automated CPAN update

* Fri Jun 01 2012 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- initial build for ALT Linux Sisyphus


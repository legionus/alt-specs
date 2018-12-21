%define _unpackaged_files_terminate_build 1
#
#   - Net-SFTP -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::SFTP
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-SFTP
%define m_distro Net-SFTP
%define m_name Net-SFTP
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-SFTP
Version: 0.12
Release: alt1

Summary: Secure File Transfer Protocol client

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Mikhail Pokidko <pma@altlinux.org>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/L/LK/LKINLEY/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 05 2009
BuildRequires: perl-Net-SSH-Perl perl-devel perl(Math/Int64.pm)

%description
*Net::SFTP* is a pure-Perl implementation of the Secure File
Transfer Protocol (SFTP) - file transfer built on top of the
SSH2 protocol. *Net::SFTP* uses *Net::SSH::Perl* to build a
secure, encrypted tunnel through which files can be transferred
and managed. It provides a subset of the commands listed in
the SSH File Transfer Protocol IETF draft, which can be found
at *http://www.openssh.com/txt/draft-ietf-secsh-filexfer-00.txt*.

SFTP stands for Secure File Transfer Protocol and is a method of
transferring files between machines over a secure, encrypted
connection (as opposed to regular FTP, which functions over an
insecure connection). The security in SFTP comes through its
integration with SSH, which provides an encrypted transport
layer over which the SFTP commands are executed, and over which
files can be transferred. The SFTP protocol defines a client
and a server; only the client, not the server, is implemented
in *Net::SFTP*.

Because it is built upon SSH, SFTP inherits all of the built-in
functionality provided by *Net::SSH::Perl*: encrypted
communications between client and server, multiple supported
authentication methods (eg. password, public key, etc.).

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes LICENSE README ToDo
%perl_vendor_privlib/Net/*

%changelog
* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Mon Oct 05 2009 Mikhail Pokidko <pma@altlinux.org> 0.10-alt1
- initial build for ALT Linux Sisyphus

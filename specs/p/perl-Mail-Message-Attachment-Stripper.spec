#
#   - Mail::Message::Attachment::Stripper -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Mail::Message::Attachment::Stripper
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Mail-Message-Attachment-Stripper
%define m_distro Mail-Message-Attachment-Stripper
%define m_name Mail::Message::Attachment::Stripper
%define m_author_id unknown
%define _enable_test 1

Name: perl-Mail-Message-Attachment-Stripper
Version: 1.01
Release: alt2.1

Summary: Strip the attachments from a mail

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Feb 04 2006
BuildRequires: perl-Devel-Symdump perl-IO-stringy perl-MIME-Types perl-Mail-Box perl-MailTools perl-Object-Realize-Later perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Simple perl-Test-Pod-Coverage perl-TimeDate perl-devel

%description
Given a Mail::Message object, detach all attachments from the
message. These are then available separately.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Mail/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt2
- fix directory ownership violation

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt1
- first build for ALT Linux Sisyphus

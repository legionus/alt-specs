#
#   - Amazon::S3 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Amazon::S3
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Amazon-S3
%define m_distro Amazon-S3
%define m_name Amazon::S3
%define m_author_id unknown
%define _enable_test 1

Name: perl-Amazon-S3
Version: 0.45
Release: alt1

Summary: A portable client library for working with and

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Sep 04 2010
BuildRequires: perl-Class-Accessor perl-Digest-HMAC perl-Digest-MD5-File perl-LWP-UserAgent-Determined perl-XML-Simple perl-devel

%description
Amazon::S3 provides a portable client interface to Amazon Simple
Storage System (S3).

"Amazon S3 is storage for the Internet. It is designed to
make web-scale computing easier for developers. Amazon S3
provides a simple web services interface that can be used to
store and retrieve any amount of data, at any time, from
anywhere on the web. It gives any developer access to the
same highly scalable, reliable, fast, inexpensive data
storage infrastructure that Amazon uses to run its own
global network of web sites. The service aims to maximize
benefits of scale and to pass those benefits on to
developers".

To sign up for an Amazon Web Services account, required to
use this library and the S3 service, please visit the Amazon
Web Services web site at http://www.amazonaws.com/.

You will be billed accordingly by Amazon when you use this
module and must be responsible for these costs.

To learn more about Amazon's S3 service, please visit:
http://s3.amazonaws.com/.

This need for this module arose from some work that needed
to work with S3 and would be distributed, installed and used
on many various environments where compiled dependencies may
not be an option. Net::Amazon::S3 used XML::LibXML
tying it to that specific and often difficult to install
option. In order to remove this potential barrier to entry,
this module is forked and then modified to use XML::SAX
via XML::Simple.

Amazon::S3 is intended to be a drop-in replacement for
<Net:Amazon::S3> that trades some performance in return for
portability.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Amazon/*

%changelog
* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt1
- initial build for ALT Linux Sisyphus


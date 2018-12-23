%define pear_name Net_DNS

Name: pear-Net_DNS
Version: 1.0.7
Release: alt1

Summary: Resolver library used to communicate with a DNS server

License: PHP-3.01
Group: Development/Other
Url: http://pear.php.net/package/Net_DNS

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_DNS-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: php5-mhash

%description
A resolver library used to communicate with a name server to perform DNS
queries, zone transfers, dynamic DNS updates, etc.
Creates an object hierarchy from a DNS server response, which allows you
to view all of the information given by the DNS server. It bypasses the
system resolver library and communicates directly with the server.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Net
%pear_testdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- new version 1.0.7 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

